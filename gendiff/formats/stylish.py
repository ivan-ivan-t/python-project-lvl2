from gendiff.formats.make_sorted import sorted_diff


def set_value(value):
    if value is True or value is False:
        return str(value).lower()
    if value is None:
        return 'null'
    else:
        return value


def stylish(diff):

    def inner(diff, space=2):
        diff = sorted_diff(diff)
        spaces = ' ' * space
        result = '{'

        for key, value in diff.items():
            if type(value) is dict:
                result += '\n' + spaces + key + ': ' + inner(value, space + 4) + '\n' + spaces + '  }'
            else:
                result += '\n' + spaces + key + ': ' + str(set_value(value))
        return result
    return inner(diff) + '\n' + '}'
