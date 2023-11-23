from flask import Flask, jsonify,request
from gpt4all import Embed4All

app = Flask(__name__)
@app.route('/api/embedding', methods=['POST'])
def create_Embedding():
    try:
        data = request.get_json()
        text = data['text']
        embedder = Embed4All()
        embeddings = embedder.embed(text)
        return jsonify({'embedding': [embeddings]})
    except:
        return jsonify({'error': 'Error during embedding'})
    
if __name__ == '__main__':
    app.run()
