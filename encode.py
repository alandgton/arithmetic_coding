from sys import argv
from string import printable

def encode(message):
    """
    ex) "test" -> 0.28851530130608194
    """
    lower, upper = 0.0, 1.0
    freq = {c: 1 for c in printable}
    freq['EOF'] = 1
    for c in message:
        if c not in freq:
            raise Exception(f"Only ASCII is supported. Invalid char: {c}")
        offset = lower
        slices = {}
        for cc in freq:
            slice_size = freq[cc]*(upper-lower)/sum(freq.values())
            slices[cc] = (offset, offset+slice_size)
            offset += slice_size
        lower, upper = slices[c]
        freq[c] += 1
    return upper

if __name__ == '__main__':
    print(encode(argv[1]))
