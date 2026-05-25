# Flight Analysis Dashboard

A Streamlit dashboard for searching flight routes and viewing basic flight analytics from a local MySQL database.

## Features

- Search flights by source and destination city.
- View route results with airline, source, destination, stops, and price.
- Display airline frequency as a pie chart.
- Display busiest cities as a table and bar chart.

## Project Structure

```text
.
|-- app.py        # Main Streamlit application
|-- dbhelper.py   # MySQL connection and query helper class
|-- sql.py        # Manual database connection/query test script
|-- check.py      # Manual flight city query test script
`-- .gitignore
```

## Requirements

- Python 3.9+
- MySQL Server
- Python packages:
  - streamlit
  - plotly
  - pandas
  - mysql-connector-python

## Setup

1. Install dependencies:

```bash
pip install streamlit plotly pandas mysql-connector-python
```

2. Make sure MySQL is running locally.

3. Create or import a MySQL database named `indigo`.

4. The app expects a `flights` table with these columns:

```text
Airline
Source
Destination
Total_Stops
Price
```

5. Update the database credentials in `dbhelper.py` if your local MySQL setup is different:

```python
host='localhost'
user='root'
password='root123'
database='indigo'
```

## Run The App

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Notes

- `sql.py` and `check.py` are helper scripts for testing database connectivity and sample queries.
- The current database connection is configured for a local MySQL server using the `mysql_native_password` authentication plugin.
