from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    return 'UNH698 Website'
@app.route('/secondpage')
def hello_otherworld():
    return render_template('other.html')
    return 'secondpage or other'
                           
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
