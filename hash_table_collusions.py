'''Generally in case of collusion we can make linked lists at that index to cover up'''
class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(100)]

    #below is the defined hash for this particular case it always varies from situation to situation
    def get_hash(self, key):
        h = 0 
        for char in key:
            h+=ord(char)
        return h%self.max  #this will genrate the index of given value
    
    def __setitem__(self,key,value) :
        h = self.get_hash(key)
        found = False
        for index,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] ==key:
                    self.arr[h][index] = (key,value)
                    found = True
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h =self.get_hash(key)
        for item in self.arr[h]:
            if item[0]==key:
                return item[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] ==key:
                del self.arr[h][index]
        
    

ht = HashTable()
ht.__setitem__('march 6',19)
ht.__setitem__('march 8',9)
ht.__setitem__('march 16',79)
ht.__setitem__('may 6',14)
ht.__setitem__('december 6',49)


print(ht.__getitem__('march 6'))
print(ht.__getitem__('march 8'))
print(ht.__getitem__('march 16'))
print(ht.__getitem__('may 6'))
print(ht.__getitem__('december 6'))








