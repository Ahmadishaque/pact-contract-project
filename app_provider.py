from flask import Flask, jsonify

app = Flask(__name__)

# This is the actual implementation of our service
@app.route('/users/1')
def get_user():
    # To pass: this must match the contract exactly!
    return jsonify({
        'id': 1,
        'full_name': 'Ahmad Ishaque'
    })

if __name__ == '__main__':
    app.run(port=5001)