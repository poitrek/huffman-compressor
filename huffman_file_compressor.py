import sys
import json
from huffman_coding import CanonicalHuffmanCoder


def byte_to_chr(bits):
    """
    Converts a string of bits to a string of corresponding characters, according
    to their ascii codes
    :param bits:
    :return: string of characters
    """
    chr_arr = ""
    portion_length = 8
    # Fill remaining bits of the array
    bits += '0' * ((portion_length - len(bits)) % portion_length)
    for i in range(0, len(bits), portion_length):
        char_code = int(bits[i: i+portion_length], 2)
        chr_arr += chr(char_code)
    return chr_arr


def chr_to_byte(chr_arr):
    """
    Converts string to a byte stream
    :param chr_arr:
    :return:
    """
    bits = ""
    for ch in chr_arr:
        bits += format(ord(ch), '#010b').replace('0b', '')
    return bits


def ord_seq(chr_arr):
    """
    Converts string to list of ascii values
    :param chr_arr:
    :return:
    """
    return [ord(ch) for ch in chr_arr]


def chr_seq(ord_arr):
    """
    Converts list of ints to a string by ascii values
    :param ord_arr:
    :return:
    """
    return "".join([chr(_ord) for _ord in ord_arr])

# TODO: zip to a binary file. Convert metadata to bytestream


zip_separator = '|'


def dump(file_in, file_out):
    """
    Compresses text file using Huffman coder
    :param file_in: input file name
    :param file_out: output file name
    """
    with open(file_in, 'r') as fin:
        text = fin.read()

    huff_coder = CanonicalHuffmanCoder(text)
    text_enc, meta_data = huff_coder.encode(text)
    # Metadata (symbol code lengths) + encoded text, in binary
    stream_out = chr_to_byte(json.dumps(meta_data) + zip_separator) + text_enc

    with open(file_out, 'wb') as fout:
        fout.write(stream_out)


def load(file_in, file_out):
    """
    Unzips a compressed file with Huffman coder
    :param file_in: input file name
    :param file_out: output file name
    """
    with open(file_in, 'r') as fin:
        stream_in = fin.read()
        # meta_data = json.loads(fin.readline())
        # text_enc = fin.readline()

    # Get metadata
    sep_pos = stream_in.find(chr_to_byte(zip_separator))
    meta_data_str = byte_to_chr(stream_in[:sep_pos])
    # Convert to dict
    meta_data = json.loads(meta_data_str)
    text_enc = stream_in[sep_pos+1:]
    # Decode
    text_dec = CanonicalHuffmanCoder().decode(text_enc, meta_data)

    with open(file_out, 'w') as fout:
        fout.write(text_dec)


class ParsingException(Exception):
    pass


if __name__ == '2__main__':
    try:
        if len(sys.argv) < 3:
            raise ParsingException("pass at least two arguments: input file & program mode")
        file_in = sys.argv[1]
        mode = sys.argv[2]
        if mode == 'zip':
            if len(sys.argv) < 4:
                file_out = 'zip_' + file_in
            else:
                file_out = sys.argv[3]
            dump(file_in, file_out)
        elif mode == 'unzip':
            if len(sys.argv) < 4:
                file_out = 'unzip_' + file_in
            else:
                file_out = sys.argv[3]
            load(file_in, file_out)
        else:
            raise ParsingException(f"incorrect mode: {mode}. Should be either 'zip' or 'unzip'")
    except ParsingException as e:
        print(f"Error parsing command line: {e}")
    # except Exception as e:
    #     print(f"Error: {e}")
