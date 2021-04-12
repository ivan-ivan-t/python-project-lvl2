from gendiff.formats.make_sorted import sorted_diff


PROP = 'Property \'{}\''
UPD = PROP + ' was updated. From {} to {}'
ADD = PROP + ' was added with value: {}'
REM = PROP + ' was removed'


def set_value(value):
    if type(value) is dict:
        return '[complex value]'
    if type(value) is bool:
        return str(value).lower()
    if value is None:
        return 'null'
    if type(value) is int:
        return value
    else:
        return '{}{}{}'.format('\'', value, '\'')


def make_path(path, keys):
    if path == '':
        return keys
    return path + '.' + keys


def plain(diff):

    def inner(diff, path=''):
        diff = sorted_diff(diff)
        result = ''
        for k, values in diff.items():
            if k[:1] == '-' and '+' + k[1:] not in diff:
                result += REM.format(make_path(path, k[2:])) + '\n'
            if k[:1] == '+':
                if '-' + k[1:] in diff:
                    result += UPD.format(
                        make_path(path, k[2:]),
                        set_value(diff['-' + k[1:]]),
                        set_value(diff['+' + k[1:]])
                    ) + '\n'
                if '-' + k[1:] not in diff:
                    result += ADD.format(
                        make_path(path, k[2:]), set_value(diff[k])
                    ) + '\n'
            if type(values) is dict:
                result += inner(values, make_path(path, k[2:]))
        return result
    return inner(diff)[:-1]
