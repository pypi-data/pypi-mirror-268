"""Module providing a function that connecting to Peaka."""
from trino.dbapi import connect


def connect_to_peaka(api_key, catalog=None, schema=None, timezone=None):
    """
    Function to connect to Peaka database.

    Args:
    - api_key (str): The API key required for authentication.
    - catalog (str): Optional. The catalog to connect to.
    - schema (str): Optional. The schema to connect to.
    - timezone (str): Optional. The timezone for the connection.

    Returns:
    - Connection object: Connection object to the Peaka database.
    """

    # Setting up connection arguments
    args = {
        "host": "dbc.peaka.studio",
        "port": 4567,
        "http_scheme": "HTTPS",
        "extra_credential": [("peakaKey", api_key)],
        "catalog": catalog,
        "schema": schema,
        "timezone": timezone
    }

    # Establishing connection using trino.dbapi.connect function
    connection = connect(**args)

    # Returning the connection object
    return connection
