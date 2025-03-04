📊 Comparison of Interest Rates and Departures
This repository is part of the course Business Intelligence (I-707-VGBI) at Reykjavík University. The project explores the relationship between policy interest rates set by the Central Bank of Iceland and departures from Keflavík International Airport to analyze how economic factors influence consumer behavior.

📌 Project Overview
Interest rates are a key economic tool used to regulate inflation and influence spending habits. This project investigates whether changes in policy interest rates have a measurable impact on outbound travel from Iceland, particularly in response to economic conditions and consumer spending power.

📂 Data Sources
Central Bank of Iceland – Monthly interest rate data (2015–2024)
Icelandic Tourist Board – Monthly departures of Icelandic residents from Keflavík Airport

🔧 Technology Stack
Programming: Python
Database: SQL (PostgreSQL/SQLite)
Data Processing: SQL Power Query, Excel
Visualization: Excel, Pandas

🚀 How to Run the Project

Make sure preferred SQL is installed on you computer. In this case PostgreSQL is used
Install dependency: pip install psycopg2

Create and load the data into the database: python load_data.py
View analysis results in excel for example. Note requires to connect the database to excel using Excel Power Query

📊 Key Findings
A correlation exists between higher interest rates and a decline in outbound travel.
Travel was lowest during COVID-19 lockdowns, despite historically low interest rates.
External factors such as currency fluctuations and economic conditions also impact travel decisions.

👥 Contributors
Bjarki Dan Andrésson - bjarkida22@ru.is

Dagur Már Oddsson - dagurmo22@ru.is

Hjördís Anna Óskarsdóttir - hjordiso22@ru.is
