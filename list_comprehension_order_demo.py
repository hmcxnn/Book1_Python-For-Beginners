"""
演示嵌套列表生成式的计算顺序
"""

# 嵌套列表生成式
matrix = [[i * j for j in range(1, 4)] 
                 for i in range(1, 4)]

print("最终结果：")
for row in matrix:
    print(row)
print()

# ========================================
# 计算顺序详解
# ========================================
print("=" * 50)
print("计算顺序详解：")
print("=" * 50)
print()

print("代码结构：")
print("[[i * j for j in range(1, 4)]   # 内层：生成一行")
print("      for i in range(1, 4)]    # 外层：控制行数")
print()

print("计算顺序：")
print()

# 外层循环 i
print("外层循环：for i in range(1, 4)")
print("  i = 1:")
print("    内层循环：for j in range(1, 4)")
print("      j = 1:  i * j = 1 * 1 = 1")
print("      j = 2:  i * j = 1 * 2 = 2")
print("      j = 3:  i * j = 1 * 3 = 3")
print("    生成第一行: [1, 2, 3]")
print()

print("  i = 2:")
print("    内层循环：for j in range(1, 4)")
print("      j = 1:  i * j = 2 * 1 = 2")
print("      j = 2:  i * j = 2 * 2 = 4")
print("      j = 3:  i * j = 2 * 3 = 6")
print("    生成第二行: [2, 4, 6]")
print()

print("  i = 3:")
print("    内层循环：for j in range(1, 4)")
print("      j = 1:  i * j = 3 * 1 = 3")
print("      j = 2:  i * j = 3 * 2 = 6")
print("      j = 3:  i * j = 3 * 3 = 9")
print("    生成第三行: [3, 6, 9]")
print()

print("=" * 50)
print("关键点：")
print("=" * 50)
print("1. 外层 for i 在后面，控制生成多少行")
print("2. 内层 for j 在前面，控制每行有多少个元素")
print("3. 计算顺序：外层 i 先固定，内层 j 变化")
print("4. 这与普通 for 循环的嵌套顺序一致！")
print()

# ========================================
# 对比普通 for 循环
# ========================================
print("=" * 50)
print("等价的普通 for 循环：")
print("=" * 50)
print()

matrix2 = []
for i in range(1, 4):          # 外层循环
    row = []
    for j in range(1, 4):      # 内层循环
        row.append(i * j)
    matrix2.append(row)

print("结果相同：")
for row in matrix2:
    print(row)
print()

print("=" * 50)
print("记忆技巧：")
print("=" * 50)
print("从右向左读：")
print("  for i in range(1, 4)  →  外层，控制行")
print("  for j in range(1, 4)  →  内层，控制列")
print("  i * j                  →  每个元素的值")
