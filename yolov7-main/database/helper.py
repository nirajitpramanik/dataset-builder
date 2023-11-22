import psycopg2
from psycopg2 import sql

db_params = {
    'dbname': 'DSA',
    'user': 'postgres',
    'password': 'Shukla@1402',
    'host': 'localhost',
    'port': 5432  
}

def insert_image():
    try:
        
        connection = psycopg2.connect(**db_params)
        
        cursor = connection.cursor()
    
        directory_address = input("Enter the directory address: ")
        
        object_name = input("Enter the name of the object: ")

        insert_query = "INSERT INTO dsa(object_name, file_directory) VALUES (%s, %s)"
        cursor.execute(insert_query, (object_name, directory_address))

        connection.commit()

        print(f"Object '{object_name}' with directory address '{directory_address}' inserted successfully.")


        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)

def insert_directory(directory_path):
    try:
       
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

   
        insert_query = sql.SQL("INSERT INTO sample (path_) VALUES ({})").format(sql.Literal(directory_path))

      
        cursor.execute(insert_query)

      
        conn.commit()

        print("Directory path stored successfully in the database.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
      
        if conn:
            conn.close()

def retrieve():
    try:
        connection = psycopg2.connect(**db_params)

        cursor = connection.cursor()


        object_name = input("Enter the name of the object: ")

    
        query = "SELECT image_path FROM dsa WHERE obj_name = %s"
        cursor.execute(query, (object_name,))

        result = cursor.fetchone()

        if result:
            file_directory = result[0]
            print(f"File directory for {object_name}: {file_directory}")
        else:
            print(f"Object with name {object_name} not found in the database.")

    
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)