import redis

redis_client = redis.Redis(
    host="redis-14453.c89.us-east-1-3.ec2.redns.redis-cloud.com",
    port="14453",
    password="6uJsqtGjitiT8p4E83kTrDKQKFHZQnkm",
)

connection_status = redis_client.ping()
if connection_status:
    print("Connected to Redis!")
else:
    print("The connection to Redis was unsuccessful!")

# def store_data(key, value, time_to_live=None):
#     try:
#         if time_to_live is None:
#             redis_client.set(key, value)
#             print(f"key '{key}' created with value '{value}'.")
#         else:
#             redis_client.setex(key, time_to_live, value)
#             print(f"Key '{key}' created with value '{value}' and a ttl of {time_to_live}.")
#     except redis.RedisError as error:
#         print(f"An error ocurred while storing data in Redis: {error}")

# # Ejemplo de uso
# store_data("full_name", "Maria Celeste")
# store_data("important_key", "important value!", time_to_live=100)

value = redis_client.get("full_name")
print(value.decode("utf-8"))