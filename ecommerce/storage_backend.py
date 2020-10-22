from storages.backends.s3boto3 import S3Boto3Storage

# pylint: disable=abstract-method
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    default_acl = 'public-read'
