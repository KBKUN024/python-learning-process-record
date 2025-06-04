# Python语法练习题答案（30题）

## 基础变量和数据类型（1-5题）

### 题目1：变量赋值与类型检查 - 答案

```python
# 创建变量
age = 25
height = 1.75
name = "张三"
is_student = True
hobbies = ["读书", "游泳", "编程"]

# 打印类型
print(f"age的类型是: {type(age)}")
print(f"height的类型是: {type(height)}")
print(f"name的类型是: {type(name)}")
print(f"is_student的类型是: {type(is_student)}")
print(f"hobbies的类型是: {type(hobbies)}")
```

### 题目2：数据类型转换 - 答案

```python
# 字符串转整数，加77，再转回字符串
num_str = "123"
num_int = int(num_str)
result = num_int + 77
result_str = str(result)
print(f"结果: {result_str}")

# 简化写法
result = str(int("123") + 77)
print(f"简化结果: {result}")
```

### 题目3：多重赋值 - 答案

```python
# 多重赋值
x, y, z = 10, 20, 30
print(f"初始值: x={x}, y={y}, z={z}")

# 交换x和y的值
x, y = y, x
print(f"交换后: x={x}, y={y}, z={z}")
```

### 题目4：格式化字符串 - 答案

```python
name = "李四"
score = 85.5

# f-string格式化
result = f"学生{name}的成绩是{score}分"
print(result)

# 其他格式化方法
result2 = "学生{}的成绩是{}分".format(name, score)
result3 = "学生%s的成绩是%.1f分" % (name, score)
print(result2)
print(result3)
```

### 题目5：输入处理 - 答案

```python
# 获取用户输入并判断是否成年
try:
    age_input = input("请输入您的年龄: ")
    age = int(age_input)
    
    if age >= 18:
        print("您已成年")
    else:
        print("您还未成年")
        
except ValueError:
    print("请输入有效的数字")
```

## 字符串操作（6-10题）

### 题目6：字符串基本操作 - 答案

```python
text = "Hello Python World"

# 转换为大写
upper_text = text.upper()
print(f"大写: {upper_text}")

# 转换为小写
lower_text = text.lower()
print(f"小写: {lower_text}")

# 获取字符串长度
length = len(text)
print(f"长度: {length}")

# 检查是否包含 "Python"
contains_python = "Python" in text
print(f"包含Python: {contains_python}")
```

### 题目7：字符串切片 - 答案

```python
s = "programming"

# 获取前5个字符
first_five = s[:5]
print(f"前5个字符: {first_five}")

# 获取后5个字符
last_five = s[-5:]
print(f"后5个字符: {last_five}")

# 获取中间的字符（从索引2到8）
middle = s[2:8]
print(f"中间字符: {middle}")

# 反转整个字符串
reversed_s = s[::-1]
print(f"反转字符串: {reversed_s}")
```

### 题目8：字符串分割与连接 - 答案

```python
email = "user@example.com"

# 使用@分割字符串
parts = email.split("@")
print(f"分割结果: {parts}")

# 将分割后的部分用_连接起来
joined = "_".join(parts)
print(f"连接结果: {joined}")
```

### 题目9：字符串替换 - 答案

```python
sentence = "我喜欢苹果，苹果很甜"

# 替换所有的"苹果"为"橘子"
new_sentence = sentence.replace("苹果", "橘子")
print(f"替换后: {new_sentence}")
```

### 题目10：字符串验证 - 答案

```python
# 测试字符串
test_strings = ["123", "abc", "123abc", "hello", "world123"]

for s in test_strings:
    print(f"\n字符串: '{s}'")
    print(f"全部是数字: {s.isdigit()}")
    print(f"全部是字母: {s.isalpha()}")
    print(f"以'he'开头: {s.startswith('he')}")
    print(f"以'lo'结尾: {s.endswith('lo')}")
```

## 列表操作（11-15题）

### 题目11：列表基本操作 - 答案

