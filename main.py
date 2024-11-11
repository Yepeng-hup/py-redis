from flask import Flask, render_template, jsonify
import json

from core.db.mysql_db import cursor, conn
from core.db.redis_db import Redis_str, Redis_list
from core.tools.tools import users_data

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SCHEDULER_TIMEZONE'] = 'Asia/Shanghai'

r_str = Redis_str(k="test", v="5t5t")
r_list = Redis_list()


def db_test():
        cursor.execute("INSERT INTO user (user_name,user_age,user_addr) VALUES "
                           "(%(name)s,%(age)s,%(addr)s)", {"name": "tom", "age": 19, "addr": "上海市浦东新区"})
        conn.commit()



@app.route("/")
def index():
      #db_test()
      # r_str.r_set()
      # rel = r_str.r_get()
      # print(f"redis: {rel}")
      for user in users_data:
            json_data=json.dumps(user)
            r_list.r_lpush(f"users", json_data)
      return render_template('index.html')


@app.route("/redis/brpop")
def brpop():
      r_list.r_rpop("users")
      return jsonify({
            "status": 200
      })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=12200, debug="debug")