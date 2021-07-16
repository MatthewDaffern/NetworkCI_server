import re
from pathlib import Path
import sys


def file_path(path_str):
    pathway = Path(path_str)
    return pathway


def get_files(path_obj):
    directory = path_obj.iterdir()
    return list(map(lambda x: x.isfile(), directory))


def find_failure(file_obj, regex_list):
    file = open(file_obj, 'r+')
    lines = file.readlines()
    file.close()
    failure_list = list()
    for i in regex_list:
        for line in lines:
            result = re.match(i, line)
            if result is not None:
                failure_list.append(result)
    return failure_list


def turn_files_to_failures(file_list, regex_list):
    result = list()
    for i in file_list:
        print(i)
        result.extend(find_failure(i, regex_list))
    return result


if __name__ == '__main__':
    path_stuff = file_path(sys.argv[1])
    list_files = get_files(path_stuff)
    find_failures = turn_files_to_failures(list_files, sys.argv[2])
    print(find_failures)