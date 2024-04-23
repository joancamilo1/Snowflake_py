# This code does the following:

- Imports necessary libraries: pandas and snowflake.connector.

- Imports connection credentials (such as account, user, password, etc.) from a file named config.

- Connects to a Snowflake database using the provided credentials.

- Executes an SQL query to select all data from a specific table.

- Retrieves the query results.

- Closes the cursor and the connection after retrieving the results.

- Creates a Pandas DataFrame using the query results and column names obtained from the cursor.

- Takes the first 100 rows of the DataFrame for a sample.

# Essentially, this code connects Python to a Snowflake database, extracts data from a specific table, and loads it into a Pandas DataFrame for further processing or analysis.
