from gendiff import gendiff
from json import loads
import json


PATH_TO_JSON_BEFORE = 'tests/fixtures/first.json'
PATH_TO_JSON_AFTER = 'tests/fixtures/second.json'
#PATH_TO_YML_BEFORE = 'tests/fixtures/file_before.yml'
#PATH_TO_YML_AFTER = 'tests/fixtures/file_after.yml'
#PATH_TO_RESULT_STYLISH = 'tests/fixtures/result_stylish.txt'
#PATH_TO_RESULT_PLAIN = 'tests/fixtures/result_plain.txt'
PATH_TO_RESULT_JSON = 'tests/fixtures/answer_json1.txt'


def test_generate_diff():

    f = open(PATH_TO_RESULT_JSON)
    result_correct_stylish = f.read()
    result_stylish = generate_diff(
        PATH_TO_JSON_BEFORE, PATH_TO_JSON_AFTER)
    assert result_stylish == result_correct_stylish
    
    
#def test_diff_json():
#    file1 = 'tests/fixtures/first.json'
#    file2 = 'tests/fixtures/second.json'
#    with open('tests/fixtures/answer_json1.txt', 'r') as answer:
#        expected = answer.read()
#    result = gendiff.generate_diff(file1, file2)
#    assert result == expected
