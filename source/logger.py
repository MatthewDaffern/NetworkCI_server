import datetime


# good
def date_creator():
    date_list = list(datetime.datetime.now().timetuple())
    date = str.join('-', list(map(lambda x: str(x), (date_list[0], date_list[1], date_list[2]))))
    time = date_list[3] + date_list[4]
    return str.join('', (date, '----', str(time)))


# good
def ingestor(list_object, file_object):
    lines = list_object
    separator = '='*80
    date = date_creator()
    lines.append(separator)
    lines.append(date)
    lines.append(separator)
    file = open(file_object, 'a+')
    print(lines)
    file.writelines(list(map(lambda x: str(x), lines)))
    return lines
