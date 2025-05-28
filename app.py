from flask import Flask, request

app = Flask(__name__)


@app.route('/divide')
def divide():
    string_args = request.args.get('num')
    if not string_args:
        return "please provide a 'num' parameter", 400
    try:
        num = int(string_args)
        if num == 0:
            return "Cannot divide by zero", 400
        return f"Result: {100 / num}"
    except ValueError:
        return "Invalid number format", 400



@app.route('/length')
def length():
    name = request.args.get('name')
    if not name:
        return "Please provide a 'name' parameter", 400

    return f"Length: {len(name)}"  


@app.route('/add')
def add():
    a = request.args.get('a')  
    b = request.args.get('b')
    if not a or not b:
        return "Please provide 'a' and 'b' parameters", 400
    try:
        a = int(a)
        b = int(b)
        result = a + b
        return f"Sum: {result}"
    except ValueError:
        return "Invalid number format", 400


@app.route('/undefined')
def undefined():
    value = request.args.get('value')
    return f"The value is: {value}"


@app.route('/index')
def index():
    data = [1, 2, 3]
    i = request.args.get('i')
    if not i:
        return "Please provide an 'i' parameter", 400
    else:
        return f"Item: {data[i]}" 


@app.route('/submit', methods=['GET', 'POST'])
def submit():

    data = request.form.get('data')
    if not data:
        return "Please provide 'data' in the form", 400  
    return f"Received: {data}"


@app.route('/call')
def call():
    def missing_function():
        return "This function is missing!"
    return missing_function()  


@app.route('/check-age')
def check_age():
    age = request.args.get('age')
    if not age:
        return "Please provide an 'age' parameter", 400
    try:    
        age = int(age)
    except ValueError:
        return "Invalid age format", 400
    if age < 18:
        return "You are underage."
    elif age > 18:
        return "You are an adult."
    else:
        return "Age is unknown?"  

if __name__ == '__main__':
    app.run(debug=True)
