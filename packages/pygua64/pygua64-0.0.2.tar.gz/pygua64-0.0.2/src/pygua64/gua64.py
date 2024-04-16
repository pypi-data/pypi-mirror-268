gua = '䷁䷖䷇䷓䷏䷢䷬䷋' \
      '䷎䷳䷦䷴䷽䷷䷞䷠' \
      '䷆䷃䷜䷺䷧䷿䷮䷅' \
      '䷭䷑䷯䷸䷟䷱䷛䷫' \
      '䷗䷚䷂䷩䷲䷔䷐䷘' \
      '䷣䷕䷾䷤䷶䷝䷰䷌' \
      '䷒䷨䷻䷼䷵䷥䷹䷉' \
      '䷊䷙䷄䷈䷡䷍䷪䷀'

from_bytes = int.from_bytes


def encode(s):
    """Encode the bytes-like object s using gua64 and return a bytes object.
    """
    encoded = bytearray()
    for i in range(0, len(s), 3):
        c = from_bytes(s[i: i + 3], 'big')
        if len(s[i: i + 3]) == 3:
            encoded += gua[c >> 18].encode()
            encoded += gua[(c >> 12) & 0x3f].encode()
            encoded += gua[(c >> 6) & 0x3f].encode()
            encoded += gua[c & 0x3f].encode()
            continue
        if len(s[i: i + 3]) == 2:
            encoded += gua[c >> 10].encode()
            encoded += gua[c >> 4 & 0x3f].encode()
            encoded += gua[(c & 0xf) << 2].encode()
            encoded += '〇'.encode()
            continue
        if len(s[i: i + 3]) == 1:
            encoded += gua[c >> 2].encode()
            encoded += gua[(c & 0x3) << 4].encode()
            encoded += '〇'.encode() * 2
    return bytes(encoded)


def decode(s):
    """Decode the bytes-like object s using gua64 and return a bytes object.
    """
    encoded = []
    gua64dict = {v: k for k, v in enumerate(gua)}
    for i in range(0, len(s), 3):
        if s[i: i + 3].decode() == '〇':
            encoded.append(255)
            continue
        encoded.append(gua64dict[s[i: i + 3].decode()])
    b = bytearray(encoded)
    encoded = []
    for i in range(0, len(b), 4):
        c = from_bytes(b[i: i + 4], 'big')
        if len(b[i: i + 4]) == 4:
            encoded.append(c >> 24 << 2 | (c >> 20 & 0x3))
            if b[i + 2] != 255:
                encoded.append((c >> 16 & 0xf) << 4 | (c >> 10 & 0xf))
            if b[i + 3] != 255:
                encoded.append((c >> 8 & 0x3) << 6 | (c & 0x3f))
    return bytes(encoded)


def verify(test_str):
    char_set = set(gua)
    char_set.add('〇')

    for char in test_str:
        if char not in char_set:
            return False

    return True


if __name__ == '__main__':
    r = encode('hello，世界'.encode())
    print(r.decode())

    r = decode('䷯䷬䷿䷶䷸䷬䷀䷌䷌䷎䷼䷲䷰䷳䷸䷘䷔䷭䷒〇'.encode())
    print(r.decode())

    r = verify('䷯䷬䷿䷶䷸䷬䷀䷌䷌䷎䷼䷲䷰䷳䷸䷘䷔䷭䷒〇')
    print(r)
