from bookstore_db_app.Bookstore import Bookstore

class recommend_books(Bookstore):
    def __init__(self):
        """Constructor to initialize an empty queue."""
        super().__init__()

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