# region 原本fastapi引用
import time

from fastapi import Depends, FastAPI, HTTPException, Query, Form
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
# 自己加的
from pydantic import BaseModel
# 自己导入的库
from fastapi.responses import FileResponse
import requests
from fastapi.responses import RedirectResponse
from fastapi.responses import StreamingResponse

from datetime import datetime
# 发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import random
from fastapi import Request
from user_agents import parse
import requests
from uuid import uuid4
# endregion

# region 爬虫作业引用
import json
import re
import subprocess
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
from sql_func import demo
from .models import CustomException
import redis
# endregion

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# 依赖
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# 接收curd添加数据库的result 判断返回"success"还是其他异常信息 成功raise 200 succmsg 失败raise 400 错误信息 无返回值
def result_handle(result, succmsg: str):
    if result == "success":
        raise HTTPException(status_code=200, detail=succmsg)
    else:
        raise HTTPException(status_code=400, detail="发生错误:"+result)


# region 下面是vue-admin-template后端

# 自己写的
class MyItem(BaseModel):
    password: str
    username: str

# 自己写的
@app.post("/admin3/api/user/login")
def test(item: MyItem):
    if item.password == "123" and item.username == "sb":
        return {"code": 20000, "data": {"token": "321"}}
    else:
        return {"code": 60, "message": "密码或用户名不对傻逼"}

# 自己写的
@app.post("/api/user/logout")
def test():
    return {"code": 20000, "message": "捏可以滚了"}

# 自己写的 返回用户信息
@app.get("/api/user/info")
def is_token(token: int = 0):
    if token == 321:
        return {
            "code": 20000, "data": {
                'roles': ['sb'],
                'introduction': 'I am a super 大傻逼',
                'avatar': 'http://localhost:8888/api/undefined',
                'name': '超级大傻逼'
            }
        }
    else:
        return {"code": 60}

# 自己写的 url请求从别处搞到 301重定向
@app.get("/undefineddddd")
def img():
    return RedirectResponse(url="https://game.gtimg.cn/images/yxzj/img201606/heroimg/505/505.jpg",
                            status_code=301)

# 自己写的 url请求从本地上传
@app.get("/api/undefined")
async def main():
    some_file_path = "sql_img/img_3.gif"
    return FileResponse(some_file_path)

# endregion


# region下面是 博客 后端

# 自己写的 获取评论 返回当前页允许的评论条数 和总数统计
@app.get("/table/info")
def table_info(PageNo: int, PageSize: int, db: Session = Depends(get_db)):
    data = {
        "comments_list": crud.get_comments(db, skip=(PageNo-1)*PageSize, limit=PageSize),
        "comments_total": crud.get_comments_count(db),
        "loading": False
    }
    return data


# 自己写的 获取ip访问历史 返回当前页允许的评论条数 和总数统计
@app.get("/iphistory/info")
def table_info(PageNo: int, PageSize: int, db: Session = Depends(get_db)):
    data = {
        "iphistory_list": crud.get_iphistory(db, skip=(PageNo-1)*PageSize, limit=PageSize),
        "iphistory_total": crud.get_iphistory_count(db),
        "loading": False
    }
    return data

# 获取{class_name}的数据 可加筛选条件 返回table数据 和 数量
@app.post("/table/{class_name}/info")
def table_info2(ipitem: schemas.IpItem, class_name: str, db: Session = Depends(get_db)):
    response = crud.get_table_info(db, skip=(ipitem.PageNo - 1) * ipitem.PageSize, limit=ipitem.PageSize,
                                   datas=ipitem.datas, class_name=class_name)

    data = {
        "list": response['list'],
        "total": response['total'],
    }

    return data


# 参数 不定表 的 不定列 返回group类型和统计个数 filter_text过滤列名
@app.get("/models/{model_name}/types/{column}")
def models_types_and_count(model_name: str, column: str, filter_text: str = "", skip: int = 0, limit: int = 10,
                           db: Session = Depends(get_db)):
    # 检查 models.model_name 和 models.model_name.column 是否存在
    if hasattr(models, model_name) and hasattr(getattr(models, model_name), column):
        model = getattr(models, model_name)
        column = getattr(model, column)
    else:
        raise HTTPException(status_code=400, detail="选项不存在或者输入有误")

    return crud.get_models_column_types2(db, column, filter_text, skip, limit)

