import math
import os
import sys
import requests

print(sys.executable)
print(sys.version)


r = requests.get("https://coreyms.com")
print(r.status_code)
