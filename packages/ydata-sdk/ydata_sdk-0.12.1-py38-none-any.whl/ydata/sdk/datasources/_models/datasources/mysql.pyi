from ydata.sdk.datasources._models.datasource import DataSource

class MySQLDataSource(DataSource):
    query: str
    def to_payload(self) -> None: ...
    def __init__(self, query) -> None: ...
