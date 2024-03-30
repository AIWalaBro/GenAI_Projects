# Chat with MYSQL Database with the help of GPT and Groq


## Features
- **Natural Language Processing**: Uses GPT-4 to interpret and respond to user queries in natural language.
- **SQL Query Generation**: Dynamically generates SQL queries based on the user's natural language input.
- **Database Interaction**: Connects to a SQL database to retrieve query results, demonstrating practical database interaction.
- **Streamlit GUI**: Features a user-friendly interface built with Streamlit, making it easy for users of all skill levels.
- **Python-based**: Entirely coded in Python, showcasing best practices in software development with modern technologies.


## Brief Explanation of How the Chatbot Works
- The chatbot works by taking a user's natural language query, converting it into a SQL query using GPT-4, executing the query on a SQL database, and then presenting the results back to the user in natural language. This process involves several steps of data processing and interaction with the OpenAI API and a SQL database, all seamlessly integrated into a Streamlit application.

- Consider the following diagram to understand how the different chains and components are built:


# Flow Chart
<p align="center">
  <img src="https://github.com/AIWalaBro/GenAI_Projects/blob/main/Chat_With_MYSQL_Database_GPT-4+MistralAI/Flowchart_mysql_chatbot1.drawio.svg" width=75% height=50%>
</p>


# Database 
<p align="center">
  <img src="https://github.com/AIWalaBro/GenAI_Projects/blob/main/Chat_with_MYSQL_Database_with_Langchain/image.png" width=75% height=75%>
</p>

## Chinook Database

- Chinook is a sample database available for SQL Server, Oracle, MySQL, etc. It can be created by running a single SQL script. Chinook database is an alternative to the Northwind database, being ideal for demos and testing ORM tools targeting single and multiple database servers.

### Supported Database Servers

* DB2
* MySQL
* Oracle
* PostgreSQL
* SQL Server
* SQL Server Compact
* SQLite


# Step to run this project

### step 1: setup the venv
```bash
- conda create -p venv_mysql_gui python=3.10 -y
- conda activate venv_mysql_gui

```

### step 2: setup you mysql database locally
```bash
- mysql -u root -p

```
### step 3: Create Database and use it, give the filepath 
```bash
- CREATE DATABASE chinook;
- USE chinook;
- SOURCE "SQL file path to load the database"

```

## Commands:

### To check which local host is runnning
```bash
- mysql -u root -p

```

### to see on which port you are running
```bash
- show variables like 'port';
```

## Caution while Load the database
`IMPORTANT:` When using a read database, you should never use any user with WRITE permissions in an application like this one. Always use a user with READ permissions only and limit its scope. Otherwise, you might expose your database to SQL injection attacks.

