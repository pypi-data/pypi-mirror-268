import binascii
import sys
from badbyte.utils.colors import RED, ORANGE, GREEN, RST
from typing import List
import string
def char_to_int(c):
    if type(c) == str:
        return ord(c)
    elif type(c) == int:
        return c
    else:
        raise "char_to_hex - value is not char or int!"


def unhexify(hexed):
    hexed = "".join(c for c in hexed if not c.isspace())
    if len(hexed) % 2 == 1:
        print(f"{RED}Bad hexdump - odd character found.{RST}")
        sys.exit(0)
    return binascii.unhexlify(hexed)

def bytestring_clear(b):
    if type(b) == int:
        b = bytes((b, ))
    tmp = str(b)
    if tmp[0:2] == 'b"' or tmp[0:2] == "b'":
        return tmp[2:-1]
    else:
        return tmp


def safe_chr(b):
    # If output is string it returns the hexadecimal
    o = chr(b)
    if o.isspace():
        return f"\\x{b:02x}"
    else:
        return o


def find_diff(payload, data):
    bad_chars = []
    modified_chars = []
    idx = 0
    mod_idx = []
    while idx < len(data) and idx < len(payload):
        if data[idx] != payload[idx]:
            if len(data)>idx+1 and len(payload) > idx+1 and data[idx+1] == payload[idx+1]:
                modified_chars.append((char_to_int(payload[idx]), char_to_int(data[idx])))
                mod_idx.append(idx)
                idx += 1
            else:
                bad_chars.append(char_to_int(payload[idx]))
                break
        idx += 1
    return bad_chars, modified_chars, data[idx:], idx, mod_idx


def generate_characters(prefix: bytes, postfix: bytes, bad: List[int]):
    payload_raw = bytes([x for x in range(255, 0, -1) if x not in bad])
    return prefix + payload_raw + postfix


def analyze(hexdump: str, prefix: bytes, postfix: bytes, payload: bytes):
    hexdump = unhexify(hexdump)
    print(f"{GREEN}Unhexed string{RST}: {hexdump}")
    cutpos = hexdump.find(prefix)
    if cutpos != -1:
        print(f"{GREEN}-> Prefix found.{RST}")
        hexdump = hexdump[cutpos:]
    else:
        print(f"{RED}-> Prefix not found.{RST}")
        sys.exit(0)
    pos = hexdump.find(postfix)
    if pos != -1:
        print(f"{GREEN}-> Postfix found.{RST}")
    else:
        print(f"{RED}-> Postfix not found.{RST}")

    hexdump_cpy = hexdump
    bad_chars, modified_chars, hexdump, idx, mod_idx = find_diff(payload, hexdump)
    bad_chars = "[" + "".join([hex(b) + f" '{safe_chr(b)}'," for b in bad_chars]) + "]"
    print(f"-> Bad characters: {RED}{bad_chars} {RST}")
    modified_chars = "[" + "".join(
        [f"{hex(m[0])} '{safe_chr(m[0])}' => {hex(m[1])} '{safe_chr(m[1])}'," for m in modified_chars]) + "]"
    print(f"-> Modified characters: {ORANGE} {modified_chars} {RST}")
    good = hexdump_cpy[0:idx]
    colored_modification = ""
    prev = 0
    for mi in mod_idx:
        # when badchar is whitespace we can not color it so let's print it as hexascii
        if bytestring_clear(good[mi]).isspace():
            tmp = '\\x' + hex(ord(bytestring_clear(good[mi])))[2:]
            colored_modification += f"{GREEN}{bytestring_clear(good[prev:mi])}{RST}{ORANGE}{tmp}{RST}"
        else:
            colored_modification += f"{GREEN}{bytestring_clear(good[prev:mi])}{RST}{ORANGE}{bytestring_clear(good[mi])}{RST}"
        prev = mi + 1
    colored_modification += f"{GREEN}{bytestring_clear(good[prev:])}{RST}"
    print("aaaa: ", idx)
    print(f"""-> Payload in colors

    {GREEN}{colored_modification}{RST}{RED}{str(hexdump_cpy[idx:])[2:-1]}{RST}

    """)


def get_cyclic_alphabet(bad):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for b in unhexify(bad):
        alphabet = alphabet.replace(chr(b), "")
    return alphabet

