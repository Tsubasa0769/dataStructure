# -*- coding:utf-8 -*-


def insert_sort(alist):
	# length = len(alist)
	# for i in range(1,length):
	# 	for j in range(i):
	# 		if alist[i - j] < alist[i - 1 - j]:
	# 			alist[i - j],alist[i - 1 - j] = alist[i - 1 - j],alist[i - j]
	# 		else:
	# 			break

	length = len(alist)
	for i in range(1,length):
		while i > 0:
			if alist[i] < alist[i - 1]:
				alist[i],alist[i - 1] = alist[i - 1],alist[i]
				i -= 1
			else:
				break;

li = [-2,-3,54,26,93,17,77,31,44,55,20]

insert_sort(li)
print(li)