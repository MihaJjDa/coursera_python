import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
#print(args.key)
#print(args.val)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    f = open(storage_path, 'w')
    f.close()

with open(storage_path, 'r+') as f:
    s = f.read()
    d = json.loads(s) if s else {}

# print(d)

if args.val:
    if args.key in d:
        d[args.key][len(d[args.key])] = args.val
    else:
        d[args.key] = {0: args.val}
    #print(d)
    with open(storage_path, 'w') as f:
        f.write(json.dumps(d))
elif args.key in d:
    print(*d[args.key].values(), sep = ", ")


   
   
