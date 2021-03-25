def make_diff(first, second):

    result = {}
    same_key = first.keys() & second.keys()
    added = second.keys() - first.keys()
    removed = first.keys() - second.keys()

    for key in same_key:
        if first[key] == second[key]:
            result['  ' + key] = first[key]
        if first[key] != second[key]:
            if type(first[key]) and type(second[key]) is dict:
                result['  ' + key] = make_diff(first[key], second[key])
            else:
                result['- ' + key] = first[key]
                result['+ ' + key] = second[key]

    for key in added:
        result['+ ' + key] = second[key]

    for key in removed:
        result['- ' + key] = first[key]

    return result
