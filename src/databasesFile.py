from database_utility import SQLite

main_database_path = "bookstore.db"
main_database_conection = SQLite(main_database_path)
main_database_conection.open()
