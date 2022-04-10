import ssl
from ldap3 import Connection, Server, ServerPool, SAFE_RESTARTABLE, Tls
from loggers.Logger import Logger
import time
import json


class LdapConnector:
    def __init__(self, config):
        self._logger = Logger.get_logger(self.__class__.__name__)
        self.servers = ServerPool()
        for server in config['servers']:
            self.servers.add(Server(server['hostname'],
                                    tls=Tls(validate=ssl.CERT_NONE)))

        self.enableTLS = False
        if config['start_tls'] == 'true':
            self.enableTLS = True

        self.user = config['username']
        self.password = config['password']
        self.conn = Connection(server=self.servers, auto_bind=False,
                               user=self.user, password=self.password,
                               version=3, client_strategy=SAFE_RESTARTABLE,
                               read_only=True)
        if not self.conn:
            raise Exception("Unable to connect to the Perun LDAP,")

        hostname = self.servers.get_current_server(self.conn)
        # enable TLS if required
        if self.enableTLS and not str(hostname).startswith("ldaps:"):
            if not self.conn.start_tls():
                raise Exception('Unable to force STARTTLS on Perun LDAP')

    def search_for_entity(self, base, filters,
                          attr_names=None):
        entries = self._search(base, filters, attr_names)
        if not entries:
            self._logger.debug(f"ldap_connector.search_for_entity "
                               f"- No entity found. Returning \'None\'. "
                               f"query base: {base} "
                               f", filter: {filters} ")
            return None

        if len(entries) > 1:
            raise Exception(f"ldap_connector.search_for_entity - "
                            f"More than one entity found. query base:"
                            f"{base}, filter: {filters}. Hint: Use "
                            f"method search_for_entities if you expect "
                            f"array of entities.")

        return entries[0]

    def search_for_entities(self, base, filters,
                            attr_names=None):
        entries = self._search(base, filters, attr_names)

        if not entries:
            self._logger.debug(f"ldap_connector.search_for_entities - "
                               f"No entities found. Returning empty "
                               f"array. query base: {base} "
                               f"filter: {filters} ")

            return entries

        return entries

    def _search(self, base, filters, attributes=None):
        hostname = self.servers.get_current_server(self.conn)
        if not self.conn.bind():
            raise Exception('Unable to bind user to the Perun LDAP,' +
                            hostname)
        self._logger.debug(f"ldap_connector.search - Connection "
                           f"to Perun LDAP established. Ready to "
                           f"perform search query. host: "
                           f"{hostname}, user: {self.user}")

        start_time = time.time()
        status, result, response, _ = \
            self.conn.search(search_base=base, search_filter=filters,
                             attributes=attributes)
        end_time = time.time()

        response_time = round(end_time - start_time, 3)
        if not response:
            return []

        entries = self._get_simplified_entries(response)

        self.conn.unbind()

        self._logger.debug(f"ldap_connector.search - search query "
                           f"proceeded in {str(response_time)}"
                           f"ms. Query base: {base}, filter: "
                           f"{filters}, response: ' "
                           f"{json.dumps(str(entries))}")

        return entries

    @staticmethod
    def _get_simplified_entries(result):

        entries = []
        for entry in result:
            entries.append(entry['attributes'])

        return entries