```python
numbers = [1, 2, 3, 4, 5]
print(f"初始列表: {numbers}")

# 在末尾添加数字6
numbers.append(6)
print(f"添加6后: {numbers}")

# 在开头插入数字0
numbers.insert(0, 0)
print(f"插入0后: {numbers}")

# 删除数字3
numbers.remove(3)
print(f"删除3后: {numbers}")

# 获取列表长度
length = len(numbers)
print(f"列表长度: {length}")
```

### 题目12：列表切片与索引 - 答案

```python
fruits = ["苹果", "香蕉", "橘子", "葡萄", "桃子"]

# 获取前三个水果
first_three = fruits[:3]
print(f"前三个水果: {first_three}")

# 获取最后两个水果
last_two = fruits[-2:]
print(f"最后两个水果: {last_two}")

# 获取每隔一个的水果（步长为2）
every_other = fruits[::2]
print(f"每隔一个的水果: {every_other}")
```

### 题目13：列表推导式 - 答案

```python
# 0到9的平方数列表
squares = [x**2 for x in range(10)]
print(f"平方数列表: {squares}")

# 1到20中的偶数列表
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"偶数列表: {evens}")

# 字符串长度列表
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(f"字符串长度列表: {lengths}")
```

### 题目14：列表排序与查找 - 答案

```python
scores = [88, 92, 76, 85, 98, 79]
print(f"原始列表: {scores}")

# 升序排序
scores_asc = sorted(scores)
print(f"升序排序: {scores_asc}")

# 降序排序
scores_desc = sorted(scores, reverse=True)
print(f"降序排序: {scores_desc}")

# 最大值和最小值
max_score = max(scores)
min_score = min(scores)
print(f"最大值: {max_score}, 最小值: {min_score}")

# 计算平均值
average = sum(scores) / len(scores)
print(f"平均值: {average:.2f}")
```

### 题目15：嵌套列表 - 答案

```python
# 创建3x3矩阵
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("初始矩阵:")
for row in matrix:
    print(row)

# 访问第2行第3列的元素（索引从0开始）
element = matrix[1][2]
print(f"\n第2行第3列的元素: {element}")

# 修改第1行第1列的元素
matrix[0][0] = 100
print(f"\n修改后第1行第1列的元素: {matrix[0][0]}")

# 打印整个矩阵
print("\n修改后的矩阵:")
for row in matrix:
    print(row)
```

## 字典与元组（16-20题）

### 题目16：字典基本操作 - 答案

```python
student = {"name": "王五", "age": 20, "major": "计算机"}
print(f"初始字典: {student}")

# 添加新的键值对
student["grade"] = "大二"
print(f"添加grade后: {student}")

# 修改年龄
student["age"] = 21
print(f"修改年龄后: {student}")

# 删除专业信息
del student["major"]
print(f"删除major后: {student}")

# 获取所有键和值
keys = list(student.keys())
values = list(student.values())
print(f"所有键: {keys}")
print(f"所有值: {values}")
```

### 题目17：字典遍历 - 答案

```python
scores = {"数学": 90, "英语": 85, "物理": 88}

# 遍历并打印所有科目和成绩
print("所有科目和成绩:")
for subject, score in scores.items():
    print(f"{subject}: {score}")

# 找出成绩最高的科目
max_subject = max(scores, key=scores.get)
max_score = scores[max_subject]
print(f"\n成绩最高的科目: {max_subject} ({max_score}分)")

# 计算总分和平均分
total_score = sum(scores.values())
average_score = total_score / len(scores)
print(f"总分: {total_score}")
print(f"平均分: {average_score:.2f}")
```

### 题目18：元组操作 - 答案

```python
coordinates = (10, 20, 30)

# 访问各个元素
print(f"第1个元素: {coordinates[0]}")
print(f"第2个元素: {coordinates[1]}")
print(f"第3个元素: {coordinates[2]}")

# 尝试修改元组（会产生错误）
try:
    coordinates[0] = 100
except TypeError as e:
    print(f"修改元组出错: {e}")

# 将元组转换为列表，修改后再转换回元组
coord_list = list(coordinates)
coord_list[0] = 100
new_coordinates = tuple(coord_list)
print(f"原始元组: {coordinates}")
print(f"修改后的元组: {new_coordinates}")
```

