import pygame
import os


class Animations:


	def create_img_array(self, directory):

		x = []
		path = './images/{}'.format(directory)

		for i in range(len(os.listdir(path))):
			file = '{}/img{}.jpg'.format(path, i)

			x.append(pygame.image.load(file))
			
		return x

if __name__ == "__main__":
	clss = Animations()

	x = clss.create_img_array('selection')


