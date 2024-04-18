from os.path import splitext
from ruamel.yaml import YAML
from json import dumps

def write_egg_files(cmd, basename, filename):
    yaml = YAML()

    with open('package_config.yaml') as file:
        value = yaml.load(file)

    argname = splitext(basename)[0]

    str_value = dumps(value, separators=(',', ':'), ensure_ascii=False)

    cmd.write_or_delete_file(argname, filename, str_value)
