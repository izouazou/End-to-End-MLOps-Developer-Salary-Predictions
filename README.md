# End-to-End-MLOps-Developer-Salary-Predictions: Setup Guide



## Prerequisites
Before setting up the application, ensure that you have the following software installed on your system:

- [Python 3.11](https://www.python.org/downloads/)  or newer
- [Git](https://git-scm.com/downloads)


Open your terminal or command prompt.    
Create a directory named "dev" and navigate to it:  

    
    mkdir dev
    cd dev
    
    
Clone the repository from GitHub:

    
    git clone https://github.com/izouazou/End-to-End-MLOps-Developer-Salary-Predictions.git
    cd End-to-End-MLOps-Developer-Salary-Predictions
    
## Environment Setup

Set up a Python virtual environment:  

    
    c:/python311/python.exe -m venv env
    env\Scripts\activate
    

Install required packages and tools.

    
    pip install -r requirements.txt
    
    
## Running the Application



With the configuration and installation steps completed, use the following commands to run the application:  

    # For local development use, debugging mode is enabled with 'debug=True' for easy troubleshooting.
    # For production or deployment, consider removing 'debug=True' to disable debugging mode.
    
    python app.py
    

Simply enter http:http://192.168.1.10:8080 in your browser to interact with the application.


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/izouazou/ToDoList/blob/main/LICENSE) file for details.



MLFLOW_TRACKING_URI=https://dagshub.com/izouazou/End-to-End-MLOps-Developer-Salary-Predictions.mlflow \
MLFLOW_TRACKING_USERNAME=izouazou \
MLFLOW_TRACKING_PASSWORD=1e86993d474c453b78ee31877b61a93590ca1c20 \
python script.py

hh


$env:MLFLOW_TRACKING_URI="https://dagshub.com/izouazou/End-to-End-MLOps-Developer-Salary-Predictions.mlflow"

$env:MLFLOW_TRACKING_USERNAME="izouazou"

$env:MLFLOW_TRACKING_PASSWORD="1e86993d474c453b78ee31877b61a93590ca1c20"
