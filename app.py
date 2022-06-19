from flask_cors import CORS
from flask import Flask, request, jsonify
from aiohttp import ClientSession

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def getPrediction():
    return "Hello Prediction Middleware"


@app.route('/predict', methods=['POST'])
async def predict():
    try:
        data = request.json
        # sentence = data['sentence']
        # endpoint = f'/api/saved_tweets/create_analyzed_tweet'
        async with ClientSession(trust_env=True) as session:
            async with session.post(f'http://178.79.135.192/predict_from_text', json=data) as response:
                return await response.json()

    except Exception as e:
        response = jsonify({'sentence': "sentence", 'error': e}), 400
        return response


if __name__ == '__main__':
    app.run(debug=True)
