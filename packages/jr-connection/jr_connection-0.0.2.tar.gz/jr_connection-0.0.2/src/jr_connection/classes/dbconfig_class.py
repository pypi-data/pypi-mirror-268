# dbconfig_class.py

from dotenv import load_dotenv
import os


class DBConfig:
    load_dotenv("./.env")

    @staticmethod
    def load_credentials():
        return {
            "db_username": os.getenv("DB_USERNAME"),
            "db_password": os.getenv("DB_PASSWORD"),
            "db_host": os.getenv("DB_HOST"),
            "db_name": os.getenv("DB_DATABASE"),
            "db_driver": os.getenv("DB_DRIVER"),
        }
