import hashlib
import zlib

content = "what is up, doc?"
header = f"blob {len(content.encode('utf-8'))}\0"
store = header + content

m = hashlib.sha1()
m.update(store.encode('utf-8'))
print(m.hexdigest())
print(zlib.compress(store.encode('utf-8')))