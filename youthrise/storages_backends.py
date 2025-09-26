from storages.backends.s3boto3 import S3Boto3Storage

class MediaRootS3BotoStorage(S3Boto3Storage):
    location = "media"            # ensures "media/" prefix is added inside bucket
    file_overwrite = False        # optional: don’t overwrite files with same name
    default_acl = "public-read"
