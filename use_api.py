from flask import Flask, request, jsonify
from scipy.spatial.distance import cosine

import tensorflow_hub as hub
import numpy as np

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

app = Flask(__name__)


@app.route('/get_similarity_score', methods=['POST', 'GET'])
def get_similarity_score():
    result = {"score": 0}
    if request.method == 'POST':
        sent1 = request.form.get('sent1')
        sent2 = request.form.get('sent2')
        sentence_embeddings = embed([sent1, sent2])
        result["score"] = 1 - cosine(sentence_embeddings[0], sentence_embeddings[1])
        print("Score::   ", result["score"])
        print("---"*30)
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False, threaded=True, host='0.0.0.0', port=8001)
