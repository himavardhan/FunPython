from flask import Flask, jsonify, request, render_template
import requests
my_app = Flask(__name__)

@my_app.route('/')
def hello_python(): 
    return 'This is your first Flask app with Python'

@my_app.route('/about')
def get_about_you(): 
    return 'This is all about completing the Gen AI Certificate'

@my_app.route('/data')
def get_json_data(): 
    return {'output':'This is all about completing the Gen AI Certificate'}

@my_app.route('/health',methods=['GET','POST'])
def health_info():
    if request.method == 'GET': return jsonify(status="OK",method="GET"),200

# you can mention specific type as path variable
@my_app.route('/product/<int:productId>/<string:name>')
def get_product(productId,name):
    print(name)
    res = requests.get(f'https://dummyjson.com/products/{productId}')
    if res.status_code == 200:
        return {"message":res.json()},200
    else:
        return {"message":'something is wrong'},500
    

@my_app.route('/myform')
def myform():
    return  render_template("myform.html")

@my_app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f'username={username} and the password ={password}'

if __name__ == "__main__":
    my_app.run(debug=True)
