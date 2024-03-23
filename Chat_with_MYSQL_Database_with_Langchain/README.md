# Chat with MYSQL Database with the help of Python and Langchain


# Database workflow
<p align="center">
  <img src="https://github.com/AIWalaBro/GenAI_Projects/blob/main/Chat_with_MYSQL_Database_with_Langchain/flow%20chart%20of%20sql.png" width=100% height=100%>
</p>


# Database look
<p align="center">
  <img src="https://github.com/AIWalaBro/GenAI_Projects/blob/main/Chat_with_MYSQL_Database_with_Langchain/image.png" width=100% height=75%>
</p>

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

## Caution while Load the database
`IMPORTANT:` When using a real database, you should never use any user with WRITE permissions in an application like this one. Always use a user with READ permissions only and limit its scope. Otherwise, you might expose your database to SQL injection attacks.
