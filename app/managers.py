import sqlite3

from models import Actors


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?);",
            (first_name, last_name)
        )

    def all(self) -> list[Actors]:
        cinema_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name};"
        )

        return [Actors(*row) for row in cinema_cursor]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, last_name = ? WHERE id = ?;",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?;",
            (id_to_delete,)
        )
        self._connection.commit()
