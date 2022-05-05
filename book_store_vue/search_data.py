from elasticsearch import Elasticsearch, helpers
import json
import pprint as pp

# Elasticsearchクライアント作成
es = Elasticsearch("http://localhost:9200")
# es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])

query = { "query": {
    "match": { "text": 'Aaron' } }
         }

#インデックス"boston"を対象に検索、5件を取得
res = es.search(index="test_index", body=query, size=5)
pp.pprint(res)

es.close()
