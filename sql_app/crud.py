from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
import time
from typing import List
from sqlalchemy import func, desc, and_, or_


# 返回评论数据
def get_comments(db: Session, skip: int, limit: int):
    """
    获取指定数量的item
    :param db: 数据库会话
    :param skip: 开始位置
    :param limit: 限制数量
    :return: item列表
    """
    # start_time = time.time()  # 记录开始时间
    top = []
    # 只有在第一页才显示置顶评论
    if skip == 0:
        top = db.query(models.Comments).filter(models.Comments.is_top is True).all()
    # 获取评论
    results = db.query(models.Comments).order_by(models.Comments.datetime.desc()).offset(skip).limit(limit).all()
    # 如果有置顶 头插
    if top:
        results = top + results
    # end_time = time.time()  # 记录结束时间
    # elapsed_time = end_time - start_time  # 计算执行时间

    # print(f"Query executed in {elapsed_time} seconds.")
    return results


# 返回子评论数据
def get_subcomments(db: Session, skip: int, limit: int, father_comment_id: int):
    """
    获取指定数量的item
    :param db: 数据库会话
    :param skip: 开始位置
    :param limit: 限制数量
    :param father_comment_id: 父评论的ID
    :return: item列表
    """
    return db.query(models.SubComments).filter(models.SubComments.comment_id == father_comment_id).order_by(models.SubComments.datetime.asc()).offset(skip).limit(limit).all()


# 返回评论总数
def get_comments_count(db: Session):
    return db.query(models.Comments).count()


# 返回子评论总数
def get_subcomments_count(db: Session, father_comment_id: int):
    return db.query(models.SubComments).filter(models.SubComments.comment_id == father_comment_id).count()


# 返回ip历史数据
def get_iphistory(db: Session, skip: int, limit: int ):
    """
    获取指定数量的item
    :param db: 数据库会话
    :param skip: 开始位置
    :param limit: 限制数量
    :return: item列表
    """
    return db.query(models.IpHistory).order_by(models.IpHistory.datetime.desc()).offset(skip).limit(limit).all()


# 返回table数据 可加筛选
def get_table_info(db: Session, skip: int, limit: int, datas: List[schemas.DataItem], class_name: str):
    """
    获取指定数量的item
    :param db: 数据库会话
    :param skip: 开始位置
    :param limit: 限制数量
    :param datas: filter筛选条件列表
    :param class_name: models里的class名
    :return: item列表
    """

    # table_name为空判断
    if hasattr(models, class_name):
        table = getattr(models, class_name)
    else:
        raise HTTPException(status_code=400, detail="选项不存在或者输入有误")


    # filter为空判断
    if not datas:
        response = {
            'list': db.query(table).order_by(table.datetime.desc()).offset(skip).limit(
                limit).all(),
            'total': db.query(table).count()
        }
        return response

    # 存放筛选条件列表
    lists = {}
    # 遍历筛选条件
    for data in datas:
        # 判断 动态选项 是否都有写 且动态选项存在
        if data.motivate_item and hasattr(table, data.motivate_item):
            # 是否已存在表
            if data.motivate_item not in lists:
                #不存在就创建
                lists[data.motivate_item] = []

            # 筛选条件列表 加表达式
            lists[data.motivate_item].append(getattr(table, data.motivate_item) == data.motivate_item_name)
        else:
            raise HTTPException(status_code=400, detail="选项不存在或者输入有误")

    # 每个item or展开 存放到lst
    # 注意！遍历字典只会遍历到key 遍历不到值
    or_conditions_lst = [or_(*lists[lst]) for lst in lists]
    # and联立所有or lst
    filters = and_(*or_conditions_lst)

    # 返回结果字典
    response = {
        'list': db.query(table).filter(filters).order_by(table.datetime.desc()).offset(skip).limit(limit).all(),
        'total': db.query(table).filter(filters).count()
    }

    return response


