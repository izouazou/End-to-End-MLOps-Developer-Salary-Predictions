from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.stage06_prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 



@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            data = {
                'Country': request.form['Country'],
                'Age': request.form['Age'],
                'EdLevel': request.form['EdLevel'],
                'RemoteWork': request.form['RemoteWork'],
                'DevType': request.form['DevType'],
                'OrgSize': request.form['OrgSize'],
                'YearsCodePro': int(request.form['YearsCodePro'])
            }
            
        
            
            obj = PredictionPipeline()
            data = pd.DataFrame([data])
            predicted_salary = obj.predict(data)

            return render_template('predict_result.html', prediction=round(predicted_salary[0], 2))
        
            

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)