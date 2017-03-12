from flask import Flask, jsonify
import json

app = Flask(__name__)

filename = 'feed.json'


@app.route('/walabot/api/v1.0/imageenergy', methods=['GET'])
def get_image_energy():
    energy = json.loads(open(filename).read())
    return jsonify(energy)


if __name__ == '__main__':
    app.run(debug=True)
