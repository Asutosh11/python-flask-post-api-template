# Raw Flask is designed to run in development environment
# To make it run in production, we use a toll called waitress
# pip install waitress

from waitress import serve

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"

# API Request from front wend is - 
# URL - 127.0.0.1:5000/json-example  
# Raw JSON Request - {"language":"french", "framework":"flask"}

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json(force=True)
    
    language = req_data['language'] + " is nice"
    framework = req_data['framework'] + ' is robust'
    
    return jsonify(language=language, framework=framework)

if __name__=='__main__':
    # app.run(host='0.0.0.0'), instead use the code below
    serve(app, host="0.0.0.0", port=5000)
    

# Response is - 
# {"framework": "flask is robust", "language": "hindi is nice"}    
