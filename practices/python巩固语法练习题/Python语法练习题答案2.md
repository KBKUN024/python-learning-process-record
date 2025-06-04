# Python语法巩固练习题2答案详解

## 文件操作与数据处理（1-7题）

### 题目1：配置文件读取器

```python
def read_config(filename):
    """读取配置文件并解析为字典"""
    config = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # 数据类型转换
                    if value.lower() == 'true':
                        config[key] = True
                    elif value.lower() == 'false':
                        config[key] = False
                    elif value.isdigit():
                        config[key] = int(value)
                    else:
                        config[key] = value
    except FileNotFoundError:
        print(f"配置文件 {filename} 不存在")
        return {}
    except Exception as e:
        print(f"读取配置文件时出错: {e}")
        return {}
    
    return config

# 创建配置文件
config_content = """database_host=localhost
database_port=5432
database_name=myapp
debug_mode=True
max_connections=100"""

with open('config.txt', 'w', encoding='utf-8') as f:
    f.write(config_content)

# 读取并解析配置
config = read_config('config.txt')
print(config)
```

### 题目2：日志文件分析器

```python
import re
from collections import defaultdict, Counter
from datetime import datetime

def analyze_log_file(log_content):
    """分析日志文件"""
    lines = log_content.strip().split('\n')
    
    # 统计数据
    level_counts = Counter()
    user_ids = set()
    errors = []
    hour_counts = defaultdict(int)
    
    for line in lines:
        # 解析日志行
        parts = line.split(' ', 3)
        if len(parts) >= 4:
            date_str = parts[0]
            time_str = parts[1]
            level = parts[2]
            message = parts[3]
            
            # 统计日志级别
            level_counts[level] += 1
            
            # 提取用户ID
            user_id_match = re.search(r'user_id=(\d+)', message)
            if user_id_match:
                user_ids.add(int(user_id_match.group(1)))
            
            # 收集错误信息
            if level == 'ERROR':
                errors.append(message)
            
            # 统计每小时日志数
            hour = int(time_str.split(':')[0])
            hour_counts[hour] += 1
    
    return {
        'level_counts': dict(level_counts),
        'user_ids': sorted(list(user_ids)),
        'errors': errors,
        'hour_counts': dict(hour_counts)
    }

# 测试日志内容
log_content = """2024-01-15 10:30:25 INFO User login successful: user_id=123
2024-01-15 10:31:10 ERROR Database connection failed: timeout
2024-01-15 10:32:15 INFO User logout: user_id=123
2024-01-15 10:33:20 WARNING High memory usage: 85%
2024-01-15 10:34:05 INFO User login successful: user_id=456
2024-01-15 10:35:30 ERROR Authentication failed: invalid_token"""

result = analyze_log_file(log_content)
print("日志级别统计:", result['level_counts'])
print("用户ID列表:", result['user_ids'])
print("错误信息:", result['errors'])
print("每小时日志数:", result['hour_counts'])
```

### 题目3：CSV数据处理器

```python
import csv
from datetime import datetime
from collections import defaultdict

def process_employee_data():
    """处理员工数据CSV文件"""
    
    # 创建CSV文件
    employees_data = [
        ['姓名', '部门', '工资', '入职日期'],
        ['张三', '技术部', '8000', '2023-01-15'],
        ['李四', '销售部', '6000', '2023-02-20'],
        ['王五', '技术部', '9000', '2022-12-10'],
        ['赵六', '人事部', '7000', '2023-03-05'],
        ['钱七', '技术部', '8500', '2023-01-25']
    ]
    
    with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(employees_data)
    
    # 读取CSV文件
    employees = []
    with open('employees.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['工资'] = int(row['工资'])
            row['入职日期'] = datetime.strptime(row['入职日期'], '%Y-%m-%d')
            employees.append(row)
    
    # 1. 计算各部门平均工资
    dept_salaries = defaultdict(list)
    for emp in employees:
        dept_salaries[emp['部门']].append(emp['工资'])
    
    dept_avg = {dept: sum(salaries)/len(salaries) 
                for dept, salaries in dept_salaries.items()}
    
    # 2. 找出工资最高和最低的员工
    max_salary_emp = max(employees, key=lambda x: x['工资'])
    min_salary_emp = min(employees, key=lambda x: x['工资'])
    
    # 3. 按入职日期排序
    sorted_employees = sorted(employees, key=lambda x: x['入职日期'])
    
    # 4. 保存结果到新CSV文件
    with open('employee_analysis.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['姓名', '部门', '工资', '入职日期']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for emp in sorted_employees:
            emp_copy = emp.copy()
            emp_copy['入职日期'] = emp_copy['入职日期'].strftime('%Y-%m-%d')
            writer.writerow(emp_copy)
    
    return {
        'dept_avg': dept_avg,
        'max_salary': max_salary_emp,
        'min_salary': min_salary_emp,
        'sorted_employees': sorted_employees
    }

result = process_employee_data()
print("各部门平均工资:", result['dept_avg'])
print("工资最高员工:", result['max_salary']['姓名'], result['max_salary']['工资'])
print("工资最低员工:", result['min_salary']['姓名'], result['min_salary']['工资'])
```

### 题目4：JSON API数据模拟

```python
import json
from collections import defaultdict

def process_api_data():
    """处理API JSON数据"""
    
    json_data = {
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
                    "is_active": True,
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
                    "is_active": False,
                    "last_login": "2024-01-10T15:20:00Z"
                }
            ]
        }
    }
    
    users = json_data["data"]["users"]
    
    # 1. 提取所有活跃用户的信息
    active_users = [user for user in users if user["is_active"]]
    
    # 2. 计算用户平均年龄
    total_age = sum(user["profile"]["age"] for user in users)
    avg_age = total_age / len(users)
    
    # 3. 按部门分组统计用户数量
    dept_counts = defaultdict(int)
    for user in users:
        dept = user["profile"]["department"]
        dept_counts[dept] += 1
    
    # 4. 找出拥有admin角色的用户
    admin_users = [user for user in users if "admin" in user["roles"]]
    
    return {
        "active_users": active_users,
        "average_age": avg_age,
        "department_counts": dict(dept_counts),
        "admin_users": admin_users
    }

result = process_api_data()
print("活跃用户数量:", len(result["active_users"]))
print("用户平均年龄:", result["average_age"])
print("部门用户统计:", result["department_counts"])
print("管理员用户:", [user["username"] for user in result["admin_users"]])
```

