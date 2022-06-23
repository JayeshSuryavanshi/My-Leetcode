from heapq import heappush,heappop
class Solution:
	def scheduleCourse(self, courses: List[List[int]]) -> int:
		if len(courses)==0:
			return 0

		courses.sort(key=lambda x:x[1])
		h=[]
		time=0

		for ele in courses:
			if ele[0]+time<=ele[1]:
				heappush(h,-ele[0])
				time+=ele[0]

			else:
				if h:
					if ele[0]<-h[0]:
						time-=-(heappop(h))
						time+=ele[0]
						heappush(h,-ele[0])

		return len(h)
        