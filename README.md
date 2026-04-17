# 📊 Stock Market Analysis using Python

---

## 📌 Overview

This project focuses on analyzing and comparing stock performance across multiple sectors using Python. It evaluates key financial metrics such as returns, volatility, and trends to generate data-driven insights and support investment decision-making.

---

## 🎯 Problem Statement

In today’s financial environment, investors are faced with multiple investment options across different sectors such as technology, banking, and energy. Each stock behaves differently in terms of growth, stability, and risk, making it difficult to make informed decisions.

This project aims to analyze historical stock data using quantitative methods to identify trends, measure risk, and compare performance across stocks. The goal is to provide meaningful insights that help in understanding which stocks are suitable for different types of investors based on their risk appetite.

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* yfinance

---

## 📊 Dataset

Stock data was collected using the yfinance API for the following companies:

* Tata Consultancy Services (TCS)
* Reliance Industries
* HDFC Bank
* Infosys

Time Period: 2020 – 2026

---

## ⚙️ Methodology

1. Data collection using yfinance
2. Data cleaning and preprocessing
3. Feature engineering:

   * Moving Averages (7-day, 30-day)
   * Daily Returns
   * Volatility
4. Data visualization
5. Comparative analysis across stocks

---

## 📈 Key Insights

* **All stocks showed long-term growth**, but performance varied across sectors
* **Normalization was required** to compare stocks fairly due to different price ranges
* **Reliance Industries delivered higher returns but with higher volatility**, indicating higher risk
* **TCS showed stable and consistent growth with low volatility**, making it a safer investment
* **Infosys provided a balance between growth and risk**
* **HDFC Bank showed moderate performance with stability**, suitable for diversification
* **Stocks within the same sector showed high correlation**, especially TCS and Infosys
* **Diversification across sectors reduces overall portfolio risk**

---

## 📊 Visualizations

### 📈 Price Comparison

<img width="1200" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/19bfc568-b7a6-487a-9a38-dc196731f5f0" />


### 📊 Normalized Performance
<img width="1200" height="600" alt="figure_2" src="https://github.com/user-attachments/assets/1dceea61-74e3-42a1-a8c9-d19080438314" />


### 📉 Volatility Analysis

<img width="1200" height="600" alt="figure_3" src="https://github.com/user-attachments/assets/738a92ef-2c4d-4779-8575-d27d7a040ac4" />


### 🔥 Correlation Heatmap

<img width="800" height="600" alt="Figure_5" src="https://github.com/user-attachments/assets/a052908f-931f-4d2f-8bdd-0553d65d78e7" />
<img width="1200" height="600" alt="Figure_4" src="https://github.com/user-attachments/assets/c11ecf15-3acf-429e-a7ad-31ddf310c44a" />


---

## 🏁 Conclusion

The analysis shows that stock performance should not be evaluated based solely on price. Instead, a combination of returns, volatility, and trends provides a clearer understanding of performance.

Different stocks serve different investment purposes. While some offer high growth with higher risk, others provide stability with consistent returns. Sector behavior also plays an important role in influencing stock performance.

---

## 📌 Final Recommendation

* High-risk investors can consider Reliance Industries for higher returns
* Risk-averse investors should prefer TCS for stability
* Infosys offers a balanced investment option
* HDFC Bank is suitable for diversification

👉 A diversified portfolio combining different sectors is recommended to balance risk and return.

---

## 🚀 Future Improvements

* Add stock price prediction using Machine Learning
* Build interactive dashboard using Power BI
* Integrate real-time stock data

---

## 📂 Project Structure

```
Stock-Market-Analysis/
│
├── main.py
├── README.md
├── requirements.txt
├── images/
```

---

## 💡 Author

Deepak Chandola
Data Analyst
