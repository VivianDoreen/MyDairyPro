from psycopg2 import connect



class DatabaseConnection():

    def __init__(self):
        """
        This constructor creates a connection to the database
        """

        #     #When on travis

        # self.connection = connect("dbname=mydiary_pro user =postgres password='' host=localhost port=5432")
        # self.connection.autocommit = True
        # self.cursor = self.connection.cursor()

            #----------------------------------------------


        #     #When on heroku

        self.connection = connect("dbname=dfnomosplgge6f "
                                  "user =stfdetvvfeyjox "
                                  "password=91a11a6231f8c068e0ddb3aa1db4a61bfe4eee3d8db2538f4708b1755eb317d8"

                                  " host=ec2-54-243-61-173.compute-1.amazonaws.com"

                                  "port=5432")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

            #----------------------------------------------

    def create_tables(self):
        """ This method creates all tables"""
        create_table_query_for_entries = (""" CREATE TABLE IF NOT EXISTS 
                                      entries(diary_id SERIAL PRIMARY KEY,
                                      name VARCHAR (50) NOT NULL, 
                                      description VARCHAR (50) NOT NULL ,
                                       user_id INTEGER NOT NULL, 
                                       date_created TIMESTAMP, 
                                       date_modified TIMESTAMP, 
                                       FOREIGN KEY (user_id)REFERENCES 
                                       users (user_id));""")

        create_table_query_for_users = ("""CREATE TABLE IF NOT EXISTS 
                    users(user_id SERIAL PRIMARY KEY,  
                    name VARCHAR(50) NOT NULL , email VARCHAR (20) NOT NULL,
                     password VARCHAR(20) NOT NULL); """
                                        )

        # Execute creating tables
        self.cursor.execute(create_table_query_for_users)
        self.cursor.execute(create_table_query_for_entries)


    def drop_table(self, table_name):
        """
        This method truncates a table
        :param table_name: 
        :return: 
        """
        self.cursor.execute("TRUNCATE TABLE {} RESTART IDENTITY CASCADE"
                            .format(table_name))
