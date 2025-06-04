"""
这个文件辨析了：一个带参数的类型检查装饰器的执行流程
"""
from functools import wraps
from typing import Any, Callable

def type_check(*expected_types):
    """
    参数化装饰器：检查函数参数类型
    
    Args:
        *expected_types: 期望的参数类型序列
    下面的“第1层执行”和“第2层执行”的两个print会在装饰器装饰到被装饰函数上时立即执行，但是内部的wrapper只有在被装饰函数执行的时候才会执行。
    """
    print(f"第1层执行: 接收期望类型 {expected_types}")
    
    def decorator(func: Callable) -> Callable:
        print(f"第2层执行: 接收函数 {func.__name__}")
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"第3层执行: 实际调用时，参数为 args={args}, kwargs={kwargs}")
            
            # 详细解析for循环
            print("\n--- for循环详细分析 ---")
            print(f"==args==: {args}")
            print(f"==expected_types==: {expected_types}")
            print(f"==zip(args, expected_types)==: {zip(args, expected_types)}")
            print(f"==list(zip(args, expected_types))==: {list(zip(args, expected_types))}")
            print(f"==list(enumerate(...))==: {list(enumerate(zip(args, expected_types)))}")
            print(f"==enumerate(...)==: {enumerate(zip(args, expected_types))}")
            
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                print(f"检查第{i+1}个参数: {arg} (类型:{type(arg)}) 是否为 {expected_type}")
                if not isinstance(arg, expected_type):
                    raise TypeError(f"参数 {i+1} 应该是 {expected_type.__name__} 类型，实际是 {type(arg).__name__}")
                print(f"✓ 第{i+1}个参数类型正确")
            
            print("--- 类型检查完成，执行原函数 ---\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用示例
@type_check(int, str, float)
def calculate_score(age: int, name: str, score: float) -> str:
    return f"{name}({age}岁) 的分数是 {score}"

# 测试正确调用
print("=== 正确调用测试 ===")
result = calculate_score(25, "张三", 95.5)
print(f"结果: {result}")

print("\n=== 错误调用测试 ===")
try:
    # 这会触发类型错误
    calculate_score("25", "张三", 95.5)  # age应该是int但传了str
except TypeError as e:
    print(f"捕获错误: {e}")

# 演示zip和enumerate的工作原理
print("\n=== zip和enumerate演示 ===")
args_example = (25, "张三", 95.5)
types_example = (int, str, float)

print(f"args: {args_example}")
print(f"types: {types_example}")
print(f"zip(args, types): {list(zip(args_example, types_example))}")
print(f"enumerate(...): {list(enumerate(zip(args_example, types_example)))}")

for i, (arg, expected_type) in enumerate(zip(args_example, types_example)):
    print(f"索引{i}: 参数{arg} -> 期望类型{expected_type}") 