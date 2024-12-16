--alter table ordered_item drop constraint ordered_item_order_id_fkey CASCADE;
--alter table product drop constraint orders_product_id_fkey CASCADE;
--alter table product drop constraint ordered_item_book_id_fkey CASCADE;



--create database d100;

--drop table if exists product;
create table if not exists product (
ID NUMERIC PRIMARY KEY,
ISBN VARCHAR(50),
TITLE VARCHAR(200),
CATEGORY VARCHAR(100),
DESCRIPTION TEXT, -- language
LANGUAGE VARCHAR(50),
PRICE DECIMAL(10,2), --(Postgres has money datatype that can be cast as numeric without loss)
--REVIEW VARCHAR(2000),
--SIMILAR_PRODUCT INTEGER [],
UNIQUE(ID)
)
;

----drop table promotional_price;
create table if not exists promotional_price (
ID NUMERIC,
PRODUCT_ID NUMERIC references product(ID),
DISCOUNT_START_DATE DATE,
DISCOUNT_END_DATE DATE,
DISCOUNT_AMOUNT NUMERIC,
primary key (ID)
)
;
--
----drop table customer;
create table if not exists customer (
ID NUMERIC primary key,
FIRST_NAME VARCHAR(200),
LAST_NAME VARCHAR(200),
EMAIL VARCHAR(200),
ADDRESS_LINE_1 VARCHAR(200),
ADDRESS_LINE_2 VARCHAR(200),
CITY VARCHAR(200),
STATE VARCHAR(100),
COUNTRY VARCHAR(100),
UNIQUE(ID)
)
;
--
----drop table payment;
create table if not exists payment (
ID NUMERIC,
CUSTOMER_ID NUMERIC references customer(ID),
PAYMENT_METHOD VARCHAR(100), -- can be "credit card, debit card"
CARD_NUMBER VARCHAR(19),
CVC_CODE NUMERIC,
PIN NUMERIC,
EXPIRATION_DATE DATE,
ADDRESS_LINE_1 VARCHAR(200),
ADDRESS_LINE_2 VARCHAR(200),
CITY VARCHAR(200),
STATE VARCHAR(100),
COUNTRY VARCHAR(100),
primary key (ID)
)
;
--
----drop table similar_books;
create table if not exists similar_books (
BOOK_ID NUMERIC references product(ID), --book_id field value can repeat in many rows
SIMILAR_BOOK_ID NUMERIC references product(ID)
)
;
----
----drop table reviews;
create table if not exists reviews (
ID NUMERIC,
BOOK_ID NUMERIC references product(ID),
TITLE VARCHAR(200) ,
BOOK_REVIEW TEXT,
CUSTOMER_ID NUMERIC references customer(ID),
PRIMARY KEY (ID)
)
;
--
----drop table orders;
create table if not exists orders (
ID NUMERIC PRIMARY KEY,
ORDER_DATE DATE,
ORDER_STATUS VARCHAR(100), -- example values "Order_Placed, Order_Fulfilled, Order_Cancelled, Return_Requested, Returned"
PRODUCT_ID NUMERIC references product(ID),
QUANTITY NUMERIC,
PRICE DECIMAL(10,2),
CUSTOMER_ID NUMERIC references customer(ID),
PAYMENT_METHOD VARCHAR(100),
CARD_NUMBER VARCHAR(19),
UNIQUE(ID)
)
--partition by range (ORDER_DATE)
;
--
----drop table ordered_item;
create table if not exists ordered_item (
ORDER_ID NUMERIC references orders(ID),
--ORDER_DATE DATE references orders(ORDER_DATE),
BOOK_ID NUMERIC references product(ID),
TITLE VARCHAR(200)
)
;
--
----drop function similar_books_population();
CREATE OR REPLACE FUNCTION similar_books_population()
RETURNS TABLE (book_id NUMERIC, recommended_book_id NUMERIC) AS $$
    SELECT
    a.id as book_id,
    b.id AS recommended_book_id
  FROM
    product a
    inner join product b on a.category = b.category and a.id != b.id
  WHERE
    a.language = b.language
  --LIMIT 5;
$$ LANGUAGE sql;

