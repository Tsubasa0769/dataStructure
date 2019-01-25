# -*- coding:utf-8 -*-

def quick_sort(alist, start, end):
	if start >= end:
		return
	mid_value = alist[start]
	low = start
	high = end - 1
	while low < high:
		while low < high and mid_value < alist[high]:
			high -= 1
		alist[low] = alist[high]

		while low < high and alist[low] <= mid_value:
			low += 1
		alist[high] = alist[low]
	alist[high] = mid_value
	quick_sort(alist, 0, high -1)
	quick_sort(alist, high + 1, end)




li = [54,26,93,17,77,31,44,44,55,20,-1,2]
start = 0
end = len(li)
quick_sort(li,start,end)
print(li)	