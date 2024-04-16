import configparser

config = configparser.ConfigParser()

# Добавьте раздел и параметры
config['Section1'] = {
    'key1': 'value1',
    'key2': 'value2'
}

config['Section2'] = {
    'key3': 'value3',
    'key4': 'value4'
}

# Запишите файл .cfg
with open('setup.cfg', 'w') as configfile:
    config.write(configfile)
