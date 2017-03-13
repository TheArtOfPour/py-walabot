from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

filename = 'feed.json'


@app.route('/walabot/api/v1.0/imageenergy', methods=['GET'])
def get_image_energy():
    energy = json.loads(open(filename).read())
    return jsonify(energy)


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
