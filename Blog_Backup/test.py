import asyncio
import time

async def process_with_asyncio_sleep(n,m,name):
    start_time = time.time()
    for i in range(n):
        print(f"{name} asyncio sleep {i}...")
        await asyncio.sleep(1)
        print(f"{name} {i} done{time.time()-start_time}...")

    for i in range(m):
        print(f"{name} time sleep {i}...")
        time.sleep(1)
    end_time = time.time()
    print(f'I am{name}')
    print(f"{name} Total time: {end_time - start_time} seconds")

async def hello():
    start_time = time.time()
    await asyncio.gather(
        process_with_asyncio_sleep(2,3,'A'),
        process_with_asyncio_sleep(1,3,'B'),

    )
    end_time = time.time()
    print(f'finally:{end_time - start_time}')

#process_with_sleep(3)
# 获取事件循环
#loop = asyncio.get_event_loop()
# 使用事件循环来运行协程
#loop.run_until_complete(hello())
# 关闭事件循环
#loop.close()

import subprocess
import re


new_return = '''request_token=PUrniTBiy6HXeBnRcilnjACL3Szk8qmBfaJPetar2h2ZMeg8; order=id%20desc; memSize=16236; bt_user_info=%7B%22status%22%3Atrue%2C%22msg%22%3A%22%u83
B7%u53D6%u6210%u529F%21%22%2C%22data%22%3A%7B%22username%22%3A%22133****2256%22%7D%7D; site_model=php; sites_path=F%3A/wwwroot; serverType=nginx; firewal
l_type=ssh; rank=list; Path=D%3A; disk-unitType=KB/s; db_page_model=mysql; backup_path=F%3A/backup; bt_config=%7B%22webserver%22%3A%22nginx%22%2C%22sites
_path%22%3A%22F%3A/wwwroot%22%2C%22backup_path%22%3A%22F%3A/backup%22%2C%22status%22%3Atrue%2C%22mysql_root%22%3A%22admin%22%2C%22email%22%3A%22admin@qq.
com%22%2C%22distribution%22%3A%22Windows%2010%20Pro%20%28build%2019045%29%20x64%20%28Py3.8.6%29%22%2C%22request_iptype%22%3A%22ipv4%22%2C%22request_type%
22%3A%22python%22%2C%22php%22%3A%5B%5D%2C%22mysql%22%3A%7B%22setup%22%3Afalse%2C%22status%22%3Afalse%2C%22version%22%3A%22%22%7D%2C%22sqlserver%22%3A%7B%
22setup%22%3Atrue%2C%22status%22%3Atrue%2C%22version%22%3Afalse%7D%2C%22ftp%22%3A%7B%22setup%22%3Afalse%2C%22status%22%3Afalse%2C%22version%22%3A%22%22%7
D%2C%22panel%22%3A%7B%22502%22%3A%22%22%2C%22port%22%3A%228888%22%2C%22address%22%3A%22113.119.182.25%22%2C%22domain%22%3A%22%22%2C%22auto%22%3A%22%22%2C
%22limitip%22%3A%22%22%2C%22templates%22%3A%5B%5D%2C%22template%22%3A%22default%22%2C%22admin_path%22%3A%22/d9AwWckZ%22%7D%2C%22systemdate%22%3A%222023-1
2-10%2018%3A20%3A44%22%2C%22show_workorder%22%3Atrue%2C%22isSetup%22%3Atrue%2C%22lan%22%3A%7B%22H1%22%3A%22%u9996%u9875%22%2C%22H2%22%3A%22%u7F51%u7AD9%u
7BA1%u7406%22%2C%22SEARCH%22%3A%22%u7F51%u7AD9%u641C%u7D22%22%2C%22PS%22%3A%22%u4F7F%u7528%u5B9D%u5854Windows%u9762%u677F%u521B%u5EFA%u7AD9%u70B9%u65F6%u
4F1A%u81EA%u52A8%u521B%u5EFA%u6743%u9650%u914D%u7F6E%uFF0C%u7EDF%u4E00%u4F7F%u7528www%u7528%u6237%u3002%22%2C%22BTN1%22%3A%22%u6DFB%u52A0%u7AD9%u70B9%22%
2C%22BTN2%22%3A%22%u4FEE%u6539%u9ED8%u8BA4%u9875%22%2C%22BTN3%22%3A%22%u9ED8%u8BA4%u7AD9%u70B9%22%2C%22BTN4%22%3A%22%u5220%u9664%u9009%u4E2D%22%2C%22BTN5
%22%3A%22%u5206%u7C7B%u7BA1%u7406%22%2C%22TH1%22%3A%22%u57DF%u540D%22%2C%22TH2%22%3A%22%u7F51%u7AD9%u72B6%u6001%22%2C%22TH3%22%3A%22%u5907%u4EFD%22%2C%22
TH4%22%3A%22%u7F51%u7AD9%u76EE%u5F55%22%2C%22TH5%22%3A%22%u5230%u671F%u65E5%u671F%22%2C%22TH6%22%3A%22%u5907%u6CE8%22%2C%22TH7%22%3A%22%u64CD%u4F5C%22%2C
%22JS1%22%3A%22%u8BF7%u5148%u5B89%u88C5Web%u670D%u52A1%u5668%21%22%2C%22JS2%22%3A%22%u53BB%u5B89%u88C5%22%7D%7D; user_uuid=fa74214b-3875-47ae-a511-e5fa1c
b01057; BaiduMap_Datas=[object%20Object]%2C[object%20Object]%2C[object%20Object]%2C[object%20Object]%2C[object%20Object]%2C[object%20Object]%2C[object%20
Object]%2C[object%20Object]%2C[object%20Object]%2C[object%20Object]%2C[object%20Object]%2C[object%20Object]%2C[object%20Object]; SECKEY_ABVK=YxFwlFXZ6kaT
YgLxJ3Co0piEFmjFbj/A6iZjogb7wGg%3D; BMAP_SECKEY=YWamA4B-ZQPhEAsQhUK6YuKhcbtLMPr2ixW1YJutzITO26UJpcaZ8M9mV7WKwfX0xFHWrLVQa689ETtEvnkcRTRsOgiapI39zsmbuJ_DV
ePV-_X11mXaGgA2WNK6v8e9Cnxq-791ezcEY-kGkOF7KYVlMRRGWeQ4Own7pf-EHw66SHjMNT9hGKA8oJTiFUoz
'''
new_return = re.findall(r'\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+', new_return, re.DOTALL)
print(new_return)