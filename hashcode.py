def hash(str):
    if not str:
        return 0
    val = ord(str[0]) << 7
    for char in str:
        val = c_mul(1000003, val) ^ ord(char)
        val = val ^ len(str)
        if val == -1:
            val = -2
        return val

def c_mul(a, b):
    return eval(hex((long(a) * b) & 0xFFFFFFFFL)[:-1])
