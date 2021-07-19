
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Annual_Income= float(request.form['Annual_Income'])
            Spending_Score= float(request.form['Spending_Score'])

            #filename_scaler = 'WineStandardScaler.pickle'
            #filename = 'Mall_Customer_model.pickle'

            # loading the model file from the storage
            #with open("WineStandardScaler.sav", 'rb') as f:
                #scalar = pickle.load(f)
            with open("MallModelForPrediction.sav", 'rb') as f:
                model = pickle.load(f)

            # predictions using the loaded model file
            data=[[Annual_Income,Spending_Score]]
            prediction=model.predict(data)
            print('prediction is', prediction[0])
            if prediction[0]==0:
                result='STANDARD'
            elif prediction[0]==1:
                result='CARE'
            elif prediction[0]==2:
                result='SMART'
            elif prediction[0]==3:
                result='CARELESS'

            else :
                result='TARGET'


            # showing the prediction results in a UI
            return render_template('results.html',prediction=result)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5004, debug=True)
	#app.run(debug=True) # running the app