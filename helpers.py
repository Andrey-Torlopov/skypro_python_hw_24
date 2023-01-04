import re
from typing import Iterable

def read_file_generator(filepath: str) -> Iterable:
    with open(filepath, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line.strip('\n')


def filter_query(param: str, data: Iterable) -> Iterable:
    return list(filter(lambda row: param in row, data))


def map_query(param: str, data: Iterable) -> Iterable:
    try:
        col = int(param)
    except ValueError:
        return []
    try:
        return list(map(lambda row: row.split(' ')[col], data))
    except IndexError:
        return []


def unique_query(data: Iterable,
                 *args: str,
                 **kwargs: dict[str, str]) -> Iterable:
    return list(set(data))


def sort_query(param: str, data: Iterable) -> Iterable:
    if param == "asc":
        return sorted(data)
    elif param == "desc":
        return sorted(data, reverse=True)
    else:
        return data


def limit_query(param: str, data: Iterable) -> Iterable:
    try:
        limit = int(param)
    except ValueError:
        return data
    
    return list(data)[:limit]


def regexp_query(param: str, data: Iterable) -> Iterable:
    result = []
    for item in data:
        regexp = re.compile(param)
        res = regexp.search(item)
        if res:
            result.append(item)
    return result
