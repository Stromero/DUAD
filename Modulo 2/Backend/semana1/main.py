from flask import Flask, request, jsonify

app = Flask(__name__)

##################################################
####       Esto es del primer ejercicio       ####
##################################################

# @app.route("/")
# def root():
#     return "<h1>Hello, World!</h1>"

# @app.route("/goodbye")
# def goodbye():
#     return "<h1>Bye, World!</h1>"

# @app.route("/information", methods=["GET", "POST"])
# def information():
#     return {
#         "year": 2025,
#         "Description": "Esto es un endpoint secundario",
#     }

# @app.route("/user/<username>")
# def profile(username):
#     return f"{username}\'s profile"

##################################################
####       Esto es del primer ejercicio      #####
##################################################

##################################################
####       Esto es del segundo ejercicio     #####
##################################################

# shows_list = [
#     {
#         "title": "3 Body Problem",
#         "genre": "Sci-Fi",
#     },
#     {
#         "title": "Severance",
#         "genre": "Thriller",
#     },
#     {
#         "title": "Black Knight",
#         "genre": "Sci-Fi",
#     },
# ]

# @app.route("/shows")
# def shows():
#     filtered_shows = shows_list
#     genre_filter = request.args.get("genre")
#     if genre_filter:
#         filtered_shows = list(
#             filter(lambda show: show["genre"] == genre_filter, filtered_shows)
#         )

#     return {"data": filtered_shows}


# @app.route("/echo", methods=["POST"])
# def echo():
#     request_body = request.json
#     return {"request_body": request_body}

##################################################
####       Esto es del segundo ejercicio     #####
##################################################

# users_list = [
# 	{
# 		"email": "action.bronson@gmail.com",
# 		"password": "123@a!",
# 	},
# ]


# @app.route("/register", methods=["POST"])
# def register_user():
#     try:
#         if "email" not in request.json:
#             raise ValueError("email missing from the body")

#         if "password" not in request.json:
#             raise ValueError("password missing from the body")

#         users_list.append(
#             {
#                 "email": request.json["email"],
#                 "password": request.json["password"],
#             }
#         )
#         return users_list
#     except ValueError as ex:
#         return jsonify(message=str(ex)), 400
#     except Exception as ex:
# 		    # enviar un mensaje por slack
#         return jsonify(message=str(ex)), 500

# if __name__ == "__main__":
#     app.run(host="localhost", debug=True)