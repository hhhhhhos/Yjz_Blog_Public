import redis
r = redis.Redis(host='localhost', port=6379, db=0, password=123321)
a=1
if a == 0:
    # 字符串类型操作
    r.set('key', 'value')  # 添加数据
    print(r.get('key'))  # 获取数据

    # 列表类型操作
    r.rpush('list', 'value2', 'value2')  # 在列表末尾添加数据
    print(r.lrange('list', 0, -1))  # 获取列表中所有数据

    # 字典类型操作
    r.hset('dict', 'field2', 'value2')  # 添加数据
    print(r.hget('dict', 'field'))  # 获取数据

    # 集合类型操作
    r.sadd('set', 'value2', 'value3')  # 添加数据
    print(r.smembers('set'))  # 获取集合中所有数据

    # 有序集合类型操作
    r.zadd('zset', {'value': 1})  # 添加数据
    print(r.zrange('zset', 0, -1))  # 获取有序集合中所有数据

#r.set('key', '995888')  # 添加数据
r.expire('key', 40)
print(r.get('key'))  # 获取数据