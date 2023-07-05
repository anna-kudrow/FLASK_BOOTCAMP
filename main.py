from flask import Flask
  

app = Flask(__name__)

@app.route('/')
def main():
     return "<h1>Hello, world</h1><br><a href='/index'>перейти на 2-ю страницу</a>"

if __name__ == '__main__':
     app.run()

@app.route('/index')
def index():
     return "It's my first project"     