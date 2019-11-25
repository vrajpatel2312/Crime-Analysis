from flask import Flask
from flask import render_template
import numpy as np
import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
    PATH='1.csv'
    df = pd.read_csv(PATH)
    borough= ['BRONX','BROOKLYN','MANHATTAN','STATEN ISLAND']
    model = ['knn','lr','dtc','clfpoly3','clfpoly2','rf']
    values={}
    year = [2017,2018,2019,2020,2021,2022]
    for i in borough:
        for j in model:
            for k in year:
                name = i+j+str(k)
                print(name)
                values[i+j+str(k)]=np.array(df[(df.year == k) & (df.model == j) & (df.borough == i) ].rate)
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August","September","October","November","December"]
    
    return render_template('/index.html', values=values, labels=labels, legend=legend)


if __name__ == "__main__":
    app.run(debug=True)
