# -*- coding:utf-8 -*-

def bubble_sort(alist):
	# n表示第几轮就结束
	n = len(alist) - 1
	i = 0
	j = 0
	while i < n:
		j = 0
		length2 = n - i
		is_change = False   #这里都是用来优化的
		while j < length2:
			if alist[j] > alist[j + 1]:
				alist[j], alist[j + 1] = alist[j + 1], alist[j]
				i = n - (j + 1)   #这里都是用来优化的
				is_change = True
			j += 1
		if is_change == False:   #这里都是用来优化的
			return
		i += 1
li = [-2,-3,54,26,93,17,77,31,44,55,20]

bubble_sort(li)
print(li)