import hashlib
import zlib

content = "what is up, doc?".encode('utf-8')
header = f"blob {len(content)}\0".encode('utf-8')
store = header + content

m = hashlib.sha1()
m.update(store)
sha1 = m.hexdigest()

path = f".git/objects/{sha1[0:2]}/{sha1[2:]}"

print(sha1)
print(path)
zlib_content = zlib.compress(store)
print(zlib.decompress(zlib_content))