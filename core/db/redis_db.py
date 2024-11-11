import redis
import traceback
import json

r = redis.Redis(host="xxxxx", port="6379", db=0, password="xxxx")


# string数据类型
class Redis_str(object):

    # def __init__(self, **kwargs):
    #     self.k = kwargs["k"]
    #     self.v = kwargs["v"]
    #     self.k_tiem = kwargs["k_time"]
    def __init__(self, k=None, v=None, k_time=None):
        self.k = k
        self.v = v
        self.k_tiem = k_time

    def r_set(self):
        try:
            r.set(self.k, self.v)
            return 
        except:
            print(traceback.format_exc())
            return json.dumps({
                "status": 500,
                "msg": f"set data type 'STR' Key [{self.k}] redis fail."
            })

    def r_get(self):
        try:
            rel = r.get(self.k)
            return rel.decode('utf-8')
        except:
            print(traceback.format_exc())
            return json.dumps({
                "status": 500,
                "msg": f"get data type 'STR' Key [{self.k}] redis fail."
            })

    def r_append(self):
        try:
            r.append(self.k, self.v)
            return json.dumps({
                "status": 200,
                "msg": f"add data type 'STR' Key [{self.k}] redis ok."
            })
        except:
            print(traceback.format_exc())
            return json.dumps({
                "status": 500,
                "msg": f"add data type 'STR' Key [{self.k}] redis fail."
            })

    def r_del(self):
        try:
            r.delete(self.k)
            return json.dumps({
                "status": 200,
                "msg": f"del data type 'STR' Key [{self.k}] redis fail."
            })
        except:
            print(traceback.format_exc())
            return json.dumps({
                "status": 500,
                "msg": f"del data type 'STR' Key [{self.k}] redis fail."
            })


# list数据类型
class Redis_list(object):

    def __init__(self, k=None, v=None, k_time=None):
        self.k = k
        self.v = v
        self.k_tiem = k_time

    # 增
    def r_lpush(self, k, v):
        try:
            r.lpush(k, v)
            return json.dumps({
                "status": 200,
                "msg": "lpush data type 'LIST' K and V redis ok."
            })
        except:
            print(traceback.format_exc())
            return json.dumps({
                "status": 500,
                "msg": "lpush data type 'LIST' K and V redis fail."
            })

    # 查
    def r_lindex(self, k, i):
        try:
            rel = r.lindex(k, i)
            return rel.decode('utf-8')
        except:
            print(traceback.format_exc())
            return json.dumps({
                "status": 500,
                "msg": "lindex data type 'LIST' K and V redis fail."
            })
    
    # 阻塞消费
    def r_brpop(self, k):
        rel = r.brpop(k)
        print(rel)
    
    
    # 不阻塞消费
    def r_rpop(self, k):
        rel = r.rpop(k)
        print(rel)

    # 删
    def r_lpop(self, k):
        try:
            r.lpop(k)
            return json.dumps({
                "status": 200,
                "msg": "lpop data type 'LIST' K and V redis ok."
            })
        except:
            print(traceback.format_exc())
            return json.dumps({
                "status": 500,
                "msg": "lpop data type 'LIST' K and V redis fail."
            })


# hash数据类型
class Redis_hash(object):
    
    def __init__(self, k=None, v=None, k_time=None):
        self.k = k
        self.v = v
        self.k_tiem = k_time

    # 增
    def r_hset(self, k, v):
        r.hset(k, mapping=v)
        print(f"{k}->{v}")

