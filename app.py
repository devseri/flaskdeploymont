from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

@app.route('/test')
def testfunc():
    return 'This is my Flask App'

@app.route('/<name>/<int:age>')
def testname(name,age):
    return f'My name is, {name} and my age is {age}'


@app.route('/handle',methods=['GET'])
def test_args_kwargs():

    args = request.args.getlist('args')
    kwargs = {key: value for key, value in request.args.items() if key != 'args'}

    args_list = list(args)
    kwargs_dict = dict(kwargs)

    result = {
        'args':args_list,
        'kwargs':kwargs_dict
    }

    return jsonify(result)

@app.route('/index')
def index():
    app_name = 'Ecommerce App'
    list1 = ['Tushar',29,56.7, 0x00123, {'city':'Pune'}]

    dict1 = {
        1001 : {'Name':'Ankita','Position':'Goverment Incometax Officer','Salary':'5000000'},
        1002 : {'Name':'Sarita','Position':'Cloud Engineer','Salary':'60000'},
        1003 : {'Name':'Vivek','Position':'System Administrator L2','Salary':'70000'},
        1004 : {'Name':'Gaurav','Position':'Devops Engineer','Salary':'65000'},
    }
    return render_template('index.html',data=app_name,list_data=list1,data_dict=dict1)


app.run()