from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

all_users = {
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
    return {'message': 'Hello World!'}


@app.route('/users')
def get_users_jsonified():
    return jsonify(get_users())


def get_users():
    users = []
    for user in all_users.values():
        users.append(user)

    return users


@app.route('/name')
def get_name():
    # 1. get username from client
    username = request.args.get('username')
    # 2. query dict to see if it has username
    no_such_user = {'message': 'user not available'}
    result = all_users.get(username)
    if result is None:
        return no_such_user, 404
    # 3. return result
    return result


if __name__ == '__main__':
    app.run()
