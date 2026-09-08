# 1、创建一个空元组
empty_tuple = tuple()
print(empty_tuple)

# 2、创建一个包含你姐妹和兄弟名字的元组
sisters = ('sister1', 'sister2')
brothers = ('brother1', 'brother2')
print(f"姐妹: {sisters}")
print(f"兄弟: {brothers}")

# 3、连接兄弟姐妹元组并将其分配给 siblings
siblings = sisters + brothers
print(f"所有兄弟姐妹: {siblings}")

# 4、你有多少兄弟姐妹？
print(f"兄弟姐妹数量: {len(siblings)}")

# 5、修改兄弟姐妹元组并添加你父母的名字，然后将其分配给 family_members
family_members = siblings + ('mother', 'father')
print(f"家庭成员: {family_members}")
