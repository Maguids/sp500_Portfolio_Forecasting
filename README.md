# SP500 Portfolio Forecasting

This project was developed for the "Artificial Intelligence and Data Science Laboratory" course and aims to **forecast future stock prices of the S&P500 index** utilizing machine learning algorithms **and applying optimization methods to select the best set of stocks for daily investment**. First Semester of the Third Year of the Bachelor's Degree in Artificial Intelligence and Data Science.

<br>

## Requirements:

	- Pandas
	- Numpy
	- Matplotlib
	- Seaborn
	- Scikit-learn
	- Tensorflow
	- Keras-tuner
	- Tqdm
	- Holidays
	- Joblib

<br>

## The Project
This project explores the **use of machine learning techniques** and **optimization methods** for **stock price forecasting** and **efficient portfolio creation** in the context of the **S&P 500 index**. Given the volatile and unpredictable nature of the financial market, the goal is to develop models that combine accurate forecasting with robust optimization strategies, such as Monte Carlo simulations. The **focus is on maximizing returns or minimizing risks**, offering a practical and grounded approach to real investment challenges. By using **historical data from 2010 to 2023 and simulating scenarios for January 2024**, the aim is to evaluate the applicability and impact of the proposed solutions on the financial market.

<br>

### The Dataset:

The data was obtained through the python file `obter_dados.py` which allowed us to access the **Yahoo Finance** data and save it to a csv. In this code file we download all available data regarding the companies that make up the S&P500 in the period between January 1, 2010 and January 31, 2024.

In order to identify the companies that make up the S&P500, we used the dataset 'sp500_companies.csv', which is available at the following link https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks?resource=download, along with other S&P500 datasets that we could use for this project. However, after analyzing this data, we realized that there were many missing values, so we chose to use only the list of companies to obtain the necessary data.

<br>

### Temporal Features
**Discrete temporal features** allow models to achieve better results as they help analyze patterns, trends, and buy/sell signals based on historical price behavior and trading volumes. Taking this into account, we decided to **group the dataset data by company**, in order to **process each action separately**, which is necessary considering that the technical indicators are calculated individually for each asset.

Therefore we decided to create a new dataset with the addition of the following indicators:
- **SMA (Simple Moving Average)**;
- **WMA (Weighted Moving Average)**;
- **Momentum**;
- **Stochastic %K e %D**;
- **MACD (Moving Average Convergence Divergence)**;
- **Larry William's R%**;
- **A/D Oscilator**;
- **CCI (Commodity Channel Index)**.

After creating the temporal features, we **divide the dataset by activity sectors** so that the model can better learn the patterns of each company.

<br>

### Models

- Random Forest
- LSTM

<br>

### Portfolio
To create the portfolios we used Monte Carlo, as a technique that allows simulating different market scenarios and evaluating the performance of different combinations of assets. 

It calculates the daily return and risk of the portfolio based on the weights assigned to each asset and optimizes these weights to balance risk and return, using a parameterized objective function.

Each day, the code analyzes the available historical data, calculates the average of the returns and the covariance matrix, and uses the Monte Carlo method to generate random combinations of weights. The weights are adjusted to respect practical limits, such as the maximum number of shares per day, and are used to calculate the daily return and update the portfolio balance.

The code tracks portfolio performance, calculating the final cumulative return and generating reports with daily returns, exported to a CSV file. This approach simulates a realistic investment management process, integrating risk analysis, optimization and practical constraints.

We use the following constraints:
- Sum of Weights Equal to 1;
- Daily Volume Limit (100 shares);
- Interruption on Reaching Limit;
- Daily Operating Cost (1 USD);
- Starting value of 10,000 USD;
- Purchasing Capacity Based on Current Balance;
- Total Volume Tracking;
- Volume-Based Weight Adjustment;
- Standardization of Weights After Adjustments.


<br>

## About the repository:

- Impacto legal e ético de projetos de otimização financeira.pdf ➡️ Is a pdf file that debates the ethical and legal implications of using AI in financial otimization;
- Lab_IACD_Project2.pdf ➡️Project statement
- T6_LabIACD_Project2.pdf ➡️ More information on how to develop the project;
- notebook.ipynb ➡️ The project in jupyter notebook format;
- obter_dados.py ➡️The code used to extract the Yahoo Finance data.

<br>

## Link to the course: 

This course is part of the **<u>first semester</u>** of the **<u>third year</u>** of the **<u>Bachelor's Degree in Artificial Intelligence and Data Science</u>** at **<u>FCUP</u>** and **<u>FEUP</u>** in the academic year 2024/2025. You can find more information about this course at the following link:

<div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
  <a href="https://sigarra.up.pt/fcup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=529878">
    <img alt="Link to Course" src="https://img.shields.io/badge/Link_to_Course-0077B5?style=for-the-badge&logo=logoColor=white" />
  </a>

  <div style="display: flex; gap: 10px; justify-content: center;">
    <a href="https://sigarra.up.pt/fcup/pt/web_page.inicial">
      <img alt="FCUP" src="https://img.shields.io/badge/FCUP-808080?style=for-the-badge&logo=logoColor=grey" />
    </a>
    <a href="https://sigarra.up.pt/feup/pt/web_page.inicial">
      <img alt="FEUP" src="https://img.shields.io/badge/FEUP-808080?style=for-the-badge&logo=logoColor=grey" />
    </a>
  </div>
</div>
