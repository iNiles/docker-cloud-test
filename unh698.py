from flask import Flask
app=Flask(__name__)

@app.route('/')

def hello_world():
  return 'UNH698 Website'

if__name__ == '__main__':
  unittest.main()
