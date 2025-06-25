from dash import Input, Output, State, dcc, html, ctx
import pandas as pd
import plotly.express as px
from app.data import stock_prices, portfolio_data

def register_callbacks(app):
    @app.callback(
        [Output('portfolio-display', 'children'),
         Output('total-value', 'children'),
         Output('investment-bar-chart', 'figure'),
         Output('investment-pie-chart', 'figure'),
         Output('investment-line-chart', 'figure')],
        [Input('add-button', 'n_clicks'),
         Input('reset-button', 'n_clicks')],
        [State('stock-symbol', 'value'),
         State('stock-quantity', 'value')]
    )
    def update_portfolio(add_clicks, reset_clicks, symbol, quantity):
        triggered = ctx.triggered_id

        if triggered == 'reset-button':
            portfolio_data.clear()
        elif triggered == 'add-button':
            if symbol and isinstance(quantity, (int, float)) and quantity > 0:
                symbol = symbol.upper()
                if symbol in stock_prices:
                    price = stock_prices[symbol]
                    investment = price * quantity
                    portfolio_data.append({
                        "Stock": symbol,
                        "Quantity": quantity,
                        "Price": price,
                        "Investment": investment
                    })

        df = pd.DataFrame(portfolio_data)
        total = df['Investment'].sum() if not df.empty else 0

        list_items = [html.Div(f"{row['Stock']} - {row['Quantity']} x ${row['Price']} = ${row['Investment']}") for _, row in df.iterrows()]

        bar_fig = px.bar(df, x="Stock", y="Investment", title="Investment by Stock") if not df.empty else {}
        pie_fig = px.pie(df, names="Stock", values="Investment", title="Portfolio Share") if not df.empty else {}
        line_fig = px.line(df, x="Stock", y="Investment", title="Investment Trend") if not df.empty else {}

        return list_items, f"💰 Total Investment: ${total}", bar_fig, pie_fig, line_fig

    @app.callback(
        Output("download-dataframe-csv", "data"),
        Input("save-button", "n_clicks"),
        prevent_initial_call=True
    )
    def download_csv(n):
        if portfolio_data:
            df = pd.DataFrame(portfolio_data)
            return dcc.send_data_frame(df.to_csv, "portfolio.csv", index=False)
