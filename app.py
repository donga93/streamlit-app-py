import streamlit as st # pip install streamlit
import plotly.graph_objects as go # pip install plotly


# ----------- SETTINGS -------
incomes = ["Salary", "3D Printing" , "Consulting"]
expenses = [ "Rent", "Fiber" , "Water & Electricity" , "Groceries" , "Child Care" , "Car" ,"Other Expenses" , "Savings" , "Entertainment" ]  
currency = "R"
page_title = "Income and Expense Tracker "
page_icon = ":money-with-wings:" # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " "+ page_icon)
