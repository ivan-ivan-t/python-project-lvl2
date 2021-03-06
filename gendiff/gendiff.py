import json


def generate_diff(first, second):

    result = ''
    pre_result = []
    first = json.load(open(first))
    second = json.load(open(second))

    for k, v in first.items():
        if k not in second:
            pre_result.append(' - {0}: {1}'.format(k, v))
        elif k in second and v == second[k]:
            pre_result.append('   {0}: {1}'.format(k, v))
        elif k in second and v != second[k]:
            pre_result.append(' - {0}: {1}\n + {2}: {3}'.format(k, v, k, second[k]))
    for k, v in second.items():
        if k not in first:
            pre_result.append(' + {0}: {1}'.format(k, v))

    for i in sorted(pre_result, key=lambda x: x[3]):
        result += '{}\n'.format(i)

    return '{\n' + result + '}'
