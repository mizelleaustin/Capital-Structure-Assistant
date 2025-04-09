# Capital Structure Assistant 📊

This Streamlit web app analyzes a company's capital structure by calculating key financial ratios and generating natural-language commentary using GPT (OpenAI).

## 📄 Features

* Upload your own Excel or CSV file containing corporate financial data

* Automatically calculates:

  * Debt-to-Equity Ratio

  * Interest Coverage Ratio

* Uses GPT (via OpenAI API) to generate finance-grade commentary per company

* Interactive, professional summaries ideal for financial analysts, students, and corporate reporting

## ⚡ Quick Start
1. Clone this Repository
```
git clone https://github.com/mizelleaustin/capital-structure-assistant.git
cd capital-structure-assistant
```
2. Create Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate
```
4. Install Dependencies
```
pip install -r requirements.txt
```
5. Run the App
```
streamlit run app.py
```

## 📂 Input File Format

Your CSV or Excel file must include the following columns:

| Column           | Description                        |
| ---------------- | ---------------------------------- |
| Company          | Company name (e.g., Apple Inc.)    |
| Total_Debt       | Total interest-bearing debt        |
| Total_Equity     | Total shareholders' equity         |
| Interest_Expense | Annual interest expense            |
| EBIT             | Earnings before Interest and Taxes |

## 🔧 Tech Stack

* Streamlit for the interactive UI

* Pandas for financial calculations

* OpenAI GPT API for natural-language analysis

## 📂 Input File Format

🚀 Future Improvements

* Export commentary to PDF or markdown

* Add benchmarking vs industry averages

* Support for WACC inputs and capital structure optimization

## 📁 License

MIT License. See LICENSE for details.
