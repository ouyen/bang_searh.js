import json
import yaml
import requests


def get_bang_dict(download=False):
    if download:
        url="https://duckduckgo.com/bang.js"

        src_dict={}


        try:
            r = requests.get(url,timeout=5)
            r.raise_for_status()
            src_dict = json.loads(r.text)
            with open("bang.js","w") as f:
                f.write(r.text)

        except:
            src_dict=get_bang_dict(download=False)

    else:
        with open("bang.js", "r") as f:
            src_dict = json.load(f)

    return src_dict

bang_dict={}
for bang in get_bang_dict():
    bang_dict[bang['t']] = bang['u']

with open("patch.yaml", "w") as f:
    patch = yaml.safe_load(f)

for bang in patch:
    bang_dict[bang] = patch[bang]

with open("bang_full.yaml", "w") as f:
    yaml.safe_dump(bang_dict, f)

with open("bang_full.json", "w") as f:
    json.dump(bang_dict, f)

