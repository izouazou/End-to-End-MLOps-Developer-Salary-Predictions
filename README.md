# End-to-End-MLOps-Developer-Salary-Predictions: Setup Guide

In this GitHub repository, we present a comprehensive solution for predicting developer salaries based on the Stack Overflow Annual Developer Survey 2023 dataset. The survey, conducted in May 2023, garnered responses from over 90,000 developers, providing valuable insights into their learning preferences, tool usage, and career aspirations.  

#### About the Dataset  

At the heart of our project is the Stack Overflow Annual Developer Survey 2023 dataset, a rich source of information that captures the diverse experiences and perspectives of developers around the world. Available for exploration and analysis, the dataset provides a detailed look into the ever-evolving landscape of the developer community.  

- [Download full dataset (CSV)](https://insights.stackoverflow.com/survey)

#### Project Overview  

Our goal is to build a robust machine learning model that predicts developer salaries by leveraging the characteristics of the survey dataset. This end-to-end machine learning operations (MLOps) solution includes data preprocessing, model training, deployment, and continuous monitoring to ensure a seamless workflow for predicting and updating salary predictions.
#### Key Features  

- **Exploratory Data Analysis (EDA)**: Dive into the survey data to unearth patterns and trends, providing a comprehensive exploration of the developer community. [Check EDA](https://github.com/izouazou/Data-Projects/tree/main/Stack_Overflow23)
- **Model Trainer**: Construct a robust and effective machine learning model by leveraging various features to predict developer salaries. [Check Model Trainer](https://github.com/izouazou/Data-Projects/tree/main/Stack_Overflow23)
- **MLOps Implementation**: Showcase the end-to-end MLOps pipeline, from model development to deployment and monitoring.


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




With the configuration and installation steps completed, use the following command to run the application:  

    # For local development use, enable debug mode with 'debug=True' for easy troubleshooting.
    # For production or deployment, consider removing 'debug=True' to disable debugging mode.
    
    python app.py
    
To initiate a comprehensive machine learning training pipeline, simply enter `http://192.168.1.10:8080/train` in your browser. This will trigger a script that serves as a conductor, orchestrating key stages including data ingestion, validation, transformation, model training, and evaluation. The script meticulously logs the initiation and completion of each stage. Once the pipeline is complete, return to `http://192.168.1.10:8080` in your browser to interact with the application.


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/izouazou/End-to-End-MLOps-Developer-Salary-Predictions/blob/main/LICENSE) file for details.