'''
# 备份一下原来的
@app.get("/models/{model_name}/types/{column}")
def models_types_and_count(model_name: str, column: str,db: Session = Depends(get_db)):
    # 检查 models.model_name 和 models.model_name.column 是否存在
    if hasattr(models, model_name) and hasattr( getattr(models, model_name) , column):
        model = getattr(models, model_name)
        column = getattr(model, column)
    else:
        raise HTTPException(status_code=400, detail="选项不存在或者输入有误")

    return crud.get_models_column_types(db, column)
'''

class MyItem2(BaseModel):
    userid: str
    userIp: str
    finallocation: str
    url: str
    unicode: str

# 传用户浏览历史到数据库 废弃前端方案 改nginx传报头到fastapi中间件
"""
@app.post("/iphistory/info")
def set_table_info(data: MyItem2,request: Request, db: Session = Depends(get_db)):
    crud.create_iphistory(db=db, iphistory=models.IpHistory(
        ip=data.userIp,
        ip_location=data.finallocation,
        unicode=data.unicode,
        url=data.url,
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    print("已添加一条历史记录 不知道成功没")
    print(request.headers.items())
"""

# 前端评论数据
class MyItem3(BaseModel):
    text: str
    textarea: str
    loading: bool

# 自己写的 测试用户数据 gets可以写def table_info(PageNo: int, PageSize: int) post好像不行 还必须指定参数类型？
# data: MyItem3必须和前端传来的完全一致？
@app.post("/send/comments")
def send_comments(data: MyItem3, request: Request, db: Session = Depends(get_db)):
    '''
    print(data.text)
    print(data.textarea)
    print(data.ip)
    print(data.location)
    '''
    # 获取ip和ip的地址
    ip_address = request.headers.get("x-real-ip")
    location = "Unknown"
    if ip_address:
        try:
            response2 = requests.get(f'https://api.vore.top/api/IPdata?ip={ip_address}').json()
            if response2.get("code") == 200:
                city = response2.get("ipdata").get("info3")
                region = response2.get("ipdata").get("info2")
                country = response2.get("ipdata").get("info1")
                if region and city:
                    if city == "基站":
                        location = country + ". " + region
                    else:
                        location = region + ". " + city
                elif city:
                    location = city
                elif region:
                    location = region
                elif country:
                    location = country
                else:
                    location = "火星人"
            else:
                location = "Unknown"
        except:
            location = "Unknown"

    if len(data.textarea) > 150 or len(data.text) > 10:
        raise HTTPException(status_code=400, detail="你真是个顽皮的小可爱")

    result = crud.create_comment(db=db, comments=models.Comments(ip=ip_address, ip_location=location,
                                                       info=data.textarea, name=data.text,
                                                       datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    if result == "success":
        raise HTTPException(status_code=200, detail="评论已被添加")
    else:
        raise HTTPException(status_code=400, detail="发生错误:"+result)

# 给modelname表新增数据
@app.post("/send")
def send_comments(data: MyItem3, modelname: str, comment_id: int, request: Request, db: Session = Depends(get_db)):
    # 判断字数合法性 防黑客
    if len(data.textarea) > 150 or len(data.text) > 10:
        raise HTTPException(status_code=400, detail="你真是个顽皮的小可爱")

    # 判断有无modelname表(models.py文件下有无名为{modelname}的class)
    if hasattr(models, modelname):
        # model变成了models.py下的某个class类 可以model()实例化对象
        model = getattr(models, modelname)
        ip_address = request.headers.get("x-real-ip")
        location = "Unknown"
        if ip_address:
            try:
                response2 = requests.get(f'https://api.vore.top/api/IPdata?ip={ip_address}').json()
                if response2.get("code") == 200:
                    city = response2.get("ipdata").get("info3")
                    region = response2.get("ipdata").get("info2")
                    country = response2.get("ipdata").get("info1")
                    if region and city:
                        if city == "基站":
                            location = country + ". " + region
                        else:
                            location = region + ". " + city
                    elif city:
                        location = city
                    elif region:
                        location = region
                    elif country:
                        location = country
                    else:
                        location = "火星人"
                else:
                    location = "Unknown"
            except:
                location = "Unknown"


        fill = {
            "comment_id" :comment_id,
            "ip" : ip_address,
            "ip_location" : location,
            "info":data.textarea,
            "name":data.text,
            "datetime":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        # filled_model或者model 实际上就是class Comments的对象实例化
        # model(**fill)构造函数
        # **fill解包等同于model(comment_id=comment_id,ip=ip_address...)
        result = crud.create_add_model(db=db, filled_model=model(**fill))
        if result == "success":
            raise HTTPException(status_code=200, detail="评论已被添加")
        else:
            raise HTTPException(status_code=400, detail="发生错误:" + result)

    else:
        raise HTTPException(status_code=400, detail="选项不存在或者输入有误")


# 发送验证邮件给客户
@app.post("/send/email")
def send_comments():
    sender = 'blogsendhelper@163.com'  # 发送邮箱地址
    passwd = 'CVRCFMXKXWCQWOVL'  # 邮箱授权码，非登陆密码
    receivers = '952666016@qq.com'  # 收件邮箱
    subject = '注册验证码'  # 主题

    # 生成6位随机数
    str_list = [str(random.randint(0, 9)) for _ in range(6)]
    ecode = ''.join(str_list)  # 验证码

    # 创建一个 MIMEMultipart 对象，并设置为 'related' 类型
    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receivers

    # 创建一个 MIMEText 对象，用于存放 HTML 内容
    content = f"""
    <tbody>
        <tr>
            <td>
                <div style="background:#fff">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <thead>
                        <tr>
                            <td valign="middle" style="padding-left:30px;background-color:#415A94;color:#fff;padding:20px 40px;font-size: 21px;">YJZ's&ensp;BLOG</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr style="padding:40px 40px 0 40px;display:table-cell">
                            <td style="font-size:24px;line-height:1.5;color:#000;margin-top:40px">邮箱验证码</td>
                        </tr>
                        <tr>
                            <td style="font-size:14px;color:#333;padding:24px 40px 0 40px">
                                {receivers}&ensp;您好！
                                <br  />
                                <br  />
                                您的验证码是： &ensp;<div style="display: inline-block;border:5px solid beige;background-color: beige;">{ecode}</div>&ensp; ，请在 30 分钟内进行验证。如果该验证码不为您本人申请，请无视。
                            </td>
                        </tr>
                        <tr style="padding:40px;display:table-cell">
                        </tr>
                        </tbody>
                    </table>
                </div>
                <div>
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                        <tr>
                            <td style="padding:20px 40px;font-size:12px;color:#999;line-height:20px;background:#f7f7f7"><a href="https://yjzblog.top/" style="font-size:14px;color:#929292">返回BLOG</a></td>
                        </tr>
                        </tbody>
                    </table>
                </div></td>
        </tr>
        </tbody>
    """
    html_part = MIMEText(content, 'html', 'utf-8')
    msg.attach(html_part)

    """ 暂时不用传图片
    # 打开图片文件，并创建一个 MIMEImage 对象
    with open('sql_img/img_1.jpg', 'rb') as f:
        img_data = f.read()
    img_part = MIMEImage(img_data)
    img_part.add_header('Content-ID', '<image>')  # 注意，这里的 'image' 应该和 HTML 内容中的 "cid:image" 相对应
    msg.attach(img_part)
    """

    try:
        s = smtplib.SMTP_SSL('smtp.163.com', 465)
        s.login(sender, passwd)
        s.sendmail(sender, receivers, msg.as_string())
        print('Send Success')
    except smtplib.SMTPConnectError as e:
        print('邮件发送失败，连接失败:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPAuthenticationError as e:
        print('邮件发送失败，认证错误:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPSenderRefused as e:
        print('邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPRecipientsRefused as e:
        print('邮件发送失败，收件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPDataError as e:
        print('邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPException as e:
        print('邮件发送失败, ', e.message)
    except Exception as e:
        print('邮件发送异常, ', str(e))

# 获取报头 测试用的
@app.get("/apitest/")
def read_items(request: Request):
    for key, value in request.headers.items():
        print(f"{key}: {value}")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 中间件 所有请求都经过这个
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    # 这里放你想做的事 #######
    db = SessionLocal()  # 创建一个新的数据库会话
    print("已启动中间件")

    # cookie处理用户user_uuid set_cookie只在直接反代时有用 post_action @log_request时set_cookie没用
    user_uuid = request.cookies.get("user_uuid")
    if user_uuid:
        print("!!!user_uuid存在")
        pass
    else:
        response.set_cookie(key="user_uuid", value=str(uuid4()))  # 设置 cookie
        print("!!!user_uuid不存在 已尝试设置！！！")
        user_uuid = "doesn't exist"

    # user_agent库处理设备信息
    user_agent_string = request.headers.get("user-agent")
    print(user_agent_string)
    user_agent = parse(user_agent_string)

    # 获取ip和ip的地址
    ip_address = request.headers.get("x-real-ip")
    print(ip_address)
    location = "Unknown"
    if ip_address:
        try:
            response2 = requests.get(f'https://api.vore.top/api/IPdata?ip={ip_address}', timeout=5).json()
            if response2.get("code") == 200:
                city = response2.get("ipdata").get("info3")
                region = response2.get("ipdata").get("info2")
                country = response2.get("ipdata").get("info1")
                if region and city:
                    location = region + ". " + city
                elif city:
                    location = city
                elif region:
                    location = region
                elif country:
                    location = country
                else:
                    location = "火星人"
            else:
                location = "Unknown"
        except Exception as e:
            print("发生了一个异常：", e)
            location = "Unknown"


    '''
    # 输出浏览器的信息
    print("请求方法：", request.method)
    print("请求地址：", request.headers.get('X-Original-URI'))
    print("ip：", ip_address)
    print("ip地点: ", location)
    print("uuid: ", user_uuid)
    print("user-agent全文：", user_agent_string)
    print("浏览器名称: ", user_agent.browser.family)
    print("浏览器版本: ", user_agent.browser.version_string)
    print("操作系统名称: ", user_agent.os.family)
    print("操作系统版本: ", user_agent.os.version)
    print("设备类型: ", user_agent.device.family)
    print("设备品牌: ", user_agent.device.brand)
    print("是否是爬虫器: ", user_agent.is_bot)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    '''
    # 传到数据库

    result = crud.create_iphistory2(db=db, iphistory2=models.IpHistory2(
        request_method=request.method,
        request_url=request.headers.get('X-Original-URI'),
        ip=ip_address,
        ip_location=location,
        unicode=user_uuid,
        browser_name=user_agent.browser.family,
        browser_version=user_agent.browser.version_string,
        os_name=user_agent.os.family,
        os_version='.'.join(map(str, user_agent.os.version)),
        device_name=user_agent.device.family,
        device_brand=user_agent.device.brand,
        is_bot=user_agent.is_bot,
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))
    print("已添加一条历史记录 结果为:"+result)
    db.close()  # 确保数据库会话在结束时被关闭
    # END #####
    return response


# 获取子评论
@app.get("/subcomment/info")
def subc_info(PageNo: int, PageSize: int, comment_id: int, db: Session = Depends(get_db)):
    data = {
        "subcomments_list": crud.get_subcomments(db, skip=(PageNo-1)*PageSize, limit=PageSize, father_comment_id=comment_id),
        "subcomments_total": crud.get_subcomments_count(db, father_comment_id=comment_id),
        "loading": False
    }
    return data

# 测试
class MyItem4(BaseModel):
    content: str

# 测试
@app.post("/yjztest")
def yjztest(data: MyItem4):
    return "运行！！！："+data.content+"😀"


@app.get("/yjztest")
def yjztest(request: Request):

    print('receive!8')
    time.sleep(9)
    print('8end!')
    return "运行！！！8："+"😀"

@app.get("/yjztest2")
def yjztest():
    print('receive!2')
    return "运行2！！！："+"😀😀😀"

# region 套接字 爬虫大作业功能模块
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    # region 功能函数

    # 发起爬虫函数
    # callback回调函数为websocket.send_text(json.dumps(x))
    # callback参数必须为字典
    # callback要await
    async def do_sth(params: dict, callback, sendsth_callback):
        print("dosth")
        if params.get('page'):
            print("dosth2")
            if 1 <= int(params['page']) <= 3:
                print("dosth3")
                datas = await demo.local_scr(params, sendsth_callback)
                if datas:
                    await sendsth_callback("爬取成功，返回数据")
                    await callback({
                        "method": "data",
                        "params": {
                            "message": datas,
                            "city_chn": params.get('city_chn'),
                            "mode": params.get('mode')
                        }
                    })
            else:
                print("raise CustomException")
                raise CustomException("页数不正确")
        else:
            print("raise CustomException")
            raise CustomException("dosth params error")

    # 发送信息到客户端函数
    async def send_sth(msg: str):
        await websocket.send_text(json.dumps({
            "method": "console",
            "params": {
                "message": msg
            }
        }))

    # 把websocket头信息记录访客记录
    def record_sth(params_all: dict):
        db = SessionLocal()

        # user_agent库处理设备信息
        user_agent_string = websocket.headers.get("user-agent")
        print(user_agent_string)
        user_agent = parse(user_agent_string)

        # 获取ip和ip的地址websocket.headers
        ip_address = websocket.headers.get("x-real-ip")
        print(ip_address)
        location = "Unknown"
        if ip_address:
            try:
                response2 = requests.get(f'https://api.vore.top/api/IPdata?ip={ip_address}', timeout=5).json()
                if response2.get("code") == 200:
                    city = response2.get("ipdata").get("info3")
                    region = response2.get("ipdata").get("info2")
                    country = response2.get("ipdata").get("info1")
                    if region and city:
                        location = region + ". " + city
                    elif city:
                        location = city
                    elif region:
                        location = region
                    elif country:
                        location = country
                    else:
                        location = "火星人"
                else:
                    location = "Unknown"
            except Exception as e:
                print("发生了一个异常：", e)
                location = "Unknown"

        '''
        # 输出浏览器的信息
        print("请求方法：", request.method)
        print("请求地址：", request.headers.get('X-Original-URI'))
        print("ip：", ip_address)
        print("ip地点: ", location)
        print("uuid: ", user_uuid)
        print("user-agent全文：", user_agent_string)
        print("浏览器名称: ", user_agent.browser.family)
        print("浏览器版本: ", user_agent.browser.version_string)
        print("操作系统名称: ", user_agent.os.family)
        print("操作系统版本: ", user_agent.os.version)
        print("设备类型: ", user_agent.device.family)
        print("设备品牌: ", user_agent.device.brand)
        print("是否是爬虫器: ", user_agent.is_bot)
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        '''
        # 传到数据库

        result = crud.create_iphistory2(db=db, iphistory2=models.IpHistory2(
            request_method='ws/wss',
            # 这里是爬虫参数 + 爬取结果
            request_url=str(params_all.get('params')) + str(params_all.get('result')),
            ip=ip_address,
            ip_location=location,
            unicode='whatever',
            browser_name=user_agent.browser.family,
            browser_version=user_agent.browser.version_string,
            os_name=user_agent.os.family,
            os_version='.'.join(map(str, user_agent.os.version)),
            device_name=user_agent.device.family,
            device_brand=user_agent.device.brand,
            is_bot=user_agent.is_bot,
            datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ))
        print("已添加一条历史记录 结果为:" + result)
        db.close()  # 确保数据库会话在结束时被关闭
        # END #####
    print(websocket.headers.get('cookie'))

    # endregion

    # region 引入全局变量/定义局部变量
    # redis代替player
    r = redis.Redis(host='localhost', port=6379, db=0, password=123321)
    # 获取列表所有元素
    player = r.lrange('player', 0, -1)
    # global player
    client_ip = None
    client_port = None
    now = None
    # socket最终结果
    final_result = {'params': None, 'result': None}
    # endregion

    # region websocket try处理
    try:
        await websocket.accept()
        # region 获取ip,端口/返回客户端ip,端口/全局player加入ip,端口
        client_ip = websocket.client.host
        client_port = websocket.client.port
        print(f"连接者: {client_ip}:{client_port}")
        await send_sth(f"{client_ip}:{client_port}已连接")

        # region 只允许一个连接者的判断
        if player:
            print(f'进入player判断，player为：{player}')
            # 创建一个管道，运行ss命令并结合grep过滤本地端口号为8080的连接 WIN命令
            #process = subprocess.Popen(f'netstat -ano | findstr {client_ip}:{client_port}', shell=True, stdout=subprocess.PIPE)
            # linux命令
            process = subprocess.Popen(f'netstat -tunlp | grep {client_ip}:{client_port}', shell=True,
                                       stdout=subprocess.PIPE)
            # 获取命令的输出
            output, error = process.communicate()
            new_return = output.decode()
            # win匹配
            #new_return = re.findall(r'\s+\S+\s+\S+\s+\S+\s+(\S+)\s+', new_return, re.DOTALL)
            # linux匹配（多一个）
            new_return = re.findall(r'\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+', new_return, re.DOTALL)
            print(new_return)
            # 防空 空则改
            if not new_return:
                new_return = ['not found']
            await send_sth(f"已有连接者：{player[0].decode()}，状态：{new_return[0]}")
            await send_sth(f"为防止反爬/被封ip，请等待{player[0].decode()}退出后重试")
            raise CustomException("已有链接")
        # endregion


        now = datetime.now()
        now = now.replace(microsecond=0)
        # 尾插入
        r.rpush('player', f'{client_ip}:{client_port} Time:{now}')
        # 两分钟后过期 防止bug导致一直在
        r.expire('player', 120)
        # player.append(f"{client_ip}:{client_port}")
        # endregion


        # region 等待接收信息 5秒超时/json转dict
        # 这里收到的是字符串
        # 5秒收不到新信息抛异常
        data = await asyncio.wait_for(websocket.receive_text(), timeout=5)
        print("收到：", data)
        # 将类似json的字符串转换为python字典
        data = json.loads(data)
        # 记录一下客户选择参数params到final_result['params'] =
        final_result['params'] = data.get('params')
        # endregion

        # region 收到信息 做点什么... 防空判断
        if data.get('method') and data['method'] == "爬虫":
            # 兰博表达式
            if data.get('params'):
                await do_sth(data['params'], lambda x: websocket.send_text(json.dumps(x)), send_sth)
            else:
                raise CustomException("params不存在")
            #await send_sth("hello")
        else:
            raise CustomException("method不存在")

        # 字典转json格式字符串
        # data = json.dumps(data)
        # await websocket.send_text(data)
        # endregion

    # endregion

    # region 异常处理
    # 对方断开连接
    except WebSocketDisconnect:
        print(f"{client_ip}:{client_port}断开了连接")
        print("客户端断开链接，发起return")
        final_result['result'] = "客户端断开链接，发起return"
        record_sth(final_result)
        r.lrem('player', 1, f'{client_ip}:{client_port} Time:{now}')
        # 这里必须return 不然下面最后会在已关闭的socket上发送信息 gg
        return
        # player -= 1
    # 等待对方发送超时
    except asyncio.TimeoutError as e:
        print(f"Timeout!：{str(e)}")
        await send_sth("等待接收信息超时，自动断开")
        final_result['result'] = f"Timeout!：{str(e)}"
    # 自定义异常
    except CustomException as e:
        print(f"自定异常：{e.message}")
        await send_sth(f"发生异常：{str(e)}")
        if e.message == "请求网站未响应，可能是城市名错误或链家没有该城市网站":
            await send_sth(e.message)
            final_result['result'] = f"自定异常：{e.message}"
    # player超过1或其他异常
    except Exception as e:
        print(f"发生了一个异常：{str(e)}")
        await send_sth(f"发生异常：{str(e)}")
        final_result['result'] = f"发生异常：{str(e)}"
    # endregion

    # region 结束链接 结尾处理
    #player.remove(f"{client_ip}:{client_port}")
    r.lrem('player', 1, f'{client_ip}:{client_port} Time:{now}')
    print("正常结束")
    await send_sth(f"{client_ip}:{client_port}正常结束，断开")
    final_result['result'] = "正常结束"
    record_sth(final_result)
    await websocket.close()
    # endregion

# endregion

# endregion


'''
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # 读取指定数量用户
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # 获取当前id的用户信息
    db_user = crud.get_user(db, user_id=user_id)
    # 如果没有信息，提示用户不存在
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    # 创建该用户的items
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # 获取所有items
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
    
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 根据email查找用户
    db_user = crud.get_user_by_email(db, email=user.email)
    # 如果用户存在，提示该邮箱已经被注册
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # 返回创建的user对象
    return crud.create_user(db=db, user=user)
'''


