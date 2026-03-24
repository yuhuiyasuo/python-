import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy import String, Integer, Boolean, Column, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

app = FastAPI()

# ---------------------- 1. 基础配置 ----------------------
# 1.1 定义模型基类（SQLAlchemy 2.0+ 推荐写法）
class Base(DeclarativeBase):    #DeclarativeBase 是ORM的核心基类  所有数据格式都要继承这个类
    pass

# 1.2 定义数据模型（对应数据库表）
class User(Base):
    # 表名
    __tablename__ = "stuents"

    # 字段定义（Column(类型, 约束)）
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键、自增、索引
    name = Column(String(50), index=True, nullable=False)  # 字符串、索引、非空
    age = Column(Integer, default=0)  # 整数、默认值
    is_active = Column(Boolean, default=True)  # 布尔、默认值


# 1.3 创建引擎（连接数据库）
# SQLite 示例：文件名为 test.db，若不存在会自动创建
ASYNC_URL_SQL = "mysql+aiomysql://root:000000@localhost:3306/sqlalcmy_test?charset=utf8"
engine = create_async_engine(
    ASYNC_URL_SQL,
    echo=True,  # 打印 SQL 语句（调试用，生产可关闭）
    pool_size  = 10,
    max_overflow = 20
)

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)   #扫描所有继承 Base 的 ORM 模型（这里只有 User），生成对应的 CREATE TABLE SQL 语句



# Uvicorn 启动 FastAPI 应用成功后，会自动触发
@app.on_event("startup")
async def startup_event():
    await create_table()


#每次操作数据库都会创建一个会话
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

#Session 是事务的核心载体：所有数据库操作（增删改查）默认都在一个事务中，只有调用 commit() 才会将所有操作提交到数据库  ACID保证
async def get_date():
    async with  AsyncSessionLocal() as session:
        try:
            yield session
            #将会话对象传递给接口函数（接口中通过 Depends(get_date) 获取）；yield 是「暂停执行」，接口操作完数据库后（执行完get_date），才会执行后续代码。

            await session.commit()
        except Exception:
            await session.rollback()  #回滚事务
            raise
        finally:
            await session.close()


@app.get("/name")
async def get_name(db: AsyncSession = Depends(get_date)):   #db获取到的就是session
    res = await db.execute(select(User))
    user = res.scalars().all()
    return user




if __name__ == "__main__":

    uvicorn.run(app,host='0.0.0.0',port=8000)












#
# # 1.4 创建会话工厂（用于操作数据库）
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# # ---------------------- 2. 核心操作 ----------------------
# def init_db():
#     """创建所有表（若表已存在则忽略）"""
#     Base.metadata.create_all(bind=engine)
#     print("数据库表创建成功！")
#
#
# def add_user(db: Session, name: str, age: int):
#     """新增用户"""
#     db_user = User(name=name, age=age)
#     db.add(db_user)  # 添加到会话
#     db.commit()  # 提交事务
#     db.refresh(db_user)  # 刷新对象（获取自增的 id 等）
#     return db_user
#
#
# def get_user(db: Session, user_id: int):
#     """查询单个用户"""
#     return db.query(User).filter(User.id == user_id).first()
#
#
# # ---------------------- 3. 执行逻辑 ----------------------
# if __name__ == "__main__":
#     # 第一步：初始化数据库（创建表）
#     init_db()
#
#     # 第二步：获取会话并操作数据
#     db = SessionLocal()  # 打开会话
#     try:
#         # 新增用户
#         new_user = add_user(db, name="张三", age=25)
#         print(f"新增用户：ID={new_user.id}, 姓名={new_user.name}, 年龄={new_user.age}")
#
#         # 查询用户
#         user = get_user(db, user_id=new_user.id)
#         if user:
#             print(f"查询到用户：{user.name}（{user.age}岁）")
#     finally:
#         db.close()  # 无论是否出错，都关闭会话