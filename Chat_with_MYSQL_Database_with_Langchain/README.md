# Chat with MYSQL Database with the help of Python and Langchain


# Database workflow
<p align="center">
  <img src="https://github.com/AIWalaBro/GenAI_Projects/blob/main/Chat_with_MYSQL_Database_with_Langchain/flow%20chart%20of%20sql.png" width=100% height=100%>
</p>


# Database look
<p align="center">
  <img src="https://github.com/AIWalaBro/GenAI_Projects/blob/main/Chat_with_MYSQL_Database_with_Langchain/image.png" width=100% height=75%>
</p>

## Chinook Database

Chinook is a sample database available for SQL Server, Oracle, MySQL, etc. It can be created by running a single SQL script. Chinook database is an alternative to the Northwind database, being ideal for demos and testing ORM tools targeting single and multiple database servers.

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
- conda create -p venv_mysql_langchain python=3.10 -y
- conda activate venv_mysql_langchain

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
- mysql -u root -padmin
```

### to see on which port you are running
```bash
- show variables like 'port';
```

## Caution while Load the database
`IMPORTANT:` When using a read database, you should never use any user with WRITE permissions in an application like this one. Always use a user with READ permissions only and limit its scope. Otherwise, you might expose your database to SQL injection attacks.
