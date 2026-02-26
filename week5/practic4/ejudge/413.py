import json
import re
import sys

data = json.loads(sys.stdin.readline())
q = int(sys.stdin.readline())

pattern = re.compile(r'\.?([a-zA-Z_][a-zA-Z0-9_]*)|\[(\d+)\]')

for _ in range(q):
    query = sys.stdin.readline().strip()
    cur = data
    ok = True

    tokens = pattern.findall(query)

    for key, idx in tokens:
        if key:
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                ok = False
                break
        else:
            idx = int(idx)
            if isinstance(cur, list) and 0 <= idx < len(cur):
                cur = cur[idx]
            else:
                ok = False
                break

    if ok:
        print(json.dumps(cur, separators=(',', ':')))
    else:
        print("NOT_FOUND")