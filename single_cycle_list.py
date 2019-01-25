# -*- coding:utf-8 -*-

class Node(object):
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class SingleCycleList(object):
	def __init__(self, node = None):
		if node:
			node.next = node		
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
		if self.__head:
			node.next = self.__head
			rear = self.__head
			while rear.next != self.__head:
				rear = rear.next
			rear.next = node
		else:
			node.next = node

		self.__head = node
	# 向尾部添加数据
	def append(self, item):
		if self.__head == None:
			self.add(item)
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			node = Node(item)
			node.next = self.__head
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
			while count < (pos - 1):
				cur = cur.next
				count += 1
			node.next = cur.next
			cur.next = node
	# 获取长度
	def length(self):
		if self.__head == None:
			return 0
		count = 1
		cur = self.__head
		while cur.next != self.__head:
			cur = cur.next
			count += 1
		return count
	# 遍历
	def travel(self):
		if self.is_empty():
			return
		cur = self.__head
		while cur.next != self.__head:
			print(cur.elem,end = ' ')
			cur = cur.next
		print(cur.elem)

	def remove(self, item):
		cur = self.__head
		if cur == None:
			return
		pre = None
		while cur.next != self.__head:
			if cur.elem == item:
				# 头节点
				if cur == self.__head:
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head

				else:
					# 中间节点
					pre.next = cur.next
				return
			else:
				pre = cur
				cur = cur.next
		# 尾节点
		if cur.elem == item:
			if cur == self.__head:
				self.__head = None
			else:
				pre.next = self.__head


	def search(self, item):
		if self.is_empty():
			return False;		
		cur = self.__head
		while cur.next != self.__head:
			if cur.elem == item:
				return True
			cur = cur.next
		return cur.elem == item

if __name__ == '__main__':
	ll = SingleCycleList()
	ll.add(1)
	ll.add(2)
	ll.add(1)
	ll.remove(1)
	ll.remove(1)
	ll.travel()
	# ll.add(11)
	# ll.append(112)
	# ll.insert(3,33)
	# print(ll.search(34))
	# ll.travel()
	# print(ll.length())