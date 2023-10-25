from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

"""
# 定义User类
class User(Base):
    __tablename__ = "users" # 定义表名
    # 定义属性
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner") # 关联Item表

# 定义Item类 
class Item(Base):
    __tablename__ = "items"  # 定义表名
    # 定义属性
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items") # 关联User表
"""

class Comments(Base):
    __tablename__ = "comments"  # 定义表名 存放评论
    # 定义属性
    id = Column(Integer, primary_key=True)
    ip = Column(String(30))  # ip地址
    ip_location = Column(String(30))  # ip地址的城市
    info = Column(String(555))  # 评论
    name = Column(String(30))  # 匿名
    datetime = Column(DateTime, index=True)  # 时间
    # has_sub = Column(Boolean, default=False) # 是否有子评论 废弃 直接评论数量为0判断
    saw_num = Column(Integer)  # 观看数量
    love_num = Column(Integer)  # 喜爱数量
    sub_num = Column(Integer)   # 评论数量
    is_top = Column(Boolean, default=False)  # 是否置顶

class SubComments(Base):
    __tablename__ = 'sub_comments'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comments.id'))
    ip = Column(String(30))  # ip地址
    ip_location = Column(String(30))  # ip地址的城市
    info = Column(String(555))  # 评论
    name = Column(String(30))  # 匿名
    datetime = Column(DateTime, index=True)  # 时间


class IpHistory(Base):
    __tablename__ = "ip_history"  # 定义表名 存放评论
    # 定义属性
    id = Column(Integer, primary_key=True)
    ip = Column(String(30))
    ip_location = Column(String(30))
    unicode = Column(String(40))  # 访客标识
    url = Column(String(300))
    datetime = Column(DateTime, index=True)

class IpHistory2(Base):
    __tablename__ = "ip_history2"  # 定义表名 存放评论
    # 定义属性
    id = Column(Integer, primary_key=True)
    request_method = Column(String(10))
    request_url = Column(String(350))
    ip = Column(String(30))
    ip_location = Column(String(30))
    unicode = Column(String(50))
    browser_name = Column(String(20))
    browser_version = Column(String(10))
    os_name = Column(String(15))
    os_version = Column(String(20))
    device_name = Column(String(20))
    device_brand = Column(String(20))
    is_bot = Column(Boolean) # 是否有子评论
    datetime = Column(DateTime, index=True)

class User(Base):
    __tablename__ = "user"  # 定义表名 存放评论
    # 定义属性
    id = Column(Integer, primary_key=True)
    name = Column(String(30))  # 名字
    email = Column(String(30)) # 注册的邮箱
    blog_url = Column(String(30)) # 用户的博客
    icon_url = Column(String(30)) # 头像地址
    last_visited = Column(DateTime) # 最后访问日期
    role = Column(String(30))  # 角色权限 visitor admin vip1 vip2
