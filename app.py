from flask import Flask

import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis-server')

redis_client.set("visitors", 0)


@app.route('/')
def hello_world():
    visitors = redis_client.get("visitors")
    redis_client.set("visitors", int(visitors)+1)
    return "Sanketh:" + str(visitors)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
