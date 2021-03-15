import plotly.figure_factory as pf
import pandas as pd
import csv

df = pd.read_csv("data.csv")
fig = pf.create_distplot([df["Avg Rating"].tolist()], ["Mobile Brand"], show_hist=False)
fig.show()