# 集合
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1、合并 A 和 B
union_set = A.union(B)
print(f"A ∪ B = {union_set}")

# 2、找到 A 和 B 的交集
intersection_set = A.intersection(B)
print(f"A ∩ B = {intersection_set}")

# 3、A 是 B 的子集吗
is_subset = A.issubset(B)
print(f"A 是 B 的子集吗: {is_subset}")

# 4、A 和 B 是不相交集合吗
is_disjoint = A.isdisjoint(B)
print(f"A 和 B 是不相交集合吗: {is_disjoint}")

# 5、将 A 与 B 合并，反之亦然
union_AB = A.union(B)
union_BA = B.union(A)
print(f"A ∪ B = {union_AB}")
print(f"B ∪ A = {union_BA}")

# 6、A 和 B 之间的对称差异是什么
symmetric_difference = A.symmetric_difference(B)
print(f"A △ B = {symmetric_difference}")

# 7、完全删除集合
del A
del B
del it_companies
print("集合 A、B、it_companies 已被删除")
