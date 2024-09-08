1. Pull Stop and Search Data from the API
We'll fetch stop and search data from the API for the Metropolitan Police Service force (force_id=metropolitan) using Python's requests library. Since the API only returns data for a specific month, we'll create a loop that pulls data for all months available.

2. Combine Data into a Pandas DataFrame
Once the data is fetched, we will combine it into a single DataFrame.

3. Clean and Format Data
We'll handle missing values, normalize the data types, and ensure the format is consistent.

4. Write the Data to CSV
We'll save the cleaned data into a CSV file.

5. Write a Process to Pull Latest Data Daily
We will schedule a job that will pull the latest data every day and append it to the existing CSV file.

6. Store Data in a Relational Database
We will describe how to store the data in a relational database, define the schema, and how to manage updates or deletions.

7. SQL Statement to Create an Aggregate View
We will create a SQL query to return an aggregate count of stop and search by crime type and date.

8. Containerize with Docker
Finally, we will containerize the solution using Docker for easy deployment.
