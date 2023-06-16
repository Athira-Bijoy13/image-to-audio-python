from flask import Flask, request
from imageconvert import finalFunct
app = Flask(__name__)

@app.route('/',methods=['GET'])
def helloworld():
   return "hello"

@app.route('/convert-text',methods=['GET'])
def hello_world():
   print(request.args.get("name"))
   a=finalFunct(request.args.get("name"))
   b={"data":a}
   return b

if __name__ == '__main__':
   app.run()

   