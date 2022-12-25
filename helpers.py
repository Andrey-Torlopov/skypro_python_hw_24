import re

def read_file_generator(filepath: str):
    # TODO: Не понятно какой тип аннотации тут надо передать,
    # чтобы потом ничего не поломалось.
    with open(filepath, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line.strip('\n')


def filter_query(param: str, data: list[str]) -> list[str]:
    return list(filter(lambda row: param in row, data))


def map_query(param: str, data: list[str]) -> list[str]:
    try:
        col = int(param)
    except ValueError:
        return []
    try:
        return list(map(lambda row: row.split(' ')[col], data))
    except IndexError:
        return []


def unique_query(data: list[str],
                 *args: str,
                 **kwargs: dict[str, str]) -> list[str]:
    return list(set(data))


def sort_query(param: str, data: list[str]) -> list[str]:
    if param == "asc":
        return sorted(data)
    elif param == "desc":
        return sorted(data, reverse=True)
    else:
        return data


def limit_query(param: str, data: list[str]) -> list[str]:
    try:
        limit = int(param)
    except ValueError:
        return data

    return data[:limit]


def regexp_query(param: str, data: list[str]) -> list[str]:
    result = []
    for item in data:
        regexp = re.compile(param)
        res = regexp.search(item)
        if res:
            result.append(item)
    return result
