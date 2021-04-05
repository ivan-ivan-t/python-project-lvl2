import argparse

from gendiff.gendiff import generate_diff


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='')
parser.add_argument('second_file', type=str, help='')
parser.add_argument('-f', '--format', default='stylish', type=str,
                    help='set format output')

args = parser.parse_args()


def main():
    print(
        generate_diff(
            args.first_file, args.second_file, args.format
        )
    )


if __name__ == '__main__':
    main()
