import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=drinkshop-sqlserver.database.windows.net,1433;"
    "DATABASE=DrinkShopDB;"
    "UID=drinkshopadmin;"
    "PWD=DrinkShop2025;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

print("OK! SQL Server connected.")