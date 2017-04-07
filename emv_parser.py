import re
import unittest

def get_element(tlv):
    idx = 0
    tag = tlv[idx]
    idx += 1
    if (int(tag, 16) & 0x1f) == 0x1f:
        tag += tlv[idx]
        idx += 1

    length = int(tlv[idx], 16)
    idx += 1

    value = tlv[idx:length + idx]
    assert length == len(value)
    return [(tag, value), tlv[length+idx:]]

def parse(tlv):
    elements = []
    t_list = re.findall('\w\w', tlv)
    res = [(), t_list]
    while res[1]:
        res = get_element(res[1])
        elements.append(res[0])
    return {element[0]: ''.join(element[1]) for element in elements}

class TestParser(unittest.TestCase):
    def test_parser(self):
        tlv = '9F10120010250000044000DAC100000000000000008407A00000000410105F2A02084082025800950500002000009A031601279C01009F02060000000010009F1A0208409F260809FB57BE95EF4BB69F2701809F34031E03009F360200AB9F37040F03DF07'
        print parse(tlv)

    def test_parser_fail(self):
        tlv = '9F10120010250000044000DAC100000000000000008407A00000000410105F2A02084082025800950500002000009A031601279C01009F02060000000010009F1A0208409F260809FB57BE95EF4BB69F2701809F34031E03009F360200AB9F37050F03DF07'
        self.assertRaises(AssertionError, parse, tlv)

if __name__ == '__main__':
    unittest.main()