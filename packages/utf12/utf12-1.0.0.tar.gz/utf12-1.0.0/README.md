# utf-12
UTF-12 encoder based on [the tapemark article](https://web.archive.org/web/20230930121239/https://tapemark.narod.ru/comp/utf12en.html)

Original tapemark article: <https://tapemark.narod.ru/comp/utf12en.html>


Following the specs, everything is in big-endian.
Ensure that inputs are big-endian.

Encodes unicode characters 07c0-D7ff, e000-10ffff

## Install
    pip install utf12

## Usage


    from utf12 import encode, decode
    encoded_bytes = encode("R2-D2")
    print(decode(encoded_bytes))

### encode(unicode_characters)
unicode_characters is a python string of unicode characters
Returns a bytes object of the slabs with trailing 0 bits on the last byte if needed

### decode(slabs)
slabs is a bytes object of the slabs for the characters
Returns a python string of the unicode characters
