class Items:
    itemname:str
    itemcode:str

    def createItems(self):
        #we will do this portion later
        print("itemcode : " + self.itemcode)
        print("itemname : " + self.itemname)
        print("Item created")
        def checkItemsWithZeroSale(self):
            #will do later todo
            pass



objItems=Items()
objItems.itemname="Sugar"
objItems.itemcode="67890"
#del objItems
objItems.createItems()
#del keyword deletes class object property
#this is tuple
tupleExample=("Shivani","Neeraj","Deepak","Prabhat","Ankit")
print(tupleExample)
print(tupleExample[0])
print(tupleExample[1])
print(tupleExample[2])
print(tupleExample[3])
print(tupleExample[4])

ShivaniTuple=("Shivani",True,25,True)
NeerajTuple=("Neeraj",True,21,True)

print(ShivaniTuple[1])
print(NeerajTuple[2])

columns=("itemname","itemcode")
print(ShivaniTuple[-2])

#len: to get tuple length
print(len(ShivaniTuple))

fruits = ("apple","banana","cherry")
(green,yellow,red) =fruits

print(green)
print(yellow)
print(red)

#looping a tuple
for tupleValue in ShivaniTuple:
    print(tupleValue)
    #if Shivani Tuple has no True in 2 position ,print "Shivani is attending the class")
    if(ShivaniTuple[1]==True):
        print("Shivani is attending the class")
    elif(ShivaniTuple[1]==False):
        print("Shivani is  not attending the class")

        # OR Second Method
        if (ShivaniTuple[1] == True):

            print("Shivani is attending the class")
        else:print("I Don't Know")






