# -*- coding:utf-8 -*-

def select_sort(alist):
	length = len(alist)
	for i in range(length - 1):
		min_index = i
		for j in range(i+1,length):
			if alist[min_index] > alist[j]:
				min_index = j
		alist[i],alist[min_index] = alist[min_index],alist[i]


li = [54,26,93,17,77,31,44,55,20]

select_sort(li)
print(li)	