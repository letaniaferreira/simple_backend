from flask import Flask
from flask import request

app = Flask(__name__)

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

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/message')
def message():
    return my_dict


@app.route('/name')
def get_name():
    # 1. get username from client
    username = request.args.get('username')
    # 2. query dict to see if it has username
    no_such_user = {'message': 'user not available'}
    result = my_dict.get(username)
    if result is None:
        return no_such_user, 404
    # 3. return result
    return result


if __name__ == '__main__':
    app.run()
