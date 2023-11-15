class LinkedList:
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            
            
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def append(self, value):
        obj = self.Node(value)
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj #uusi objekti lisätään tailissa tällä hetkellä olevan objektiin 
            self.tail = obj #tail päivitetään nyt ohjaamaan äsken lisättyyn uuteen objektiin
            
            
            
    def __getitem__(self,index):
        i = 0
        current = self.head
        while i < index:
            i+=1
            current = current.next
            if current == None:
                raise IndexError(str(index)+" suurempi kuin listan pituus")
        
        return current.value            
            
     
    def __str__(self):
        if not self.head:
            return "[]"
        s = "["
        current = self.head
        while current.next:
            s+=repr(current.value)
            s+=", "
            current = current.next
        s+=repr(current.value)+"]"
        return s
    
    def __repr__(self):
        if not self.head:
            return "[]"
        s = "["
        current = self.head
        while current.next:
            s+=repr(current.value)
            s+=", "
            current = current.next
        s+=str(current.value)+"]"
        return s

    def pop(self, index):
        if index == 0:#onko indeksi 0
            self.head = self.head.next#korvataan objekti seuraavalla
        else:
            nykobj = self.head #laitetaan objekti muistiin
            #kelataan objekti objektilta eteenpäin ja käytetään kahta apumuuttujaa nykobj ja nykmennyt
            for i in range(0,index): 
                nykmennyt = nykobj #laitetaan muistiin aijempi objekti
                if nykobj.next == None:
                    pass
                else:
                    nykobj = nykmennyt.next
        
            #korvataan oikean indeksin objekti seuraavalla objektilla
            nykmennyt.next = nykobj.next

            

            



x = LinkedList()
x.append(5)
x.append(6)
x.append(7)
x.append(8)
x.pop(3)
print(x)

