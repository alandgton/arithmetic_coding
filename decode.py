from sys import argv
from string import printable

EOF = r"\EOF"

def decode(num):
    """
    0.16969768002839405 -> "hello"
    """
    result = []
    lower, upper = 0.0, 1.0
    freq = {c: 1 for c in printable}
    freq[EOF] = 1
    while True:
        offset = lower
        for i, cc in enumerate(freq):
            slice_size = freq[cc]*(upper-lower)/sum(freq.values())
            if offset + slice_size > num:
                result.append(cc)
                freq[cc] += 1
                lower, upper = offset, offset + slice_size
                break
            else:
                offset += slice_size
        if result[-1] == EOF:
            result.pop()
            break
    return "".join(result)

if __name__ == '__main__':
    print(decode(float(argv[1])))
