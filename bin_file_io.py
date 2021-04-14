from huffman_file_compressor import byte_to_chr, chr_to_byte, ord_seq, chr_seq


def write():
    text = 'ala ma kota'
    with open('ala.bin', 'wb') as f:
        f.write(bytes(ord_seq(text)))


def read():
    with open('ala.bin', 'rb') as f:
        txt = f.read().decode()
        print(txt)
        print(type(txt))


if __name__ == '__main__':
    read()
