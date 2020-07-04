from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


my_dict = {
    'jota': {
        'name': 'Jota',
        'local de compra': 'mercado de maridos'
    },
    'leta': {
        'name': 'leta',
        'local de compra': 'mercado de namoesposas'
    }
}


@app.route('/message')
def message():
    return my_dict


@app.route('/name')
def get_name():
    # 1. get username from client
    username = request.args.get('username')
    # 2. query dict to see if it has username
    result = my_dict[username]
    # 3. return result

    return result


if __name__ == '__main__':
    app.run()
