from sqlalchemy import create_engine, insert
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, text
from datetime import datetime
# SQLite 示例（文件型数据库，echo=True 会打印执行的SQL，调试用）
#engine = create_engine("sqlite:///demo.db", echo=True)

# MySQL 示例
engine = create_engine(
    "mysql+pymysql://root:12345678@localhost:3306/sqlalchemy_test?charset=utf8mb4",
    pool_size=5,  # 连接池大小
    max_overflow=10  # 最大溢出连接数
)



# 元数据容器，所有表都注册到这里
metadata = MetaData()

# 定义用户表
user_table = Table(
    "users",  # 表名
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, comment="主键ID"),
    Column("name", String(50), nullable=False, comment="用户名"),
    Column("age", Integer, index=True, comment="年龄"),
    Column("created_at", DateTime, server_default=text("CURRENT_TIMESTAMP"), comment="创建时间")
)

metadata.create_all(engine)



with engine.connect() as conn:
    # 单条插入
    stmt = insert(user_table).values(name="张三", age=25)
    conn.execute(stmt)

    # 批量插入（性能远高于循环单条插入）
    conn.execute(
        insert(user_table),
        [
            {"name": "李四", "age": 30},
            {"name": "王五", "age": 28},
            {"name": "赵六", "age": 22}
        ]
    )
    conn.commit()  # 必须显式提交事务

print("查询数据")

from sqlalchemy import select, and_, or_

with engine.connect() as conn:
    # 1. 查询所有字段
    stmt = select(user_table)
    result = conn.execute(stmt)
    for row in result:
        print(row.id, row.name, row.age)  # 支持属性访问和下标访问

    # 2. 条件查询 + 排序 + 分页
    stmt = (
        select(user_table)
        .where(and_(user_table.c.age > 23, user_table.c.name.like("张%")))
        .order_by(user_table.c.age.desc())
        .limit(2)
        .offset(0)
    )
    rows = conn.execute(stmt).all()

    # 3. 查询指定字段
    stmt = select(user_table.c.name, user_table.c.age)
    result = conn.execute(stmt)

from sqlalchemy import update

with engine.connect() as conn:
    # 条件更新
    stmt = update(user_table).where(user_table.c.id == 1).values(age=26)
    conn.execute(stmt)
    conn.commit()

from sqlalchemy import delete

with engine.connect() as conn:
    stmt = delete(user_table).where(user_table.c.age < 23)
    conn.execute(stmt)
    conn.commit()


