import time
import hashlib
import pathlib
import json
import deployer
import config_checker
from functools import partial


# good
def snooze(minutes):
    return time.sleep(minutes*60)


# good
def get_hash(string_object):
    file = bytes(string_object)
    hash_result = hashlib.sha3_256(file)
    return hash_result.hexdigest()


# good
def get_files(path_object):
    file_path = pathlib.Path(path_object)
    return list(file_path.iterdir())


# good
def get_string_of_file(file_name):
    file = open(file_name, 'r+')
    string = str(file.read())
    return string


# good
def get_hash_of_list(file_list):
    result = dict()
    for i in file_list:
        result[i] = get_hash(get_hash_of_list(i))
    return result


# good
def dump_to_json(file_name, dump_object):
    file = open(file_name, 'w+')
    json.dump(dump_object, file)
    file.close()
    return dump_object


# good
def load_from_json(file_name):
    file = open(file_name, 'r+')
    json_config = json.load(file)
    return json_config


# good
def run_check(config, ci_config):
    repo_checker_partial = partial(config_checker.check, config_file=ci_config)
    result = list()
    for i in config.keys():
        if get_hash(get_string_of_file(i)) is not config[i]:
            if repo_checker_partial(network_config=i) is not 'REJECT':
                string = 'configuring using ' + str(i)
                print(string)
                result.append(string)
                result.append(deployer.main(i))
    return result


# good
def quick_hash(string):
    hashy_hash = hashlib.sha3_256(str.encode(string))
    return hashy_hash.hexdigest()


# good
def main(daemon_config):
    result = list()
    daemon = daemon_config
    hashtrack_file_location = daemon['hashtrack_file_location']
    if not pathlib.Path(hashtrack_file_location).exists():
        string_files = list(map(lambda x: str(x), pathlib.Path(daemon['ciconfig_file_path']).iterdir()))
        hash_track = open(hashtrack_file_location, 'w+')
        hash_track_object = list()
        for i in string_files:
            file = open(i, 'r+')
            hash_object = quick_hash(file.read())
            hash_track_object.append([i, hash_object])
        json.dump(hash_track_object, hash_track)
        hash_track.close()
        ciconfig_file = open('CIConfig_file_location', 'r+')
        ciconfig = json.load(ciconfig_file)
        hash_track_config = open(hashtrack_file_location, 'r+')
        for i in hash_track_config:
            hash_dis = open(i[0], 'r+')
            current_hash_state = quick_hash(hash_dis.read())
            if current_hash_state is not i[1]:
                checker_partial = partial(config_checker.check, config_file=ciconfig)
                result.append(deployer.main(checker_partial(network_config=deployer.import_connection_settings(i[0]))))

    else:
        ciconfig_file = open('CIConfig_file_location', 'r+')
        ciconfig = json.load(ciconfig_file)
        hash_track_config = open(hashtrack_file_location, 'r+')
        for i in hash_track_config:
            hash_dis = open(i[0], 'r+')
            current_hash_state = quick_hash(hash_dis.read())
            if current_hash_state is not i[1]:
                checker_partial = partial(config_checker.check, config_file=ciconfig)
                result.append(deployer.main(checker_partial(network_config=deployer.import_connection_settings(i[0]))))
    return result


# good
def loop(function):
    while True:
        function


# good
if __name__ == '__main__':
    loop(main('daemon.json'))