### 题目5：数据备份工具

```python
import os
import shutil
from datetime import datetime
import json

class BackupTool:
    def __init__(self, source_dir, backup_dir):
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.backup_report = {
            "backup_time": None,
            "files_backed_up": [],
            "total_size": 0,
            "status": "success"
        }
    
    def create_backup(self):
        """创建备份"""
        try:
            # 创建备份目录
            os.makedirs(self.backup_dir, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.backup_report["backup_time"] = timestamp
            
            total_size = 0
            
            # 遍历源目录中的文件
            for filename in os.listdir(self.source_dir):
                source_path = os.path.join(self.source_dir, filename)
                
                if os.path.isfile(source_path):
                    # 为备份文件添加时间戳
                    name, ext = os.path.splitext(filename)
                    backup_filename = f"{name}_{timestamp}{ext}"
                    backup_path = os.path.join(self.backup_dir, backup_filename)
                    
                    # 复制文件
                    shutil.copy2(source_path, backup_path)
                    
                    # 计算文件大小
                    file_size = os.path.getsize(source_path)
                    total_size += file_size
                    
                    self.backup_report["files_backed_up"].append({
                        "original": filename,
                        "backup": backup_filename,
                        "size": file_size
                    })
            
            self.backup_report["total_size"] = total_size
            
        except Exception as e:
            self.backup_report["status"] = "failed"
            self.backup_report["error"] = str(e)
    
    def generate_report(self):
        """生成备份报告"""
        report_filename = f"backup_report_{self.backup_report['backup_time']}.json"
        report_path = os.path.join(self.backup_dir, report_filename)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.backup_report, f, ensure_ascii=False, indent=2)
        
        print(f"备份完成！")
        print(f"备份文件数: {len(self.backup_report['files_backed_up'])}")
        print(f"总大小: {self.backup_report['total_size']} 字节")
        print(f"报告文件: {report_path}")

# 示例使用
def demo_backup():
    # 创建测试文件
    os.makedirs("source_files", exist_ok=True)
    test_files = ["test1.txt", "test2.txt", "config.json"]
    
    for filename in test_files:
        with open(f"source_files/{filename}", 'w') as f:
            f.write(f"这是 {filename} 的内容")
    
    # 执行备份
    backup_tool = BackupTool("source_files", "backup_files")
    backup_tool.create_backup()
    backup_tool.generate_report()

demo_backup()
```

### 题目6：文件监控器

```python
import os
import json
from datetime import datetime

class FileMonitor:
    def __init__(self, monitor_dir):
        self.monitor_dir = monitor_dir
        self.snapshot_file = "file_snapshot.json"
        self.log_file = "file_changes.log"
    
    def get_file_info(self, filepath):
        """获取文件信息"""
        stat = os.stat(filepath)
        return {
            "size": stat.st_size,
            "modified": stat.st_mtime,
            "created": stat.st_ctime
        }
    
    def take_snapshot(self):
        """记录当前文件状态"""
        snapshot = {}
        
        if not os.path.exists(self.monitor_dir):
            return snapshot
        
        for filename in os.listdir(self.monitor_dir):
            filepath = os.path.join(self.monitor_dir, filename)
            if os.path.isfile(filepath):
                snapshot[filename] = self.get_file_info(filepath)
        
        with open(self.snapshot_file, 'w') as f:
            json.dump(snapshot, f, indent=2)
        
        return snapshot
    
    def load_snapshot(self):
        """加载之前的快照"""
        try:
            with open(self.snapshot_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def detect_changes(self):
        """检测文件变化"""
        old_snapshot = self.load_snapshot()
        current_snapshot = {}
        
        changes = {
            "added": [],
            "modified": [],
            "deleted": []
        }
        
        # 获取当前文件状态
        if os.path.exists(self.monitor_dir):
            for filename in os.listdir(self.monitor_dir):
                filepath = os.path.join(self.monitor_dir, filename)
                if os.path.isfile(filepath):
                    current_snapshot[filename] = self.get_file_info(filepath)
        
        # 检测新增和修改的文件
        for filename, info in current_snapshot.items():
            if filename not in old_snapshot:
                changes["added"].append(filename)
            elif info["modified"] > old_snapshot[filename]["modified"]:
                changes["modified"].append(filename)
        
        # 检测删除的文件
        for filename in old_snapshot:
            if filename not in current_snapshot:
                changes["deleted"].append(filename)
        
        return changes
    
    def log_changes(self, changes):
        """记录变化到日志"""
        if not any(changes.values()):
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n=== {timestamp} ===\n")
            
            for added in changes["added"]:
                f.write(f"新增文件: {added}\n")
            
            for modified in changes["modified"]:
                f.write(f"修改文件: {modified}\n")
            
            for deleted in changes["deleted"]:
                f.write(f"删除文件: {deleted}\n")

# 示例使用
def demo_file_monitor():
    monitor = FileMonitor("watch_dir")
    
    # 创建监控目录和一些测试文件
    os.makedirs("watch_dir", exist_ok=True)
    with open("watch_dir/file1.txt", 'w') as f:
        f.write("原始内容")
    
    # 首次快照
    print("创建初始快照...")
    monitor.take_snapshot()
    
    # 模拟文件变化
    print("模拟文件变化...")
    with open("watch_dir/file2.txt", 'w') as f:  # 新增文件
        f.write("新文件")
    
    import time
    time.sleep(1)  # 确保修改时间不同
    
    with open("watch_dir/file1.txt", 'w') as f:  # 修改文件
        f.write("修改后的内容")
    
    # 检测变化
    changes = monitor.detect_changes()
    print("检测到的变化:", changes)
    
    # 记录变化
    monitor.log_changes(changes)
    
    # 更新快照
    monitor.take_snapshot()

demo_file_monitor()
```

### 题目7：数据导入导出器

