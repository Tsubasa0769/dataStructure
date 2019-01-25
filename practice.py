# -*- coding:utf-8 -*-
import random
li = ['冒泡','选择','插入','希尔','快排','归并']
n = len(li)
print(random.choice(li))
print(random.choice(li))
# 插入 快排
def insert_sort(alist):
	n = len(alist)
	for i in range(1, n):
		while i > 0:
			if alist[i] < alist[i -1]:
				alist[i],alist[i-1] = alist[i-1],alist[i]
				i -= 1
			else:
				break

def quick_sort(alist,start,end):
	mid_value = alist[start]
	left = start
	right = end
	if left >= right:
		return 
	while left < right:
		while left < right:
			if alist[right] > mid_value:
				right -= 1
			else:
				alist[left] = alist[right]
				left += 1
				break

		while left < right:
			if alist[left] <= mid_value:
				left += 1
			else:
				alist[right] = alist[left]
				right -= 1
				break
	alist[right] = mid_value
	quick_sort(alist, start, right - 1)
	quick_sort(alist, right + 1, end)


# li = [54,26,93,17,77,31,44,55,20]
# insert_sort(li)

li = [54,26,93,17,77,31,44,55,20]
n = len(li) - 1
insert_sort(li)
print(li)	