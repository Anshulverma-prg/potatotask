from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(['http://elasticsearch:9200'])

@app.route('/query', methods=['GET'])
def query_tweets():
    term = request.args.get('term')
    res = es.search(index='tweets', body={
        "query": {
            "match": {
                "text": term
            }
        }
    })
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
