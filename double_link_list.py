# -*- coding:utf-8 -*-

class Node(object):
	def __init__(self, elem):
		self.elem = elem
		self.next = None
		self.prev = None

class DoubleLinkList(object):
	def __init__(self, node = None):
		self.__head = node
	# 判断是否为空
	def is_empty(self):
		return self.__head == None

	# 向头部添加数据
	def add(self, item):
		# 我自己的思想
		# node = Node(item)
		# self.__head.prev = node
		# node.next = self.__head
		# self.__head = node

		node = Node(item)
		node.next = self.__head
		self.__head = node
		node.next.prev = node
	# 向尾部添加数据
	def append(self, item):
		node = Node(item)
		if self.__head == None:
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			node.prev = cur
			cur.next = node
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
			while count < pos:
				cur = cur.next
				count += 1
			cur.prev.next = node
			node.prev = cur.prev
			node.next = cur
			cur.prev = node
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
		while cur != None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = cur.next
					if cur.next:
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev
				break
			else:
				cur = cur.next

	def search(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			cur = cur.next
		return False

if __name__ == '__main__':
	ll = DoubleLinkList()
	ll.append(1)
	ll.append(2)
	ll.append(3)
	ll.append(4)
	ll.remove(1)
	ll.travel()
	ll.remove(3)
	ll.travel()
	ll.add(11)
	ll.travel()
	ll.insert(2,39)
	ll.travel()