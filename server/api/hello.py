from flask_restful import Resource

class Hello(Resource):
  def get(self):
    return {"data": "Hello World!"}