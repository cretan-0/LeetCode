class Solution(object):
    def defangIPaddr(self, address):
        address = list(map(lambda x: x.replace('.', '[.]'), address))
        x = ''.join(address)
        return x
        