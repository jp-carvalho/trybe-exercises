class PostgresConnection:
    def execute(self, query: str) -> list[str]:
        return [
            f"Postgres executou a query '{query}'",
            "e retornou mais uma string adicional",
        ]


class PostgresDatabase:
    def connection(self, connection_url: str = "123") -> PostgresConnection:
        if connection_url == "123":
            raise ValueError("invalid connection")
        return PostgresConnection()
