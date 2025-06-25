#  Stock Portfolio Tracker Dashboard

A modern and interactive dashboard built with Dash to track your stock portfolio using manually defined prices. Designed to be simple, clean, and user-friendly.

---

##  Features

-  Add stocks using a dropdown 
-  Hardcoded stock prices (no API needed)
-  Calculates total investment
-  Pie chart and bar chart visualizations
-  Line chart for simulated trends
-  Download your portfolio as a CSV
-  Reset/Clear portfolio with one click
-  Dark theme UI (custom CSS)

---

##  Folder Structure

stock_portfolio_tracker/
│
├── app/
│ ├── layout.py # Dash layout components
│ ├── callbacks.py # Logic for interactivity
│ └── data.py # Hardcoded prices + portfolio store
│
├── assets/
│ └── style.css # Custom CSS styling
│
├── main.py # Main entry point
├── requirements.txt # Dependencies
└── README.md # This file

---

##  Setup Instructions

1. Clone the repo or download the folder

2. Install dependencies:
    pip install -r requirements.txt

3. Run the app:
    python main.py

4. Open in browser:
    Go to http://127.0.0.1:805