from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime as dt
import os

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client.get_database('Twlio')
messages_collection = db.get_collection('Messages')

@app.route('/', methods=['GET'])
def home():
    return 'Hello user Webhook with MongoDB is live!'


@app.route('/webhook', methods=['POST'])
def webhook():
    sender = request.form.get('From')
    body = request.form.get('Body')

    print(f"Data Received - From: {sender}, Body: {body}")

    if sender and body:
        message_info = {
            "message_timestamp": dt.datetime.now(),
            "from": sender,
            "message": body
        }
        result = messages_collection.insert_one(message_info)
        print(f"Payload: {message_info}")
        print(f"Message Salved With ID: {result.inserted_id}")

    return jsonify({"status": "received"}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)