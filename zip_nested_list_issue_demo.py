"""
演示 zip() 处理嵌套列表时可能出现的问题
"""

# 原始代码（正常工作）
print("=== 原始代码：纯数字向量 ===")
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]

dot_product = 0
for a_i, b_i in zip(a, b):
    dot_product += (a_i * b_i)

print(f"a = {a}")
print(f"b = {b}")
print(f"向量内积为：{dot_product}")
print()

# 问题代码：包含嵌套列表的向量
print("=== 问题代码：包含嵌套列表 ===")
a = [1, 2, [3, 4, 5]]
b = [6, 7, [8, 9, 0]]

print(f"a = {a}")
print(f"b = {b}")
print()

# 查看 zip 的结果
print("zip(a, b) 的配对结果：")
for pair in zip(a, b):
    print(f"  {pair}")
print()

# 尝试计算内积（会出错）
print("尝试计算内积：")
dot_product = 0
try:
    for a_i, b_i in zip(a, b):
        dot_product += (a_i * b_i)
    print(f"向量内积为：{dot_product}")
except TypeError as e:
    print(f"❌ 错误：{e}")
    print(f"   原因：无法将列表与数字或列表相乘")
print()

# 解决方案1：展平嵌套列表
print("=== 解决方案1：展平嵌套列表 ===")
def flatten(lst):
    """将嵌套列表展平"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

a_flat = flatten(a)
b_flat = flatten(b)

print(f"展平后 a = {a_flat}")
print(f"展平后 b = {b_flat}")

dot_product = 0
for a_i, b_i in zip(a_flat, b_flat):
    dot_product += (a_i * b_i)

print(f"向量内积为：{dot_product}")
print()

# 解决方案2：递归处理
print("=== 解决方案2：递归处理 ===")
def recursive_dot_product(a, b):
    """递归计算包含嵌套列表的向量内积"""
    result = 0
    for a_i, b_i in zip(a, b):
        if isinstance(a_i, list) and isinstance(b_i, list):
            result += recursive_dot_product(a_i, b_i)
        elif isinstance(a_i, list) or isinstance(b_i, list):
            # 一个是列表，一个是数字 - 需要展平
            a_flat = flatten([a_i]) if isinstance(a_i, list) else [a_i]
            b_flat = flatten([b_i]) if isinstance(b_i, list) else [b_i]
            result += sum(x * y for x, y in zip(a_flat, b_flat))
        else:
            result += a_i * b_i
    return result

dot_product = recursive_dot_product(a, b)
print(f"递归计算内积为：{dot_product}")
print()

# 解决方案3：使用 NumPy（推荐，需要安装 numpy）
print("=== 解决方案3：使用 NumPy ===")
try:
    import numpy as np
    a_np = np.array(flatten(a))
    b_np = np.array(flatten(b))
    dot_product = np.dot(a_np, b_np)
    print(f"NumPy 计算内积为：{dot_product}")
except ImportError:
    print("⚠️  NumPy 未安装，跳过此方案")
    print("   安装命令: pip install numpy")
print()

# 总结
print("=== 总结 ===")
print("当向量包含嵌套列表时，直接使用 zip() 会导致 TypeError")
print("因为 Python 无法对列表进行乘法运算")
print()
print("解决方案：")
print("1. 展平嵌套列表后再计算")
print("2. 使用递归处理嵌套结构")
print("3. 使用 NumPy 等数值计算库（推荐）")
