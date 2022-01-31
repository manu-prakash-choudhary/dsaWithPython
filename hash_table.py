class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(100)]

    #below is the defined hash for this particular case it always varies from situation to situation
    def get_hash(self, key):
        h = 0 
        for char in key:
            h+=ord(char)
        return h%self.max  #this will genrate the index of given value
    def __setitem__(self,key,value) :
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = value
        else:
            print("Value already exists change hash function")
    
    def __getitem__(self,key):
        h =self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

ht = HashTable()
ht.__setitem__('march 6',19)
ht.__setitem__('march 8',9)
ht.__setitem__('march 16',79)
ht.__setitem__('may 6',14)
ht.__setitem__('april 6',49)


print(ht.__getitem__('march 6'))
print(ht.__getitem__('march 8'))
print(ht.__getitem__('march 16'))
print(ht.__getitem__('may 6'))
print(ht.__getitem__('april 6'))






