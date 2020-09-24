import json
import argparse
import os
import tempfile


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='key for stored or new value')
    parser.add_argument('--val', help='value to store with specific key')
    parser.add_argument('--remove', help='remove storage file', action='store_true')
    return parser.parse_args()


def get_json_data(storage_path):
    """loads json data from storage_path"""
    with open(storage_path, 'r+') as json_file:
        try:
            json_data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            json_data = dict()
    return json_data


def write_json_data(storage_path, json_data):
    """write json_data to storage_path file"""
    with open(storage_path, 'w') as json_file:
        json.dump(json_data, json_file)


def write_value(dict_data, key, value):
    if key in dict_data.keys():
        dict_data[key].append(value)
    else:
        dict_data[key] = [value]


def get_value(dict_data, key):
    if key in dict_data.keys():
        return ', '.join(dict_data[key])
    else:
        return ''


def remove_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


def main(storage_path):
    if not os.path.exists(storage_path):
        open(storage_path, 'w').close()
    args = parse()
    json_data = get_json_data(storage_path)
    if args.key and args.val:
        write_value(json_data, args.key, args.val)
        write_json_data(storage_path, json_data)
    elif args.key:
        print(get_value(json_data, args.key))
    elif args.remove:
        remove_file(storage_path)
    else:
        print('Invalid Arguments')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
