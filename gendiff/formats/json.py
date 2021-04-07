import json
from gendiff.formats.make_sorted import sorted_diff


def render_json(diff):
    diff = sorted_diff(diff)
    return json.dumps(diff, indent=2)
