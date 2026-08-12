from pydantic import BaseModel, field_validator


class IoConfig(BaseModel):
    io_trigger_times: int | None

    @field_validator("io_trigger_times", mode="before")
    @classmethod
    def before_validator(cls, v):
        print(f"【1️⃣ before校验器执行】此时还没有实例self！")
        print(f"    收到原始输入值 v={v}, type={type(v)}\n")
        if v is None:
            return None
        if isinstance(v, float):
            raise ValueError(f"禁止浮点数 {v}")
        return v

    def __init__(self, **data):
        print(f"【3️⃣ 进入模型__init__，开始创建实例self】\n")
        super().__init__(**data)


if __name__ == "__main__":
    print("=====开始实例化 IoConfig(io_trigger_times='123')=====\n")
    obj = IoConfig(io_trigger_times="123")
    print(f"✅最终实例对象: {obj}")
    print(f"✅实例属性值: obj.io_trigger_times = {obj.io_trigger_times}, type={type(obj.io_trigger_times)}")