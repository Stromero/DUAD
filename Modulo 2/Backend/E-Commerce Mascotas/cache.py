# cache.py
import redis
import json
from functools import wraps
from flask import jsonify

redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def get_cache(key):
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None

def set_cache(key, value, expire=60):
    redis_client.setex(key, expire, json.dumps(value))

def delete_cache(key):
    redis_client.delete(key)

# Decorador para cachear respuestas
def cache_response(key, expire=60):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cached_data = get_cache(key)
            if cached_data:
                return jsonify({"source":"cache", "data":cached_data}), 200
            
            result = func(*args, **kwargs)

            #Cacheamos solo si el resultado es exitoso
            if isinstance(result, tuple) and len(result) == 2 and result[1] == 200:
                set_cache(key, result[0].get_json()["data"], expire)
            
            return result
        return wrapper
    return decorator

def invalidate_cache(keys: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # Si la operación fue exitosa, invaliamos las claves

            if isinstance(result, tuple) and len(result) == 2 and result[1] in [200, 204]:
                for key in keys:

                    resolved_key = key.format(**kwargs)
                    delete_cache(resolved_key)

            return result
        return wrapper
    return decorator
