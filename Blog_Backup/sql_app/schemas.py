from typing import List, TypeVar

from pydantic import BaseModel
from datetime import datetime

'''
class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
        
'''
# 泛型
T = TypeVar('T')
# 动态查找的 选项 和 参数
class DataItem(BaseModel):
    motivate_item:str
    motivate_item_name:T

# 访客历史记录 分页 查询筛选列表
class IpItem(BaseModel):
    PageNo: int
    PageSize: int
    datas: List[DataItem]

class FilterItem(BaseModel):
    datas: List[DataItem]

class Ob(BaseModel):
    time1: datetime
    time2: datetime

class Login(BaseModel):
    name: str
    password: str

class R(BaseModel):
    code: str
    msg: str
    data: T

    # 静态方法
    @staticmethod
    def success(data: T):
        return R(code="1", msg="", data=data)

    @staticmethod
    def error(msg: str):
        return R(code="0", msg=msg, data=None)

