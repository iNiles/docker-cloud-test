from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html")

@app.route('/secondpage')
def hello_otherworld():
    return render_template('other.html")
                           
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
