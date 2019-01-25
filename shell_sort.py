# -*- coding:utf-8 -*-


def shell_sort(alist):
	# length = len(alist)
	# gap = length // 2
	# while gap != 0:
	# 	for i in range(1,length):
	# 		j = i
	# 		while i > 0 and (i + gap - 1) < length:
	# 			if alist[i + gap - 1] < alist[i - 1]:
	# 				alist[i + gap - 1],alist[i - 1] = alist[i - 1],alist[i + gap - 1]
	# 				i -= gap
	# 			else:
	# 				break;
	# 	gap = gap // 2

	n = len(alist)
	gap = n // 2
	while gap > 0:
		for i in range(gap, n):
			while i > 0:
				if alist[i] < alist[i - gap]:
					alist[i],alist[i - gap] = alist[i - gap],alist[i]
					i -= gap
				else:
					break
		gap //= 2


li = [-2,-3,54,26,93,26,17,77,31,44,55,20]

shell_sort(li)
print(li)