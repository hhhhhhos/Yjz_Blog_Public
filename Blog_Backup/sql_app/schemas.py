from typing import List

from pydantic import BaseModel

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

# 动态查找的 选项 和 参数
class DataItem(BaseModel):
    motivate_item:str
    motivate_item_name:str

# 访客历史记录 分页 查询筛选列表
class IpItem(BaseModel):
    PageNo: int
    PageSize: int
    datas: List[DataItem]