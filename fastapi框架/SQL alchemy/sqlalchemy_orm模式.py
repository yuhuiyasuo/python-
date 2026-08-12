from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import String, Integer, DateTime, text, create_engine
from datetime import datetime


engine = create_engine(
    "mysql+pymysql://root:12345678@localhost:3306/sqlalchemy_test?charset=utf8mb4",
    pool_size=5,  # 连接池大小
    max_overflow=10  # 最大溢出连接数
)

Session = sessionmaker(bind=engine)
# 1. 声明基类，所有ORM模型都继承它
class Base(DeclarativeBase):
    pass

# 2. 定义用户模型
class User(Base):
    __tablename__ = "users"  # 对应数据库表名

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(index=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

# 3. 创建表（和Core共用metadata）
Base.metadata.create_all(engine)


# with Session() as session:
#     # 单条新增
#     user = User(name="孙七", age=27)
#     session.add(user)
#     session.commit()  # 提交后才会写入数据库
#     print(user.id)  # 提交后可获取自增主键
#
#     # 批量新增
#     users = [
#         User(name="周八", age=29),
#         User(name="吴九", age=31)
#     ]
#     session.add_all(users)
#     session.commit()




from sqlalchemy import select, and_

with Session() as session:
    # 1. 查询所有
    stmt = select(User)
    # scalars() 提取结果中的模型对象；all() 返回列表
    users = session.execute(stmt).scalars().all()
    for user in users:
        print(user.name, user.age)

    # 2. 条件查询 + 获取单条
    stmt = select(User).where(and_(User.age > 25, User.name == "张三"))
    user = session.execute(stmt).scalars().first()  # 第一条，无则返回None

    # 3. 主键查询（推荐，会走缓存）
    user = session.get(User, 1)

    # 4. 排序 + 分页
    stmt = select(User).order_by(User.age.desc()).limit(2).offset(1)
    users = session.execute(stmt).scalars().all()

    # 5. 统计数量
    from sqlalchemy import func
    count = session.execute(select(func.count(User.id))).scalar()




# with Session() as session:
#     # 方式1：先查询再删除
#     user = session.get(User, 2)
#     if user:
#         session.delete(user)
#         session.commit()
#
#     # 方式2：批量条件删除
#     from sqlalchemy import delete
#     stmt = delete(User).where(User.age > 30)
#     session.execute(stmt)
#     session.commit()