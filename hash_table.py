class HashTable:
    ''' Hash table data structure'''
    def __init__(self):
        ''' declaration of string that creates an array of size 11 with each index being have the
        None value'''
        self.list = [None]*11

    @staticmethod
    def hash(self,n):
        ''''
        :param n: int
        :return : return index in list to store number
        '''
        return n % 11
    def get(self,n):
        '''
        :param n: int
        :return: int value from list
        '''
        return self.list[hash(n)]
    def set(self, n,v):
        '''

        :param n: int
        :param v: can be any type.
        '''
        self.list[hash(n)] = v


hash_table = HashTable()
hash_table.set(1, 'Distributed')
hash_table .set(5, 7)
print(hash_table.get(1))
print(hash_table.get(5))