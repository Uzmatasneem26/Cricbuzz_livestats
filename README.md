# 🏏 Cricbuzz LiveStats: Real-Time Cricket Insights & SQL Analytics

[**Live Demo App**](https://cricbuzz-livestats.streamlit.app/)

An interactive multi-page cricket analytics dashboard built with **Python, SQLite, and Streamlit**.
It integrates cricket match data (sample JSON or live API), stores it in a database, and provides live dashboards, visualizations, and SQL query practice.



---

## Features
- 🌐 API integration (Cricbuzz/unofficial JSON or sample dataset)
- 🗄️ SQLite database backend
- 📊 Streamlit multi-page dashboard
- 🔍 Custom SQL query interface
- 📤 Export data to CSV
- 📦 Deployable on Streamlit Cloud / Render


## Tech Stack
- **Python 3.12** (pandas, sqlite3, SQLAlchemy, requests)
- **Streamlit** (for the web app)
- **SQLite** (lightweight database)
- **Tabulate** (pretty console output)
- **SQLAlchemy** (connection handling)
- **Pandas** (data wrangling)
- **Requests** (API integration)

---

## Project Structure

```
cricbuzz-livestats/
│
├── streamlit_app.py # Main entry point
├── logo.png # App logo
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── cricket.db # SQLite database (generated)
├── sample_cricket_data.json # Mock cricket data
│
├── utils/
│ ├── create_db.py # Script to create & populate DB
│ └── db_connection.py # Centralized DB functions
│
├── pages/
│ ├── 1_Home.py
│ ├── 2_Matches.py
│ ├── 3_Players.py
│ ├── 4_SQL_Queries.py
│ ├── 5_CRUD.py
│ ├── 6_Matches_CRUD.py
│ ├── 7_Scores_CRUD.py
│ ├── 8_Visualizations.py
│ └── 9_Analytics_Overview.py


```
---

## Run the App

```bash

\# Install dependencies

pip install -r requirements.txt



\# Run Streamlit app

streamlit run streamlit\_app.py

```

## Description

•	Home Page → Navigation + Project overview

•	Matches & Players Pages → Explore raw data

•	Scorecards & Visuals → Runs, wickets, comparisons

•	SQL Queries Page → 25 beginner → advanced queries + custom query box

•	CRUD Pages → Add, update, delete records

•	Analytics Overview → Leaderboards, KPIs, trends

## Use Cases

•	Sports Media & Broadcasting

•	Fantasy Cricket Platforms

•	Cricket Analytics Firms

•	Educational SQL Projects

## Credits

•	Mock data created for portfolio purposes

•	Inspired by Cricbuzz APIs and community-built cricket datasets

---
