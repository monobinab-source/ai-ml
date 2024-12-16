import random
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""
TO: take out review from product table. Rename product to book
add msrp_price in product
rename price table to promotional_price.
add foreign keys
"""

class Bookstore:
    def __init__(self, conn, cur, num_rows):
        self._conn = conn #_note suggests that the variable is private and should be accessed usign getter and setter.
        self._cur = cur
        self._num_rows = num_rows

    def get_conn(self):
        return self._conn

    def get_cur(self):
        return self._cur

    def get_num_rows(self):
        return self._num_rows

    def set_conn(self, value):
        self._conn = value

    def set_cur(self, value):
        self._cur = value

    def set_num_rows(self, value):
        self._num_rows = value

    def generate_customer_table_data(self):
        for i in range(self._num_rows):
            id = i+1
            # first_name = 'First_' + str(random.randint(1, 100))
            # last_name = 'Last_' + str(random.randint(1, 100))
            first_name = 'First_' + str(id)
            last_name = 'Last_' + str(id)
            email = first_name + '_' + last_name + '@example.com'


            insert_query = """
                INSERT INTO customer (id, first_name, last_name, email)
                VALUES (%s, %s, %s, %s);
            """

            self._cur.execute(insert_query, (id, first_name, last_name, email))


    def generate_product_table_data(self):
            for i in range(self._num_rows):
                id = i + 1
                isbn = f"ISBN-{str(random.randint(1000, 9999))}"
                language = random.choice(["English", "French", "Spanish"])
                if language == "English":
                    title = f"Random Book {i + 1} (EN)"

                    category = random.choice(["Fiction", "Non-Fiction"])  # limiting to 2 categories to find similar products easily (took off "Science Fiction", "Fantasy)
                    description = f"This is a randomly generated description for book {i + 1} in English"
                    # description_sp = ""
                    # description_fr = ""
                if language == "Spanish":
                    title = f"Libro aleatorio {i + 1} (ES)"
                    category = random.choice(["Ficción", "No ficción"])  # Adjust for Spanish translations
                    description = f"Esta es una descripción aleatoria para el libro {i + 1} en español"

                if language == "French":
                    title = f"Livre aléatoire {i + 1} (FR)"

                    category = random.choice(["Fiction", "Non-Fiction"])  # Adjust for French translations
                    description = f"Ceci est une description aléatoire pour le livre {i + 1} en français"

                # price = round(random.uniform(10, 100), 2)
                #review = f"A random review for book {i + 1}"
                # similar_products = [random.randint(1, self._num_rows) for _ in range(3)]
                # all_existing_ids = range(1, i + 1)
                # similar_products = random.sample(all_existing_ids, 3)

                insert_query = """
                    INSERT INTO product (ID, ISBN, TITLE, CATEGORY, DESCRIPTION, LANGUAGE)
                    VALUES  (%s, %s, %s, %s, %s, %s);
                """

                self._cur.execute(insert_query, (id, isbn, title, category, description, language))


    def generate_payment_table_data(self):
        for i in range(self._num_rows):
            id = i + 1
            customer_id = i + 1
            payment_method = random.choice(["credit card", "debit card"])

            if payment_method == "credit card":
                card_number = "XXXX-XXXX-XXXX-" + str(random.randint(1000, 9999))
                cvc_code = str(random.randint(100, 999))
                pin = None
                expiration_date = f"2024-{str(random.randint(1, 12)).zfill(2)}-{str(random.randint(1, 28)).zfill(2)}"
            if payment_method == "debit card":
                card_number = "XXXX-XXXX-XXXX-" + str(random.randint(1000, 9999))
                cvc_code = None
                pin = str(random.randint(1000, 9999))
                expiration_date = f"2024-{str(random.randint(1, 12)).zfill(2)}-{str(random.randint(1, 28)).zfill(2)}"

            address_line_1 = f"Address Line 1 {i + 1}"
            address_line_2 = f"Address Line 2 {i + 1}"
            city = f"City {i + 1}"
            state = random.choice(["CA", "NY", "TX", "FL"])
            country = "USA"

            insert_query = """
                INSERT INTO payment (ID, CUSTOMER_ID, PAYMENT_METHOD, CARD_NUMBER, CVC_CODE, PIN, EXPIRATION_DATE, ADDRESS_LINE_1, ADDRESS_LINE_2, CITY, STATE, COUNTRY)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """

            self._cur.execute(insert_query, (id, customer_id, payment_method, card_number, cvc_code, pin, expiration_date, address_line_1, address_line_2, city, state, country))

    def generate_reviews_table_data(self):
        for i in range(self._num_rows):
            id = i + 1
            self._cur.execute("SELECT id, title FROM product ORDER BY RANDOM() LIMIT 1")
            book_id, title = self._cur.fetchone()
            review = random.choice(["This is a great book.", "This book covers all the fundamentals.", "This book covers advanced topics well."])
            self._cur.execute("SELECT id, email FROM customer ORDER BY RANDOM() LIMIT 1")
            customer_id, email = self._cur.fetchone()

            insert_reviews_query = """
                INSERT INTO reviews (ID, BOOK_ID, TITLE, BOOK_REVIEW, CUSTOMER_ID)
                values (%s, %s, %s, %s, %s)
            """
            self._cur.execute(insert_reviews_query, (id, book_id, title, review, customer_id))


    def generate_promotional_price_table_data(self):
        for i in range(self._num_rows):
            id = i + 1
            product_id = i+1
            # price = round(random.uniform(10, 100), 2)
            discount_start_date = datetime.date(2023, random.randint(1, 12), random.randint(1, 28))
            discount_end_date = datetime.date(2024, random.randint(1, 12), random.randint(1, 28))
            discount_amount = round(random.uniform(0, 20), 2)

            insert_promotional_price_query = """
                INSERT INTO promotional_price (ID, PRODUCT_ID, DISCOUNT_START_DATE, DISCOUNT_END_DATE, DISCOUNT_AMOUNT)
                VALUES (%s, %s, %s, %s, %s);
            """

            self._cur.execute(insert_promotional_price_query, (id, product_id, discount_start_date, discount_end_date, discount_amount))


    def generate_orders_data(self):
        for i in range(self._num_rows):
            order_id = i + 1
            order_date = datetime.date(2023, random.randint(1, 12), random.randint(1, 28))
            order_status = random.choice(["Order_Placed", "Order_Fulfilled", "Order_Cancelled", "Return_Requested", "Returned"])
            quantity = random.randint(1, 10)
            self._cur.execute("SELECT ID, email FROM customer ORDER BY RANDOM() LIMIT 1")
            id, email = self._cur.fetchone()
            customer_id = id
            # print("Customer ID is ", id)
            # print("Customer Email is ", email)
            # result = cur.fetchall()
            # if result:
            #     customer_id = result[0]
            #     print("customer id is ", customer_id)

            # Select product_id and price based on a random product_id
            self._cur.execute("SELECT ID, PRICE FROM product ORDER BY RANDOM() LIMIT 1")
            product_id, price = self._cur.fetchone()
            # print(product_id)
            # print(price)

            # Select payment_method and credit_card_number based on customer_id
            # print(self._cur.mogrify("SELECT PAYMENT_METHOD, CARD_NUMBER FROM payment WHERE CUSTOMER_ID = %s", (customer_id,)))
            self._cur.execute("SELECT PAYMENT_METHOD, CARD_NUMBER FROM payment WHERE CUSTOMER_ID = %s", (customer_id,))
            payment_method, card_number = self._cur.fetchone()
            # print(payment_method, card_number)

            insert_order_query = """
                INSERT INTO orders (ID, ORDER_DATE, ORDER_STATUS, PRODUCT_ID, QUANTITY, PRICE, CUSTOMER_ID, PAYMENT_METHOD, CARD_NUMBER)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """

            self._cur.execute(insert_order_query, (order_id, order_date, order_status, product_id, quantity, price, customer_id, payment_method, card_number))


    def generate_ordered_item_table(self):
        for i in range(self._num_rows):
            self._cur.execute("SELECT ID, ORDER_DATE FROM orders ORDER BY RANDOM() LIMIT 1")
            order_id, order_date = self._cur.fetchone()
            self._cur.execute("SELECT ID, TITLE FROM product ORDER BY RANDOM() LIMIT 1")
            book_id, title = self._cur.fetchone()

            insert_ordered_item_query = """
                INSERT INTO ORDERED_ITEM (ORDER_ID, BOOK_ID, TITLE)
                VALUES (%s, %s, %s)
                """
            self._cur.execute(insert_ordered_item_query , (order_id, book_id, title))

    def find_similar_products(self, df, title, category):
        """
        Finds similar products based on title similarity.

        Args:
            df: Pandas DataFrame containing product information.
            title: The title of the product to find similar products for.
            top_n: The number of top similar products to return.

        Returns:
            A list of similar product IDs.
        """
        print("starting search")

        df['similarity'] = df['title'].str.contains(title, case=False) & (df['category'] == category)
        print("Number of Similar title books are: ", df['similarity'].sum())
        similar_products = df[df['similarity']].sort_values('similarity', ascending=False)
        return similar_products


    # def populate_similar_books(self):
    #     for i in range(self._num_rows):
    #         self._cur.execute("SELECT book_id, recommended_book_id FROM similar_books_population();")
    #         book_id, similar_book_id = self._cur.fetchone()
    #         # print(book_id, similar_book_id)
    #
    #         insert_similar_books_query = """
    #             INSERT INTO SIMILAR_BOOKS (BOOK_ID, SIMILAR_BOOK_ID)
    #             VALUES (%s, %s)
    #             """
    #         try:
    #             self._cur.execute(insert_similar_books_query, (book_id, similar_book_id))
    #         except Exception as e:
    #             print("Error in populating similar books table: ", e)


    def populate_similar_books(self):
        # Fetch all similar book pairs
        self._cur.execute("SELECT book_id, recommended_book_id FROM similar_books_population();")
        similar_books = self._cur.fetchall()

        for book_id, similar_book_id in similar_books:
            # Debugging print statement
            print(book_id, similar_book_id)

            # Insert each pair into SIMILAR_BOOKS
            insert_similar_books_query = """
                INSERT INTO SIMILAR_BOOKS (BOOK_ID, SIMILAR_BOOK_ID)
                VALUES (%s, %s)
            """
            try:
                self._cur.execute(insert_similar_books_query, (book_id, similar_book_id))
            except Exception as e:
                print("Error in populating similar books table: ", e)

        # Commit the transaction
        self._conn.commit()



