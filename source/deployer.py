from json import load
import netmiko


# good
def import_connection_settings(file_name):
    """loads the JSON"""
    with open(file_name, 'r+') as config:
        result = load(config)
    return result


# yada yada
def process_connection(config):
    """Creates the NetMiko Connect object and adds it to the dictionary"""
    config['connection'] = netmiko.ConnectHandler(**config['config'])
    return config


# good
def process_commands(config_and_connection_object):
    """goes into config mode and configures each command. Inefficient because it configs and exits for each section."""
    config_and_connection_object['result'] = list()
    for i in config_and_connection_object['commands']:
        print(i)
        output = config_and_connection_object['connection'].send_config_set(config_and_connection_object['commands'][i])
        print(output)
        config_and_connection_object['result'].append(output)
    return config_and_connection_object


# good
def save_action(config_and_connection_object):
    """Found that I had forgotten to save the config each time.
    This enables me to separately address each device's save functionality as part of the config."""
    output = config_and_connection_object['connection'].\
        send_command_timing(config_and_connection_object['save']['save_command'])
    if config_and_connection_object['save']['search_string'] in output:
        config_and_connection_object['connection'].\
            send_command_timing(config_and_connection_object['save']['response_character'])
    return config_and_connection_object


# good
def print_result(config_connection_and_result_object):
    """loggy log log logersson."""
    file_name = 'result.txt'
    file = open(file_name, 'a+')
    for i in config_connection_and_result_object['result']:
        print(i)
        file.write(i)
    file.close()
    print('\n\n\n Your config result is in result.txt')
    return config_connection_and_result_object


# good
def main(config_object):
    """ void main(string[], args)"""
    return print_result(
            save_action(
             process_commands(
                 process_connection(
                     import_connection_settings(config_object)))))


# good
if __name__ == '__main__':
    main('deploy_config.json')
