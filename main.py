from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime as dt
import os

app = Flask(__name__)

# Conexão com o MongoDB
MONGO_URI = os.getenv('MONGO_URI')  # Vamos colocar no Heroku depois
client = MongoClient(MONGO_URI)
db = client.get_database('Twlio')  # Nome do banco
messages_collection = db.get_collection('Messages')  # Nome da coleção

@app.route('/', methods=['GET'])
def home():
    return 'Heloo user Webhook with MongoDB is live!'

@app.route('/webhook', methods=['POST'])
def webhook():
    sender = request.form.get('From')
    body = request.form.get('Body')

    print(f"Dados recebidos - From: {sender}, Body: {body}")

    if sender and body:
        message_info = {
            "message_timestamp": dt.datetime.now(),
            "from": sender,
            "message": body
        }
        result = messages_collection.insert_one(message_info)  # Salva no Mongo direto
        print(f"Payload: {message_info}")
        print(f"Mensagem salva com o ID: {result.inserted_id}")

    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)