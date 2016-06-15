__author__ = 'Vishal Garg(vg3660)'
"""
	Class used for testing the program
"""
class Task:
	__slots__ = "time_left", "name", "time"

	def __init__( self, name, time ):
		self.time_left = time
		self.name = name
		self.time = time

	def __str__(self):
		return str(self.name) + " " + str(self.time) + " " + str(self.time_left)

"""
	Class used for creating a list
"""
class node:
	__slots__ = 'data','next'
	def __init__(self,data,next=None):
		self.data=data
		self.next=next

"""
	PriorityQueue Class
	It has 3 private instance variables front, rear and func
"""
class PriorityQueue:
	__slots__='__front','__rear','__func'

	#This is the constructor of the class which takes function to be used for finding the element to execute as argument
	def __init__(self,after):
		self.__front=self.__rear=None
		self.__func=after

	#This function simply appends the element at the end
	def enqueue(self,newValue):
		if self.__front==None:
			self.__front=self.__rear=node(newValue)
		else:
			self.__rear.next=node(newValue)
			self.__rear=self.__rear.next

	#This function returns the str form of the Priority Queue
	def __str__(self):
		Output=''
		temp=self.__front
		while temp!=None:
			Output+=str(temp.data) + " "
			temp=temp.next
		return Output

	#Here we are just telling that insert and enqueue are the same thing
	insert = enqueue

	#isEmpty function checks if the Queue is empty or not
	def isEmpty(self):
		if self.__front==None:
			return True
		else:
			return False

	#peek function returns the object which is to be executed next
	def peek(self):
		temp=self.__front
		assert not temp==None," List is empty!!"
		data=temp.data
		while temp.next!=None:
			temp=temp.next
			if self.__func(data,temp.data):
				data=temp.data
		return data

	#Dequeue function removes the element which should be having maximum priority
	#according to the after function
	def dequeue(self):
		data=self.peek()
		#Checking if there is nothing is the list
		if data==None:
			return None
		#Special case when data is the first element of the queue
		if self.__front.data==data:
			if self.__front==self.__rear:
				data=self.__front.data
				self.__front=self.__rear=None
			else:
				self.__front=self.__front.next
		else:
			counter=temp=self.__front
			temp=temp.next
			while temp.data!=data:
				counter=temp
				temp=temp.next
			counter.next=temp.next
			#Special case when element to be removed is at the end
			if temp==self.__rear:
				self.__rear=counter
		return data

	#Saying that remove and dequeue are the same
	remove = dequeue

#Base function for implementing the Priority Queue according to minimum time left
def prio(v,u):
	if v.time_left>u.time_left:
		return True
	else:
		return False

def main():
	myQ=PriorityQueue(prio)
	#We can remove the comment in next lines to check what happens when there
	#is nothing in the queue and we try to peek or dequeue
	#myQ.peek()
	#myQ.dequeue()
	myQ.insert(Task("eat",1))
	myQ.insert(Task("sleep",3))
	myQ.insert(Task("repeat",2))
	print(myQ.peek())
	myQ.dequeue()
	print(myQ)
	print(myQ.isEmpty())

if __name__=='__main__':
	main()