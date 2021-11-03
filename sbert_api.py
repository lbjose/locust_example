from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
from flask import Flask, request, jsonify

app = Flask(__name__)

model_save_path = "all-mpnet-base-v2"
model = SentenceTransformer(model_save_path)


@app.route('/get_similarity_score', methods=['POST', 'GET'])
def get_similarity_score():
    result = {"score": 0}
    if request.method == 'POST':
        sent1 = request.form.get('sent1')
        sent2 = request.form.get('sent2')
        sentence_embeddings = model.encode([sent1, sent2])
        result["score"] = 1 - cosine(sentence_embeddings[0], sentence_embeddings[1])
        print("Score::   ", result["score"])
        print("---"*30)
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False, threaded=True, host='0.0.0.0', port=8001)