```python
import json
import csv
import xml.etree.ElementTree as ET
from typing import List, Dict, Any

class DataConverter:
    def __init__(self):
        self.supported_formats = ['json', 'csv', 'xml']
    
    def json_to_csv(self, json_data: List[Dict], csv_filename: str):
        """JSON转CSV"""
        if not json_data:
            return False
        
        # 扁平化嵌套字典
        flattened_data = []
        for item in json_data:
            flattened_item = self._flatten_dict(item)
            flattened_data.append(flattened_item)
        
        # 获取所有字段名
        fieldnames = set()
        for item in flattened_data:
            fieldnames.update(item.keys())
        fieldnames = sorted(list(fieldnames))
        
        # 写入CSV
        with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(flattened_data)
        
        return True
    
    def csv_to_json(self, csv_filename: str, json_filename: str):
        """CSV转JSON"""
        try:
            with open(csv_filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = []
                for row in reader:
                    # 恢复嵌套结构
                    nested_row = self._unflatten_dict(row)
                    data.append(nested_row)
            
            with open(json_filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"转换失败: {e}")
            return False
    
    def _flatten_dict(self, d: Dict, parent_key: str = '', sep: str = '.') -> Dict:
        """扁平化字典"""
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                # 简单处理列表：转为字符串
                items.append((new_key, json.dumps(v, ensure_ascii=False)))
            else:
                items.append((new_key, v))
        return dict(items)
    
    def _unflatten_dict(self, d: Dict, sep: str = '.') -> Dict:
        """反扁平化字典"""
        result = {}
        for key, value in d.items():
            if sep in key:
                keys = key.split(sep)
                current = result
                for k in keys[:-1]:
                    if k not in current:
                        current[k] = {}
                    current = current[k]
                
                # 尝试解析JSON字符串
                try:
                    current[keys[-1]] = json.loads(value)
                except (json.JSONDecodeError, TypeError):
                    current[keys[-1]] = value
            else:
                # 尝试解析JSON字符串
                try:
                    result[key] = json.loads(value)
                except (json.JSONDecodeError, TypeError):
                    result[key] = value
        
        return result
    
    def validate_data(self, data: Any, data_type: str = 'json') -> bool:
        """验证数据格式"""
        if data_type == 'json':
            return isinstance(data, (list, dict))
        elif data_type == 'csv':
            # 检查是否是有效的CSV数据
            return isinstance(data, list) and all(isinstance(row, dict) for row in data)
        return False
    
    def batch_convert(self, file_list: List[str], source_format: str, target_format: str):
        """批量转换文件"""
        results = []
        
        for filename in file_list:
            try:
                if source_format == 'json' and target_format == 'csv':
                    with open(filename, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    if self.validate_data(data, 'json'):
                        output_filename = filename.replace('.json', '.csv')
                        success = self.json_to_csv(data, output_filename)
                        results.append({'file': filename, 'success': success})
                
                elif source_format == 'csv' and target_format == 'json':
                    output_filename = filename.replace('.csv', '.json')
                    success = self.csv_to_json(filename, output_filename)
                    results.append({'file': filename, 'success': success})
                
            except Exception as e:
                results.append({'file': filename, 'success': False, 'error': str(e)})
        
        return results

# 示例使用
def demo_data_converter():
    converter = DataConverter()
    
    # 创建测试数据
    test_data = [
        {
            "id": 1,
            "name": "张三",
            "profile": {
                "age": 25,
                "city": "北京",
                "skills": ["Python", "JavaScript"]
            },
            "active": True
        },
        {
            "id": 2,
            "name": "李四",
            "profile": {
                "age": 30,
                "city": "上海",
                "skills": ["Java", "SQL"]
            },
            "active": False
        }
    ]
    
    # 保存测试JSON文件
    with open('test_data.json', 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)
    
    # JSON转CSV
    print("JSON转CSV...")
    success = converter.json_to_csv(test_data, 'test_data.csv')
    print(f"转换成功: {success}")
    
    # CSV转JSON
    print("CSV转JSON...")
    success = converter.csv_to_json('test_data.csv', 'converted_data.json')
    print(f"转换成功: {success}")
    
    # 批量转换
    print("批量转换...")
    results = converter.batch_convert(['test_data.json'], 'json', 'csv')
    print("批量转换结果:", results)

demo_data_converter()
```

## 异常处理基础（8-12题）

### 题目8：用户输入验证器

```python
import re
import logging

class ValidationError(Exception):
    """自定义验证异常"""
    pass

class UserInputValidator:
    def __init__(self):
        self.error_log = []
        
        # 配置日志
        logging.basicConfig(
            filename='validation_errors.log',
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def validate_username(self, username):
        """验证用户名"""
        if not username:
            raise ValidationError("用户名不能为空")
        
        if len(username) < 3 or len(username) > 20:
            raise ValidationError("用户名长度必须在3-20个字符之间")
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError("用户名只能包含字母、数字和下划线")
        
        return True
    
    def validate_password(self, password):
        """验证密码"""
        if not password:
            raise ValidationError("密码不能为空")
        
        if len(password) < 8:
            raise ValidationError("密码长度至少8个字符")
        
        if not re.search(r'[a-z]', password):
            raise ValidationError("密码必须包含小写字母")
        
        if not re.search(r'[A-Z]', password):
            raise ValidationError("密码必须包含大写字母")
        
        if not re.search(r'\d', password):
            raise ValidationError("密码必须包含数字")
        
        return True
    
    def validate_email(self, email):
        """验证邮箱"""
        if not email:
            raise ValidationError("邮箱不能为空")
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValidationError("邮箱格式不正确")
        
        return True
    
    def validate_age(self, age_str):
        """验证年龄"""
        try:
            age = int(age_str)
            if age < 18 or age > 100:
                raise ValidationError("年龄必须在18-100之间")
            return True
        except ValueError:
            raise ValidationError("年龄必须是数字")
    
    def validate_user_input(self, max_retries=3):
        """完整的用户输入验证流程"""
        fields = {
            'username': self.validate_username,
            'password': self.validate_password,
            'email': self.validate_email,
            'age': self.validate_age
        }
        
        user_data = {}
        
        for field_name, validator in fields.items():
            retry_count = 0
            
            while retry_count < max_retries:
                try:
                    value = input(f"请输入{field_name}: ")
                    validator(value)
                    user_data[field_name] = value
                    print(f"✅ {field_name}验证通过")
                    break
                    
                except ValidationError as e:
                    retry_count += 1
                    error_msg = f"{field_name}验证失败: {e}"
                    print(f"❌ {error_msg}")
                    
                    # 记录错误日志
                    self.logger.error(error_msg)
                    self.error_log.append({
                        'field': field_name,
                        'error': str(e),
                        'retry': retry_count
                    })
                    
                    if retry_count >= max_retries:
                        print(f"❌ {field_name}验证失败次数过多，跳过该字段")
                        break
                    else:
                        print(f"还有 {max_retries - retry_count} 次重试机会")
        
        return user_data

# 示例使用
def demo_validator():
    validator = UserInputValidator()
    
    # 模拟用户输入（实际使用时会从控制台输入）
    test_cases = [
        ("ab", "用户名太短"),
        ("valid_user123", "有效用户名"),
        ("123", "密码太短"),
        ("ValidPass123", "有效密码"),
        ("invalid-email", "无效邮箱"),
        ("user@example.com", "有效邮箱"),
        ("15", "年龄太小"),
        ("25", "有效年龄")
    ]
    
    for value, description in test_cases:
        try:
            if "用户名" in description:
                validator.validate_username(value)
            elif "密码" in description:
                validator.validate_password(value)
            elif "邮箱" in description:
                validator.validate_email(value)
            elif "年龄" in description:
                validator.validate_age(value)
            
            print(f"✅ {description}: {value}")
            
        except ValidationError as e:
            print(f"❌ {description}: {e}")

demo_validator()
```

### 题目9：文件操作异常处理

```python
import os
import shutil
import tempfile
from contextlib import contextmanager

class FileOperationError(Exception):
    """文件操作异常"""
    pass

class SafeFileOperator:
    def __init__(self):
        self.backup_dir = "file_backups"
        os.makedirs(self.backup_dir, exist_ok=True)
    
    def safe_read_file(self, filepath, encoding='utf-8'):
        """安全读取文件"""
        try:
            # 检查文件是否存在
            if not os.path.exists(filepath):
                raise FileOperationError(f"文件 {filepath} 不存在")
            
            # 检查文件权限
            if not os.access(filepath, os.R_OK):
                raise FileOperationError(f"没有读取 {filepath} 的权限")
            
            # 检查文件大小（避免内存问题）
            file_size = os.path.getsize(filepath)
            if file_size > 100 * 1024 * 1024:  # 100MB限制
                raise FileOperationError(f"文件 {filepath} 过大 ({file_size} 字节)")
            
            with open(filepath, 'r', encoding=encoding) as f:
                content = f.read()
            
            return content
            
        except PermissionError:
            raise FileOperationError(f"权限不足，无法读取 {filepath}")
        except UnicodeDecodeError as e:
            raise FileOperationError(f"文件编码错误: {e}")
        except MemoryError:
            raise FileOperationError(f"文件 {filepath} 太大，内存不足")
        except Exception as e:
            raise FileOperationError(f"读取文件时发生未知错误: {e}")
    
    def create_backup(self, filepath):
        """创建文件备份"""
        if os.path.exists(filepath):
            backup_name = f"{os.path.basename(filepath)}.backup"
            backup_path = os.path.join(self.backup_dir, backup_name)
            shutil.copy2(filepath, backup_path)
            return backup_path
        return None
    
    @contextmanager
    def atomic_write(self, filepath, mode='w', encoding='utf-8'):
        """原子性写入文件"""
        # 创建临时文件
        temp_fd, temp_path = tempfile.mkstemp(
            dir=os.path.dirname(filepath) or '.',
            prefix=f'.{os.path.basename(filepath)}.tmp'
        )
        
        try:
            # 关闭文件描述符，用Python的open重新打开
            os.close(temp_fd)
            
            with open(temp_path, mode, encoding=encoding) as temp_file:
                yield temp_file
            
            # 原子性地移动临时文件到目标位置
            if os.name == 'nt':  # Windows
                if os.path.exists(filepath):
                    os.remove(filepath)
            
            shutil.move(temp_path, filepath)
            
        except Exception:
            # 出错时清理临时文件
            try:
                os.remove(temp_path)
            except OSError:
                pass
            raise
    
    def safe_write_file(self, filepath, content, encoding='utf-8'):
        """安全写入文件"""
        try:
            # 检查目录是否存在，不存在则创建
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
            
            # 检查磁盘空间（简单检查）
            if hasattr(shutil, 'disk_usage'):
                free_space = shutil.disk_usage(directory or '.').free
                content_size = len(content.encode(encoding))
                if content_size > free_space:
                    raise FileOperationError("磁盘空间不足")
            
            # 创建备份
            backup_path = self.create_backup(filepath)
            
            try:
                # 原子性写入
                with self.atomic_write(filepath, 'w', encoding) as f:
                    f.write(content)
                
                print(f"✅ 文件 {filepath} 写入成功")
                if backup_path:
                    print(f"📁 备份文件保存在: {backup_path}")
                
            except Exception as e:
                # 写入失败时恢复备份
                if backup_path and os.path.exists(backup_path):
                    shutil.copy2(backup_path, filepath)
                    print(f"🔄 已从备份恢复文件: {filepath}")
                raise e
                
        except PermissionError:
            raise FileOperationError(f"权限不足，无法写入 {filepath}")
        except OSError as e:
            if e.errno == 28:  # No space left on device
                raise FileOperationError("磁盘空间不足")
            elif e.errno == 36:  # File name too long
                raise FileOperationError("文件名太长")
            else:
                raise FileOperationError(f"系统错误: {e}")
        except Exception as e:
            raise FileOperationError(f"写入文件时发生未知错误: {e}")

# 示例使用和测试
def demo_safe_file_operator():
    operator = SafeFileOperator()
    
    # 测试场景1：正常读写操作
    print("=== 测试1：正常文件操作 ===")
    try:
        # 写入文件
        content = "这是一个测试文件\n包含多行内容"
        operator.safe_write_file("test_file.txt", content)
        
        # 读取文件
        read_content = operator.safe_read_file("test_file.txt")
        print(f"读取的内容: {read_content}")
        
    except FileOperationError as e:
        print(f"文件操作错误: {e}")
    
    # 测试场景2：读取不存在的文件
    print("\n=== 测试2：读取不存在的文件 ===")
    try:
        content = operator.safe_read_file("nonexistent_file.txt")
    except FileOperationError as e:
        print(f"预期的错误: {e}")
    
    # 测试场景3：写入到只读目录（模拟）
    print("\n=== 测试3：权限测试 ===")
    try:
        # 在某些系统上，/root 目录可能没有写权限
        # 这里只是示例，实际测试需要根据系统调整
        if os.name != 'nt':  # 非Windows系统
            operator.safe_write_file("/root/test.txt", "测试内容")
    except FileOperationError as e:
        print(f"权限错误（预期）: {e}")
    
    # 测试场景4：原子性写入演示
    print("\n=== 测试4：原子性写入 ===")
    try:
        with operator.atomic_write("atomic_test.txt") as f:
            f.write("第一行\n")
            f.write("第二行\n")
            # 如果这里发生异常，文件不会被创建或部分写入
        print("原子性写入成功")
    except Exception as e:
        print(f"原子性写入失败: {e}")

demo_safe_file_operator()
```

### 题目10：网络请求模拟器

```python
import time
import random
from enum import Enum
from typing import Optional, Dict, Any

class NetworkError(Exception):
    """网络错误基类"""
    pass

class TimeoutError(NetworkError):
    """超时错误"""
    pass

class ConnectionError(NetworkError):
    """连接错误"""
    pass

class DNSError(NetworkError):
    """DNS解析错误"""
    pass

class NetworkErrorType(Enum):
    TIMEOUT = "timeout"
    CONNECTION_REFUSED = "connection_refused"
    DNS_ERROR = "dns_error"
    SUCCESS = "success"

class NetworkSimulator:
    def __init__(self, success_rate=0.7):
        self.success_rate = success_rate
        self.attempt_log = []
    
    def simulate_request(self, url: str) -> NetworkErrorType:
        """模拟网络请求"""
        # 随机决定请求结果
        rand = random.random()
        
        if rand < self.success_rate:
            return NetworkErrorType.SUCCESS
        elif rand < self.success_rate + 0.1:
            return NetworkErrorType.TIMEOUT
        elif rand < self.success_rate + 0.2:
            return NetworkErrorType.CONNECTION_REFUSED
        else:
            return NetworkErrorType.DNS_ERROR
    
    def make_request(self, url: str, timeout: int = 5) -> Dict[str, Any]:
        """执行单次请求"""
        start_time = time.time()
        
        # 模拟请求延迟
        time.sleep(random.uniform(0.1, 0.5))
        
        result = self.simulate_request(url)
        
        if result == NetworkErrorType.SUCCESS:
            return {
                "status": "success",
                "data": f"Response from {url}",
                "status_code": 200,
                "response_time": time.time() - start_time
            }
        elif result == NetworkErrorType.TIMEOUT:
            raise TimeoutError(f"Request to {url} timed out after {timeout}s")
        elif result == NetworkErrorType.CONNECTION_REFUSED:
            raise ConnectionError(f"Connection to {url} refused")
        else:
            raise DNSError(f"DNS resolution failed for {url}")

class RetryableNetworkClient:
    def __init__(self, max_retries=3, base_delay=1.0, backoff_factor=2.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.backoff_factor = backoff_factor
        self.simulator = NetworkSimulator()
        self.request_log = []
    
    def calculate_delay(self, attempt: int) -> float:
        """计算指数退避延迟"""
        return self.base_delay * (self.backoff_factor ** (attempt - 1))
    
    def request_with_retry(self, url: str, fallback_response=None) -> Dict[str, Any]:
        """带重试机制的网络请求"""
        last_exception = None
        
        for attempt in range(1, self.max_retries + 1):
            try:
                print(f"🔄 第 {attempt} 次尝试请求 {url}")
                
                response = self.simulator.make_request(url)
                
                # 记录成功请求
                self.request_log.append({
                    "url": url,
                    "attempt": attempt,
                    "status": "success",
                    "response_time": response.get("response_time", 0)
                })
                
                print(f"✅ 请求成功！")
                return response
                
            except NetworkError as e:
                last_exception = e
                
                # 记录失败请求
                self.request_log.append({
                    "url": url,
                    "attempt": attempt,
                    "status": "failed",
                    "error": str(e),
                    "error_type": type(e).__name__
                })
                
                print(f"❌ 第 {attempt} 次尝试失败: {e}")
                
                # 如果不是最后一次尝试，则等待后重试
                if attempt < self.max_retries:
                    delay = self.calculate_delay(attempt)
                    print(f"⏳ {delay:.1f}秒后重试...")
                    time.sleep(delay)
                else:
                    print(f"💥 所有重试均失败，使用降级方案")
        
        # 所有重试均失败，返回降级响应
        if fallback_response is not None:
            print(f"🔄 使用降级响应")
            return fallback_response
        
        # 如果没有降级方案，抛出最后一个异常
        raise last_exception
    
    def bulk_request(self, urls: list, fallback_responses=None) -> Dict[str, Any]:
        """批量请求"""
        results = {}
        fallback_dict = fallback_responses or {}
        
        for url in urls:
            try:
                fallback = fallback_dict.get(url)
                response = self.request_with_retry(url, fallback)
                results[url] = response
            except Exception as e:
                results[url] = {"status": "failed", "error": str(e)}
        
        return results
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取请求统计信息"""
        if not self.request_log:
            return {"total_requests": 0}
        
        total_requests = len(self.request_log)
        successful_requests = len([r for r in self.request_log if r["status"] == "success"])
        failed_requests = total_requests - successful_requests
        
        # 按错误类型统计
        error_types = {}
        for request in self.request_log:
            if request["status"] == "failed":
                error_type = request.get("error_type", "Unknown")
                error_types[error_type] = error_types.get(error_type, 0) + 1
        
        # 计算平均重试次数
        urls = list(set([r["url"] for r in self.request_log]))
        avg_attempts = sum([
            max([r["attempt"] for r in self.request_log if r["url"] == url])
            for url in urls
        ]) / len(urls) if urls else 0
        
        return {
            "total_requests": total_requests,
            "successful_requests": successful_requests,
            "failed_requests": failed_requests,
            "success_rate": successful_requests / total_requests if total_requests > 0 else 0,
            "error_types": error_types,
            "average_attempts": avg_attempts
        }

# 示例使用
def demo_network_client():
    client = RetryableNetworkClient(max_retries=3, base_delay=1.0)
    
    # 测试单个请求
    print("=== 测试单个请求 ===")
    try:
        fallback = {"status": "fallback", "data": "Cached response", "source": "cache"}
        response = client.request_with_retry("https://api.example.com/users", fallback)
        print(f"最终响应: {response}")
    except Exception as e:
        print(f"请求最终失败: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 测试批量请求
    print("=== 测试批量请求 ===")
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/products",
        "https://api.example.com/orders"
    ]
    
    fallback_responses = {
        "https://api.example.com/users": {"status": "cached", "data": "Cached users"},
        "https://api.example.com/products": {"status": "cached", "data": "Cached products"}
    }
    
    results = client.bulk_request(urls, fallback_responses)
    
    print("批量请求结果:")
    for url, result in results.items():
        print(f"  {url}: {result.get('status', 'unknown')}")
    
    print("\n" + "="*50 + "\n")
    
    # 显示统计信息
    print("=== 请求统计信息 ===")
    stats = client.get_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")

demo_network_client()
```

