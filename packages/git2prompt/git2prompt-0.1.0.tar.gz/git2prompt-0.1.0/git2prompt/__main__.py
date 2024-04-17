import sys
import os.path
from git2prompt import traverse_tree
from igittigitt import IgnoreParser


def create_ignore_parser(basedir: str) -> IgnoreParser:
    parser = IgnoreParser()
    for path, dirs, files in os.walk(basedir):
        for file in files:
            if file.endswith('.gitignore'):
                parser.parse_rule_file(os.path.join(path, file), base_dir=path)
    return parser


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    ignore_path = os.path.join(root, '.gitignore')
    if os.path.exists(ignore_path):
        ignore = create_ignore_parser(root).match
    else:
        ignore = lambda x: False

    for block in traverse_tree(root=root, ignore=ignore):
        print(block)


if __name__ == '__main__':
    main()
