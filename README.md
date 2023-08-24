# arithmetic_coding
[Arithmetic Coding](https://en.wikipedia.org/wiki/Arithmetic_coding)
- A form of entropy encoding used in loss-less data compression
- A message is encoded into a single number `q`, where `0.0 <= q < 1.0`
- Frequently used characters will be stored with fewer bits
  - Relatively unfrequent characters will be encoded with more bits
