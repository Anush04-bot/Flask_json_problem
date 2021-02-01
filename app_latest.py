# import main Flask class and request object
import json
import re
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/v1/sanitized/input/', methods=['POST'])
def json_example():
    request_data = request.get_json()
    for x,y in request_data.items():
        res = sql_inj(x,y)
    print(res)
    return res


def sql_inj(k_key,v_value):  
    lst = []
    with open('my_sql_queries.json') as f:
        y = json.load(f)

    for key, value in y.items():
        lst.append(key)
    
    if k_key in lst:
        #val = y[k_key]
        if (type(y[k_key]) == list) and (len(y[k_key]) > 0):
            for i in range(len(y[k_key])):
                val = y[k_key][i]
                f_val = re.findall(v_value,val)
                if v_value in f_val:
                    return 'unsanitised'
                    
            return 'sanitised'
    else:
        return 'sanitised'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)