### 题目19：字典推导式 - 答案

```python
words = ["apple", "banana", "cherry"]

# 单词到其长度的映射
word_lengths = {word: len(word) for word in words}
print(f"单词长度映射: {word_lengths}")

# 单词到其首字母的映射
word_first_letters = {word: word[0] for word in words}
print(f"单词首字母映射: {word_first_letters}")
```

### 题目20：数据结构综合 - 答案

```python
# 学生成绩管理系统
class StudentManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, age, subjects_scores):
        """添加新学生"""
        self.students[name] = {
            "age": age,
            "scores": subjects_scores
        }
        print(f"学生 {name} 添加成功")
    
    def query_student(self, name):
        """查询学生信息"""
        if name in self.students:
            student = self.students[name]
            print(f"姓名: {name}")
            print(f"年龄: {student['age']}")
            print(f"成绩: {student['scores']}")
            return student
        else:
            print(f"未找到学生 {name}")
            return None
    
    def calculate_average(self, name):
        """计算学生平均分"""
        if name in self.students:
            scores = self.students[name]["scores"]
            average = sum(scores.values()) / len(scores)
            print(f"{name} 的平均分: {average:.2f}")
            return average
        else:
            print(f"未找到学生 {name}")
            return None

# 使用示例
manager = StudentManager()

# 添加学生
manager.add_student("张三", 20, {"数学": 90, "英语": 85, "物理": 88})
manager.add_student("李四", 19, {"数学": 78, "英语": 92, "物理": 85})

# 查询学生信息
manager.query_student("张三")

# 计算平均分
manager.calculate_average("张三")
```

## 控制流程（21-25题）

### 题目21：条件判断 - 答案

```python
def analyze_number(num):
    """分析数字的性质"""
    # 正数、负数或零
    if num > 0:
        sign = "正数"
    elif num < 0:
        sign = "负数"
    else:
        sign = "零"
    
    # 奇数或偶数
    if num != 0:
        parity = "偶数" if num % 2 == 0 else "奇数"
    else:
        parity = "零（既不是奇数也不是偶数）"
    
    # 是否能被3整除
    divisible_by_3 = "能被3整除" if num % 3 == 0 else "不能被3整除"
    
    print(f"数字 {num} 是 {sign}，{parity}，{divisible_by_3}")

# 测试
test_numbers = [15, -8, 0, 7, 12]
for num in test_numbers:
    analyze_number(num)
```

### 题目22：多重条件 - 答案

```python
def grade_level(score):
    """根据成绩划分等级"""
    if 90 <= score <= 100:
        return "优秀"
    elif 80 <= score <= 89:
        return "良好"
    elif 70 <= score <= 79:
        return "中等"
    elif 60 <= score <= 69:
        return "及格"
    elif 0 <= score <= 59:
        return "不及格"
    else:
        return "无效成绩"

# 测试
test_scores = [95, 85, 75, 65, 45, 105]
for score in test_scores:
    level = grade_level(score)
    print(f"成绩 {score} 分: {level}")
```

### 题目23：循环基础 - 答案

```python
# 1. 计算1到100的和
# for循环
sum_for = 0
for i in range(1, 101):
    sum_for += i
print(f"for循环计算1到100的和: {sum_for}")

# while循环
sum_while = 0
i = 1
while i <= 100:
    sum_while += i
    i += 1
print(f"while循环计算1到100的和: {sum_while}")

# 2. 打印九九乘法表的前5行
print("\n九九乘法表前5行:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="  ")
    print()

# 3. 找出1到50中所有的质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for num in range(1, 51):
    if is_prime(num):
        primes.append(num)

print(f"\n1到50中的质数: {primes}")
```

### 题目24：循环控制 - 答案

