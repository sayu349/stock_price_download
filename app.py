# Flaskライブラリ
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file


import numpy as np
import pandas as pd
import yfinance as yf
#from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

# おまじない
app = Flask(__name__,static_folder='./templates/images')

def stock_price_return(company_name,start_date,end_date):
    ticker = yf.download(company_name, start = start_date, end = end_date)
    ticker.to_excel("result.xlsx")


@app.route('/')
def stock_price_input():
    return render_template("/stock_price_input.html")

@app.route('/result',methods=["GET","POST"])
def stock_price_calc_result():
    company_name = request.form['company_name'] + ".T"
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    need_data = request.form.getlist('need_data')

    stock_price_return(company_name,start_date,end_date)
    return render_template("stock_price_calc_result.html",
        need_data = need_data,
        start_date = start_date,
        end_date = end_date,
        company_name = company_name)