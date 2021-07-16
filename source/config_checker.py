import json
import re
from functools import partial


# good
def load_config(config_file):
    file_obj = open(config_file, 'r+')
    return json.load(file_obj)


# good
def require(config_file, network_config):
    tasks = config_file['require']
    config = network_config
    lol_random_int = 1
    for items in tasks:
        config['commands'][str('config'+str(lol_random_int))] = list(items)
        lol_random_int += 1
    return config


# good
def replace(config_file, network_config):
    tasks = config_file['replace']
    commands_to_parse = network_config['commands']
    keys = commands_to_parse.keys()
    for strings in tasks.keys():
        for i in keys:
            commands_to_parse[i] = commands_to_parse[i].replace(strings, str(tasks[strings]))
    network_config['commands'] = commands_to_parse
    return network_config


# good
def reject(config_file, network_config):
    tasks = config_file['reject']
    commands_to_parse = network_config['commands']
    for strings in tasks:
        for command in commands_to_parse.values():
            if re.match(strings, str.join('', command)) is not None:
                return 'REJECT'
    return network_config


# good
def check(config_file, network_config):
    ci_config = config_file
    require_partial = partial(require, config_file=ci_config)
    replace_partial = partial(replace, config_file=ci_config)
    reject_partial = partial(reject, config_file=ci_config)
    return reject_partial(network_config=replace_partial(network_config=require_partial(network_config=network_config)))


if __name__ == '__main__':
    check('CIConfig.json', 'deploy_config.json')
