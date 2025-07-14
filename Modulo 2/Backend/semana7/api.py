# from flask import Flask, request, jsonify, Response
# import json
# from db import DB_Manager
# from jwt import JWT_Manager

# db = DB_Manager()
# jwt_manager = JWT_Manager()

# app = Flask("user-service")

# @app.route("/liveness")
# def liveness():
#     return "<p>Hello, World!</p>"


# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json() # data is empty
#     if(data.get('username') == None or data.get('password') == None):
#         return Response(status=400)
#     else:
#         result = db.insert_user(data.get('username'), data.get('password'))
#         user_id = result[0]

#         token = jwt_manager.encode({'id': user_id})

#         return jsonify(token=token)

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json() # data is empty
#     if(data.get('username') == None or data.get('password') == None):
#         return Response (status=400)
#     else:
#         result = DB_Manager.get_user(data.get('username'), data.get('password'))

#         if(result == None):
#             return Response(status=403)
#         else:
#             user_id = result[0]
#             token = JWT_Manager.encode({'id':user_id})

#             return jsonify(token=token)

# @app.route('/me')
# def me():
#     try:
#         token = request.headers.get('Authorization')
#         if(token is not None):
#             token = token.replace('Bearer', '')
#             decoded = JWT_Manager.decode(token)
#             user_id = decoded['id']
#             user = DB_Manager.get_user_by_id(user_id)
#             return jsonify(id=user_id, username=user[1])
#         else:
#             return Response(status=403)
#     except Exception as e:
#         return Response(status=500)

# if __name__ == "__main__":
#      app.run(host="localhost",debug=True)

from db import DB_Manager
from jwebt import JWT_Manager
from flask import Flask, request, Response, jsonify


app = Flask("user-service")
db_manager = DB_Manager()
jwt_manager = JWT_Manager('habitosatomicos', 'HS256')


@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = db_manager.insert_user(data.get('username'), data.get('password'))
        user_id = result[0]

        token = jwt_manager.encode({'id':user_id})
        
        return jsonify(token=token)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = db_manager.get_user(data.get('username'), data.get('password'))

        if(result == None):
            return Response(status=403)
        else:
            user_id = result[0]
            token = jwt_manager.encode({'id':user_id})
        
            return jsonify(token=token)

@app.route('/me')
def me():
    try:
        token = request.headers.get('Authorization')
        if(token is not None):
            test = token.replace("Bearer ","")
            print(test)
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']

            user = db_manager.get_user_by_id(user_id)

            return jsonify(id=user_id, username=user[1])
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

if __name__ == "__main__":
    app.run(host="localhost",debug=True)