```python
# 1. 使用break找出第一个大于100的平方数
for i in range(1, 20):
    square = i ** 2
    if square > 100:
        print(f"第一个大于100的平方数: {i}² = {square}")
        break

# 2. 使用continue跳过偶数，只打印1到20的奇数
print("\n1到20的奇数:")
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 3. 使用嵌套循环打印星号三角形
print("\n星号三角形:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

### 题目25：异常处理 - 答案

```python
# 1. 除零错误
def safe_division(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("错误: 除数不能为零")
        return None

safe_division(10, 2)
safe_division(10, 0)

# 2. 索引越界错误
def safe_list_access(lst, index):
    try:
        value = lst[index]
        print(f"索引 {index} 的值: {value}")
        return value
    except IndexError:
        print(f"错误: 索引 {index} 越界")
        return None

test_list = [1, 2, 3, 4, 5]
safe_list_access(test_list, 2)
safe_list_access(test_list, 10)

# 3. 类型转换错误
def safe_int_conversion(value):
    try:
        result = int(value)
        print(f"转换成功: {value} -> {result}")
        return result
    except ValueError:
        print(f"错误: 无法将 '{value}' 转换为整数")
        return None

safe_int_conversion("123")
safe_int_conversion("abc")

# 4. 文件不存在错误
def safe_file_read(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"文件内容: {content}")
            return content
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 不存在")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

safe_file_read("existing_file.txt")
safe_file_read("non_existing_file.txt")
```

## 函数与模块（26-30题）

### 题目26：函数定义与调用 - 答案

```python
import math

# 1. 计算圆的面积
def circle_area(radius):
    """计算圆的面积"""
    return math.pi * radius ** 2

# 2. 判断一个数是否为素数
def is_prime(n):
    """判断是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 3. 反转字符串
def reverse_string(s):
    """反转字符串"""
    return s[::-1]

# 4. 计算阶乘
def factorial(n):
    """计算阶乘"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 测试函数
print(f"半径为5的圆的面积: {circle_area(5):.2f}")
print(f"17是否为素数: {is_prime(17)}")
print(f"反转字符串'hello': {reverse_string('hello')}")
print(f"5的阶乘: {factorial(5)}")
```

### 题目27：函数参数 - 答案

```python
# 1. 位置参数：计算两个数的和
def add_two_numbers(a, b):
    """计算两个数的和"""
    return a + b

# 2. 默认参数：问候函数
def greet(name, language="中文"):
    """问候函数，可选择语言"""
    greetings = {
        "中文": f"你好，{name}!",
        "英文": f"Hello, {name}!",
        "日文": f"こんにちは、{name}!",
        "韩文": f"안녕하세요, {name}!"
    }
    return greetings.get(language, f"Hello, {name}!")

# 3. 可变参数：计算多个数的乘积
def multiply_numbers(*numbers):
    """计算多个数的乘积"""
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result

# 4. 关键字参数：创建学生信息
def create_student(**info):
    """创建学生信息"""
    student = {}
    for key, value in info.items():
        student[key] = value
    return student

# 测试函数
print(f"3 + 5 = {add_two_numbers(3, 5)}")
print(greet("张三"))
print(greet("Tom", "英文"))
print(f"2 * 3 * 4 = {multiply_numbers(2, 3, 4)}")
student = create_student(name="李四", age=20, major="计算机")
print(f"学生信息: {student}")
```

### 题目28：Lambda函数 - 答案

```python
# 1. 计算两个数的最大值
max_of_two = lambda x, y: x if x > y else y
print(f"max(5, 8) = {max_of_two(5, 8)}")

# 2. 将字符串列表按长度排序
words = ["python", "java", "c", "javascript", "go"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"按长度排序: {sorted_by_length}")

# 3. 过滤出列表中的偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {even_numbers}")

# 4. 将数字列表每个元素平方
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"平方数: {squared_numbers}")
```

### 题目29：装饰器基础 - 答案

```python
import time
from functools import wraps

# 1. 计算函数执行时间的装饰器
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

# 2. 在函数执行前后打印日志的装饰器
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"开始执行函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完成")
        return result
    return wrapper

