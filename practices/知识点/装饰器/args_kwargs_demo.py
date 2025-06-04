"""
这个文件辨析了：为什么装饰器必须用 *args, **kwargs
"""
from functools import wraps

print("=== 为什么装饰器必须用 *args, **kwargs ===\n")

# 错误示例：固定参数的装饰器
def bad_decorator(func):
    @wraps(func)
    def wrapper(a, b):  # ❌ 只能处理2个参数的函数
        print("调用前处理")
        return func(a, b)
    return wrapper

# 正确示例：通用装饰器
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):  # ✅ 能处理任意参数的函数
        print("调用前处理")
        return func(*args, **kwargs)
    return wrapper

# 测试函数们
def func1():
    return "无参数函数"

def func2(x):
    return f"单参数函数: {x}"

def func3(x, y):
    return f"双参数函数: {x}, {y}"

def func4(x, y, z=10):
    return f"带默认值: {x}, {y}, {z}"

def func5(x, y, *args, **kwargs):
    return f"复杂函数: {x}, {y}, args={args}, kwargs={kwargs}"

# 应用装饰器
@good_decorator
def test_func1():
    return "测试1"

@good_decorator  
def test_func2(x):
    return f"测试2: {x}"

@good_decorator
def test_func3(x, y, z=100, name="默认"):
    return f"测试3: {x}, {y}, {z}, {name}"

# 测试不同调用方式
print("1. 无参数调用:")
print(test_func1())

print("\n2. 位置参数调用:")
print(test_func2("hello"))

print("\n3. 混合参数调用:")
print(test_func3(1, 2))
print(test_func3(1, 2, 300))
print(test_func3(1, 2, z=400, name="自定义"))

print("\n4. 关键字参数调用:")
print(test_func3(x=10, y=20, name="关键字"))

print("\n=== wrapper参数能否为空？ ===")

# 错误示例：空参数装饰器
def empty_wrapper_decorator(func):
    @wraps(func)
    def wrapper():  # ❌ 不接收任何参数
        print("空包装器")
        return func()  # 只能调用无参数函数
    return wrapper

@empty_wrapper_decorator
def no_param_func():
    return "我没有参数"

print("空参数函数调用:", no_param_func())

# 如果对有参数的函数使用空包装器会出错
try:
    @empty_wrapper_decorator  
    def has_param_func(x):
        return f"我有参数: {x}"
    
    has_param_func(123)  # 这会报错
except TypeError as e:
    print(f"错误示例: {e}")

print("\n=== *args, **kwargs 的灵活性演示 ===")

@good_decorator
def flexible_func(*args, **kwargs):
    return f"位置参数: {args}, 关键字参数: {kwargs}"

print("调用1:", flexible_func())
print("调用2:", flexible_func(1, 2, 3))
print("调用3:", flexible_func(a=1, b=2))
print("调用4:", flexible_func(1, 2, c=3, d=4)) 