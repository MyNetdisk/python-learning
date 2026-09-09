# 1、创建一个名为 dog 的空字典
dog = dict()
print(f"空字典: {dog}")

# 2、向 dog 字典添加 name、color、breed、legs、age 键
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 2
print(f"dog 字典: {dog}")

# 3、创建一个学生字典
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 25,
    "marital status": "Single",
    "skills": ["Python", "JavaScript"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main St"
}
print(f"学生字典: {student}")

# 4、获取学生字典的长度
print(f"字典长度: {len(student)}")

# 5、获取 skills 的值并检查数据类型
print(f"skills 的值: {student['skills']}")
print(f"skills 的数据类型: {type(student['skills'])}")

# 6、修改 skills 值，添加一到两个技能
student["skills"].append("Java")
student["skills"].append("C++")
print(f"更新后的 skills: {student['skills']}")

# 7、获取字典的键列表
keys_list = list(student.keys())
print(f"键列表: {keys_list}")

# 8、获取字典的值列表
values_list = list(student.values())
print(f"值列表: {values_list}")

# 9、使用 items() 方法将字典变为由元组组成的列表
items_list = list(student.items())
print(f"元组列表: {items_list}")

# 10、删除字典中的一项
student.pop("age")
print(f"删除 age 后: {student}")

# 11、删除其中一个字典
del student
print("student 字典已被删除")
