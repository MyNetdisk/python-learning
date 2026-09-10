person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': '芬兰',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '太空街',
        'zipcode': '02210'
    }
}

# 1、检查是否有 skills 键，如果有则打印中间技能
if 'skills' in person:
    skills = person['skills']
    mid = len(skills) // 2
    print(f"中间技能: {skills[mid]}")
else:
    print('没有技能信息')

# 2、检查是否有 skills 键，如果有则检查是否具备 Python 技能
if 'skills' in person:
    if 'Python' in person['skills']:
        print('他有 Python 技能')
    else:
        print('他没有 Python 技能')
else:
    print('没有技能信息')

# 3、根据技能判断开发者类型
skills = person.get('skills', [])
skills_set = set(skills)

if skills:
    if skills_set >= {'React', 'Node', 'MongoDB'}:
        print('他是全栈开发者')
    elif skills_set >= {'Node', 'Python', 'MongoDB'}:
        print('他是后端开发者')
    elif skills_set >= {'JavaScript', 'React'}:
        print('他是前端开发者')
    else:
        print('未知头衔')
else:
    print('没有技能信息')

# 4、如果该人结婚了且居住在芬兰，打印信息
if person.get('is_married') and person.get('country') == '芬兰':
    print(f"{person['first_name']} {person['last_name']}住在{person['country']}。他已婚。")
