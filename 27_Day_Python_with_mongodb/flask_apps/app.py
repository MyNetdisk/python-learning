from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import MONGO_URI, DB_NAME
from bson.objectid import ObjectId  # id对象

app = Flask(__name__)

# ---------- 建立连接 ----------
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
print(client.list_database_names())

try:
    client.admin.command("ping")
    print("MongoDB 连接成功")
except ConnectionFailure:
    print("MongoDB 连接失败")

db = client[DB_NAME]
collection = db["users"]


# ---------- 路由示例 ----------

@app.route("/")
def index():
    return jsonify({"message": "Flask + MongoDB OK"})


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)}), 201


@app.route("/users", methods=["GET"])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
