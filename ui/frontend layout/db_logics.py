import psycopg2
from psycopg2 import sql

# Function to create a connection to the database
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="db_name",       # Replace with your DB name
            user="postgres",         # Replace with your DB user
            password="db_psswd", # Replace with your DB password
            host="localhost",            # Database host (localhost or IP)
            port="5432"                  # Default PostgreSQL port
        )
        return conn
    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
        return None

def login_query(username,password,user_type):
    conn = create_connection()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        login_command= """
        SELECT * FROM student WHERE
        student_id=
        AND user_password=password
        ;"""
        cursor.execute(login_command)
        conn.commit()
        #login logic
    except Exception as e:
        print(f"Error finding relatable records,please contact the admin: {e}")
    finally:
        cursor.close()
        conn.close()