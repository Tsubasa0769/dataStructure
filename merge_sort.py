# -*- coding:utf-8 -*-

def merge_sort(alist):
	n = len(alist)
	if n <= 1:
		return alist
	mid = n // 2
	left_li = merge_sort(alist[:mid])
	right_li = merge_sort(alist[mid:])
	left_cursor ,right_cursor = 0,0
	result = []
	while left_cursor < len(left_li) and right_cursor < len(right_li):
		if left_li[left_cursor] <= right_li[right_cursor]:
			result.append(left_li[left_cursor])
			left_cursor += 1
		else:
			result.append(right_li[right_cursor])
			right_cursor += 1			
	result += left_li[left_cursor:]
	result += right_li[right_cursor:]
	return result



li = [54,26,93,17,77,31,44,44,55,20,-1,-2]
new_li = merge_sort(li)
print(new_li)	