### 题目11：数据库连接模拟器

```python
import time
import random
from enum import Enum
from typing import Optional, Dict, Any, List
from contextlib import contextmanager

class DatabaseError(Exception):
    """数据库异常基类"""
    pass

class ConnectionTimeoutError(DatabaseError):
    """连接超时异常"""
    pass

class AuthenticationError(DatabaseError):
    """认证失败异常"""
    pass

class DatabaseNotFoundError(DatabaseError):
    """数据库不存在异常"""
    pass

class SQLSyntaxError(DatabaseError):
    """SQL语法错误异常"""
    pass

class ConstraintViolationError(DatabaseError):
    """数据约束违反异常"""
    pass

class DatabaseConnectionState(Enum):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    ERROR = "error"

class MockDatabase:
    def __init__(self, name: str, success_rate: float = 0.8):
        self.name = name
        self.success_rate = success_rate
        self.connection_state = DatabaseConnectionState.DISCONNECTED
        self.transaction_active = False
        self.tables = {"users": [], "products": [], "orders": []}
    
    def simulate_connection(self, username: str, password: str) -> bool:
        """模拟数据库连接"""
        # 模拟网络延迟
        time.sleep(random.uniform(0.1, 0.3))
        
        # 模拟各种连接错误
        rand = random.random()
        
        if rand < 0.1:  # 10% 概率连接超时
            raise ConnectionTimeoutError("数据库连接超时")
        elif rand < 0.15:  # 5% 概率认证失败
            raise AuthenticationError("用户名或密码错误")
        elif rand < 0.18:  # 3% 概率数据库不存在
            raise DatabaseNotFoundError(f"数据库 '{self.name}' 不存在")
        elif rand < self.success_rate:
            return True
        else:
            raise DatabaseError("未知数据库错误")
    
    def execute_query(self, sql: str) -> Dict[str, Any]:
        """模拟SQL查询执行"""
        if self.connection_state != DatabaseConnectionState.CONNECTED:
            raise DatabaseError("数据库未连接")
        
        # 模拟SQL语法检查
        if "SELEC" in sql.upper() and "SELECT" not in sql.upper():
            raise SQLSyntaxError(f"SQL语法错误: {sql}")
        
        # 模拟约束违反
        if "INSERT" in sql.upper() and "duplicate" in sql.lower():
            raise ConstraintViolationError("违反唯一性约束")
        
        # 模拟执行延迟
        time.sleep(random.uniform(0.05, 0.2))
        
        return {
            "status": "success",
            "rows_affected": random.randint(1, 10),
            "execution_time": random.uniform(0.1, 0.5)
        }

class DatabaseConnectionManager:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.database = MockDatabase(config["database"], config.get("success_rate", 0.8))
        self.connection_pool = []
        self.max_retries = config.get("max_retries", 3)
        self.retry_delay = config.get("retry_delay", 1.0)
        self.connection_log = []
    
    def connect_with_retry(self) -> bool:
        """带重试机制的数据库连接"""
        for attempt in range(1, self.max_retries + 1):
            try:
                print(f"🔄 第 {attempt} 次尝试连接数据库 '{self.config['database']}'")
                
                success = self.database.simulate_connection(
                    self.config["username"],
                    self.config["password"]
                )
                
                if success:
                    self.database.connection_state = DatabaseConnectionState.CONNECTED
                    print(f"✅ 数据库连接成功！")
                    
                    self.connection_log.append({
                        "timestamp": time.time(),
                        "attempt": attempt,
                        "status": "success"
                    })
                    
                    return True
                    
            except DatabaseError as e:
                print(f"❌ 连接失败: {e}")
                
                self.connection_log.append({
                    "timestamp": time.time(),
                    "attempt": attempt,
                    "status": "failed",
                    "error": str(e),
                    "error_type": type(e).__name__
                })
                
                if attempt < self.max_retries:
                    delay = self.retry_delay * attempt  # 线性退避
                    print(f"⏳ {delay}秒后重试...")
                    time.sleep(delay)
        
        print(f"💥 数据库连接失败，已达到最大重试次数")
        self.database.connection_state = DatabaseConnectionState.ERROR
        return False
    
    @contextmanager
    def transaction(self):
        """事务管理上下文管理器"""
        if self.database.connection_state != DatabaseConnectionState.CONNECTED:
            raise DatabaseError("数据库未连接")
        
        print("📝 开始事务")
        self.database.transaction_active = True
        transaction_log = []
        
        try:
            yield transaction_log
            
            # 事务提交
            print("✅ 事务提交成功")
            
        except Exception as e:
            # 事务回滚
            print(f"🔄 事务回滚: {e}")
            
            # 模拟回滚操作
            for operation in reversed(transaction_log):
                print(f"  撤销操作: {operation}")
            
            raise e
        finally:
            self.database.transaction_active = False
            print("📝 事务结束")
    
    def execute_query_safe(self, sql: str) -> Optional[Dict[str, Any]]:
        """安全执行SQL查询"""
        try:
            if self.database.connection_state != DatabaseConnectionState.CONNECTED:
                # 尝试重新连接
                if not self.connect_with_retry():
                    return None
            
            result = self.database.execute_query(sql)
            
            # 记录查询日志
            self.connection_log.append({
                "timestamp": time.time(),
                "type": "query",
                "sql": sql,
                "status": "success",
                "result": result
            })
            
            return result
            
        except DatabaseError as e:
            print(f"❌ 查询执行失败: {e}")
            
            self.connection_log.append({
                "timestamp": time.time(),
                "type": "query",
                "sql": sql,
                "status": "failed",
                "error": str(e),
                "error_type": type(e).__name__
            })
            
            return None
    
    def get_connection_statistics(self) -> Dict[str, Any]:
        """获取连接统计信息"""
        total_connections = len([log for log in self.connection_log if log.get("type") != "query"])
        successful_connections = len([log for log in self.connection_log 
                                    if log.get("status") == "success" and log.get("type") != "query"])
        
        total_queries = len([log for log in self.connection_log if log.get("type") == "query"])
        successful_queries = len([log for log in self.connection_log 
                                if log.get("type") == "query" and log.get("status") == "success"])
        
        error_types = {}
        for log in self.connection_log:
            if log.get("status") == "failed":
                error_type = log.get("error_type", "Unknown")
                error_types[error_type] = error_types.get(error_type, 0) + 1
        
        return {
            "total_connection_attempts": total_connections,
            "successful_connections": successful_connections,
            "total_queries": total_queries,
            "successful_queries": successful_queries,
            "connection_success_rate": successful_connections / total_connections if total_connections > 0 else 0,
            "query_success_rate": successful_queries / total_queries if total_queries > 0 else 0,
            "error_types": error_types,
            "current_state": self.database.connection_state.value
        }

# 示例使用
def demo_database_manager():
    # 数据库配置
    config = {
        "host": "localhost",
        "port": 5432,
        "database": "testdb",
        "username": "admin",
        "password": "password123",
        "max_retries": 3,
        "retry_delay": 1.0,
        "success_rate": 0.7  # 模拟70%成功率
    }
    
    db_manager = DatabaseConnectionManager(config)
    
    # 测试连接
    print("=== 测试数据库连接 ===")
    if db_manager.connect_with_retry():
        
        # 测试普通查询
        print("\n=== 测试普通查询 ===")
        queries = [
            "SELECT * FROM users",
            "SELEC * FROM products",  # 语法错误
            "INSERT INTO users VALUES (1, 'duplicate')",  # 约束违反
            "UPDATE users SET name='John' WHERE id=1"
        ]
        
        for sql in queries:
            print(f"\n执行查询: {sql}")
            result = db_manager.execute_query_safe(sql)
            if result:
                print(f"查询结果: {result}")
        
        # 测试事务
        print("\n=== 测试事务管理 ===")
        try:
            with db_manager.transaction() as transaction_log:
                transaction_log.append("INSERT INTO users VALUES (1, 'Alice')")
                transaction_log.append("INSERT INTO users VALUES (2, 'Bob')")
                
                # 模拟事务中的操作
                for operation in transaction_log:
                    print(f"  执行: {operation}")
                    db_manager.execute_query_safe(operation)
                
                # 模拟事务中发生错误
                if random.random() < 0.3:  # 30%概率发生错误
                    raise DatabaseError("模拟事务错误")
                    
        except DatabaseError as e:
            print(f"事务处理异常: {e}")
    
    # 显示统计信息
    print("\n=== 数据库连接统计 ===")
    stats = db_manager.get_connection_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")

demo_database_manager()
```

