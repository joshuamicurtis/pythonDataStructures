class HashTable(object):
    def __init__(self, size):
        self.size = size # size should be a prime number
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.openSlots = self.size

    def put(self, key, data):
        # Check if hashtable needs to be enlarged
        if self.openSlots < self.size / 3:
            newHash = HashTable(find_next_prime(self.size * 2))
            for i in range(self.size):
                if self.slots[i] != None:
                    newHash[self.slots[i]] = self.data[i]
            self.slots = newHash.slots
            self.data = newHash.data
            self.size = newHash.size
            self.openSlots = newHash.openSlots
        
        # Decrement number of open slots
        self.openSlots -= 1                 
        hashvalue = self.hashfunction(key,len(self.slots))
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key:
            self.data[hashvalue] = data     # replace old data with new data
        else:
            nextslot = self.rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] != None and \
                            self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else: 
                self.data[nextslot] = data # replace old data with new data
                
    def hashfunction(self, key, size):
        return key % size
        
    def rehash(self,oldhash,size):
        return (oldhash + 1) % size
        
    def get(self,key):
        startslot =self.hashfunction(key,len(self.slots))
        
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data
         
    def __getitem__(self, key):
        return self.get(key)
        
    def __setitem__(self,key,data):
        self.put(key,data)

def find_next_prime(size):
    a = size + 1
    b = size * 2 # Bertrand's postulate
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None        
H = HashTable(7)

H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20]='duck'
print(H[20])
print(H[99])
print(H.size)
print(H.openSlots)
print(H.data[0])
print 'cat' in H.data
print 'bat' in H.data
print find_next_prime(10000000)