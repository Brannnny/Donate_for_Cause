import psycopg2

# AWS RDS PostgreSQL connection details


def db_connect(
    DB_HOST = "your-db-instance.xxxxxx.us-east-1.rds.amazonaws.com",
    DB_PORT = "5432",
    DB_NAME = "your_database",
    DB_USER = "your_username",
    DB_PASS = "your_password"
):

    try:
        # Establish the connection
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        print("✅ Connection to AWS RDS PostgreSQL successful!")

    except Exception as e:
        print("❌ Error connecting to the database:", e)

    return conn
