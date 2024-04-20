from elasticsearch import Elasticsearch as ESClient

from elasticsearch import (
    ApiError,
    SerializationError,
    ConnectionError,
    ConnectionTimeout,
    SSLError,
    NotFoundError,
)

class ElasticSearch(object):
    # region member

    _ES_ERRORS_MSG = "{method} - {status}"
    _FAILED = "FAILED"
    _SUCCESS = "SUCCESS"
    _client = None

    # endregion
    # region method

    def __init__(self, host, username, password, ca_certs, client_cert, client_key):
        ElasticSearch._client = self.connect(
            host, username, password, ca_certs, client_cert, client_key
        )

    def connect(self, host, username, password, ca_certs, client_cert, client_key) -> ESClient:
        # connect to elasticsearch db and return client
        try:
            es_client = ESClient(
                f"https://{host}",
                http_auth=(username, password),
                ca_certs=ca_certs,
                client_cert=client_cert,
                client_key=client_key,
                verify_certs=True
            )
            return es_client
        except SSLError as se:
            # ssl connection error
            print(se)
        except ConnectionError as e:
            # error from http connection
            print(e)
        except ConnectionTimeout as ce:
            # error timeout
            print(ce)

    def index_exists(self, index):
        es_client = ElasticSearch._client
        return es_client.indices.exists(index=index).body

    def create_index(self, index_name, es_mapping={}):
        es_client = ElasticSearch._client
        idx_exists = self.index_exists(index=index_name, es_client=es_client)
        # create an index with mapping
        if not idx_exists:
            index_created = es_client.indices.create(index=index_name, mappings=es_mapping)
            print(index_created._body)
        else:
            print("Index {idx} already exists".format(idx=index_name))

    def delete_index(self, index_name):
        es_client = ElasticSearch._client
        # delete an index
        es_client.delete(index=index_name)

    def insert_or_replace(self, index_name, message, id=None) -> str:
        es_client = ElasticSearch._client
        res = ""
        # insert a document into elasticsearch db
        try:
            if id is not None:
                # if id is valid then replace the document _source
                res = es_client.index(index=index_name, id=id, document=message)
            else:
                # if no id provided then create
                res = es_client.index(index=index_name, document=message)
        except ApiError as e:
            print(e.body)
            raise e
        except SerializationError as se:
            print(se.errors)
            raise se
        return res["_id"]

    def bulk_action(self, index_name, data, action):
        es_client = ElasticSearch._client
        records = []
        '''
        ## Template for Create
        action = create, update, delete
        {"_op_type": "create",
        "_index":"",
        "_source": ''}
        '''
        for rec in data:
            if action == 'update':
              records.append(
                  {
                      "_op_type": action,
                      "_index": index_name,
                      "_id": '',
                      "_source": rec
                  }
              )
            else:
                records.append(
                  {
                      "_op_type": action,
                      "_index": index_name,
                      "_source": rec
                  }
              )
        print(records)
        stat = helpers.bulk(es_client, records)
        print(stat)

    def get_id(self, index_name, query):
        es_client = ElasticSearch._client
        # return the id of document by query
        result = es_client.search(index=index_name, query=query)
        data = result["hits"]["hits"]
        if len(data) == 0:
            return ""
        else:
            return data[0]["_id"]

    def delete_by_id(self, index_name, id):
        es_client = ElasticSearch._client
        try:
            # delete a document by id
            return es_client.delete(index=index_name, id=id)
        except NotFoundError as nfe:
            print(nfe, "Line: ", nfe.__traceback__.tb_lineno)
            print(
                ElasticSearch._ES_ERRORS_MSG.format(
                    method="delete_by_id", status=ElasticSearch._FAILED
                )
            )
            return None

    def update_by_id(self, index_name, data, id):
        es_client = ElasticSearch._client
        try:
            # update a document by id using custom query/fields
            return es_client.update(index=index_name, id=id, body=data)
        except NotFoundError as nfe:
            print(nfe, "Line: ", nfe.__traceback__.tb_lineno)
            print(
                ElasticSearch._ES_ERRORS_MSG.format(
                    method="update_by_id", status=ElasticSearch._FAILED
                )
            )
            return None
        except SerializationError as se:
            print(se, "Line: ", se.__traceback__.tb_lineno)
            print(
                ElasticSearch._ES_ERRORS_MSG.format(
                    method="update_by_id", status=ElasticSearch._FAILED
                )
            )
            return None

    def search(self, index_name, query={}, _from=0, size=10):
        # search a document by query
        es_client = ElasticSearch._client
        result = None

        if len(query.keys()) == 0:
            result = es_client.search(index=index_name, from_=_from, size=size)
        else:
            result = es_client.search(index=index_name, query=query, from_=_from, size=size)

        total = result["hits"]["total"]["value"]
        rows = result["hits"]["hits"]

        return (total, rows)

    def close(self):
        if ElasticSearch._client is not None:
            ElasticSearch._client.close()

    # endregion

    # bulk methods
