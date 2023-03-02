class Node:
    def __init__(self, val):
        self.data =val
        self.next =None
        self.prev =None

class DoublyLinkedList:
    def __init__(self):
        self.head =None
        self.tail =None

    def add(self, o):    #append obj in list
        n =Node(o)
        if self.head==None:
            self.head =n
            self.tail =n
        else:
            t =self.tail
            self.tail.next =n
            n.prev =t
            self.tail =n

    def pop(self):
        if self.head ==None:
            raise Exception("Can't Pop from empty list")
        elif self.head.next==None:
            self.head =None
            self.tail =None
        else:
            t =self.tail.prev
            
            self.tail.prev =None
            self.tail =t
            self.tail.next =None

    def remove(self, val):   #remove specific value from list
        if self.head==None:
            raise Exception("List is empty")
        elif self.head.data==val:
            t =self.head.next
            self.head =t
            self.head.prev =None
        elif self.tail.data==val:
            t =self.tail.prev 
            self.tail =t
            self.tail.next =None
        else:
            c =self.head
            while c!=None:
              
                if c.data==val:
                    temp =c.prev
                    temp.next =c.next
                    c.next.prev =temp
                    return
                c =c.next
            raise Exception("Not found")

    def add_after(self, v1,v2):    #inset v1 after v2
        n =Node(v1)
        if self.head==None:
            raise Exception("Empty List")
        elif self.tail.data==v2:
            self.tail.next =n
            n.prev =self.tail
            self.tail =n
        else:
            c =self.head
     
            while c!=None:
                if c.data==v2:
                    

                    t =c.next
                    c.next =n
                    n.prev =c
                    n.next =t
                    t.prev =n
                   
                    return
                c =c.next
            raise Exception("Not conatin value")
    def add_before(self,v1,v2):    #add v1 before v2
        n =Node(v1)
        if self.head==None:
            raise Exception("Empty List")
        elif self.head.data==v2:
            n.next =self.head
            self.head.prev =n
            self.head =n

        else:
            c =self.head
            while c!=None:
                print(c.data)
                if c.data==v2:

                    temp =c.prev
                    c.prev.next =n
                    c.prev =n
                    n.prev =temp
                    n.next =c
                
                    return
                c =c.next
            raise Exception("Not found")

        
    def display(self):

        c =self.head
        while c!=None:
            print(c.data, end=" ")
            c =c.next
        print()
def main():
    d =DoublyLinkedList()
    d.add(10)
    d.pop()
    d.display()
    d.add(20)
    d.add(30)
    d.add(40)
    d.display()
    d.pop()
    d.display()

    d.add_after(10000,20)
    d.display()
    d.add_after(100,30)
    d.display()
    #d.add_after(40,19)   #exception will raise
    d.add_before(10,20)
    d.add_before(67,30)
    d.add_before(2,10)
    d.remove(2)
    d.remove(100)
    d.remove(20)
    
  
    d.display()

    




main()

