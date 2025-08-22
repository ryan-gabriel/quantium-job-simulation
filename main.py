from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('output/data.csv')

fig = px.bar(df, x="date", y="sales", color="region", barmode="group")

app.layout = html.Div(
    style={
        "backgroundColor": "#121212",
        "minHeight": "100vh",
        "padding": "0",
        "margin": "0",
        "fontFamily": "Arial, sans-serif",
    },
    children=[
        html.Link(rel="stylesheet", href="/assets/style.css"),

        html.H1(
            "Pink Morsel Data Visualizer",
            style={
                "color": "#fff",
                "textAlign": "center",
                "padding": "1.5rem",
                "margin": "0",
                "backgroundColor": "#1f1f1f",
                "borderBottom": "2px solid #ff69b4",
                "fontSize": "2rem",
                "letterSpacing": "1px",
            },
        ),

        html.P(
            "Dash: A web application framework for your data.",
            style={
                "color": "#bbb",
                "padding": "1rem 2rem",
                "margin": "0",
                "textAlign": "center",
                "fontSize": "1.1rem",
            },
        ),

        html.Div(
            style={
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                "padding": "1rem",
                "backgroundColor": "#1f1f1f",
                "margin": "1rem auto",
                "borderRadius": "12px",
                "width": "fit-content",
                "boxShadow": "0 2px 8px rgba(0,0,0,0.4)",
            },
            children=[
                dcc.RadioItems(
                    ['north', 'east', 'south', 'west', 'all'],
                    'north',
                    id='region-type',
                    inline=True,
                    style={
                        "color": "white",
                        "fontSize": "1rem",
                        "display":"flex",
                        "gap":"8px"
                    },
                )
            ],
        ),

        html.Div(
            style={
                "padding": "1rem 2rem",
            },
            children=[
                dcc.Graph(
                    id='graph',
                    figure=fig,
                    style={
                        "borderRadius": "12px",
                        "backgroundColor": "#1f1f1f",
                        "padding": "1rem",
                        "boxShadow": "0 4px 12px rgba(0,0,0,0.6)",
                    },
                )
            ],
        ),
    ],
)


@callback(
    Output('graph', 'figure'),
    Input('region-type', 'value'),
)
def update_graph(input_value):
    if input_value == "all":
        fig = px.bar(df, x="date", y="sales", color="region", barmode="group")
        return fig
    updated_df = df[df['region'] == input_value]
    fig = px.bar(updated_df, x="date", y="sales", color="region", barmode="group")
    return fig


if __name__ == '__main__':
    app.run(debug=True)
