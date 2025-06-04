"""
这个文件超级详细的解释了：带参数的装饰器执行时机
"""
from functools import wraps
from typing import Any, Callable

print("=== 装饰器执行时机详细分析 ===\n")

def type_check(*expected_types):
    """参数化装饰器：检查函数参数类型"""
    print(f"🔥 第1层执行: type_check({expected_types}) 被调用")
    print("   ↳ 这发生在：Python解释器遇到 @type_check(int, str) 时")
    
    def decorator(func: Callable) -> Callable:
        print(f"🔥 第2层执行: decorator({func.__name__}) 被调用")
        print("   ↳ 这发生在：装饰器语法糖的第二阶段")
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"🔥 第3层执行: wrapper被调用，参数{args}")
            print("   ↳ 这发生在：实际调用被装饰的函数时")
            return func(*args, **kwargs) # 这里开始真正执行被装饰的函数，也就是说，经过一系列的装饰操作（做其他事情），现在终于可以执行被装饰的函数本体了，做的一系列操作实际上就是扩展了被装饰的原函数的功能
        """
            注意⚠️了注意⚠️了！你可能现在又不理解装饰器了，你可能有下面的疑问：
                当我在调用greet(25,'Alice')的时候，是不是实际上就相当于调用:wrapper(25,'Alice')?
            然后我发现在wrapper内部是return func(*args, **kwargs)，是不是意思就是直接在wrapper返回func的执行结果？
            所以表现出来的就是我调用greet(25,'Alice')的时候，就好像和没装饰的时候一样直接执行的？
            ✅没错，我的上述理解都是正确的。
            装饰器的本质
            1. 调用替换：greet(25, 'Alice') 实际上就是 wrapper(25, 'Alice')
                - 因为装饰后 greet 已经指向了 wrapper 函数对象
            2. 透明代理：wrapper 内部的 return func(*args, **kwargs) 确实是：
                - 直接返回原始函数的执行结果
                - func 保存着原始的 greet 函数引用
            3. 用户体验：表现得"像没装饰一样"是因为：
                - wrapper 做完额外工作（如类型检查、日志等）后
                - 原样调用并返回原函数结果
                - 对外接口保持一致
            调用链：greet(25, 'Alice') → wrapper(25, 'Alice') → 相当于是调用原始的greet(25, 'Alice')，因为wrapper会返回这个函数的执行结果
            这就是装饰器的透明增强模式：在不改变原函数接口的前提下，扩展其功能。
        """
        print(f"   ↳ decorator返回wrapper函数对象: {wrapper}") # 这里输出： <function greet at 0x1063b7380>，因为被包裹的函数名字叫做greet，所以这里是function greet
        return wrapper
    
    print(f"   ↳ type_check返回decorator函数对象: {decorator}") # 会输出：<function type_check.<locals>.decorator at 0x1063b5b20>，其中的...<locals>.decorator中的decorator其实可以自定义，和你写的函数名有关，比如你叫decorator1，这里就是<locals>.decorator1
    return decorator

print("\n=== 关键理解：装饰器语法糖的等价形式 ===")

print("当你写：")
print("@type_check(int, str)")
print("def my_func(a, b):")
print("    return a + b")

print("\n等价于：")
print("def my_func(a, b):")
print("    return a + b")
print("my_func = type_check(int, str)(my_func)") # 👀这里实际上非常清晰明了了，被装饰的时候，先执行type_check(int, str)，它会返回一个第二层的decorator，又因为type_check(int, str)(my_func)的最右边又个小括号，其实就相当于decorator(my_func),这很明显了吧，没错，就是执行这个decorator，所以第二层才会被执行到

print("\n让我们一步步分解：")
print("1. type_check(int, str)     ← 第1层执行，返回decorator")
print("2. decorator(my_func)       ← 第2层执行，返回wrapper")
print("3. my_func = wrapper        ← my_func现在指向wrapper")

print("\n=== 实际演示 ===")

print("定义装饰器...")
# 装饰器定义时没有任何执行

print("\n开始装饰函数...")

@type_check(int, str)  # 这里会执行第1层和第2层！
def greet(age, name):
    """问候函数"""
    return f"Hello {name}, you are {age} years old"

print("\n装饰完成！函数还没有被调用。")
print(f"greet 现在指向: {greet}") # 输出：<function greet at 0x1063b7380>， 这是一个wrapper对象，可以看到，和装饰器内部输出的wrapper的引用是一样的
print(f"greet.__name__: {greet.__name__}")

print("\n现在调用函数...")
result = greet(25, "Alice")  # 这里才执行第3层wrapper！
print(f"调用结果: {result}")

print("\n=== 为什么第2层decorator会立即执行？ ===")

print("因为装饰器语法等价于两次连续的函数调用：")

print("\n手动模拟装饰过程：")
def manual_func(x, y):
    return x * y

print("步骤1: 调用 type_check(int, int)")
step1_result = type_check(int, int)  # 第1层执行
print(f"步骤1结果: {step1_result} (这是decorator函数)")

print("\n步骤2: 调用 decorator(manual_func)")  
step2_result = step1_result(manual_func)  # 第2层执行
print(f"步骤2结果: {step2_result} (这是wrapper函数)")

print("\nmanual_func 现在指向wrapper:")
manual_func = step2_result

print("\n调用装饰后的函数:")
result = manual_func(3, 4)  # 第3层执行
print(f"最终结果: {result}")

print("\n=== 执行时机总结 ===")
print("✅ 第1层 type_check():     在遇到@语法时立即执行")
print("✅ 第2层 decorator():      在装饰过程中立即执行")  
print("⏰ 第3层 wrapper():        只在实际调用函数时执行")

print("\n=== 证明：装饰器在导入时就执行 ===")

print("即使我们不调用函数，装饰过程也已经完成：")

@type_check(float, str, bool)
def never_called_function(price, name, active):
    """这个函数永远不会被调用"""
    return f"{name}: ${price}, active={active}"

print("看到了吗？即使不调用 never_called_function，")
print("第1层和第2层的代码也已经执行了！")

print("\n=== 这就是为什么模块导入时装饰器会执行 ===")
print("当Python导入一个模块时，所有的@装饰器都会立即执行前两层代码！") 