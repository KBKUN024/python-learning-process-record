"""
这个文件辨析了：关于@wraps在装饰器中的使用和重要性‼️
"""
from functools import wraps
import inspect

print("=== @wraps 的重要性演示 ===\n")

# 没有使用 @wraps 的装饰器
def decorator_without_wraps(func):
    def wrapper(*args, **kwargs):
        """这是包装器函数"""
        print("装饰器逻辑")
        return func(*args, **kwargs)
    return wrapper

# 使用了 @wraps 的装饰器  
def decorator_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """这是包装器函数"""
        print("装饰器逻辑")
        return func(*args, **kwargs)
    return wrapper

# 原始函数
def original_function(x, y):
    """
    这是原始函数的文档
    
    Args:
        x: 第一个参数
        y: 第二个参数
    Returns:
        x + y 的结果
    """
    return x + y

# 应用不同的装饰器
decorated_without_wraps = decorator_without_wraps(original_function)
decorated_with_wraps = decorator_with_wraps(original_function)

# 比较函数元信息
print("1. 函数名称比较:")
print(f"原始函数名: {original_function.__name__}")
print(f"没用@wraps: {decorated_without_wraps.__name__}")
print(f"使用@wraps: {decorated_with_wraps.__name__}")

print("\n2. 文档字符串比较:")
print(f"原始函数文档: {original_function.__doc__}")
print(f"没用@wraps: {decorated_without_wraps.__doc__}")
print(f"使用@wraps: {decorated_with_wraps.__doc__}")

print("\n3. 模块信息比较:")
print(f"原始函数模块: {original_function.__module__}")
print(f"没用@wraps: {decorated_without_wraps.__module__}")
print(f"使用@wraps: {decorated_with_wraps.__module__}")

print("\n4. 参数签名比较:")
print(f"原始函数签名: {inspect.signature(original_function)}")
print(f"没用@wraps: {inspect.signature(decorated_without_wraps)}")
print(f"使用@wraps: {inspect.signature(decorated_with_wraps)}")

print("\n=== 实际影响演示 ===")

# 这在调试和文档生成中很重要
def debug_function_info(func):
    """打印函数的调试信息"""
    print(f"函数名: {func.__name__}")
    print(f"文档: {func.__doc__[:50]}..." if func.__doc__ else "无文档")
    print(f"参数: {inspect.signature(func)}")

print("\n调试原始函数:")
debug_function_info(original_function)

print("\n调试未使用@wraps的装饰函数:")
debug_function_info(decorated_without_wraps)

print("\n调试使用@wraps的装饰函数:")
debug_function_info(decorated_with_wraps)

print("\n=== 最佳实践示例 ===")

def production_decorator(func):
    """
    生产级装饰器最佳实践
    """
    @wraps(func)  # ✅ 必须使用 @wraps
    def wrapper(*args, **kwargs):
        """
        包装器函数
        
        保持原函数的所有元信息完整
        """
        try:
            print(f"调用函数: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"函数 {func.__name__} 执行成功")
            return result
        except Exception as e:
            print(f"函数 {func.__name__} 执行失败: {e}")
            raise
    return wrapper

@production_decorator
def calculate(a: int, b: int) -> int:
    """
    计算两个数的和
    
    Args:
        a: 第一个整数
        b: 第二个整数
        
    Returns:
        两数之和
        
    Raises:
        TypeError: 当参数不是整数时
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("参数必须是整数")
    return a + b

# 测试生产级装饰器
print(f"\n装饰后的函数名: {calculate.__name__}")
print(f"装饰后的文档: {calculate.__doc__}")
print(f"装饰后的签名: {inspect.signature(calculate)}")

# 调用测试
result = calculate(10, 20)
print(f"计算结果: {result}")

print("\n=== @wraps 的技术细节 ===")

# @wraps 实际复制的属性
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__',
                       '__doc__', '__annotations__')
WRAPPER_UPDATES = ('__dict__',)

print("@wraps 复制的属性:")
for attr in WRAPPER_ASSIGNMENTS:
    print(f"  {attr}: {getattr(calculate, attr, '未设置')}")

print("\n@wraps 更新的属性:")  
for attr in WRAPPER_UPDATES:
    print(f"  {attr}: {getattr(calculate, attr, '未设置')}")

print(f"\n原始函数引用: {calculate.__wrapped__}")  # @wraps 会设置这个属性 