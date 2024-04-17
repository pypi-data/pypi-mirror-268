import pandas as pd

from .config import init_config


class Table:
    def __init__(self, table_id: str, workspace_id: str, data: pd.DataFrame):
        self._config = init_config()
        self.table_id = table_id
        self.workspace_id = workspace_id
        self.data = data

    @property
    def client_url(self) -> str:
        return f"{self._config.CLIENT_URL}/app/tables/{self.table_id}?wid={self.workspace_id}"


__all__ = ["Table"]
