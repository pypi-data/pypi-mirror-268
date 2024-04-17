import logging
from enum import Enum

from influxdb import InfluxDBClient, DataFrameClient
from onepasswordconnectsdk.models import Item

from .secretmanagerbase import SecretManagerBase, SecretMetadata


class InfluxPrivilege(Enum):
    READ = 0
    WRITE = 1  # Influx does not allow read for this permission
    ALL = 2
    ADMIN = 3


class InfluxSecretItem(SecretMetadata):
    def __init__(self, server: str, port, username: str, password: str, Environment: str, database: str = None,
                 **kwargs):
        self.server = server
        self.port = int(port)
        self.username = username
        self.password = password
        self.environment = Environment
        self.database = database
        self.privilege = InfluxPrivilege[kwargs['database permission']]

    def metadata(self):
        md = dict(self.__dict__)
        del md['password']
        return md


class InfluxFactory(SecretManagerBase[InfluxSecretItem]):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__class__.__name__)

    def tag_filter(self):
        return 'DB/InfluxDB'

    def process_item(self, item: Item):
        metadata = {}
        for field in item.fields:
            if field.value is not None:
                metadata[field.label] = field.value
        return InfluxSecretItem(**metadata)

    def create_influx_client(self, database, privilege: InfluxPrivilege) -> InfluxDBClient:
        return self.__create_client(database, privilege, InfluxDBClient)

    def create_df_client(self, database, privilege: InfluxPrivilege) -> DataFrameClient:
        return self.__create_client(database, privilege, DataFrameClient)

    def __create_client(self, database, privilege: InfluxPrivilege, influx_type):
        item = self.find_item(database, privilege)
        if item:
            self.logger.info(f'Creating {influx_type.__name__} for database={item.database}...')
            return self.make_client(influx_type, item)

    @staticmethod
    def make_client(influx_type, item: InfluxSecretItem):
        return influx_type(host=item.server, port=item.port,
                           username=item.username, password=item.password,
                           database=item.database)

    def find_item(self, database, privilege: InfluxPrivilege) -> InfluxSecretItem:
        items = self.find(database=database)
        items.sort(key=lambda i: i.privilege.value, reverse=False)
        for item in items:
            if item.privilege.value >= privilege.value:
                return item
