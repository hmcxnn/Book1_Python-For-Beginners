"""
zip() 函数处理嵌套列表的演示
"""

# 示例1: zip 处理包含列表的列表（二维列表）
print("=== 示例1: zip 处理二维列表 ===")
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# zip 会按位置配对每个子列表
result = list(zip(list1, list2))
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"zip(list1, list2) = {result}")
print()

# 示例2: 使用 * 解包来"转置"二维列表
print("=== 示例2: 使用 * 解包转置二维列表 ===")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"原始矩阵 = {matrix}")

# *matrix 解包成三个独立的列表
transposed = list(zip(*matrix))
print(f"转置后 = {transposed}")
print()

# 示例3: 不规则嵌套列表（长度不同）
print("=== 示例3: 不规则嵌套列表 ===")
list1 = [[1, 2], [3, 4, 5], [6]]
list2 = [['a', 'b'], ['c', 'd', 'e'], ['f']]

result = list(zip(list1, list2))
print(f"zip(list1, list2) = {result}")
print("注意: zip 只会配对到最短的可迭代对象长度")
print()

# 示例4: 三层嵌套列表
print("=== 示例4: 三层嵌套列表 ===")
nested1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
nested2 = [[['a', 'b'], ['c', 'd']], [['e', 'f'], ['g', 'h']]]

result = list(zip(nested1, nested2))
print(f"zip(nested1, nested2) = {result}")
print()

# 示例5: 使用 zip 处理嵌套列表的元素
print("=== 示例5: 处理嵌套列表的元素 ===")
names = [['张', '三'], ['李', '四'], ['王', '五']]
ages = [[20], [25], [30]]

# zip 配对后，可以进一步处理
for name_list, age_list in zip(names, ages):
    full_name = ''.join(name_list)
    age = age_list[0]
    print(f"{full_name} 的年龄是 {age}")
print()

# 示例6: 使用 zip 和列表推导式处理嵌套列表
print("=== 示例6: zip + 列表推导式 ===")
list1 = [[1, 2, 3], [4, 5, 6]]
list2 = [[10, 20, 30], [40, 50, 60]]

# 对应元素相加
result = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(list1, list2)]
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"对应元素相加 = {result}")
print()

# 示例7: itertools.zip_longest 处理不等长嵌套列表
print("=== 示例7: itertools.zip_longest ===")
from itertools import zip_longest

list1 = [[1, 2, 3], [4, 5]]
list2 = [['a', 'b', 'c'], ['d', 'e', 'f']]

# zip_longest 可以填充缺失值
result = list(zip_longest(list1, list2, fillvalue=None))
print(f"zip_longest(list1, list2) = {result}")
print()

# 示例8: 多个嵌套列表同时 zip
print("=== 示例8: 多个嵌套列表 ===")
list1 = [[1, 2], [3, 4]]
list2 = [['a', 'b'], ['c', 'd']]
list3 = [[10, 20], [30, 40]]

result = list(zip(list1, list2, list3))
print(f"zip(list1, list2, list3) = {result}")
print()

# 总结
print("=== 总结 ===")
print("1. zip() 可以处理嵌套列表，它会按位置配对最外层的元素")
print("2. 使用 * 解包可以转置二维列表")
print("3. zip 只配对到最短的可迭代对象长度")
print("4. 对于不等长列表，使用 itertools.zip_longest")
print("5. 可以结合列表推导式处理嵌套列表的内部元素")
