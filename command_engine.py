from dataclasses import dataclass
from helpers import read_file_generator, filter_query, map_query
from helpers import sort_query, limit_query, unique_query, regexp_query
from typing import Iterable


@dataclass(slots=False)
class Command:
    name: str
    value: str


@dataclass
class CommandEnginge:
    commands: list[Command]
    filename: str
    _params: dict[str, str]

    def __init__(self, queries: dict[str, str]) -> None:
        self._params = queries
        self.commands = []

        result = self._prepeare_commands()
        if not result:
            self.commands = []

    def execute(self) -> Iterable:
        data = read_file_generator(f'data/{self.filename}')

        for item in self.commands:
            if item.name == 'filter':
                data = filter_query(item.value, data)
            if item.name == 'map':
                data = map_query(item.value, data)
            if item.name == 'unique':
                data = unique_query(data)
            if item.name == 'sort':
                data = sort_query(item.value, data)
            if item.name == 'limit':
                data = limit_query(item.value, data)
            if item.name == 'regexp':
                data = regexp_query(item.value, data)
        return list(data)

    # Private

    def _prepeare_commands(self) -> bool:
        self.filename = str(self._params.get('file_name'))

        if self.filename is None:
            return False

        cmd1 = self._params.get('cmd1')
        value1 = self._params.get('value1')

        cmd2 = self._params.get('cmd2')
        value2 = self._params.get('value2')

        if cmd1 and value1:
            self.commands.append(Command(cmd1, value1))

        if cmd2 and value2:
            self.commands.append(Command(cmd2, value2))

        return len(self.commands) > 0
