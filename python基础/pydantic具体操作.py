# 导入必要依赖
from typing import TypeVar, Generic, Type, Optional, List

import Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# 1. 定义泛型类型（复用你提供的代码）
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

# 2. 定义 CRUD 基类（补充核心 CRUD 方法）
class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD 基类，包含默认的增删改查方法
        :param model: SQLAlchemy 模型类（如 User）
        """
        self.model = model

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        """根据 ID 查询单条记录"""
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """批量查询记录（支持分页）"""
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """创建新记录"""
        # 将 Pydantic 模型转为字典，排除额外字段
        obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data)  # 创建 SQLAlchemy 模型实例
        db.add(db_obj)
        db.commit()  # 提交事务
        db.refresh(db_obj)  # 刷新实例，获取数据库自动生成的字段（如 id）
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | dict
    ) -> ModelType:
        """更新记录"""
        # 处理传入的参数（支持 Pydantic 模型或字典）
        obj_data = obj_in.model_dump() if isinstance(obj_in, BaseModel) else obj_in
        for field in obj_data:
            if field in obj_data:
                setattr(db_obj, field, obj_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        """删除记录"""
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj

# 3. 数据库配置（使用 SQLite 内存数据库，无需额外安装）
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # SQLite 特有参数
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 4. 定义 SQLAlchemy 模型（User 表）
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)

# 5. 定义 Pydantic 校验模型（数据校验/序列化）
class UserCreate(BaseModel):
    """创建用户时的入参校验模型"""
    name: str
    email: str
    age: Optional[int] = None

    class Config:
        from_attributes = True  # 支持从 ORM 模型实例初始化

class UserUpdate(BaseModel):
    """更新用户时的入参校验模型"""
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

    class Config:
        from_attributes = True

# 6. 实现 User 专属的 CRUD 类（可扩展自定义方法）
class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    # 可以添加自定义方法，比如根据邮箱查询用户
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

# 实例化 User CRUD 操作对象
user_crud = CRUDUser(User)

# 7. 实际使用演示
def demo():
    # 创建数据库表，继承 Base 后，Base.metadata.create_all(bind=engine) 会自动在数据库中创建 users 表（如果不存在）。
    Base.metadata.create_all(bind=engine)
    # 获取数据库会话，打开对engin所绑定表的操作对象
    db = SessionLocal()

    try:
        # 1. 创建用户，会自动校验这些数据的类型
        user_create = UserCreate(name="张三", email="zhangsan@example.com", age=25)
        new_user = user_crud.create(db, obj_in=user_create)
        print(f"创建用户成功：ID={new_user.id}, 姓名={new_user.name}, 邮箱={new_user.email}")

        # 2. 根据 ID 查询用户
        user = user_crud.get(db, id=new_user.id)
        print(f"查询用户成功：{user.name}")

        # 3. 根据邮箱查询用户
        user_by_email = user_crud.get_by_email(db, email="zhangsan@example.com")
        print(f"按邮箱查询用户：{user_by_email.name}")

        # 4. 更新用户信息
        user_update = UserUpdate(age=26, name="张三_更新")
        updated_user = user_crud.update(db, db_obj=user, obj_in=user_update)
        print(f"更新用户成功：姓名={updated_user.name}, 年龄={updated_user.age}")

        # 5. 批量查询用户
        users = user_crud.get_multi(db, skip=0, limit=10)
        print(f"批量查询用户数量：{len(users)}")

        # 6. 删除用户
        deleted_user = user_crud.remove(db, id=new_user.id)
        print(f"删除用户成功：{deleted_user.name}")

    finally:
        # 关闭会话
        db.close()

if __name__ == "__main__":
    demo()