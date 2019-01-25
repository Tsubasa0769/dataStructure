# -*- coding:utf-8 -*-

class Node(object):
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class SingleLinkList(object):
	def __init__(self, node = None):
		self.__head = node
	# 判断是否为空
	def is_empty(self):
		return self.__head == None

	# 向头部添加数据
	def add(self, item):
		# if self.__head == None:
		# 	self.__head = Node(item)
		# else:
		# 	self.__head, self.__head.next = Node(item), self.__head
		node = Node(item)
		node.next = self.__head
		self.__head = node
	# 向尾部添加数据
	def append(self, item):
		if self.__head == None:
			self.__head = Node(item)
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = Node(item)
	# 插入指定位置
	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length() - 1):
			self.append(item)
		else:
			node = Node(item)
			count = 0
			cur = self.__head
			while count < (pos - 1):
				cur = cur.next
				count += 1
			node.next = cur.next
			cur.next = node
	# 获取长度
	def length(self):
		count = 0
		cur = self.__head
		while cur != None:
			cur = cur.next
			count += 1
		return count
	# 遍历
	def travel(self):
		cur = self.__head
		while cur != None:
			print(cur.elem,end = ' ')
			cur = cur.next
		print('')

	def remove(self, item):
		cur = self.__head
		pre = None
		while cur != None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = self.__head.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next

	def search(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			cur = cur.next
		return False

if __name__ == '__main__':
	ll = SingleLinkList()
	ll.add(1)
	ll.travel()