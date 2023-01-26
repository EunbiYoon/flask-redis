from flask import Flask
from flask_redis import FlaskRedis

# make flask app
app = Flask(__name__)
redis_cache=FlaskRedis(app, host='localhost', port=6379, db=0)

# make flask app
app = Flask(__name__)

# business logic 
@app.route('/set/<string:key>/<string:value>')
def set(key,value):
    # if cache hit then get from redis
    if redis_cache.exists(key):
        pass
    else:
        redis_cache.set(key,value)
    return "OK"


# business logic 
@app.route('/get/<string:key>')
def get(key):
    # if cache hit then get from redis
    if redis_cache.exists(key):
        return redis_cache.get(key)
    else:
        return f"{key} not exists"

app.run("127.0.0.1", port="9111", debug=True)