# 3. 验证函数参数类型的装饰器
def type_check(*expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"参数 {i+1} 应该是 {expected_type.__name__} 类型")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用装饰器
@timer
@logger
def slow_function():
    time.sleep(0.1)
    return "完成"

@type_check(int, int)
def add_integers(a, b):
    return a + b

# 测试
print(slow_function())
print(f"2 + 3 = {add_integers(2, 3)}")

try:
    add_integers(2, "3")  # 这会引发TypeError
except TypeError as e:
    print(f"类型错误: {e}")
```

### 题目30：模块与包 - 答案

```python
# 1. 创建数学工具模块 (math_utils.py)
# 文件内容：
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

def power(base, exponent):
    return base ** exponent
"""

# 2. 创建字符串工具模块 (string_utils.py)
# 文件内容：
"""
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    clean_s = s.lower().replace(' ', '')
    return clean_s == clean_s[::-1]

def count_words(s):
    return len(s.split())

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))
"""

# 3. 主程序中使用模块
# 由于我们无法实际创建文件，这里演示import的用法

# 导入自定义模块的方式：
# import math_utils
# from string_utils import reverse_string, is_palindrome
# import string_utils as su

# 4. 使用Python标准库模块
import random
import datetime
import os

# random模块示例
print("=== random模块示例 ===")
print(f"随机整数(1-10): {random.randint(1, 10)}")
print(f"随机浮点数: {random.random():.4f}")

colors = ["红", "绿", "蓝", "黄"]
print(f"随机选择颜色: {random.choice(colors)}")

numbers = list(range(1, 11))
random.shuffle(numbers)
print(f"打乱后的数字: {numbers}")

# datetime模块示例
print("\n=== datetime模块示例 ===")
now = datetime.datetime.now()
print(f"当前时间: {now}")
print(f"格式化时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

today = datetime.date.today()
print(f"今天日期: {today}")

tomorrow = today + datetime.timedelta(days=1)
print(f"明天日期: {tomorrow}")

# os模块示例
print("\n=== os模块示例 ===")
print(f"当前工作目录: {os.getcwd()}")
print(f"用户主目录: {os.path.expanduser('~')}")

# 环境变量
path = os.environ.get('PATH', '未找到PATH环境变量')
print(f"PATH环境变量前50个字符: {path[:50]}...")

# 路径操作
file_path = "/home/user/documents/file.txt"
print(f"文件名: {os.path.basename(file_path)}")
print(f"目录名: {os.path.dirname(file_path)}")
print(f"分离路径: {os.path.split(file_path)}")

# 模拟math_utils和string_utils的使用
print("\n=== 模拟模块使用 ===")

# 数学工具函数（模拟导入）
def add(a, b): return a + b
def multiply(a, b): return a * b

print(f"5 + 3 = {add(5, 3)}")
print(f"4 * 7 = {multiply(4, 7)}")

# 字符串工具函数（模拟导入）
def reverse_string(s): return s[::-1]
def is_palindrome(s): 
    clean_s = s.lower().replace(' ', '')
    return clean_s == clean_s[::-1]

print(f"反转'hello': {reverse_string('hello')}")
print(f"'level'是否为回文: {is_palindrome('level')}")
print(f"'A man a plan a canal Panama'是否为回文: {is_palindrome('A man a plan a canal Panama')}")
```

---

## 总结

这30道题目涵盖了Python的核心语法要素：

1. **基础语法**：变量、数据类型、类型转换
2. **字符串处理**：切片、格式化、方法调用
3. **数据结构**：列表、字典、元组的操作
4. **控制流程**：条件判断、循环、异常处理
5. **函数编程**：函数定义、参数传递、装饰器
6. **模块系统**：导入、使用标准库

通过这些练习，你应该能够：
- 熟练掌握Python基础语法
- 理解Python的数据结构特性
- 运用控制流程解决问题
- 编写和使用函数
- 处理异常情况
- 使用Python标准库

建议按顺序完成所有题目，并在理解答案的基础上尝试自己的变化和扩展。 