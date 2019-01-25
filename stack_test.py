# -*- coding:utf-8 -*-

class Stack(object):

	def __init__(self):
		self.__list = []

	def push(self, item):
		"""
		这个可以从头部或者尾部来存数据
		但根据 顺序表 和 链表 实现的方式不同，复杂度就不同
		"""
		self.__list.append(item)

	def pop(self):
		return self.__list.pop()

	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.__list[-1]

	def is_empty(self):
		return not self.__list

	def size(self):
		return len(self.__list)


if __name__ == '__main__':
	s = Stack()
	print(s.is_empty())
	s.push(1)
	print(s.is_empty())
	s.push(2)
	s.push(3)
	print(s.peek())
	print(s.size())
	print(s.pop())
	print(s.size())	
