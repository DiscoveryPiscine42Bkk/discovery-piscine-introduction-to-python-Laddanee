import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    sting_to_search = sys.argv[2]
    occurrences = re.findall(re.escape(keyword), sting_to_search)
    print(len(occurrences))
else:
    print("none")