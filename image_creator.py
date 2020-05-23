from PIL import Image, ImageDraw
import os
import pathlib



import random


class CreateImages:

	def __init__(self):

		self.WIDTH = 175
		self.HEIGHT = 175
		self.im = Image.new('RGB', (self.WIDTH, self.HEIGHT), color = "#4D4D4D")
		self.draw = ImageDraw.Draw(self.im)

		self.previous_arrays = [0]
		self.count = 0

		self.img_steps = 0



	def create_frame(self, array, array_len, sort_folder):

		chunck = 0
		if array_len <= 90:
			chunck = round(self.WIDTH / array_len)
		else:
			chunck = self.WIDTH / array_len


		self.draw.rectangle([0, 0, self.WIDTH, self.HEIGHT], fill = ("#4D4D4D"))

		x = array
		self.previous_arrays.append(array.copy())

		greatest = array[0]
		
		bar_width = chunck
		bar_height = self.HEIGHT - 50

		#algorithm to search the greatest value
		for i in array:

			if i > greatest:
				greatest = i

		if self.previous_arrays[self.count] != array:
			for i in range(array_len):

				x0 = (((chunck / 2) - (bar_width / 2)) + chunck*i) + 0.1 * chunck
				y0 = self.HEIGHT
				x1 = (((chunck / 2) + (bar_width / 2)) + chunck*i) - 0.1 * chunck
				y1 = self.HEIGHT - (bar_height * (array[i] / greatest))

				self.draw.rectangle([x0, y0, x1, y1], fill = (255, 255, 255))

			

			path = "./images/{}/img{}.jpg".format(sort_folder, self.img_steps)
			self.img_steps += 1

			self.im.save(fp = str(path), format = 'jpeg', quality = 60, optimize = True)

		self.count += 1

		


	def delete_all(self, directory):

		path = './images/{}'.format(directory)
		files = os.scandir(path)
		x = 0

		for i in files:
			if os.path.exists(i):
				os.remove(i)

	def check_img(self, directory, steps):

		path = './images/{}'.format(directory)
		count = 0

		for file in pathlib.Path(path).iterdir():
			if file.is_file():
				count += 1

			if count == steps + 1:
				return True 



			


if __name__ == "__main__":

	clss = CreateImages()

	x = list(range(1 + 1, 5000 + 1))
	random.shuffle(x)

	clss.create_frame(x, len(x), 0, 'bubble')

