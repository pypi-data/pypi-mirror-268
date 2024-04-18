from bitstring import BitArray

"""
    @param BitArray bit_array
    @param int offset
    @return bytes
"""
def get_slab(bit_array,offset=0):
    output_bitarr=BitArray(length=16)
    for i in range(0,12):
        output_bitarr[i+4] = bit_array[i+offset]
    return output_bitarr.tobytes()

"""
    @param int integer
    @return BitArray
"""
def make_slab(integer):
    input_bitarr=BitArray(integer.to_bytes(2,"big"))
    output_bitarr=BitArray(length=12)
    for i in range(0,12):
        output_bitarr[i] = input_bitarr[i+4]
    return output_bitarr

"""
    @param string unicode_characters
    @return bytes
"""
def encode(unicode_characters):
    if not isinstance(unicode_characters, str):
        raise TypeError("Argument #1 unicode_characters is not of the type string")

    if len(unicode_characters) == 0:
        return bytes()
    
    output_bytes = BitArray()

    for character in unicode_characters:
        character = ord(character)
        if not (    (character >= 0 and character <= 0xD7FF)
                or  (character >= 0xE000 and character <= 0x10FFFF)):
            raise Exception("Character out of bounds")
        
        if character < 0x7c0:
            output_bytes.append(make_slab(character))
            continue

        output_bytes.append(make_slab((character >> 10) + 0x7c0))
        output_bytes.append(make_slab((character & 0x3ff)|0xc00))
    
    return output_bytes.tobytes()

"""
    @param bytes slabs
    @return string
"""
def decode(slabs):
    if not isinstance(slabs, bytes):
        raise TypeError("Argument #1 slabs is not of the type bytes")

    bits_length = len(slabs) * 8
    if bits_length < 12:
        raise Exception("Not enough bits in slab")
    bits_parsed = 0
    
    output_string = ""

    bit_array = BitArray(slabs)

    while bits_parsed <= bits_length - 12:
        #slab 1
        slab = get_slab(bit_array, bits_parsed)
        bits_parsed += 12
        slab_int=int.from_bytes(slab, "big")

        if slab_int >= 0xc00:
            raise Exception("Slab larger than 0xC00 here now returning")

        #if a follow-up slab
        if slab_int >= 0x7c0:
            if bits_parsed > bits_length - 12:
                raise Exception("Not enough bits to build a character")
            
            slab_minus = slab_int - 0x7c0
            slab_minus = slab_minus << 10

            next_slab = get_slab(bit_array, bits_parsed)
            bits_parsed += 12
            next_slab_int = int.from_bytes(next_slab, "big")
            if next_slab_int < 0xc00:
                raise Exception("Second slab value is < 0xC00")
            output_character = slab_minus | (next_slab_int & 0x3ff)
            if not (   (output_character >= 0x07C0 and output_character <= 0xD7FF)
                    or (output_character >= 0xE000 and output_character <= 0x10FFFF)
                    ):
                raise Exception("Output character out of range 0x07C0-0xD7FF, 0xE000-0x10FFFF")
            output_string += chr(output_character)
        else:
            output_string += chr(slab_int)
        

    return output_string