### 题目12：API错误处理框架

```python
import json
import time
from enum import Enum
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from collections import defaultdict

class HTTPStatus(Enum):
    """HTTP状态码枚举"""
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

class ErrorCode(Enum):
    """错误码枚举"""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    AUTHENTICATION_FAILED = "AUTHENTICATION_FAILED"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_INPUT = "INVALID_INPUT"
    DUPLICATE_RESOURCE = "DUPLICATE_RESOURCE"

@dataclass
class ErrorDetail:
    """错误详细信息"""
    field: str
    message: str
    code: Optional[str] = None

class APIError(Exception):
    """API异常基类"""
    def __init__(self, 
                 error_code: ErrorCode, 
                 message: str, 
                 http_status: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
                 details: List[ErrorDetail] = None,
                 request_id: str = None):
        self.error_code = error_code
        self.message = message
        self.http_status = http_status
        self.details = details or []
        self.request_id = request_id
        self.timestamp = time.time()
        super().__init__(message)

class ValidationError(APIError):
    """参数验证错误"""
    def __init__(self, message: str, details: List[ErrorDetail] = None, request_id: str = None):
        super().__init__(
            error_code=ErrorCode.VALIDATION_ERROR,
            message=message,
            http_status=HTTPStatus.BAD_REQUEST,
            details=details,
            request_id=request_id
        )

class AuthenticationError(APIError):
    """认证失败错误"""
    def __init__(self, message: str = "认证失败", request_id: str = None):
        super().__init__(
            error_code=ErrorCode.AUTHENTICATION_FAILED,
            message=message,
            http_status=HTTPStatus.UNAUTHORIZED,
            request_id=request_id
        )

class AuthorizationError(APIError):
    """权限不足错误"""
    def __init__(self, message: str = "权限不足", request_id: str = None):
        super().__init__(
            error_code=ErrorCode.PERMISSION_DENIED,
            message=message,
            http_status=HTTPStatus.FORBIDDEN,
            request_id=request_id
        )

class ResourceNotFoundError(APIError):
    """资源未找到错误"""
    def __init__(self, resource: str, resource_id: str = None, request_id: str = None):
        message = f"资源 {resource}"
        if resource_id:
            message += f" (ID: {resource_id})"
        message += " 未找到"
        
        super().__init__(
            error_code=ErrorCode.RESOURCE_NOT_FOUND,
            message=message,
            http_status=HTTPStatus.NOT_FOUND,
            request_id=request_id
        )

class InternalServerError(APIError):
    """服务器内部错误"""
    def __init__(self, message: str = "服务器内部错误", request_id: str = None):
        super().__init__(
            error_code=ErrorCode.INTERNAL_ERROR,
            message=message,
            http_status=HTTPStatus.INTERNAL_SERVER_ERROR,
            request_id=request_id
        )

class ErrorResponseFormatter:
    """错误响应格式化器"""
    
    def __init__(self, locale: str = "zh-CN"):
        self.locale = locale
        self.translations = self._load_translations()
    
    def _load_translations(self) -> Dict[str, Dict[str, str]]:
        """加载国际化消息"""
        return {
            "zh-CN": {
                "VALIDATION_ERROR": "参数验证失败",
                "AUTHENTICATION_FAILED": "认证失败",
                "PERMISSION_DENIED": "权限不足",
                "RESOURCE_NOT_FOUND": "资源未找到",
                "INTERNAL_ERROR": "服务器内部错误",
                "INVALID_INPUT": "输入参数无效",
                "DUPLICATE_RESOURCE": "资源已存在"
            },
            "en-US": {
                "VALIDATION_ERROR": "Validation failed",
                "AUTHENTICATION_FAILED": "Authentication failed",
                "PERMISSION_DENIED": "Permission denied",
                "RESOURCE_NOT_FOUND": "Resource not found",
                "INTERNAL_ERROR": "Internal server error",
                "INVALID_INPUT": "Invalid input",
                "DUPLICATE_RESOURCE": "Resource already exists"
            }
        }
    
    def format_error_response(self, error: APIError) -> Dict[str, Any]:
        """格式化错误响应"""
        # 获取本地化消息
        translated_message = self.translations.get(self.locale, {}).get(
            error.error_code.value, 
            error.message
        )
        
        response = {
            "error": {
                "code": error.error_code.value,
                "message": translated_message,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(error.timestamp)),
                "request_id": error.request_id or self._generate_request_id()
            }
        }
        
        # 添加详细错误信息
        if error.details:
            response["error"]["details"] = [
                {
                    "field": detail.field,
                    "message": detail.message,
                    "code": detail.code
                }
                for detail in error.details
            ]
        
        return response
    
    def _generate_request_id(self) -> str:
        """生成请求ID"""
        import uuid
        return str(uuid.uuid4())[:8]

class ErrorStatistics:
    """错误统计"""
    
    def __init__(self):
        self.error_counts = defaultdict(int)
        self.error_history = []
        self.hourly_stats = defaultdict(lambda: defaultdict(int))
    
    def record_error(self, error: APIError):
        """记录错误"""
        # 统计错误类型
        self.error_counts[error.error_code.value] += 1
        
        # 记录错误历史
        self.error_history.append({
            "timestamp": error.timestamp,
            "error_code": error.error_code.value,
            "http_status": error.http_status.value,
            "message": error.message,
            "request_id": error.request_id
        })
        
        # 按小时统计
        hour = int(error.timestamp // 3600)
        self.hourly_stats[hour][error.error_code.value] += 1
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        total_errors = sum(self.error_counts.values())
        
        if total_errors == 0:
            return {"total_errors": 0}
        
        # 计算错误率
        error_rates = {
            error_type: count / total_errors
            for error_type, count in self.error_counts.items()
        }
        
        # 最近1小时的错误
        current_hour = int(time.time() // 3600)
        recent_errors = self.hourly_stats.get(current_hour, {})
        
        return {
            "total_errors": total_errors,
            "error_counts": dict(self.error_counts),
            "error_rates": error_rates,
            "recent_errors": dict(recent_errors),
            "most_common_error": max(self.error_counts.items(), key=lambda x: x[1])[0] if self.error_counts else None
        }

class APIErrorHandler:
    """API错误处理器"""
    
    def __init__(self, locale: str = "zh-CN"):
        self.formatter = ErrorResponseFormatter(locale)
        self.statistics = ErrorStatistics()
    
    def handle_error(self, error: Exception, request_id: str = None) -> tuple[Dict[str, Any], int]:
        """处理错误并返回响应"""
        # 将普通异常转换为APIError
        if not isinstance(error, APIError):
            if isinstance(error, ValueError):
                api_error = ValidationError(str(error), request_id=request_id)
            elif isinstance(error, PermissionError):
                api_error = AuthorizationError(str(error), request_id=request_id)
            elif isinstance(error, FileNotFoundError):
                api_error = ResourceNotFoundError("文件", request_id=request_id)
            else:
                api_error = InternalServerError(f"未知错误: {str(error)}", request_id=request_id)
        else:
            api_error = error
        
        # 记录错误统计
        self.statistics.record_error(api_error)
        
        # 格式化响应
        response = self.formatter.format_error_response(api_error)
        
        return response, api_error.http_status.value

# 示例使用和测试
def demo_api_error_handler():
    handler = APIErrorHandler("zh-CN")
    
    # 测试不同类型的错误
    test_errors = [
        ValidationError(
            "用户数据验证失败",
            details=[
                ErrorDetail("email", "邮箱格式不正确", "INVALID_EMAIL"),
                ErrorDetail("age", "年龄必须在18-100之间", "INVALID_RANGE")
            ],
            request_id="req_001"
        ),
        AuthenticationError("JWT token已过期", request_id="req_002"),
        AuthorizationError("需要管理员权限", request_id="req_003"),
        ResourceNotFoundError("用户", "12345", request_id="req_004"),
        InternalServerError("数据库连接失败", request_id="req_005"),
        
        # 普通异常
        ValueError("无效的参数值"),
        PermissionError("文件访问权限不足"),
        FileNotFoundError("配置文件不存在")
    ]
    
    print("=== API错误处理测试 ===")
    for i, error in enumerate(test_errors, 1):
        print(f"\n--- 测试 {i}: {type(error).__name__} ---")
        response, status_code = handler.handle_error(error, f"req_{i:03d}")
        
        print(f"HTTP状态码: {status_code}")
        print(f"响应内容: {json.dumps(response, ensure_ascii=False, indent=2)}")
    
    # 显示错误统计
    print("\n=== 错误统计信息 ===")
    stats = handler.statistics.get_statistics()
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    
    # 测试国际化
    print("\n=== 国际化测试 ===")
    en_handler = APIErrorHandler("en-US")
    error = ValidationError("测试错误", request_id="req_i18n")
    response, _ = en_handler.handle_error(error)
    print("英文响应:", json.dumps(response, indent=2))

demo_api_error_handler()
``` 