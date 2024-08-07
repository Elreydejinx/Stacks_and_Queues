
def line():
    line = "~~~~~~~~~~~~~~"
    print(line)


class Orders():

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class OrderQueue():
    def __init__(self):
        self.head = None
        self.tail = None

    def placedOrder(self, data):
        new_order = Orders(data)
        if self.head == None:
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order

    def viewOrders(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def recievedOrders(self):
        if self.head == None:
            return "Order not found"
        else:
            completedOrders = self.head
            self.head = self.head.next
            return completedOrders.data
        
orderlist = OrderQueue()

orderlist.placedOrder('cheeseburger')
orderlist.placedOrder('fries')
orderlist.placedOrder('chickenTenders')
orderlist.placedOrder('Coke')
orderlist.placedOrder('side of tatortots')
orderlist.placedOrder('sundae')

orderlist.viewOrders()


class OrderFinished():

    def __init__(self):
        self.head = None
        self.tail = None

    
    def addToOrder(self,data):
        additionalOrder = Orders(data)
        if self.head == None:
            self.head = additionalOrder
            self.tail = additionalOrder
            print(f'{additionalOrder}: this order is up!!!')

        else:
            self.tail.next = additionalOrder
            additionalOrder.prev = self.tail
            self.tail = additionalOrder
            print('that order doesn''t''exist')


    def ViewAddedOrder(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

    def orderDelivered(self):
        if not self.tail:
            print("No orders to fill")
        delivered = self.tail
        self.tail = delivered.prev
        self.tail.next = None
        return delivered.data
    
    def specialOrder(self, inx, data):
        specialOrder = Orders(data)
        current = self.head
        dishes = 1

        while dishes < inx:
            current = self.head
            dishes += 1

        specialOrder.next = current.next
        specialOrder.prev = current
        current.next = specialOrder
        specialOrder.next.prev = specialOrder


placedOrders = OrderFinished()
placedOrders.addToOrder('stake and cheese dinner') 
placedOrders.addToOrder('grilled chicken w/ rice')
placedOrders.addToOrder('Salmon and yellow rice')
placedOrders.addToOrder('cheeseburger and fries')

placedOrders.ViewAddedOrder()

line()

print('orders filled')
print(placedOrders.orderDelivered())
print(placedOrders.orderDelivered())

line()

placedOrders.specialOrder(1,"grilled cheese")
print("special orders")
placedOrders.ViewAddedOrder()