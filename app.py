from flask import Flask, render_template, jsonify, request
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle

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
        name = request.args['name']
        registration = request.args['id']
        name_list = ['Vishwanathan', 'Ramkumar', 'Cyndee']
        return render_template("home.html", name = name, registration = registration, name_list= name_list)

    @app.route('/analyse')
    def analyse():
        df = pd.read_csv('./data/binary.csv')
        data = df.head()
        print(data)
        return "hello world"

# Using Jupyter nodebook, we will train the model and save
    @app.route('/train')
    def train():
        url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        dataframe = pd.read_csv(url, names=names)
        array = dataframe.values
        X = array[:,0:8]
        Y = array[:,8]
        test_size = 0.33
        seed = 7
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size)
        model = LogisticRegression()
        model.fit(X_train, Y_train)
        # save the model to disk
        filename = './models/finalized_model.sav'
        pickle.dump(model, open(filename, 'wb'))
        return "trained"

    @app.route('/test')
    def test():
        filename = './models/finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        dataframe = pd.read_csv(url, names=names)
        array = dataframe.values
        X = array[:,0:8]
        Y = array[:,8]
        test_size = 0.33
        seed = 7
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size)
        result = loaded_model.score(X_test, Y_test)
        print(result)
        return "tested"

    # IRIS data linear regression
    @app.route('/iris/test')
    def iris_test():
        # Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)


    app.run(host='0.0.0.0', debug=True, port=5000)