import psycopg2
#from generate_data import generate_customer_table_data, generate_product_table_data, generate_payment_table_data, generate_price_table_data, generate_orders_data
from Bookstore import Bookstore
import os
import pandas as pd


def main():
    """
    pre: before running this program create two env variables.
        1. export DB_USER=<user_username>
        2. export DB_PASSWORD=<your_password>

        create the database in postgres.
        It also takes an user input to find similar books.
    post:  This program can do the following:
            1. call the table_ddls.sql script and create the tables.
            2. It calls Bookstore class to populate the tables with random data.
            3. Then it provides recommendation of similar books from user input of title and genre
    return:
    :return:
    """
    try:
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")
    except Exception as e:
        print("Please provide username or password.", e)
    try:
        conn = psycopg2.connect(
            database="d100",#toptal_project
            user=db_user,
            password=db_password,
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        num_rows = 10


        # filename = "table_ddls.sql"
        # try:
        #     with open(filename, 'r') as f:
        #         sql_script = f.read()
        #         cur.execute(sql_script)
        #         conn.commit()
        #         print("DDLs executed successfully.")
        # except Exception as e:
        #     print("Error in executing table creation script:", e)
        #     raise
        #
        #
        my_bookstore = Bookstore(conn, cur, num_rows)
        # my_bookstore.generate_customer_table_data()
        # my_bookstore.generate_product_table_data()
        # my_bookstore.generate_payment_table_data()
        # my_bookstore.generate_promotional_price_table_data()
        # my_bookstore.generate_orders_data()
        # my_bookstore.generate_ordered_item_table()
        # my_bookstore.generate_reviews_table_data()
        # print("Data generated and inserted into tables successfully.")
        # conn.commit()
        try:
            print("Lets find similar books.")
            my_bookstore.populate_similar_books()
            similar_book_sql_function = "select * from similar_books_population();"
            cur.execute(similar_book_sql_function)
            results = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            df = pd.DataFrame(results, columns=column_names)
            df = pd.DataFrame(results, columns=column_names)
            print("similar book table content is: \n", df)

            print("Now lets suggest a similar books by book title and genre.")
            title = input("Enter the book title: ")
            category = input("Enter genre of book: ")
            print("You entered:", title)
            sql_query = "select * from product;"
            cur.execute(sql_query)
            results = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            df = pd.DataFrame(results, columns = column_names)
            print("product table content is: \n", df)
            print("similar_books are:")
            print(my_bookstore.find_similar_products(df, title, category))
        except Exception as e:
            print("Error in finding similar books.", e)
            raise


    except Exception as e:
        print("An error occurred in generating, inserting data into tables or finding recommendations:", e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    main()