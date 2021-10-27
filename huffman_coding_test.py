import unittest
from huffman_coding import insert_sorted, SimpleHuffmanCoder, HuffmanTreeNode, inverse_symbol_code_length_dict


class InsertSortedTest(unittest.TestCase):

    def test_insert_sorted_simple(self):
        li = [0, 3, 6, 9, 12, 15]
        insert_sorted(li, 10)
        self.assertListEqual(li, [0, 3, 6, 9, 10, 12, 15])

    def test_insert_sorted_maximum(self):
        li = [0, 3, 6, 9, 12]
        insert_sorted(li, 14)
        self.assertListEqual(li, [0, 3, 6, 9, 12, 14])

    def test_insert_sorted_minimum_desc(self):
        li = [12, 9, 6, 3]
        insert_sorted(li, 0, desc=True)
        self.assertListEqual(li, [12, 9, 6, 3, 0])

    def test_insert_sorted_tuples(self):
        li = [('a', 0), ('b', 3), ('c', 6), ('d', 9), ('e', 12)]
        insert_sorted(li, ('x', 7), key=lambda x: x[1])
        target_li = [('a', 0), ('b', 3), ('c', 6), ('x', 7), ('d', 9), ('e', 12)]
        self.assertListEqual(li, target_li)

    def test_insert_sorted_desc(self):
        li = [8, 6, 4, 2, 0]
        insert_sorted(li, 3, desc=True)
        self.assertListEqual(li, [8, 6, 4, 3, 2, 0])

    def test_insert_sorted_member_key(self):
        li_nodes = [HuffmanTreeNode(sym, cnt) for (sym, cnt) in [('a', 20), ('b', 16), ('c', 12), ('d', 8)]]
        insert_sorted(li_nodes, HuffmanTreeNode('x', 13), key=lambda x: x.cnt, desc=True)
        target_li_nodes = [HuffmanTreeNode(sym, cnt) for (sym, cnt) in
                           [('a', 20), ('b', 16), ('x', 13), ('c', 12), ('d', 8)]]
        self.assertListEqual(li_nodes, target_li_nodes)


class SymbolFrequenciesTest(unittest.TestCase):

    def test_simple(self):
        text = "the thrilling thrift"
        sf = SimpleHuffmanCoder.symbol_frequencies(text)
        self.assertDictEqual(sf,
                             {'t': 4, 'h': 3, 'e': 1, ' ': 2, 'r': 2, 'i': 3, 'l': 2, 'n': 1, 'g': 1, 'f': 1})

    def test_empty(self):
        self.assertDictEqual(SimpleHuffmanCoder.symbol_frequencies(""), dict())


class HuffmanStringCoderTest(unittest.TestCase):

    def test_huffman_empty(self):
        coder = SimpleHuffmanCoder("")
        self.assertDictEqual(coder._code_dict, dict())

    def test_huffman_one_symbol(self):
        coder = SimpleHuffmanCoder("a")
        self.assertDictEqual(coder._code_dict, {'a': ''})
        # string = 'a' * 10
        # self.assertEqual(string, coder.decode(coder.encode(string)))

    def test_huffman_two(self):
        coder = SimpleHuffmanCoder("ab")
        self.assertDictEqual(coder._code_dict, {'a': '1', 'b': '0'})
        string = "abbabaabbbbab"
        self.assertEqual(coder.decode(coder.encode(string)), string)

    # def test_huffman(self):
    #     string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore " \
    #              "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " \
    #              "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse " \
    #              "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, " \
    #              "sunt in culpa qui officia deserunt mollit anim id est laborum "
    #     coder = SimpleHuffmanCoder(string)


class OthersTest(unittest.TestCase):

    def test_inverse_symbol_code_length_dict(self):
        symbol_code_len = {'r': 4, 'b': 6, 'y': 6, 'e': 3, 'i': 4, 'a': 4, 'o': 4, ' ': 3, 'c': 5, 'f': 6,
                           'd': 6, 'l': 5, 'm': 6}
        target_inv_dict = {3: ' e', 4: 'aior', 5: 'cl', 6: 'bdfmy'}
        self.assertDictEqual(target_inv_dict, inverse_symbol_code_length_dict(symbol_code_len))


if __name__ == '__main__':
    unittest.main()
