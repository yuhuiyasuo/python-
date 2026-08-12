from dataclasses import dataclass, field
from fastapi import APIRouter

def _field_tag_router(tags: list[str]):
    # 关键：t=tags 默认参数，立即捕获当前传入的tags，修复闭包延迟绑定
    return field(default_factory=lambda : APIRouter(tags=tags))


@dataclass
class _Routers:
    base: APIRouter = _field_tag_router(["variable - 基础操作"])
    mapper: APIRouter = _field_tag_router(["variable - 映射器操作"])
    special_mapper: APIRouter = _field_tag_router(["variable - 特殊映射器操作"])
    link: APIRouter = _field_tag_router(["variable - 链接操作"])
    batch: APIRouter = _field_tag_router(["variable - 批量操作"])
    ws: APIRouter = _field_tag_router(["variable - WebSocket操作"])
    serial_port: APIRouter = _field_tag_router(["variable - serial_port操作"])
    scanner: APIRouter = _field_tag_router(["variable - 扫描器操作"])
    sse: APIRouter = _field_tag_router(["variable - SSE操作"])
    docs: APIRouter = _field_tag_router(["variable - 文档操作"])


routers = _Routers()
print(routers.base.tags)       # ['variable - 基础操作']
print(routers.mapper.tags)     # ['variable - 映射器操作']
print(routers.docs.tags)       # ['variable - 文档操作']