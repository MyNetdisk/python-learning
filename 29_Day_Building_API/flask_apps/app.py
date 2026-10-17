# 导入flask
from datetime import datetime, UTC

from flask import Flask, Response, request
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import MONGO_URI, DB_NAME
from bson.objectid import ObjectId  # id对象
from bson.errors import InvalidId
import json
import os

app = Flask(__name__)

# ---------- 建立连接 ----------
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
print(client.list_database_names())  # 打印数据库名称

# 创建数据库
db = client[DB_NAME]

try:
    client.admin.command('ping')
    print("MongoDB 连接成功")
except ConnectionFailure:
    print("MongoDB 连接失败")


@app.route("/api/v1.0/students", methods=["GET"])
def students():
    student_list = list(db.students.find({}, {"_id": 0}))
    return Response(json.dumps(student_list), mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find_one({"_id": ObjectId(id)})
    if student is None:
        return Response(json.dumps({"error": "学生不存在"}), mimetype='application/json', status=404)
    student["_id"] = str(student["_id"])
    return Response(json.dumps(student), mimetype='application/json')


@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or not data.get("name"):
        return Response(json.dumps({"error": "name is required"}), mimetype='application/json', status=400)
    name = data.get("name")
    country = data.get("country", "")
    city = data.get("city", "")
    skills = data.get("skills", [])
    bio = data.get("bio", "")
    birthyear = data.get("birthyear", "")

    if isinstance(skills, str):
        skills = [s.strip() for s in skills.split(",") if s.strip()]

    student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": skills,
        "bio": bio,
        "created_at": datetime.now(UTC).isoformat()
    }

    result = db.students.insert_one(student)

    return Response(json.dumps({"message": "学生创建成功", "id": str(result.inserted_id)}), mimetype='application/json',
                    status=201)


@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    try:
        query = {"_id": ObjectId(id)}
    except InvalidId:
        return Response(json.dumps({"error": "Invalid ID"}), mimetype='application/json', status=400)
    data = request.get_json()
    if not data or not data.get("name"):
        return Response(json.dumps({"error": "name is required"}), mimetype='application/json', status=400)
    name = data.get("name")
    country = data.get("country", "")
    city = data.get("city", "")
    skills = data.get("skills", [])
    bio = data.get("bio", "")
    birthyear = data.get("birthyear", "")
    if isinstance(skills, str):
        skills = [s.strip() for s in skills.split(",") if s.strip()]

    student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": skills,
        "bio": bio,
        "updated_at": datetime.now(UTC).isoformat()
    }
    result = db.students.update_one(query, {"$set": student})

    if result.modified_count == 0:
        return Response(json.dumps({"error": "学生不存在"}), mimetype='application/json', status=404)

    return Response(json.dumps({"message": "学生更新成功", "id": id, "modified_count": result.modified_count}),
                    mimetype='application/json',
                    status=200)


@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    try:
        query = {"_id": ObjectId(id)}
    except InvalidId:
        return Response(json.dumps({"error": "Invalid ID"}), mimetype='application/json', status=400)
    result = db.students.delete_one(query)
    if result.deleted_count == 0:
        return Response(json.dumps({"error": "学生不存在"}), mimetype='application/json', status=404)
    return Response(json.dumps({"message": "学生删除成功", "id": id, "deleted_count": result.deleted_count}),
                    mimetype='application/json',
                    status=200)


if __name__ == "__main__":
    # 部署时使用
    # 使其在生产和开发环境都能工作
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
