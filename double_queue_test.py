# -*- coding:utf-8 -*-

class doubleQueue(object):

	def __init__(self):
		self.__list = []

	def add_front(self, item):
		self.__list.insert(0, item)

	def add_rear(self, item):
		self.__list.append(item)

	def remove_front(self):
		return self.__list.pop(0)

	def remove_rear(self):
		return self.__list.pop()

	def is_empty(self):
		return not self.__list

	def size(self):
		return len(self.__list)	

if __name__ == '__main__':

	q = doubleQueue()
	q.add_rear(1)
	q.add_rear(2)
	print(q.remove_front())