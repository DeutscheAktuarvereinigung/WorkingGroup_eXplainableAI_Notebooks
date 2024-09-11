<p style="font-size:19px; text-align:left; margin-top: 15px;"><i>German Association of Actuaries (DAV) — Working Group "Explainable Artificial Intelligence"</i></p>
<p style="font-size:30px; text-align:left; margin-bottom: 15px"><b>README: Toy Example "Model-Agnostic Explainability Methods for Regression Problems: A Case Study on Medical Costs Data"<br>
</b></p>
<p style="font-size:19px; text-align:left; margin-bottom: 15px; margin-bottom: 15px">

## Description

This README provides installation instructions and an overview of the case study titled *"Model-Agnostic Explainability Methods for Regression Problems: A Case Study on Medical Costs Data."* The notebook demonstrates how to apply a range of model-agnostic explainability techniques to a machine learning regression problem using medical costs data. The case study offers insights at two levels: global explainability, which helps understand the overall model behavior, and local explainability, which sheds light on the factors driving individual predictions.
By leveraging techniques such as global surrogate models, Partial Dependence Plots (PDP), Accumulated Local Effects (ALE), SHAP, and LIME, the study aims to enhance transparency and trust in machine learning models that often act as black boxes. This makes it particularly relevant for actuaries, data scientists, and other stakeholders looking to interpret and validate predictive models.

## Getting Started

There are two ways to explore and run the notebook, allowing you to gain hands-on experience with the model-agnostic explainability methods:

1. **Running Locally**:  
   You can download the Jupyter Notebook file along with a `requirements.txt` file, which lists all the necessary packages and their respective version numbers. To run the notebook on your local machine, simply follow these steps:
   - Ensure that you have a Python environment set up with Jupyter Notebook.
   - Install the required libraries using the `requirements.txt` file by running `pip install -r requirements.txt` in your terminal.
   - Once the dependencies are installed, open and run the notebook on your local machine.

2. **Running on Kaggle**:  
   Alternatively, you can access and run the notebook directly on [Kaggle](https://www.kaggle.com/code/simonhatzesberger/model-agnostic-xai-methods-for-regression) without the need to download any files or install packages on your own machine. This option provides a seamless experience, as you can execute the notebook in Kaggle’s environment with all necessary dependencies pre-installed. No registration is required, and everything can be run in your browser.

## Content Overview

The case study includes the following main files:

1. **Jupyter Notebook (`toy_python_regression_MedicalCosts.ipynb`)**: This Python notebook provides a comprehensive exploration of model-agnostic explainability methods applied to a medical costs regression task. The focus is on understanding both global and local aspects of the model's behavior.
2. **Rendered HTML file (`toy_python_regression_MedicalCosts.html`)**: The fully executed notebook, including all outputs and visualizations, is available in HTML format for easy review in any web browser.
3. **Rendered PDF file (`toy_python_regression_MedicalCosts.pdf`)**: The notebook is also provided as a PDF for those who prefer a static, easily shareable format.
4. **Dataset (`MedicalCosts.csv`)**: This file contains the underlying medical costs dataset, which is used throughout the notebook for building the regression model and applying the explainability methods.

The notebook walks through the following steps:

- **Exploratory Data Analysis (EDA)**: A brief exploration of the medical costs dataset, including features such as age, sex, body mass index (BMI), number of children, smoking status, and regional location, which are used to predict individual medical costs.
- **Model Training and Evaluation**: The CatBoost algorithm, a high-performance black-box machine learning model, is trained to predict medical costs based on the features identified in the EDA. Model performance is evaluated to ensure accurate predictions.
- **Global Explainability Methods**: Methods such as global surrogate models, Partial Dependence Plots (PDP), Accumulated Local Effects (ALE), and Permutation Feature Importance (PFI) are applied to analyze the overall model behavior.
- **Local Explainability Methods**: Techniques like SHAP, LIME, and ICE plots provide insights into individual predictions and decision-making processes of the model.

The aim is to equip users with both theoretical and practical tools for better understanding machine learning models, particularly in regression contexts.

## Key Learning Points

- The notebook presents various explainability methods for actuaries, data scientists, and others interested in interpretable AI.
- It demonstrates the use of model-agnostic techniques that can be applied across different machine learning models, making the results generalizable.
- A CatBoost model is used for demonstration purposes, but the methodology is designed to be adaptable to other models.

For quick browsing, both the HTML and PDF versions of the executed notebook are available. Please note that GitHub may only show raw HTML files, so they need to be downloaded and opened in a browser or a PDF viewer for proper visualization.

## Author

Simon Hatzesberger (<a href="mailto:simon.hatzesberger@gmail.com">simon.hatzesberger@gmail.com</a>)

## Version History

* 1.0 Initial Release

## License

This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details.
