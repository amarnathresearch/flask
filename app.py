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

    @app.route('/iris/input')
    def iris_input():
        return render_template("iris_input.html")

        

    @app.route('/iris/test', methods=['GET'])
    def iris_test():

        print(request.args)
        f1 = request.args['f1']
        f2 = request.args['f2']
        f3 = request.args['f3']
        f4 = request.args['f4']
        pkl_filename = './models/iris_model.pkl'
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file)
            
        sample = [[f1, f2, f3, f4]]
        Ypredict = pickle_model.predict(sample)
        print("Ypredict", Ypredict)
        return str(Ypredict[0])


    @app.route('/admit/input')
    def admit_input():
        return render_template("admission_input.html")

# http://localhost:5000/admit/test?gre=300&gpa=3.7&rank=3
    @app.route('/admit/test', methods=['GET'])
    def admit_test():

        print(request.args)
        gre = request.args['gre']
        gpa = request.args['gpa']
        rank = request.args['rank']
        # pkl_filename = './models/sam_admission_model.pkl'
        # pkl_filename = './models/jayanth_admit_model.pkl'
        # pkl_filename = './models/sam_admission_model_v1.pkl'
        pkl_filename = './models/rimjhim_admit_model.pkl'
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file)
            
        sample = [[gre, gpa, rank]]
        Ypredict = pickle_model.predict(sample)
        print("Ypredict", Ypredict)
        return str(Ypredict[0])

# Sentiment analysis


    app.run(host='0.0.0.0', debug=True, port=5000)