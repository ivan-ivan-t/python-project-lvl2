from gendiff import gendiff
from json import loads
import json
import yaml


def test_diff_json():
    file1 = 'tests/fixtures/first.json'
    file2 = 'tests/fixtures/second.json'
    with open('tests/fixtures/answer_diff.txt', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected


def test_diff_yml():
    file1 = 'tests/fixtures/first.yaml'
    file2 = 'tests/fixtures/second.yaml'
    with open('tests/fixtures/answer_diff.txt', 'r') as answer:
        expect = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expect


def test_stylish_json():
    file1 = ''
    file2 = ''
    with open('', 'r') as answer:
	expected = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected



def test_stylish_yaml():
    file1 = ''
    file2 = ''
    with open('', 'r') as answer:
        expected = answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected
