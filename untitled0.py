import streamlit as st
import twstock
import pandas as pd

# 檢查 twstock.codes 中的內容
def check_twstock_codes():
    codes_data = []
    for stock_id, stock_info in twstock.codes.items():
        stock_data = {'股票代碼': stock_id}
        for key, value in vars(stock_info).items():
            stock_data[key] = value
        codes_data.append(stock_data)
    return codes_data

# 顯示結果在 Streamlit 中
st.title("twstock.codes 內容檢查")
codes_data = check_twstock_codes()
st.write(pd.DataFrame(codes_data))
