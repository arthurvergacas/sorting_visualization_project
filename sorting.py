'''
Selection Sort   |
Bubble Sort      | <--- O(n^2), ou seja, se eu aumento n 10 vezes, o tempo 
Insertion Sort   |       de execução aumenta 100 vezes (10^2) 
Merge Sort       <----- O(n log n), ou seja, se eu aumento n 10 vezes, o tempo 
                        vai aumentar mais ou menos 10 vezes (10 log 10 = 10)
'''
from timeit import default_timer as timer
from image_creator import CreateImages
import random


class SortingMethods:
	
	def __init__(self):

		self.elapsedTime_selection = 0
		self.elapsedTime_bubble = 0
		self.elapsedTime_insertion = 0
		self.elapsedTime_merge = 0

		self.selec_img = CreateImages()
		self.bubble_img = CreateImages()
		self.insert_img = CreateImages()
		self.merge_img = CreateImages()

		#booleans to handle animations of each algorithm
		self.select_ani = False
		self.bubble_ani = False
		self.insert_ani = False
		self.merge_ani = False


		#merge sort stuff to make it work (don't ask me why and how)
		self.steps = 0
		self.count = 0
		self.original = []
		self.temp = self.original
		self.merge_bool_s = True
		self.temp_array = [1]


	def SelectionSort(self, array):
		self.selec_img.img_steps = 0 

		self.selec_img.delete_all('selection') #<-- deleting previous files

		moves = 0
		steps = 0
		self.selec_img.create_frame(array, len(array), 'selection')

		#print("---SelectionSort---")

		start = timer()
		
		for i in range(len(array) - 1):

			minJ = i 
			
			for j in range(i + 1, len(array)):
				if array[j] < array[minJ]:
					minJ = j
				moves += 1

			array[i], array[minJ] = array[minJ], array[i]
			steps += 1
			self.selec_img.create_frame(array, len(array), 'selection')

		end = timer()
		self.elapsedTime_selection = str("{:.6f}".format(end - start))

		#print("Time elapsed:", self.elapsedTime_selection, " seconds")
		#print("Moves: ", moves, "\n")


		#ensure that images have been created
		# while self.select_ani == False:
		# 	if self.img.check_img('selection', steps) == True:
		# 		self.select_ani = True

		return array	

	def BubbleSort(self, array):
		self.bubble_img.img_steps = 0 

		self.bubble_img.delete_all('bubble')

		moves = 0
		steps = 0
		self.bubble_img.create_frame(array, len(array), 'bubble')

		#print("---BubbleSort---")

		start = timer()

		incomplete = True
		n = 1

		while(incomplete):
			incomplete = False
			for i in range(len(array) - n):
				if array[i] > array[i + 1]:
					array[i], array[i + 1] = array[i + 1], array[i]
					incomplete = True
				moves += 1
			steps += 1
			self.bubble_img.create_frame(array, len(array), 'bubble')
			n += 1

		end = timer()
		self.elapsedTime_bubble = str("{:.6f}".format(end - start))

		#print("Time elapsed: ", self.elapsedTime_bubble, " seconds")
		#print("Moves: ", moves, "\n")

		#ensure that images have been created
		# while self.bubble_ani == False:
		# 	if self.img.check_img('bubble', steps) == True:
		# 		self.bubble_ani = True

		return array

	def InsertionSort(self, array):
		self.insert_img.img_steps = 0 

		self.insert_img.delete_all('insertion')

		moves = 0
		steps = 0
		self.insert_img.create_frame(array, len(array), 'insertion')

		#print("---InsertionSort---")

		start = timer()

		for i in range(1, len(array)):

			temp = array[i]
			j = i

			while j > 0 and temp < array[j - 1]:
				array[j] = array[j - 1]
				j -= 1
				moves += 1
			array[j] = temp
			moves += 1
			steps += 1
			self.insert_img.create_frame(array.copy(), len(array), 'insertion')

		end = timer()
		self.elapsedTime_insertion = str("{:.6f}".format(end - start))

		#print("Time elapsed:", self.elapsedTime_insertion, " seconds")
		#print("Moves: ", moves, "\n")


		return array


	def MergeSort(self, array):

		if self.merge_bool_s:
			self.steps = 0
			self.count = 0
			self.original = array
			self.temp = self.original
			self.merge_bool_s = False
			self.temp_array = [1]





		if len(array) > 1:

			middle = len(array)//2

			leftArray = array[:middle]
			rightArray = array[middle:]


			self.MergeSort(leftArray)
			self.MergeSort(rightArray)

			l = 0
			r = 0
			a = 0

			while l < len(leftArray) and r < len(rightArray):

				if leftArray[l] < rightArray[r]:
					array[a] = leftArray[l]
					l += 1
				else:
					array[a] = rightArray[r]
					r += 1
				a += 1


			while l < len(leftArray):
				array[a] = leftArray[l]
				l += 1
				a += 1

			while r < len(rightArray):
				array[a] = rightArray[r]
				r += 1
				a += 1


		if len(array) != len(self.temp_array):
			self.temp_array = array
			if len(array) != 1:
				self.count -= len(array)

		self.temp = self.original
		for i in range(len(array)):
			self.temp[self.count] = array[i]

			self.count += 1

		self.merge_img.create_frame(self.temp, len(self.temp), 'merge')
		self.steps += 1

		
		return array

	def CallMerge(self, array):
		self.merge_img.img_steps = 0 

		self.merge_img.delete_all('merge')
		
		#print("---MergeSort---\n")

		start = timer()

		

		x = self.MergeSort(array)

		end = timer()
		self.elapsedTime_merge = str("{:.6f}".format(end - start))
		
		#print("Time elapsed:", self.elapsedTime_merge , " seconds")

		return x

	def CreateArray(self, minValue, maxValue):

		#return numpy.random.randint(minValue, maxValue + 1, amount)
		x = list(range(minValue + 1, maxValue + 1))
		random.shuffle(x)

		return x

	def InitializeMergeVariables(self):
		self.steps = 0
		self.count = 0
		self.original = []
		self.temp = self.original
		self.merge_bool_s = True
		self.temp_array = [1]



if __name__ == "__main__":

	clss = SortingMethods()

	'''------se voce quiser escolher os numeros da array-------'''
	#numbers = input("Numbers: ").split()
	#numbers = [int(i) for i in numbers]



	# minValue = int(input("Coloque o valor mínimo: "))
	# maxValue = int(input("Coloque o valor máximo: "))
	# amount = int(input("Coloque o número de dígitos: "))
	# # # write = str(input("Quer ver a array ordenada? (s/n) "))
	# # print("\n")

	#numbers = clss.CreateArray(0, 10)
	# numbers = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	#print(numbers)

	# if write == 's':
	# 	SelectionSort(numbers)
	# 	BubbleSort(numbers)
	#   CallMerge(numbers)
	# 	print(InsertionSort(numbers), "\n")

	# else:
	# 	SelectionSort(numbers)
	# 	BubbleSort(numbers)
	# 	InsertionSort(numbers)
	#   CallMerge(numbers)
	# numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	#clss.SelectionSort(numbers)
	# BubbleSort(numbers)
	# print(clss.InsertionSort(numbers))
	# clss.MergeSort(numbers)
