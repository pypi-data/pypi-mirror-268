from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


def gql_client(uri, headers=None):

    # Select your transport with a defined URL endpoint
    transport = AIOHTTPTransport(url=uri, headers=headers)

    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)
