import io
import os
from sislv4utils.config import Config
from minio import Minio, credentials

class ObjectStore(object):
    # region members

    _default_chunk_size = 8*1024*1024

    # endregion

    # region methods

    def __init__(self, cf: Config):
        endpoint = cf.s3_host + ':' + str(cf.s3_port)
        provider = credentials.LdapIdentityProvider(sts_endpoint=('http://' + endpoint),
            ldap_username=cf.appuser, ldap_password=cf.apppass)
        self._s3 = Minio(endpoint=endpoint, secure=cf.s3_tls, credentials=provider)

    # downloads an object from minio to local file
    def download(self, bucket_name: str, objectid: str, localfile: str) -> bool:
        self._s3.fget_object(bucket_name=bucket_name, object_name=objectid, file_path=localfile)
        return os.path.isfile(localfile)

    # uploads a local file to minio
    def upload(self, bucket_name: str, objectid: str, localfile: str) -> bool:
        self._s3.fput_object(bucket_name=bucket_name, object_name=objectid, file_path=localfile)
        return self.object_exists(bucket_name=bucket_name, object_name=objectid)

    # saves an object on minio from data
    def put_object(self, bucket_name: str, object_name: str, data: any) -> None:
        self._s3.put_object(bucket_name=bucket_name, object_name=object_name,
            data=io.BytesIO(data), length=-1, part_size=ObjectStore._default_chunk_size)

    # checks if a bucket already exists
    def bucket_exists(self, bucket_name: str) -> bool:
        return self._s3.bucket_exists(bucket_name)

    # checks if an object already exists
    def object_exists(self, bucket_name: str, object_name: str) -> bool:
        try: self._s3.stat_object(bucket_name=bucket_name, object_name=object_name)
        except: return False
        else: return True

    # endregion
