# flake8: noqa
import time

from typing import (
    Any, Callable, Dict, Iterable, List, Optional, Tuple
)
from openfinance.utils.recall.base import RecallBase

from elasticsearch import Elasticsearch
from elasticsearch import helpers

class ES(RecallBase):
    name = "es"
    max_num = 800
    client: Elasticsearch

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_config(
        cls,
        config
    ):
        name = "es"
        host = config[name].get("host", "localhost")
        port = config[name].get("port", 9200)
        max_num = config[name].get("max_recall_num", 800)
        client = Elasticsearch(
            [{'host': host, 'port': port, 'scheme': 'http'}]
        )
        mapping = {
            "mappings": {
                "properties": {
                    "title": {
                        "type": "text",
                        "analyzer": "ik_max_word"  # 指定分词器
                    }
                }
            }
        }    
        client.indices.create(index=name, body=mapping, ignore=400)
        return cls(name=name, max_num=max_num, client=client)

    def insert(
        self,
        docs: Dict[str, Any]
    ):
        """
            docs: {'id': { 'title': 'new_value1', 'doc': 'new_value2'} },
        """
        """批量写入"""
        actions = []
        for sid, docs in docs.items():
            action = {
                "_index": self.name,
                "_type": "_doc",
                "_id": sid,
                "_source": docs
            }
            # print(index)
            actions.append(action)
        ret = helpers.bulk(self.client, actions)
        # print(ret)
        return ret
    
    def delete(
        self,
        query = {"match_all": {}}
    ):
        body = {  
            "query": query
        }
        return self.client.delete_by_query(index="es", body=body)

    def update(
        self,
        id_to_docs: Dict[str, str]
    ):
        """
            docs : {'doc': 'new_value1', 'score': 'new_value2'}
        """
        actions = []  
        
        # 为每个要更新的文档创建一个更新动作  
        for doc_id, doc in id_to_docs.items():
            action = {  
                '_op_type': 'update',  
                '_index': self.name,  
                '_id': doc_id,  
                'script': {  
                    'source': 'ctx._source = params',  
                    'lang': 'painless',  
                    'params': doc  
                }  
            }  
            actions.append(action)  
        
        # 使用helpers.bulk函数执行批量更新  
        try:  
            success, failed = bulk(es, actions, stats_only=True)  
            # print(f'成功更新的文档数: {success}')  
            # print(f'更新失败的文档数: {failed}')  
        except BulkIndexError as e:  
            # 处理批量更新中的错误  
            print('批量更新过程中发生错误:', e)  
            # 你可以从e.errors中获取每个失败操作的详细信息  
            # for error in e.errors:  
            #     print(error)        

    def similarity_search(
        self, 
        q,
        size=50,
    ):
        if isinstance(q, dict):  # support for complicated search
            query = {
                "query": {
                    "bool": q
                }
            }         
        else:
            query = {
                "query": {
                    "match": {
                        "title": q
                    }
                },
                "size": size
            }
        docs = self.client.search(index=self.name, body=query)
        results = []
        for doc in docs.body["hits"]["hits"][:self.max_num]:
            results.append({
                "content": doc["_source"],
                "score": doc['_score']
            })
        return results

if __name__ == "__main__":
    es = ES.from_config({"es": {}})
