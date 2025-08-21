from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('output/data.csv')

fig = px.bar(df, x="date", y="sales", color="region", barmode="group")

app.layout = html.Div(children=[
    # Global style via html.Style
     html.Link(rel="stylesheet", href="/assets/style.css"),
    
    html.H1(children='Pink Morsel Data Visualizer', style={
        "color": "white",
        "width": "100%",
        "padding": "1rem",
        "textAlign": "center",
        "backgroundColor": "#141414"
    }),

    html.Div(children='Dash: A web application framework for your data.', style={
        "color": "white",
        "padding": "0 1rem"
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig,
        style={"margin": "0", "padding": "0"}
    )
])

if __name__ == '__main__':
    app.run(debug=True)
