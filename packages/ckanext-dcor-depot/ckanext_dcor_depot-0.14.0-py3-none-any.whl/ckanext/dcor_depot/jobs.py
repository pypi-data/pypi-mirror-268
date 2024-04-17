import pathlib
import warnings

from ckan import logic
from dcor_shared import (
    get_ckan_config_option, get_resource_path, s3, s3cc, sha256sum,
    wait_for_resource
)

from .orgs import MANUAL_DEPOT_ORGS
from .paths import USER_DEPOT


class NoSHA256Available(UserWarning):
    """Used for missing SHA256 sums"""
    pass


def admin_context():
    return {'ignore_auth': True, 'user': 'default'}


def backup_resource_from_s3_to_block_storage_job(resource):
    """Copy resources from S3 to local block storage

    As long as we do not have a backup strategy for S3, make sure
    that there is a copy of each resource either in the "resources"
    directory or in the "dcor_object_store.local_backup_location"
    directory.

    TODO: remove this method once we have a backup strategy for S3.
    """
    rid = resource["id"]
    # Make sure the resource is available for processing
    wait_for_resource(rid)

    # Check the legacy local resource
    path_legacy = get_resource_path(rid)
    if not path_legacy.exists():
        # Check the local backup directory
        backup_loc = get_ckan_config_option(
            "dcor_object_store.local_backup_location")
        if backup_loc is not None:
            # We have this variable defined which means we can back up to it
            path_bu = pathlib.Path(backup_loc) / rid[:3] / rid[3:6] / rid[6:]
            if not path_bu.exists():
                path_bu.parent.mkdir(parents=True, exist_ok=True)
                # set up a temporary download file path
                path_tmp = path_bu.with_name(path_bu.name + "_temp")
                path_tmp.unlink(missing_ok=True)
                if s3.is_available():
                    # perform the download from s3
                    s3_client, _, _ = s3.get_s3()
                    bucket_name, object_name = \
                        s3cc.get_s3_bucket_object_for_artifact(rid)
                    s3_client.download_file(
                        bucket_name, object_name, str(path_tmp))
                    # if we got here, then everything went fine
                    path_tmp.rename(path_bu)
                    return path_bu

    return False


def patch_resource_noauth(package_id, resource_id, data_dict):
    """Patch a resource using package_revise"""
    package_revise = logic.get_action("package_revise")
    revise_dict = {"match": {"id": package_id},
                   f"update__resources__{resource_id}": data_dict}
    package_revise(context=admin_context(), data_dict=revise_dict)


def migrate_resource_to_s3_job(resource):
    """Migrate a resource to the S3 object store"""
    rid = resource["id"]
    # Make sure the resource is available for processing
    wait_for_resource(rid)
    path = get_resource_path(rid)

    # Only attempt to upload if the file has been uploaded to block storage.
    if path.exists():
        sha256 = resource.get("sha256")
        if sha256 is None:
            warnings.warn(f"Resource {rid} has no SHA256 sum yet and I will "
                          f"compute it now. This should not happen unless you "
                          f"are running pytest with synchronous jobs!",
                          NoSHA256Available)
            sha256 = sha256sum(path)
        # Perform the upload
        s3_url = s3cc.upload_artifact(
            resource_id=rid,
            path_artifact=path,
            artifact="resource",
            # avoid an empty SHA256 string being passed to the method
            sha256=sha256,
            override=False,
        )

        # Append the S3 URL to the resource metadata
        patch_resource_noauth(
            package_id=resource["package_id"],
            resource_id=resource["id"],
            data_dict={
                "s3_available": True,
                "s3_url": s3_url})

        return s3_url
    return False


def symlink_user_dataset_job(pkg, usr, resource):
    """Symlink resource data to human-readable depot"""
    path = get_resource_path(resource["id"])
    if not path.exists():
        # nothing to do (skip, because resource is on S3 only)
        return False

    org = pkg["organization"]["name"]
    if org in MANUAL_DEPOT_ORGS or path.is_symlink():
        # nothing to do (skip, because already symlinked)
        return False

    user = usr["name"]
    # depot path
    depot_path = (USER_DEPOT
                  / (user + "-" + org)
                  / pkg["id"][:2]
                  / pkg["id"][2:4]
                  / f"{pkg['name']}_{resource['id']}_{resource['name']}")

    depot_path.parent.mkdir(exist_ok=True, parents=True)

    symlinked = True

    # move file to depot and create symlink back
    try:
        path.rename(depot_path)
    except FileNotFoundError:
        # somebody else was faster (avoid race conditions)
        if not depot_path.exists():
            raise
        else:
            symlinked = False

    try:
        path.symlink_to(depot_path)
    except FileNotFoundError:
        # somebody else was faster (avoid race conditions)
        if not path.is_symlink():
            raise
        else:
            symlinked = False

    return symlinked
