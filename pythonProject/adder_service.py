from flask import Flask, request

app = Flask(__name__)


@app.route('add', methods=['POST'])
def add():
    num1 = request.form('num1')
    num2 = request.form('num2')
    try:
        result = int(num1) + int(num2)
        return str(result)
    except:
        return 'Invalid Input'


app.run(debug=True)
