from elasticsearch import Elasticsearch, helpers
import json
import pprint as pp
import random

def gendata(books):

    book_list = []
    for tmp in books:
        tmp_dict = {}
        for key, value in tmp.items():
            if key == 'category':
                value = value.split(' > ')[-1]
                print(value)
            tmp_dict[key] = value
        tmp_dict['rating'] = random.uniform(0, 5)
        
        book_list.append(tmp_dict)
    
    # bulkで扱えるデータ構造に変換します
    for book in book_list:
        # pp.pprint(book)
        yield {
            "_op_type": "create",
            "_index": "test_index",
            "_source": book
        }


with open('./test.json') as f:
    books = json.load(f)
    
# Elasticsearchクライアント作成
es = Elasticsearch("http://localhost:9200")
# exit()
es.indices.delete(index="test_index")

helpers.bulk(es, gendata(books))

pp.pprint(es.indices.get_mapping(index="test_index"))

# インデックス一覧の取得
# indices = es.cat.indices(index='*', h='index').splitlines()
# インデックスの表示
# for index in indices:
# print(index)

es.close()
