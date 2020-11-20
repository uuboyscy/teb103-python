from flask import Flask, request
from test import addFun

app = Flask(__name__)

@app.route('/hello_get')
def hello_get():
    return '<h1>hello flask</h1>'

@app.route('/greet/<name>')
def greet(name):
    outStr = """
    <h1>
    Hello %s
    </h1>"""%(name)
    return outStr

@app.route('/hello')
def hello():
    name = request.args.get('name')
    age = request.args.get('age')
    outStr = """Hello %s, you are %s years old."""%(name, age)
    return outStr

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    method = request.method
    outStr = """
    <h1>Who are you?</h1>
    <form action="/hello_post" method="POST">
    <input name="username">
    <button>Submit</button>
    </form>
    """
    if method == 'GET':
        return outStr
    else:
        username = request.form.get('username')
        outStr += """
        Hello %s
        """%(username)
        return outStr

@app.route('/add/<x>/<y>')
def add(x, y):
    sumTwo = addFun.add(int(x), int(y))
    return str(sumTwo)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
