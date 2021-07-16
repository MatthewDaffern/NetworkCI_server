config = dict()
config['example'] = dict()
config['test'] = dict()
config['nested-config'] = dict()

config['nested-config']['test1'] = 1
config['nested-config']['test2'] = 2
config['nested-config']['test3'] = 3

print(config)


from json import dumps

print(dumps(config))