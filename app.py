# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/v1/sanitized/input/', methods=['POST'])
def json_example():
    request_data = request.get_json()

    lst =[]
    sql_check = ['insert','update','delete']

    if request_data:
        if 'validate' in request_data:
        	for x,y in request_data.items():
        		if y in sql_check:
        			return 'sanitized'
        		else:
        			return 'unsanitized'


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)