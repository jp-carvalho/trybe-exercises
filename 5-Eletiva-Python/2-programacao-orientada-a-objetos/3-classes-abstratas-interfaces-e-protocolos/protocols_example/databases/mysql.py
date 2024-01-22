class MySQLConnection:
    def execute(self, query: str) -> list[str]:
        return [f"MySQL executou a query '{query}'"]


class MySQLDatabase:
    def connection(self, connection_url: str) -> MySQLConnection:
        if connection_url == "":
            raise ValueError("Invalid connection")

        return MySQLConnection()
