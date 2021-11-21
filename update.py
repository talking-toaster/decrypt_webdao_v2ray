import base64
import main

node = base64.b64encode(decrypt(get_key(), get_raw_link()).encode()).decode()

print(node)