# 返回 column 的 group分类 和个数[{"筛选项目": 项目名, "count": 有多少个}...]
def get_models_column_types(db: Session, column):
    # column可以为models.IpHistory2.ip_location
    """
    获取IpHistory2.ip_location的所有类型及其数量
    :param db: 数据库会话
    :return: 类型及其数量
    """

    # 创建一个子查询，返回每个column值及其对应的计数
    subquery = db.query(column, func.count(column).label('count')).group_by(column).subquery()

    # 在主查询中使用子查询，并按照计数的降序进行排序
    result = db.query(subquery).order_by(desc(subquery.c.count)).all()
    # result = db.query(column, func.count(column)).group_by(column).all()
    return [{"type": types, "count": count} for types, count in result]


# 改版 想试试过滤筛选filter_text为筛选文本
def get_models_column_types2(db: Session, column, filter_text: str, skip: int, limit: int):
    # column可以为models.IpHistory2.ip_location
    # 创建一个子查询，返回每个column值及其对应的计数
    #column = models.IpHistory2.ip_location
    subquery = db.query(column.label('type'), func.count(column).label('count')).group_by(column).subquery()

    # 在主查询中使用子查询，并按照计数的降序进行排序 筛选字段
    result = db.query(subquery).filter(subquery.c.type.like(f"%{filter_text}%")).order_by(desc(subquery.c.count)) \
        .offset(skip).limit(limit).all()
    # result = db.query(column, func.count(column)).group_by(column).all()
    return [{"type": types, "count": count} for types, count in result]


# 测试
def crud_test(db: Session):
    result = db.query(models.IpHistory2.id, func.count(models.IpHistory2.id)).group_by(models.IpHistory2.id).offset(0).limit(3).all()
    result_json = [{"type": types, "count": count} for types, count in result]
    # 测试发现 直接返回包含元祖的列表有时会报错
    print(result_json) # 显示[('广州市. 海珠',), ('广州市. 海珠',), ('广州市. 海珠',), ('广州市. 海珠',), ('广州市. 海珠',)]
    return result_json

# 返回ip历史总数
def get_iphistory_count(db: Session):
    return db.query(models.IpHistory).count()

# 返回table总数
def get_table_count(db: Session, table_name: str):
    if hasattr(models, table_name):
        table = getattr(models, table_name)
    else:
        raise HTTPException(status_code=400, detail="选项不存在或者输入有误")

    return db.query(table).count()

# 新增评论
def create_comment(db: Session, comments: models.Comments):
    db.add(comments)
    try:
        db.commit()
        return "success"
    except Exception as e:
        return str(e)



# 新增浏览历史 废弃
def create_iphistory(db: Session, iphistory: models.IpHistory):
    db.add(iphistory)
    db.commit()

# 新增浏览历史2
def create_iphistory2(db: Session, iphistory2: models.IpHistory2):
    db.add(iphistory2)
    try:
        db.commit()
        return "success"
    except Exception as e:
        return str(e)


# 新增你想新增的ModelsClass
def create_add_model(db: Session, filled_model):
    db.add(filled_model)
    try:
        db.commit()
        return "success"
    except Exception as e:
        return str(e)
'''
def get_user(db: Session, user_id: int):
    """
    根据id获取用户信息
    :param db: 数据库会话
    :param user_id: 用户id
    :return: 用户信息
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    根据email获取用户信息
    :param db: 数据库会话
    :param email: 用户email
    :return: 用户信息
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    获取特定数量的用户
    :param db: 数据库会话
    :param skip: 开始位置
    :param limit: 限制数量
    :return: 用户信息列表
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """
    创建用户
    :param db: 数据库会话
    :param user: 用户模型
    :return: 根据email和password登录的用户信息
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)      # 添加到会话
    db.commit()          # 提交到数据库
    db.refresh(db_user)  # 刷新数据库
    return db_user

def mytest():
    print()
    return {"666"}



def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    获取指定数量的item
    :param db: 数据库会话
    :param skip: 开始位置
    :param limit: 限制数量
    :return: item列表
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    """
    创建用户item
    :param db: 数据库会话
    :param item: Item对象
    :param user_id: 用户id
    :return: Item模型对象
    """
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
'''

