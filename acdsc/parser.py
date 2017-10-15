#!/usr/bin/python3

import configparser


class ACParser(configparser.ConfigParser):

    optionxform = str

    def prefix_sections(self, prefix):
        def startswith_prefix(value):
            return value.startswith('{}_'.format(prefix))

        return sorted(filter(startswith_prefix, self.sections()),
                      key=numeric_sort)

    def write(self, fp):
        for section in self._sections:
            fp.write('[{}]\n'.format(section))
            for (key, value) in self._sections[section].items():
                if key == '__name__':
                    continue
                if (value is not None) or (self._optcre == self.OPTCRE):
                    key = '='.join((key, str(value).replace('\n', '\n\t')))
                fp.write('{}\n'.format(key))
            fp.write('\n')


def convert_key(key):
    return key.upper().replace('-', '_')


def convert_ini_key(ini_key):
    return ini_key.lower().replace('_', '-')


def to_ini(kv):
    key, value = kv
    if value is not None:
        if isinstance(value, str):
            return (convert_key(key), value.encode('utf-8'))
        return (convert_key(key), '{}'.format(value))
    return (convert_key(key), value)


def make_ac_parser(config_file):
    parser = ACParser()
    parser.read(config_file)
    return parser


def numeric_sort(a):
    return int(a.split('_')[-1])


def get_next_section(section, sections):
    return '{}_{}'.format(
        section,
        int(sorted(sections, key=numeric_sort)[-1].split('_')[-1]) + 1)
