# -*- coding:utf-8 -*-

def binary_search(alist, item):
	# n = len(alist)
	# mid = n // 2
	# if mid == 0:
	# 	if item  == alist[mid]:
	# 		return True
	# 	else:
	# 		return False

	# if item == alist[mid]:
	# 	return True
	# elif item < alist[mid]:
	# 	return binary_search(alist[:mid],item)
	# else:
	# 	return binary_search(alist[mid+1:],item)
	n = len(alist)
	mid = n // 2
	if n > 0:
		if item == alist[mid]:
			return True
		elif item < alist[mid]:
			return binary_search(alist[:mid],item)
		else:
			return binary_search(alist[mid+1:],item)
	return False		


def binary_search_2(alist, item):
	n = len(alist)
	start = 0
	end = n - 1
	while start <= end:
		mid = (start + end) // 2
		if item == alist[mid]:
			return True
		elif item < alist[mid]:
			end = mid - 1
		else:
			start = mid + 1
	return False


li = [1,2,3,4,5,6,7,8]
# print(binary_search(li,3))
print(binary_search_2(li,3))