# MySQL document reference: https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
import mysql.connector

# -------------------------------------------
# Dev database doesn't have SSL enabled,
# but production database has SSL.
# Common config will be load from config file
# -------------------------------------------
db_config = app_config.get("db")
# db_config = {
#     "user": "username",
#     "password": "my_pass",
#     "host": "1.1.1.1",
#     "database": "my-db",
# }

ssl_option = {
    "key": "/path/to/key.pem",
    "cert": "/path/to/cert.pem",
    "ca": "/path/to/ca.pem"
}

try:
    mysql.connector.connect(**db_config)
except mysql.connector.errors.ProgrammingError as exc:
    db_config.update(ssl_option)
    mysql.connector.connect(**db_config)
