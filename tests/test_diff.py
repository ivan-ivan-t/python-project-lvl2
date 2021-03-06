from gendiff import gendiff
from json import loads
import json

       
def test_diff_json():
    file1 = 'tests/fixtures/first.json'
    file2 = 'tests/fixtures/second.json'
    with open('tests/fixtures/answer_json1.txt', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected
