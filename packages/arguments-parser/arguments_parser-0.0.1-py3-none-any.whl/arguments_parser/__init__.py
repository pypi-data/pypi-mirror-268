__version__ = "0.0.1"
__author__ = 'Danny Vaca'

import sys
import json

class ArgumentsParser:
    DEBUG = True

    @staticmethod
    def debug(*a, **b):
        if ArgumentsParser.DEBUG:
            print(*a, **b)

    @staticmethod
    def parse():
        return ArgumentsParser._parse(sys.argv[1:])

    @staticmethod
    def _parse(arguments):
        #input('parsing: ' + str(arguments))
        last_key = None
        command = None
        flags = {}
        for index, key in enumerate(arguments):
            ArgumentsParser.debug('key', key)
            if last_key == None:
                ArgumentsParser.debug('\t', 'last_key == None')
                if key.startswith('--'):
                    ArgumentsParser.debug('\t', f'{key}.startswith(\'--\')')
                    if '=' in key:
                        ArgumentsParser.debug('\t', f'\'=\' in {key}')
                        key_value = key.split('=')
                        flags[key_value[0]] = key_value[1]
                    else:
                        ArgumentsParser.debug('\t', f'\'=\' not in {key}')
                        flags[key] = None
                        last_key = key
                else:
                    ArgumentsParser.debug('\t', f'not {key}.startswith(\'--\')')
                    if command != None:
                        subcommand = ArgumentsParser._parse(arguments[index:])
                        command = ArgumentsParser(command, flags, subcommand)
                        return command
                    command = key
            else:
                if key.startswith('--'):
                    ArgumentsParser.debug('\t', f'{key}.startswith(\'--\')')
                    flags[last_key] = None
                    if '=' in key:
                        ArgumentsParser.debug('\t', f'\'=\' in {key}')
                        key_value = key.split('=')
                        flags[key_value[0]] = key_value[1]
                        last_key = None
                    else:
                        ArgumentsParser.debug('\t', f'\'=\' not in {key}')
                        flags[key] = None
                        last_key = key
                else:
                    ArgumentsParser.debug('\t', f'not {key}.startswith(\'--\')')
                    flags[last_key] = key
                    last_key = None
            ArgumentsParser.debug('command', command, 'flags', flags)

        if command != None:
            return ArgumentsParser(command, flags, None)
    def __init__(self, command, flags, subcommand):
        self.command = command
        self.flags = flags
        self.subcommand = subcommand
    def json(self):
        return {'command': self.command, 'flags': self.flags, 'subcommand': None if self.subcommand is None else self.subcommand.json()}
    def __str__(self):
        return json.dumps(self.json(), indent=4)

if __name__ == '__main__':
    command = ArgumentsParser.parse()
    print('command')
    print(command)
