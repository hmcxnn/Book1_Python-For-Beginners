import numpy as np
import matplotlib.pyplot as plt

# 创建简单的一维数组
x1_array = np.array([1, 2, 3])
x2_array = np.array([10, 20])

print("原始数组:")
print("x1_array =", x1_array)
print("x2_array =", x2_array)
print()

# 使用 meshgrid 创建二维网格
xx1, xx2 = np.meshgrid(x1_array, x2_array)

print("meshgrid 结果:")
print("xx1 (行坐标网格):")
print(xx1)
print("\nxx2 (列坐标网格):")
print(xx2)
print()

print("分析:")
print("xx1 中，每一行的值都相同：")
print("  第0行:", xx1[0, :], "- 都是来自 x1_array 的值")
print("  第1行:", xx1[1, :], "- 都是来自 x1_array 的值")
print()

print("xx2 中，每一列的值都相同：")
print("  第0列:", xx2[:, 0], "- 都是来自 x2_array 的值")
print("  第1列:", xx2[:, 1], "- 都是来自 x2_array 的值") 
print("  第2列:", xx2[:, 2], "- 都是来自 x2_array 的值")
print()

print("配对坐标点:")
for i in range(xx1.shape[0]):
    for j in range(xx1.shape[1]):
        print(f"点({i},{j}): (x1={xx1[i,j]}, x2={xx2[i,j]})")

# 可视化
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(xx1, cmap='viridis', aspect='auto')
plt.title('xx1 (每行相同)')
plt.colorbar()
for i in range(xx1.shape[0]):
    for j in range(xx1.shape[1]):
        plt.text(j, i, f'{xx1[i,j]}', ha='center', va='center', color='white', fontweight='bold')

plt.subplot(1, 3, 2)
plt.imshow(xx2, cmap='plasma', aspect='auto')
plt.title('xx2 (每列相同)')
plt.colorbar()
for i in range(xx2.shape[0]):
    for j in range(xx2.shape[1]):
        plt.text(j, i, f'{xx2[i,j]}', ha='center', va='center', color='white', fontweight='bold')

plt.subplot(1, 3, 3)
plt.scatter(xx1.flatten(), xx2.flatten(), s=100, alpha=0.7, c='red')
for i in range(xx1.shape[0]):
    for j in range(xx1.shape[1]):
        plt.annotate(f'({xx1[i,j]},{xx2[i,j]})', 
                    (xx1[i,j], xx2[i,j]), 
                    xytext=(5, 5), textcoords='offset points')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('所有坐标点')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n总结:")
print("您的理解完全正确！")
print("- xx1: 每一行的值都相同（水平方向重复 x1_array）")
print("- xx2: 每一列的值都相同（垂直方向重复 x2_array）")
print("这样就形成了所有可能的 (x1, x2) 坐标组合的完整网格。")