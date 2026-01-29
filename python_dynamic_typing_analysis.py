"""
Python动态类型分析示例
演示动态类型对性能和内存使用的影响
"""

import sys
import time
from typing import Union

def demonstrate_dynamic_typing():
    """演示Python动态类型的特点"""
    print("=== Python动态类型演示 ===")
    
    # 同一个变量可以存储不同类型的数据
    x = 42  # 整数
    print(f"x = {x}, type: {type(x)}, size: {sys.getsizeof(x)} bytes")
    
    x = "Hello"  # 字符串
    print(f"x = {x}, type: {type(x)}, size: {sys.getsizeof(x)} bytes")
    
    x = [1, 2, 3, 4, 5]  # 列表
    print(f"x = {x}, type: {type(x)}, size: {sys.getsizeof(x)} bytes")
    
    x = {"key": "value"}  # 字典
    print(f"x = {x}, type: {type(x)}, size: {sys.getsizeof(x)} bytes")


def compare_memory_overhead():
    """比较Python对象的内存开销"""
    print("\n=== 内存开销比较 ===")
    
    # Python整数对象的开销
    python_int = 42
    print(f"Python int: {sys.getsizeof(python_int)} bytes (值: {python_int})")
    
    # Python字符串对象的开销  
    python_str = "A"
    print(f"Python str: {sys.getsizeof(python_str)} bytes (值: '{python_str}')")
    
    # 列表中的每个元素都是对象引用
    int_list = [1, 2, 3, 4, 5]
    print(f"Python list of 5 ints: {sys.getsizeof(int_list)} bytes")
    
    # 计算列表中所有整数对象的总开销
    total_int_overhead = sum(sys.getsizeof(item) for item in int_list)
    print(f"所有整数对象总开销: {total_int_overhead} bytes")
    print(f"总内存使用: {sys.getsizeof(int_list) + total_int_overhead} bytes")


def performance_comparison():
    """性能比较：动态类型 vs 静态类型思维"""
    print("\n=== 性能比较 ===")
    
    # 动态类型：需要运行时类型检查
    def dynamic_add(a, b):
        """动态类型加法，运行时类型检查"""
        return a + b
    
    # 模拟静态类型：使用类型提示（但仍是动态）
    def typed_add(a: int, b: int) -> int:
        """带类型提示的加法"""
        return a + b
    
    # 性能测试
    numbers = list(range(1000000))
    
    # 测试动态加法
    start = time.time()
    result1 = sum(dynamic_add(i, 1) for i in numbers[:10000])
    dynamic_time = time.time() - start
    
    # 测试"类型化"加法
    start = time.time() 
    result2 = sum(typed_add(i, 1) for i in numbers[:10000])
    typed_time = time.time() - start
    
    print(f"动态加法耗时: {dynamic_time:.4f} 秒")
    print(f"类型提示加法耗时: {typed_time:.4f} 秒")
    print(f"注意：类型提示在运行时不会进行实际的类型检查")


def demonstrate_type_checking_overhead():
    """演示类型检查开销"""
    print("\n=== 类型检查开销演示 ===")
    
    def flexible_function(data):
        """灵活处理不同类型的函数"""
        if isinstance(data, int):
            return data * 2
        elif isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return len(data)
        else:
            return str(data)
    
    test_data = [
        42,
        "hello",
        [1, 2, 3, 4, 5],
        {"key": "value"}
    ]
    
    # 测试运行时类型检查的开销
    start = time.time()
    for _ in range(100000):
        for item in test_data:
            result = flexible_function(item)
    overhead_time = time.time() - start
    
    print(f"处理 {len(test_data)} 种不同类型数据 100000 次")
    print(f"总耗时: {overhead_time:.4f} 秒")
    print(f"平均每次类型检查: {(overhead_time / (100000 * len(test_data))) * 1000000:.2f} 微秒")


def analyze_python_object_model():
    """分析Python对象模型的开销"""
    print("\n=== Python对象模型分析 ===")
    
    # 每个Python对象都包含额外的元数据
    class SimpleClass:
        def __init__(self, value):
            self.value = value
    
    obj = SimpleClass(42)
    
    print("Python对象的组成部分：")
    print(f"1. 对象本身: {sys.getsizeof(obj)} bytes")
    print(f"2. 对象的__dict__: {sys.getsizeof(obj.__dict__)} bytes")
    print(f"3. 类对象: {sys.getsizeof(SimpleClass)} bytes")
    
    # 演示装箱开销
    print("\n装箱开销示例：")
    # 在C语言中，一个int通常是4或8字节
    # 在Python中，每个int都是一个对象
    small_int = 1
    big_int = 2**100
    
    print(f"小整数 1: {sys.getsizeof(small_int)} bytes")
    print(f"大整数 2^100: {sys.getsizeof(big_int)} bytes")


if __name__ == "__main__":
    demonstrate_dynamic_typing()
    compare_memory_overhead()
    performance_comparison()
    demonstrate_type_checking_overhead()
    analyze_python_object_model()
    
    print("\n=== 结论 ===")
    print("""
    Python的动态类型确实会导致一定程度的"臃肿"，主要体现在：
    
    1. 内存开销：
       - 每个对象都需要存储类型信息
       - 装箱操作：简单数据类型也被包装成对象
       - 额外的元数据和引用计数信息
    
    2. 性能开销：
       - 运行时类型检查
       - 动态方法查找
       - 类型推断和验证
    
    3. 但动态类型也带来了：
       - 编程灵活性
       - 代码简洁性
       - 快速原型开发
       - 多态性的天然支持
    
    这是一种设计权衡：用一些性能和内存换取开发效率和语言表达力。
    """)