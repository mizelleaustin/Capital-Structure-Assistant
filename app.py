import streamlit as st
import pandas as pd
import openai
import os

st.set_page_config(page_title="Capital Structure Assistant", layout="centered")
st.title("📊 Capital Structure Assistant")

# --- Upload Section ---
uploaded_file = st.file_uploader("Upload your financial Excel or CSV file", type=["csv", "xlsx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1]
    df = pd.read_excel(uploaded_file) if file_ext == "xlsx" else pd.read_csv(uploaded_file)

    # Check for required columns
    required_cols = {"Company", "Total_Debt", "Total_Equity", "Interest_Expense", "EBIT"}
    if not required_cols.issubset(df.columns):
        st.error(f"Missing columns. Your file must include: {', '.join(required_cols)}")
    else:
        # Compute Ratios
        df['Debt_to_Equity'] = df['Total_Debt'] / df['Total_Equity']
        df['Interest_Coverage'] = df['EBIT'] / df['Interest_Expense']

        # Display the calculated metrics
        st.subheader("Calculated Financial Ratios")
        st.dataframe(df[["Company", "Debt_to_Equity", "Interest_Coverage"]])

        # OpenAI API key
        openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

        if openai_api_key:
            openai.api_key = openai_api_key
            st.subheader("📄 GPT-Generated Capital Structure Commentary")

            for _, row in df.iterrows():
                company = row['Company']
                de = row['Debt_to_Equity']
                ic = row['Interest_Coverage']

                prompt = f"""
You are a corporate finance analyst. Analyze the following capital structure information for {company}:

- Debt-to-Equity Ratio: {de:.2f}
- Interest Coverage Ratio: {ic:.2f}

Generate a narrative summary that:
1. Explains what the ratios indicate.
2. Assesses the company’s financial risk.
3. Discusses pros and cons of increasing either debt or equity.
4. Uses clear, professional language suitable for a finance executive.
"""
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=500
                    )
                    commentary = response["choices"][0]["message"]["content"]
                    with st.expander(f"Analysis for {company}"):
                        st.write(commentary.strip())
                except Exception as e:
                    st.error(f"Failed to generate analysis for {company}: {str(e)}")
