import re


def file_reader(file_object):
    with open(file_object, 'r+') as file:
        return file.readlines()


def return_succeeding_lines(pattern, file_line_object):
    compiled_pattern = re.compile(pattern)
    return list(map(lambda x: compiled_pattern.match(x), file_line_object))


def strip_characters(keywords_to_remove, file_line_object):
    def replace_text(keywords_to_remove_inner, file_line):
        line = str(file_line)
        for keywords in keywords_to_remove_inner:
            line.replace(keywords, line)
        return line
    listy = list()
    for i in file_line_object:
        listy.append(replace_text(keywords_to_remove, i))
    return listy


def create_json_string(file_line_object):
    yay_formatted_list = list()
    for i in file_line_object:
        yay_formatted_list.append(str.join('', ('"', i[0], '"', ': [', str.join(',', i[1:]), ']')))
    final_string = str('{' + str.join(',', yay_formatted_list) + '}')
    return final_string


def dump_string_to_file(text, file_object):
    with open(file_object, 'w+') as file:
        file.write(text)
    return file_object


def main(python_file):
    python_file_object = file_reader(python_file)
    pattern_string = '.*def.*'
    parsed_lines = return_succeeding_lines(pattern_string, python_file_object)
    keywords = ['def', '(', ',', ')', ':', '  ']
    characters_stripped = strip_characters(keywords, parsed_lines)
    json_str_thing = create_json_string(characters_stripped)
    return dump_string_to_file(json_str_thing, python_file)
