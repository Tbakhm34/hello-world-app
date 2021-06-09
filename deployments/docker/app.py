from flask import Flask,  jsonify 
import os 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello, my name is Tolganay Akhmetkaliyeva, and I am a developer',
        'environment': os.environ.get('ENVIRONMENT'),
        'owner': 'Tolganay',
        'namespace': os.environ.get('NAMESPACE')
    })
    
@app.route('/tolganay')
def tolganay():
    return jsonify({
        'message': 'This is Tolganay Akhmetkalievas page'
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)