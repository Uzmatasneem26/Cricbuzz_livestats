# query_db.py
import sqlite3
import pandas as pd

DB_PATH = "cricket.db"

def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    try:
        return pd.read_sql(query, conn)
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()
    finally:
        conn.close()

if __name__ == "__main__":
    #  Show all matches
    print("\n Matches:")
    print(run_query("SELECT * FROM matches LIMIT 5;"))

    #  Show all players
    print("\n Players:")
    print(run_query("SELECT * FROM players LIMIT 5;"))

    #  Show all team scores
    print("\n Scores:")
    print(run_query("SELECT * FROM scores LIMIT 5;"))

    #  Show player-level stats (new table!)
    print("\n Player Stats:")
    print(run_query("SELECT * FROM player_stats LIMIT 10;"))
