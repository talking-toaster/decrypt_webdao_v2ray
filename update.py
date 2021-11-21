import base64
from main import *

node = base64.b64encode(decrypt(get_key(), get_raw_link()).encode()).decode()

print(node)