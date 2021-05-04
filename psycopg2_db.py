import psycopg2


class DataBase:
    def __init__(self):
        self.connection = psycopg2.connect(user='xlgmlvqjrcynpu',
                                           password='70d6b2cd9485a4c80e791fcf1d1e37368a1983712599f7a3a302081c4c346444',
                                           host='ec2-34-252-251-16.eu-west-1.compute.amazonaws.com',
                                           port='5432',
                                           database='dfhh3u6n4e58v')
        self.cursor = self.connection.cursor()
        self.table = '''CREATE TABLE Users
                          (ID             INT       PRIMARY KEY   NOT NULL,
                          USER_ID         INT                NOT NULL,
                          NEWS_SUBSCRIPTION       BOOL,
                          CURRENCY_SUBSCRIPTION     BOOL); '''

    def add_new_user(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT ID FROM users")
            rows = self.cursor.fetchall()
            id_number = 1
            for row in rows:
                id_number += 1
            return self.cursor.execute(
                f"INSERT INTO users (ID, USER_ID, NEWS_SUBSCRIPTION, CURRENCY_SUBSCRIPTION) VALUES {(id_number, user_id, False, False)}")

    def get_news_subscribers(self, status):
        with self.connection:
            self.cursor.execute(
                f"SELECT * FROM Users WHERE NEWS_SUBSCRIPTION = {status}")
            return self.cursor.fetchall()

    def get_currency_subscribers(self, status):
        with self.connection:
            self.cursor.execute(
                f"SELECT * FROM Users WHERE CURRENCY_SUBSCRIPTION = {status}")
            return self.cursor.fetchall()

    def news_subscribe_unsubscribe(self, user_id, status):
        with self.connection:
            self.cursor.execute(
                f"UPDATE Users SET NEWS_SUBSCRIPTION = {status} WHERE USER_ID = {user_id}")

    def currency_subscribe_unsubscribe(self, user_id, status):
        with self.connection:
            self.cursor.execute(
                f"UPDATE Users SET CURRENCY_SUBSCRIPTION = {status} WHERE USER_ID = {user_id}")

    def check_news_subscribtion(self, user_id):
        self.cursor.execute(
            f'SELECT NEWS_SUBSCRIPTION FROM Users WHERE USER_ID = {user_id}')
        status = self.cursor.fetchone()
        print(status)
        return status

    def check_currency_subscribtion(self, user_id):
        self.cursor.execute(
            f'SELECT CURRENCY_SUBSCRIPTION FROM Users WHERE USER_ID = {user_id}')
        status = self.cursor.fetchone()
        print(status)
        return status

    def print_users(self):
        self.cursor.execute("SELECT * FROM Users")
        rows = self.cursor.fetchall()
        for row in rows:
            print("ID", row[0])
            print("USER_ID", row[1])
            print("NEWS_SUBSCRIPTION", row[2])
            print("CURRENCY_SUBSCRIPTION", row[3])

    def check_user_existion(self, user_id):
        with self.connection:
            self.cursor.execute(
                f"SELECT * FROM Users WHERE USER_ID = {user_id}")
            res = self.cursor.fetchall()
            return bool(len(res))

    def close(self):
        self.connection.close()


db = DataBase()
