import io
import os
from minio import Minio, credentials

class ObjectStore(object):
    # region members

    _default_chunk_size = 8*1024*1024

    # endregion
    # region constructor / destructor

    def __init__(self, host: str, port: int, username: str, password: str, tls: bool, ):
        endpoint = host + ':' + str(port)
        provider = credentials.LdapIdentityProvider(
            sts_endpoint=('http://' + endpoint),
            ldap_username=username,
            ldap_password=password
        )
        self.s3 = Minio(endpoint=endpoint, secure=tls, credentials=provider)

    # endregion
    # region members

    def download(self, bucket_name: str, objectid: str, localfile: str) -> bool:
        self.s3.fget_object(bucket_name=bucket_name, object_name=objectid, file_path=localfile)
        return os.path.isfile(localfile)

    def upload(self, bucket_name: str, objectid: str, localfile: str) -> bool:
        self.s3.fput_object(bucket_name=bucket_name, object_name=objectid, file_path=localfile)
        return self.object_exists(bucket_name=bucket_name, object_name=objectid)

    def put_object(self, bucket_name: str, object_name: str, data: any):
        self.s3.put_object(bucket_name=bucket_name, object_name=object_name,
                           data=io.BytesIO(data), length=-1,
                           part_size=ObjectStore._default_chunk_size)

    def bucket_exists(self, bucket_name: str) -> bool:
        return self.s3.bucket_exists(bucket_name)

    def object_exists(self, bucket_name: str, object_name: str) -> bool:
        try:
            self.s3.stat_object(bucket_name=bucket_name, object_name=object_name)
        except:
            return False
        else:
            return True

    # endregion
