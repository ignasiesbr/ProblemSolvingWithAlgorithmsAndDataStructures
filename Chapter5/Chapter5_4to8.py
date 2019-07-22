# 4. implement the __len__ method for MAP ADT
# 5. implement contains
# 6. implement delete
# 8. implement quadratic probing.

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __len__(self):
        len = 0
        for item in self.slots:
            if item is not None:
                len = len + 1
        return len

    def __contains__(self, item):
        for aitem in self.data:
            if aitem == item:
                return True
        return False

    def __delitem__(self, key):
        hashval = self.hashfunction(key,self.size)
        if self.slots[hashval] == key:
            self.slots[hashval] = None
            self.data[hashval] = None
        else:
            nextslot = self.rehash(hashval,self.size)
            while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,self.size)
            if self.slots[nextslot] == key:
                self.slots[nextslot] = None
                self.data[nextslot] = None

    def rehashQuadratic(self, oldhash, size, key):
        j = 2
        rehash = (oldhash + 1) % size
        while self.slots[rehash] is not None and self.slots[rehash] is not key:
            rehash = (oldhash + (j * j)) % size
            j = j + 1
        return rehash

H=HashTable()
H[54]="cat"
H[21] = "dog"
print(H.slots)
print(H.data)
H.__delitem__(21)
print(H.slots)
print(H.data)

