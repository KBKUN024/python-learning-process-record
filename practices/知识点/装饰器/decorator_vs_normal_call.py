"""
这个文件辨析了：装饰器 vs 普通函数调用的区别
"""
print("=== 装饰器 vs 普通函数调用的区别 ===\n")

def my_decorator_factory(param):
    """装饰器工厂函数"""
    print(f"🎯 装饰器工厂被调用: param={param}")
    
    def decorator(func):
        print(f"🎯 装饰器被调用: func={func.__name__}")
        
        def wrapper(*args, **kwargs):
            print(f"🎯 包装器被调用: args={args}")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

def my_normal_function(param):
    """普通函数"""
    print(f"🔴 普通函数被调用: param={param}")
    
    def inner_function(func):
        print(f"🔴 内部函数被调用: func={func.__name__}")
        return func
    
    return inner_function

print("=== 情况1: 使用装饰器语法 ===")
print("写代码: @my_decorator_factory('hello')")

@my_decorator_factory('hello')  # 立即执行！
def test_function1():
    return "test1"

print("装饰完成，函数定义完毕\n")

print("=== 情况2: 手动调用相同的函数 ===")
print("写代码: result = my_normal_function('hello')")

# 只有显式调用才会执行
print("现在调用 my_normal_function('hello'):")
result = my_normal_function('hello')

print(f"返回值: {result}")

def test_function2():
    return "test2"

print("现在调用 result(test_function2):")
final_result = result(test_function2)
print(f"最终结果: {final_result}\n")

print("=== 关键区别总结 ===")
print("装饰器语法 @my_decorator_factory('hello'):")
print("  ✅ Python解释器自动执行两次调用")
print("  ✅ my_decorator_factory('hello') 立即执行")
print("  ✅ 返回的decorator(test_function1) 立即执行")
print()
print("普通函数调用:")
print("  ⚪ 只有你显式调用时才执行")
print("  ⚪ my_normal_function('hello') 需要手动调用")
print("  ⚪ 返回的函数也需要手动调用")

print("\n=== 这就是为什么你的观察是正确的！ ===")
print("@type_check(int, str) 等价于:")
print("1. temp_decorator = type_check(int, str)    # 第1层立即执行")
print("2. my_func = temp_decorator(my_func)        # 第2层立即执行")
print("3. wrapper代码只在调用my_func()时才执行     # 第3层延迟执行")

print("\n=== 模块导入时的影响 ===")
print("当你import一个模块时:")
print("- 所有@装饰器都会立即执行前两层")
print("- 即使你从不调用被装饰的函数")
print("- 这就是为什么有些装饰器会影响导入性能") 