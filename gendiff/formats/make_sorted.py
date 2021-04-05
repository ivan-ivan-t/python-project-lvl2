def sorted_diff(diff):
    pre_result = {}
    result = {}

    for key, value in diff.items():

        if type(value) is dict:
            if key[:1] == ' ' or key[:1] == '+' or key[:1] == '-':
                pre_result[key] = sorted_diff(value)
            else:
                pre_result['  ' + key] = sorted_diff(value)
        else:
            if key[:1] == ' ' or key[:1] == '+' or key[:1] == '-':
                pre_result[key] = diff[key]
            else:
                pre_result['  ' + key] = diff[key]

    for key in sorted(pre_result.keys(), key=lambda x: x[2:]):

        if type(pre_result[key]) is dict:
            result[key] = sorted_diff(pre_result[key])
        else:
            result[key] = pre_result[key]

    return result
