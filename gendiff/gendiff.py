from gendiff.makediff import make_diff
from gendiff.parser import parse
from gendiff.formats.stylish import stylish
from gendiff.formats.plain import plain
from gendiff.formats.json import render_json


def generate_diff(after, before, name_formater='stylish'):

    after = parse(after)
    before = parse(before)

    diff = make_diff(after, before)
    make_diff_format = select_formater(name_formater)

    return make_diff_format(diff)


def select_formater(name):

    formaters = {
        'stylish': stylish,
        'plain': plain,
        'json': render_json
    }

    return formaters[name]
