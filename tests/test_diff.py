from gendiff.gendiff import generate_diff
from json import loads


def test_diff_json():
    file1 = 'tests/fixtures/first.json'
    file2 = 'tests/fixtures/second.json'
    with open('tests/fixtures/answer_diff.txt', 'r') as answer:
        expected = answer.read()
    result = generate_diff(file1, file2)
    assert result == expected


def test_diff_yml():
    file1 = 'tests/fixtures/first.yaml'
    file2 = 'tests/fixtures/second.yaml'
    with open('tests/fixtures/answer_diff.txt', 'r') as answer:
        expect = answer.read()
    result = generate_diff(file1, file2)
    assert result == expect


def test_stylish_json():
    file1 = 'tests/fixtures/first2.json'
    file2 = 'tests/fixtures/second2.json'
    with open('tests/fixtures/answer_stylish.txt', 'r') as answer:
        expected = answer.read()
    result = generate_diff(file1, file2)
    assert result == expected


def test_stylish_yaml():
    file1 = 'tests/fixtures/first2.yaml'
    file2 = 'tests/fixtures/second2.yaml'
    with open('tests/fixtures/answer_stylish.txt', 'r') as answer:
        expected = answer.read()
    result = generate_diff(file1, file2)
    assert result == expected


def test_plain_json():
    file1 = 'tests/fixtures/first2.json'
    file2 = 'tests/fixtures/second2.json'
    with open('tests/fixtures/answer_plain.txt', 'r') as answer:
        expected = answer.read()
    result = generate_diff(file1, file2, 'plain')
    assert result == expected


def test_plain_yaml():
    file1 = 'tests/fixtures/first2.yaml'
    file2 = 'tests/fixtures/second2.yaml'
    with open('tests/fixtures/answer_plain.txt', 'r') as answer:
        expected = answer.read()
    result = generate_diff(file1, file2, 'plain')
    assert result == expected


def test_json():
    file1 = 'tests/fixtures/first2.json'
    file2 = 'tests/fixtures/second2.json'
    with open('tests/fixtures/answer_json.json', 'r') as answer:
        expected = loads(answer.read())
    result = loads(generate_diff(file1, file2, 'json'))
    assert result == expected
