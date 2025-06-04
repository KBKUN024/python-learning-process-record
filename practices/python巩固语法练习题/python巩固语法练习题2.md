# Python语法巩固练习题2（30题）

## 文件操作与数据处理（1-7题）

### 题目1：配置文件读取器
在后端开发中，配置文件是必不可少的。编写一个程序来读取和解析配置文件。

**任务要求：**
- 创建一个名为 `config.txt` 的文件，内容如下：
```
database_host=localhost
database_port=5432
database_name=myapp
debug_mode=True
max_connections=100
```
- 编写程序读取这个文件
- 将配置解析为字典格式
- 支持不同数据类型的自动转换（字符串、整数、布尔值）

**预期输出：**
```python
{
    'database_host': 'localhost',
    'database_port': 5432,
    'database_name': 'myapp',
    'debug_mode': True,
    'max_connections': 100
}
```

### 题目2：日志文件分析器
日志分析是后端开发的重要技能。分析一个简单的访问日志文件。

**给定日志内容：**
```
2024-01-15 10:30:25 INFO User login successful: user_id=123
2024-01-15 10:31:10 ERROR Database connection failed: timeout
2024-01-15 10:32:15 INFO User logout: user_id=123
2024-01-15 10:33:20 WARNING High memory usage: 85%
2024-01-15 10:34:05 INFO User login successful: user_id=456
2024-01-15 10:35:30 ERROR Authentication failed: invalid_token
```

**任务要求：**
1. 统计不同日志级别的数量
2. 提取所有用户ID
3. 找出所有错误信息
4. 统计每小时的日志条数

### 题目3：CSV数据处理器
编写一个程序处理员工数据CSV文件。

**CSV文件内容（employees.csv）：**
```
姓名,部门,工资,入职日期
张三,技术部,8000,2023-01-15
李四,销售部,6000,2023-02-20
王五,技术部,9000,2022-12-10
赵六,人事部,7000,2023-03-05
钱七,技术部,8500,2023-01-25
```

**任务要求：**
1. 读取CSV文件并转换为字典列表
2. 计算各部门的平均工资
3. 找出工资最高和最低的员工
4. 按入职日期排序
5. 将结果保存到新的CSV文件

### 题目4：JSON API数据模拟
模拟处理来自API的JSON响应数据。

**JSON数据：**
```json
{
  "status": "success",
  "data": {
    "users": [
      {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "roles": ["admin", "user"],
        "profile": {
          "first_name": "张",
          "last_name": "三",
          "age": 28,
          "department": "技术部"
        },
        "is_active": true,
        "last_login": "2024-01-15T10:30:00Z"
      },
      {
        "id": 2,
        "username": "user1",
        "email": "user1@example.com",
        "roles": ["user"],
        "profile": {
          "first_name": "李",
          "last_name": "四",
          "age": 25,
          "department": "销售部"
        },
        "is_active": false,
        "last_login": "2024-01-10T15:20:00Z"
      }
    ]
  }
}
```

**任务要求：**
1. 解析JSON数据
2. 提取所有活跃用户的信息
3. 计算用户平均年龄
4. 按部门分组统计用户数量
5. 找出拥有admin角色的用户

### 题目5：数据备份工具
编写一个简单的数据备份工具。

**任务要求：**
1. 创建一个包含多个文本文件的目录
2. 编写程序将这些文件复制到备份目录
3. 在备份文件名后添加时间戳
4. 计算并显示备份的文件总大小
5. 生成备份报告文件

### 题目6：文件监控器
创建一个简单的文件变化监控器。

**任务要求：**
1. 记录指定目录中文件的初始状态（文件名、大小、修改时间）
2. 编写函数检测文件变化
3. 识别新增、删除、修改的文件
4. 将变化记录到日志文件中

### 题目7：数据导入导出器
编写一个通用的数据格式转换工具。

**任务要求：**
1. 支持JSON到CSV的转换
2. 支持CSV到JSON的转换
3. 处理嵌套的JSON数据
4. 提供数据验证功能
5. 支持批量文件处理

## 异常处理基础（8-12题）

### 题目8：用户输入验证器
编写一个健壮的用户输入验证系统。

**验证要求：**
1. 用户名：3-20个字符，只能包含字母、数字、下划线
2. 密码：至少8个字符，包含大小写字母、数字
3. 邮箱：标准邮箱格式
4. 年龄：18-100之间的整数

**任务要求：**
- 使用异常处理来处理各种输入错误
- 提供友好的错误提示信息
- 支持重试机制
- 记录错误日志

### 题目9：文件操作异常处理
编写一个安全的文件操作系统。

**功能要求：**
1. 安全地读取文件（处理文件不存在、权限不足等异常）
2. 安全地写入文件（处理磁盘空间不足、路径错误等异常）
3. 自动创建备份
4. 原子性写入（要么完全成功，要么完全回滚）

**测试场景：**
- 读取不存在的文件
- 写入到只读目录
- 处理大文件时的内存问题

### 题目10：网络请求模拟器
模拟网络请求中的各种异常情况。

**任务要求：**
1. 模拟不同类型的网络错误（超时、连接拒绝、DNS错误）
2. 实现重试机制（指数退避）
3. 设置最大重试次数
4. 记录每次尝试的详细信息
5. 提供降级方案

### 题目11：数据库连接模拟器
模拟数据库连接和操作中的异常处理。

**异常类型：**
1. 连接超时
2. 认证失败
3. 数据库不存在
4. SQL语法错误
5. 数据约束违反

**任务要求：**
- 为每种异常定义自定义异常类
- 实现连接重试机制
- 提供事务回滚功能
- 记录详细的错误信息

### 题目12：API错误处理框架
设计一个统一的API错误处理框架。

**错误类型：**
1. 参数验证错误（400）
2. 认证失败（401）
3. 权限不足（403）
4. 资源未找到（404）
5. 服务器内部错误（500）

**任务要求：**
- 定义错误码和错误消息
- 实现错误响应格式化
- 支持国际化错误消息
- 提供错误统计功能

## 类与对象入门（13-18题）

### 题目13：用户管理系统
设计一个简单的用户管理系统。

**User类要求：**
```python
class User:
    def __init__(self, username, email, password):
        # 初始化用户信息
        
    def authenticate(self, password):
        # 验证密码
        
    def update_profile(self, **kwargs):
        # 更新用户信息
        
    def to_dict(self):
        # 转换为字典格式
        
    def __str__(self):
        # 字符串表示
```

**UserManager类要求：**
- 管理多个用户
- 支持用户注册、登录、删除
- 提供用户搜索功能
- 统计用户信息

### 题目14：商品库存管理
创建一个商品库存管理系统。

**Product类要求：**
- 属性：商品ID、名称、价格、库存数量、类别
- 方法：增加库存、减少库存、更新价格、是否有库存

**Inventory类要求：**
- 管理多个商品
- 添加新商品
- 库存预警（低于阈值时报警）
- 生成库存报告
- 计算总价值

### 题目15：订单处理系统
设计一个简单的订单处理系统。

**Order类要求：**
- 订单号、客户信息、商品列表、订单状态、创建时间
- 计算订单总金额
- 更新订单状态
- 添加/删除商品

**OrderManager类要求：**
- 创建新订单
- 查询订单
- 统计订单数据
- 处理退款

### 题目16：日志记录器类
实现一个面向对象的日志记录系统。

**Logger类要求：**
- 支持不同日志级别（DEBUG, INFO, WARNING, ERROR）
- 格式化日志消息
- 写入文件和控制台
- 日志文件轮转
- 过滤日志级别

### 题目17：缓存管理器
实现一个简单的内存缓存系统。

**Cache类要求：**
- 存储键值对
- 支持过期时间（TTL）
- LRU淘汰策略
- 缓存统计（命中率、大小等）
- 清空缓存

### 题目18：配置管理器
创建一个配置管理类。

**ConfigManager类要求：**
- 从文件加载配置
- 支持嵌套配置访问（如：config.get('database.host')）
- 配置验证
- 默认值处理
- 配置更新和保存

## 装饰器与高级函数（19-23题）

### 题目19：性能监控装饰器
编写一个装饰器来监控函数执行性能。

**功能要求：**
1. 测量函数执行时间
2. 记录函数调用次数
3. 计算平均执行时间
4. 检测慢查询（超过阈值的调用）
5. 生成性能报告

**使用示例：**
```python
@performance_monitor(threshold=1.0)
def slow_function():
    time.sleep(2)
    return "完成"
```

### 题目20：权限验证装饰器
创建一个权限验证装饰器，用于API接口权限控制。

**功能要求：**
1. 检查用户是否登录
2. 验证用户角色
3. 检查特定权限
4. 支持多个权限组合
5. 记录访问日志

**使用示例：**
```python
@require_permission('admin', 'user_management')
def delete_user(user_id):
    pass

@require_login
def get_profile():
    pass
```

### 题目21：缓存装饰器
实现一个函数结果缓存装饰器。

**功能要求：**
1. 基于参数缓存函数结果
2. 支持TTL（生存时间）
3. 缓存大小限制
4. 缓存命中率统计
5. 手动清除缓存

**使用示例：**
```python
@cache(ttl=300, max_size=100)
def expensive_calculation(x, y):
    time.sleep(1)  # 模拟耗时计算
    return x * y + sum(range(1000))
```

### 题目22：重试装饰器
创建一个自动重试装饰器。

**功能要求：**
1. 指定最大重试次数
2. 指数退避策略
3. 特定异常类型重试
4. 重试回调函数
5. 记录重试日志

**使用示例：**
```python
@retry(max_attempts=3, backoff_factor=2, exceptions=[ConnectionError])
def unreliable_network_call():
    pass
```

### 题目23：参数验证装饰器
实现函数参数验证装饰器。

**功能要求：**
1. 类型验证
2. 数值范围验证
3. 字符串长度验证
4. 自定义验证规则
5. 详细错误信息

**使用示例：**
```python
@validate_params({
    'name': {'type': str, 'min_length': 2, 'max_length': 50},
    'age': {'type': int, 'min': 0, 'max': 150},
    'email': {'type': str, 'pattern': r'.*@.*\..*'}
})
def register_user(name, age, email):
    pass
```

## 数据验证与处理（24-28题）

### 题目24：表单数据验证器
创建一个通用的表单数据验证系统。

**验证规则：**
```python
user_form_rules = {
    'username': {
        'required': True,
        'type': 'string',
        'min_length': 3,
        'max_length': 20,
        'pattern': r'^[a-zA-Z0-9_]+$'
    },
    'email': {
        'required': True,
        'type': 'email'
    },
    'age': {
        'required': False,
        'type': 'integer',
        'min': 13,
        'max': 120
    },
    'tags': {
        'required': False,
        'type': 'list',
        'element_type': 'string'
    }
}
```

**任务要求：**
1. 实现各种验证规则
2. 支持嵌套数据验证
3. 提供详细的错误信息
4. 支持自定义验证函数

### 题目25：数据清洗工具
编写一个数据清洗工具，处理脏数据。

**处理任务：**
1. 去除前后空格
2. 统一日期格式
3. 标准化电话号码格式
4. 处理缺失值
5. 检测和处理异常值

**测试数据：**
```python
dirty_data = [
    {'name': '  张三  ', 'phone': '138-0013-8000', 'birth': '1990/01/15', 'salary': ''},
    {'name': 'Li Si', 'phone': '13800138001', 'birth': '1985-02-20', 'salary': '999999'},
    {'name': '', 'phone': '138 0013 8002', 'birth': '1990.03.25', 'salary': '5000'},
]
```

### 题目26：API参数解析器
实现一个API参数解析和验证系统。

**功能要求：**
1. 解析URL查询参数
2. 解析JSON请求体
3. 解析表单数据
4. 类型转换
5. 默认值处理

**示例用法：**
```python
@parse_params({
    'page': {'type': int, 'default': 1, 'min': 1},
    'size': {'type': int, 'default': 10, 'min': 1, 'max': 100},
    'keyword': {'type': str, 'required': False},
    'sort': {'type': str, 'choices': ['name', 'date', 'price']}
})
def search_products(page, size, keyword=None, sort='name'):
    pass
```

### 题目27：数据格式转换器
创建一个多格式数据转换工具。

**支持格式：**
1. JSON ↔ CSV
2. JSON ↔ XML
3. CSV ↔ Excel
4. 嵌套JSON扁平化
5. 数据类型推断

**任务要求：**
- 处理不同的字符编码
- 保持数据类型信息
- 处理大文件（流式处理）
- 提供转换进度

### 题目28：数据统计分析器
实现一个数据统计分析工具。

**统计功能：**
1. 基本统计（平均值、最大值、最小值、中位数）
2. 分组统计
3. 百分位数计算
4. 数据分布分析
5. 异常值检测

**测试数据：**
```python
sales_data = [
    {'product': 'iPhone', 'category': 'Electronics', 'price': 999, 'quantity': 10},
    {'product': 'Book', 'category': 'Books', 'price': 29, 'quantity': 50},
    {'product': 'Laptop', 'category': 'Electronics', 'price': 1299, 'quantity': 5},
    # ... 更多数据
]
```

## 网络编程基础（29-30题）

### 题目29：HTTP客户端模拟器
编写一个简单的HTTP客户端。

**功能要求：**
1. 发送GET、POST请求
2. 处理请求头和响应头
3. 支持JSON数据传输
4. 处理HTTP状态码
5. 支持基本认证
6. 错误处理和重试

**使用示例：**
```python
client = HTTPClient()
response = client.get('https://api.example.com/users')
response = client.post('https://api.example.com/users', json={'name': '张三'})
```

### 题目30：简单Web服务器
实现一个基础的HTTP服务器。

**功能要求：**
1. 处理GET、POST请求
2. 静态文件服务
3. 路由系统
4. 请求参数解析
5. 响应格式化
6. 基本的错误处理

**路由示例：**
```python
server = SimpleWebServer()

@server.route('/hello', methods=['GET'])
def hello():
    return {'message': 'Hello, World!'}

@server.route('/users', methods=['POST'])
def create_user():
    data = server.get_json()
    return {'status': 'created', 'user': data}

server.run(host='localhost', port=8080)
```

---

## 完成说明

这30道题目是在练习题1基础上的进阶版本，更贴近后端开发的实际应用场景。重点关注：

### 学习重点

1. **文件操作**：配置文件、日志文件、数据文件的处理
2. **异常处理**：构建健壮的应用程序
3. **面向对象**：理解类的设计和使用
4. **装饰器**：Python的高级特性，在Web开发中广泛使用
5. **数据处理**：数据验证、清洗、转换等后端常见任务
6. **网络编程**：为学习Web框架打基础

### 实践建议

1. **循序渐进**：按顺序完成题目，每道题都要动手实践
2. **扩展思考**：在完成基本要求后，思考如何优化和扩展
3. **错误处理**：重点关注异常处理，这是生产环境的关键
4. **代码复用**：学会设计可复用的代码模块
5. **性能考虑**：思考代码的性能影响

### 下一步学习

完成这些练习后，您将具备学习Web框架（如Flask、Django、FastAPI）的坚实基础，可以开始真正的后端Web开发学习。

记住：**优秀的后端开发者 = 扎实的基础 + 实践经验 + 持续学习** 