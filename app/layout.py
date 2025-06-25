from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H2("📈 Stock Portfolio Tracker", className="text-center text-info my-4"),

    dbc.Row([
        dbc.Col([
            dbc.Label("Select Stock Symbol"),
            dcc.Dropdown(
                id='stock-symbol',
                options=[
                    {"label": "Apple (AAPL)", "value": "AAPL"},
                    {"label": "Tesla (TSLA)", "value": "TSLA"},
                    {"label": "Google (GOOG)", "value": "GOOG"},
                    {"label": "Microsoft (MSFT)", "value": "MSFT"},
                    {"label": "Meta (META)", "value": "META"},
                ],
                placeholder="Select a stock",
                className="mb-2",
                clearable=False
            ),


            dbc.Label("Quantity"),
            dcc.Input(id='stock-quantity', type='number', placeholder='e.g., 5', className="form-control mb-2"),

            dbc.Button("Add Stock", id='add-button', color="success", className="mb-2 w-100"),
            dbc.Button("🔄 Reset Portfolio", id='reset-button', color="danger", className="w-100 mb-3"),

            dbc.Checkbox(id="theme-toggle", label="🌙 Dark Mode", value=True, className="mb-2")
        ], width=4),

        dbc.Col([
            html.H4("📊 Portfolio Summary"),
            html.Div(id='portfolio-display', className='mt-2'),
            html.H5(id='total-value', className='text-warning mt-3'),

            dcc.Graph(id='investment-bar-chart', className='mt-4'),
            dcc.Graph(id='investment-pie-chart'),
            dcc.Graph(id='investment-line-chart'),

            dbc.Button("Download CSV", id='save-button', color="info", className="mt-3"),
            dcc.Download(id="download-dataframe-csv")
        ], width=8)
    ])
], fluid=True)
