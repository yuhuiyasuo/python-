from sqlalchemy import create_engine, func
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

# 1. 创建引擎（连接数据库，echo=True 打印生成的 SQL 语句，调试用）
engine = create_engine(
    "mysql+aiomysql://root:000000@localhost:3306/sqlalcmy_test?charset=utf8",  # SQLite 数据库文件
    echo=True,            # 打印 SQL 日志（生产环境建议关闭）
    pool_size=10,         # 连接池大小
    max_overflow=20       # 连接池最大溢出数
)

# 2. 创建 ORM 基类（所有模型类都继承这个基类）
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# 3. 创建会话工厂（Session 是操作数据库的入口）
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,  # 关闭自动刷新
    autocommit=False, # 关闭自动提交
    expire_on_commit=False  # 提交后不失效对象
)

# 获取会话实例（每次操作数据库都创建一个会话）
def get_db():
    db = SessionLocal()
    try:
        yield db  # 生成会话对象
    finally:
        db.close()  # 确保会话关闭