from ldap3 import Connection, Server
from logging import debug
import time
import json
from typing import List, Any, Optional, Dict


class LdapConnector:
    def __init__(self, config):
        # TODO change config <list> to config <file>
        # IGNORE THIS CONSTRUCTOR, IT IS NOT YET IMPLEMENTED
        # CORRECTLY (CONFIG FILE IS MISSING)
        self.hostname = config[0]
        self.user = config[1]
        self.password = config[2]
        self.enableTLS = config[3]

    def search_for_entity(self, base: str, filters: str,
                          attr_names: Optional[List[Any]] = None) \
            -> Optional[Dict[Any]]:
        entries = self._search(base, filters, attr_names)

        if not entries:
            debug('sspmod_perun_LdapConnector.search_for_entity '
                  '- No entity found. Returning \'None\'. ',
                  'query base: ', base, ', filter: ', filters, '"')

            return None

        if len(entries) > 1:
            raise Exception('sspmod_perun_LdapConnector.search_for_entity - '
                            'More than one entity found.', 'query base:',
                            base, ', filter:', filters, '.', 'Hint: Use '
                            'method ''search_for_entities if you expect '
                            'array of entities.')

        return entries[0]

    def search_for_entities(self, base: str, filters: str,
                            attr_names: Optional[List[Any]] = None) \
            -> Optional[List[Dict[Any]]]:
        entries = self._search(base, filters, attr_names)

        if not entries:
            debug('LdapConnector.search_for_entities - '
                  'No entities found. Returning empty array. ',
                  'query base: ', base, ', filter: ', filters, '"')

            return entries

        return entries

    def _search(self, base: str, filters: str, attributes:
                Optional[List[Any]] = None) -> Optional[List[Dict[Any]]]:
        conn = Connection(server=Server(self.hostname), auto_bind=False,
                          user=self.user, password=self.password, version=3)
        if not conn:
            raise Exception("Unable to connect to the Perun LDAP,",
                            self.hostname)

        # enable TLS if required
        if self.enableTLS and not self.hostname.startswith("ldaps:"):
            if not conn.start_tls():
                raise Exception('Unable to force STARTTLS on Perun LDAP')

        if not conn.bind():
            raise Exception('Unable to bind user to the Perun LDAP,',
                            self.hostname)

        debug('LdapConnector.search - Connection '
              'to Perun LDAP established. Ready to '
              'perform search query. host: ',
              self.hostname, ', user: ', self.user)

        start_time = time.time()
        conn.search(search_base=base, search_filter=filters,
                    attributes=attributes)
        end_time = time.time()

        response_time = round(end_time - start_time, 3)
        result = conn.response

        if not conn.response:
            return []

        entries = self.__get_simplified_entries(result)

        conn.unbind()

        debug('sspmod_perun_LdapConnector.search - search query proceeded in ',
              response_time, 'ms. ', 'Query base: ', base, ', filter: ',
              filters, ', response: ', json.dumps(entries))

        return entries

    @staticmethod
    def __get_simplified_entries(result: List[Dict[Any]]) -> List[Dict[Any]]:
        entries = []
        for entry in result:
            new_entry = dict()
            for attr in entry:
                values = entry[attr]

                del values['count']

                new_entry[attr] = values

            entries.append(new_entry)

        return entries
