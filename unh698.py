from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'If I get this server up it will be a miracle UNH698 Website' 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
