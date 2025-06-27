# 🗄️ 数据库学习指南

## 📁 目录结构

```
数据库/
├── README.md                      # 本文件 - 学习指南
├── 数据库学习计划.md              # 完整的2周学习计划
├── docker-compose.yml             # Docker环境配置
├── 1. 数据库基础学习.ipynb        # 基础理论和SQLite实践
├── 2. 数据库实战练习.ipynb        # 综合项目练习
├── 3. PostgreSQL进阶.ipynb        # PostgreSQL和ORM (待创建)
└── 4. Redis缓存实战.ipynb         # Redis操作 (待创建)
```

## 🚀 快速开始

### 1. 环境准备

#### 方案一：最简单 (推荐新手)
```bash
# 只需要Python，SQLite已内置
python --version  # 确保Python已安装
pip install pandas jupyter  # 安装必要库
```

#### 方案二：完整环境 (推荐进阶)
```bash
# 确保已安装Docker和Docker Compose
docker --version
docker-compose --version

# 启动所有数据库服务
cd 知识路线/数据库
docker-compose up -d

# 查看服务状态
docker-compose ps
```

### 2. 开始学习

#### 第1步：阅读学习计划
```bash
# 打开学习计划文档
open 数据库学习计划.md
```

#### 第2步：基础学习
```bash
# 启动Jupyter Notebook
jupyter notebook

# 打开第一个notebook
# 1. 数据库基础学习.ipynb
```

#### 第3步：实战练习
```bash
# 完成基础学习后，打开实战练习
# 2. 数据库实战练习.ipynb
```

## 🔗 服务访问地址

### Docker服务 (如果启动了完整环境)
- **MySQL**: `localhost:3306` ⭐ **用户要求**
  - 用户名: `student` (或 `root`)
  - 密码: `student123`
  - 数据库: `learning_db`

- **PostgreSQL**: `localhost:5432`
  - 用户名: `student`
  - 密码: `student123`
  - 数据库: `learning_db`

- **Redis**: `localhost:6379`

- **MongoDB**: `localhost:27017`
  - 用户名: `student`
  - 密码: `student123`

- **pgAdmin** (PostgreSQL管理工具): http://localhost:8080
  - 邮箱: `student@example.com`
  - 密码: `admin123`

## 📚 学习顺序

### 🎯 2周学习计划

#### 第1周：SQL基础
1. **第1-2天**: `1. 数据库基础学习.ipynb`
2. **第3-4天**: 完成所有基础练习
3. **第5-6天**: `2. 数据库实战练习.ipynb`
4. **第7天**: 复习和总结

#### 第2周：进阶实战
1. **第8-9天**: `3. PostgreSQL进阶.ipynb`
2. **第10-11天**: `4. Redis缓存实战.ipynb`
3. **第12-13天**: 综合项目实战
4. **第14天**: 总结和拓展学习

## 🛠️ 依赖安装

### Python包
```bash
pip install -r requirements.txt
```

### requirements.txt 内容:
```
pandas>=1.5.0
jupyter>=1.0.0
psycopg2-binary>=2.9.0  # PostgreSQL驱动
redis>=4.0.0            # Redis客户端
pymongo>=4.0.0          # MongoDB驱动
sqlalchemy>=2.0.0       # ORM框架
```

## 🎯 学习目标

### 基础目标 (第1周)
- ✅ 理解关系型数据库概念
- ✅ 掌握SQL基础语法 (CRUD)
- ✅ 能够设计简单的数据库表
- ✅ 使用Python操作SQLite
- ✅ 了解数据库安全最佳实践

### 进阶目标 (第2周)
- ✅ 掌握PostgreSQL使用
- ✅ 学会使用ORM框架
- ✅ 理解Redis缓存机制
- ✅ 能够设计复杂的数据库架构
- ✅ 掌握数据库性能优化

## 🔧 故障排除

### 常见问题

#### 1. Docker服务启动失败
```bash
# 检查端口占用
netstat -an | grep 5432

# 停止冲突服务
sudo lsof -ti:5432 | xargs kill -9

# 重新启动
docker-compose down
docker-compose up -d
```

#### 2. Jupyter无法连接数据库
```bash
# 检查网络连接
ping localhost

# 确认服务状态
docker-compose logs postgres
```

#### 3. Python包安装问题
```bash
# 使用虚拟环境
python -m venv db_learning
source db_learning/bin/activate  # Linux/Mac
# db_learning\Scripts\activate   # Windows

pip install -r requirements.txt
```

## 📖 扩展资源

### 官方文档
- [PostgreSQL官方文档](https://www.postgresql.org/docs/)
- [Redis官方文档](https://redis.io/documentation)
- [SQLAlchemy官方文档](https://docs.sqlalchemy.org/)

### 在线练习
- [SQLBolt](https://sqlbolt.com/) - SQL交互式学习
- [W3Schools SQL](https://www.w3schools.com/sql/) - SQL教程
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) - PostgreSQL专项教程

### 推荐书籍
- 《SQL基础教程》- MICK
- 《高性能MySQL》- Baron Schwartz
- 《PostgreSQL实战》- 谭峰

## 🎊 完成标志

学完本系列教程，你应该能够：

1. **独立设计** 中等复杂度的数据库架构
2. **熟练编写** 各种SQL查询语句
3. **使用Python** 进行数据库操作和ORM开发
4. **理解并应用** 数据库安全和性能最佳实践
5. **搭建并管理** PostgreSQL和Redis服务

---

**🚀 准备开始你的数据库学习之旅吗？从`1. 数据库基础学习.ipynb`开始吧！** 