from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

if __name__ == '__main__':

    # Router and Controller
    @app.route('/home')
    def hello():
        return "Hello World !"

    @app.route('/home/dashboard')
    def home():
        return "You are in home page"
    

    @app.route('/list', methods=["GET"])
    def list():
        names = ['amarnath', 'ram', 'goyal']
        return str(names)

    @app.route('/dic', methods=["GET", "POST"])
    def dic():
        names = {'id':1, 'name':'Amarnath', 'designation':'consultant'}
        return jsonify(names)

    @app.route('/dashboard')
    def dashboard():
        print(request)
        print(request.args)
        print(request.args['id'])
        print(request.args['name'])
        name = 'amarnath'
        name_list = ['Vishwanathan', 'Ramkumar', 'Cyndee']
        return render_template("home.html", name = name, name_list= name_list)



    app.run(host='0.0.0.0', debug=True, port=5000)