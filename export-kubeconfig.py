#!/usr/bin/env python3
import sys
import base64
import yaml

def read_contents(path):
  with open(path, 'rb') as f:
    return base64.b64encode(f.read()).decode('utf8')

def replace_path_with_contents(obj, key):
  path = obj.get(key)
  if path:
    obj[key + '-data'] = read_contents(path)
    del obj[key]

def replace_items(config, items_key, item_key, keys):
  items = config.get(items_key)
  if items:
    for item in items:
      data = item.get(item_key)
      if data:
        for key in keys:
          replace_path_with_contents(data, key)

def main():
  # load from stdin
  config = yaml.load(sys.stdin, Loader=yaml.SafeLoader)

  # replace clusters
  replace_items(config=config, items_key='clusters',
               item_key='cluster', keys=['certificate-authority'])

  # replace users
  replace_items(config=config, items_key='users',
               item_key='user', keys=['client-certificate', 'client-key'])

  # dump to stdout
  yaml.dump(config, sys.stdout)

if __name__ == "__main__":
    main()
