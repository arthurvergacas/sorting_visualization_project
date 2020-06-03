import pygame
import pygame_gui

import threading #AAAAA MONNNNSTERRRRRR BIRRRRRRRRRRRRRRRRR (in a good way)
import time

from sorting import SortingMethods
from animation import Animations

class SortGUI:

	number = None

	def __init__(self):


		self.sort_met = SortingMethods()
		self.ani = Animations()
		

		self.minValue = None
		self.maxValue = None

		pygame.init()

		pygame.display.set_caption("Sorting Algorithms Visualization")

		self.window_surface = pygame.display.set_mode((800, 600))
		self.window_surface.convert_alpha()
		self.ui_manager = pygame_gui.UIManager((800, 600), 'theme.json')

		self.background = pygame.Surface((800, 600))
		self.background.fill(pygame.Color('#4D4D4D'))


		#----FONTS--------

		self.regular_font = pygame.font.Font('./fonts/OpenSans-Regular.ttf', 14)
		self.tiny_regular_font = pygame.font.Font('./fonts/OpenSans-SemiBold.ttf', 11)
		self.large_bold_font = pygame.font.Font('./fonts/OpenSans-SemiBold.ttf', 18)
		self.medium_bold_font = pygame.font.Font('./fonts/OpenSans-SemiBold.ttf', 14)
		self.bold_font = pygame.font.Font('./fonts/OpenSans-SemiBold.ttf', 16)


		#-----BUTTONS-----
		self.selection_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(50, 275, 125, 50), text = "Selection Sort", manager = self.ui_manager)
		self.bubble_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(242, 275, 125, 50), text = "Bubble Sort", manager = self.ui_manager)
		self.insertion_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(434, 275, 125, 50), text = "Insertion Sort", manager = self.ui_manager)
		self.merge_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(626, 275, 125, 50), text = "Merge Sort", manager = self.ui_manager)




		#----INPUT-------
		self.input_box = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect(40, 51, 415, 60), manager = self.ui_manager)
		allowed_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
		self.input_box.set_allowed_characters(allowed_char)



		self.custom_array_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(475, 40, 250, 50), text = "Create Custom Array", manager = self.ui_manager)



		self.input_minValue = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect(280, 135, 100, 60), manager = self.ui_manager)
		self.input_minValue.set_allowed_characters('numbers')

		self.input_maxValue = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect(280, 170, 100, 60), manager = self.ui_manager)
		self.input_maxValue.set_allowed_characters('numbers')



		self.create_array_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(475, 142, 250, 50), text = "Create Random Array", manager = self.ui_manager)		



		#-----SCREEN TEXT-----
		#custom array
		self.custom_text = self.large_bold_font.render("Create custom array:", True, (255, 255, 255))
		self.custom_info = self.tiny_regular_font.render("Each array element separated by spaces", True, (140, 140, 139))

		#random array
		self.random_text = self.large_bold_font.render("Create random array:", True, (255, 255, 255))
		self.random_info = self.tiny_regular_font.render("Use it to create large arrays", True, (140, 140, 139))

		self.min_text = self.medium_bold_font.render("Minimun value of your array:", True, (255, 255, 255))
		self.max_text = self.medium_bold_font.render("Maximum value of your array:", True, (255, 255, 255))

		#warning that the user haven't set the array
		self.warn_no_array = self.medium_bold_font.render("You must first create an array", True, (20, 20, 20))

		#warning that the user haven't set an input value
		self.warn_no_input = self.bold_font.render("You must first type an array, or set minimun and maximum values", True, (255, 255, 255))

		#array created text
		self.array_created_text = self.large_bold_font.render("Array Created", True, (255, 255, 255))

		#"made by" text
		self.made_by_text = self.regular_font.render("Made by Arthur Vergaças", True, (150, 150, 150))


		#----SORT TEXT BOOLEANS--------
		self.selec_bool = False
		self.bubble_bool = False
		self.insert_bool = False
		self.merge_bool = False


		#-----WARNING TEXT BOOLEANS AND SLEEPS-----
		self.no_array_bool = False
		self.no_array_sleep = 0

		self.no_input = False
		self.no_input_sleep = 0

		self.array_created = False
		self.array_created_sleep = 0




		#----ANIMATION BOOLEANS------
		self.selec_ani_bool = False
		self.bubble_ani_bool = False
		self.insert_ani_bool = False
		self.merge_ani_bool = False

		#----ANIMATION COUNTERS-----

		self.selec_index = 0
		self.current_time_selec = 0
		

		self.bubble_index = 0
		self.current_time_bubble = 0

		self.insert_index = 0
		self.current_time_insert = 0

		self.merge_index = 0
		self.current_time_merge = 0




		#-----THREADING------
		#loading text bools

		#----selection----
		self.selec_sorting_loading_bool = False
		self.selec_creating_loading_bool = False

		#----bubble----
		self.bubble_sorting_loading_bool = False
		self.bubble_creating_loading_bool = False

		#----insertion----
		self.insert_sorting_loading_bool = False
		self.insert_creating_loading_bool = False

		#----merge----
		self.merge_sorting_loading_bool = False
		self.merge_creating_loading_bool = False


		#loading texts
		self.sorting_loading0 = self.large_bold_font.render("Sorting array.", True, (255, 255, 255))
		self.sorting_loading1 = self.large_bold_font.render("Sorting array..", True, (255, 255, 255))
		self.sorting_loading2 = self.large_bold_font.render("Sorting array...", True, (255, 255, 255))
		self.sorting_loading = [self.sorting_loading0, self.sorting_loading1, self.sorting_loading2]

		self.current_time_sorting = 0
		self.index_sorting = 0


		self.creating_loading0 = self.large_bold_font.render("Creating animation.", True, (255, 255, 255))
		self.creating_loading1 = self.large_bold_font.render("Creating animation..", True, (255, 255, 255))
		self.creating_loading2 = self.large_bold_font.render("Creating animation...", True, (255, 255, 255))
		self.creating_loading = [self.creating_loading0, self.creating_loading1, self.creating_loading2]

		self.current_time_creating = 0
		self.index_creating = 0

		#SELECT
		self.selec_bool_text_thread = False

		#BUBBLE
		self.bubble_bool_text_thread = False

		#INSERT
		self.insert_bool_text_thread = False

		#MERGE
		self.merge_bool_text_thread = False





		#setup for running
		self.is_running = True
		self.clock = pygame.time.Clock()

	#functions to create the text
	def create_selec_text(self):
		time_selec_text = self.sort_met.elapsedTime_selection
		selec_text = "Time elapsed: {}".format(time_selec_text)
		self.ui_selec_text = self.regular_font.render(selec_text, True, (255, 255, 255))	

	def create_bubble_text(self):
		time_bubble_text = self.sort_met.elapsedTime_bubble
		bubble_text = "Time elapsed: {}".format(time_bubble_text)
		self.ui_bubble_text = self.regular_font.render(bubble_text, True, (255, 255, 255))

	def create_insert_text(self):
		time_insert_text = self.sort_met.elapsedTime_insertion
		insert_text = "Time elapsed: {}".format(time_insert_text)
		self.ui_insert_text = self.regular_font.render(insert_text, True, (255, 255, 255))

	def create_merge_text(self):
		time_merge_text = self.sort_met.elapsedTime_merge
		merge_text = "Time elapsed: {}".format(time_merge_text)
		self.ui_merge_text = self.regular_font.render(merge_text, True, (255, 255, 255))
		


	#function to get user input of any box entry and TRASNFORMS IT TO A LIST OF INTS
	def get_user_input(self, box_entry):

		input_text = box_entry.get_text()
		input_text = input_text.split()
		input_text = [int(i) for i in input_text]

		return input_text
			

	def call_select_thread(self):
		self.selec_sorting_loading_bool = True
		
		
		self.sort_met.SelectionSort(SortGUI.number.copy())
		

		self.selec_sorting_loading_bool = False


		self.selec_creating_loading_bool = True
		
		self.selec_imgs = self.ani.create_img_array('selection')
		
		self.selec_creating_loading_bool = False


		self.create_selec_text()

		self.selec_bool_text_thread = True

		self.selec_ani_bool = not self.selec_ani_bool

		


	def call_bubble_thread(self):
		self.bubble_sorting_loading_bool = True

		
		self.sort_met.BubbleSort(SortGUI.number.copy())

		self.bubble_sorting_loading_bool = False


		self.bubble_creating_loading_bool = True
		
		self.bubble_imgs = self.ani.create_img_array('bubble')
		
		self.bubble_creating_loading_bool = False


		self.create_bubble_text()

		self.bubble_bool_text_thread = True

		self.bubble_ani_bool = not self.bubble_ani_bool



	def call_insert_thread(self):
		self.insert_sorting_loading_bool = True
	
		
		self.sort_met.InsertionSort(SortGUI.number.copy())


		self.insert_sorting_loading_bool = False

		self.insert_creating_loading_bool = True

		self.insert_imgs = self.ani.create_img_array('insertion')

		self.insert_creating_loading_bool = False


		self.create_insert_text()

		self.insert_bool_text_thread = True

		self.insert_ani_bool = not self.insert_ani_bool


	def call_merge_thread(self):
		self.merge_sorting_loading_bool = True
		
		
		self.sort_met.merge_bool_s = True #thing to make merge work
		self.sort_met.CallMerge(SortGUI.number.copy())

		

		self.merge_sorting_loading_bool = False

		self.merge_creating_loading_bool = True

		self.merge_imgs = self.ani.create_img_array('merge')

		self.merge_creating_loading_bool = False


		self.create_merge_text()

		self.merge_bool_text_thread = True

		self.merge_ani_bool = not self.merge_ani_bool


	def loading_sort(self, x_pos, y_pos):
		self.current_time_sorting += self.dt_loading

		if self.current_time_sorting >= 0.5:
			self.index_sorting += 1
			self.current_time_sorting = 0

		if self.index_sorting >= len(self.sorting_loading):
			self.index_sorting = 0

		self.window_surface.blit(self.sorting_loading[self.index_sorting], (x_pos, y_pos))

	def loading_images(self, x_pos, y_pos):
		self.current_time_creating += self.dt_loading

		if self.current_time_creating >= 0.5:
			self.index_creating += 1
			self.current_time_creating = 0

		if self.index_creating >= len(self.creating_loading):
			self.index_creating = 0 

		self.window_surface.blit(self.creating_loading[self.index_creating], (x_pos, y_pos))

	
	

	#------MAIN LOOP------
	def run(self):


		while self.is_running:

			delta_time = self.clock.tick(30)/1000.0
			self.dt_loading = delta_time

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.is_running = False

				#---- SORT BUTTONS------


				if event.type == pygame.USEREVENT:
					if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
						if event.ui_element == self.selection_button:

							if self.selec_ani_bool == True:
								selec_is_done = True


							if SortGUI.number is not None:
								if not self.selec_bool:


									self.selec_bool_text_thread = False

									selec_main_thread = threading.Thread(target = self.call_select_thread)
									selec_main_thread.daemon = True
									selec_main_thread.start()
									selec_initialize = True

									selec_ani_x = 20
									selec_ani_y = 358
									
								self.selec_bool = not self.selec_bool

							elif SortGUI.number is None:
								no_array_x = 15
								no_array_y = 325
								if self.no_array_sleep != 0:
									self.no_array_sleep -= 50 
								self.no_array_bool = True
								
				if event.type == pygame.USEREVENT:
					if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
						if event.ui_element == self.bubble_button:

							if self.bubble_ani_bool:
								bubble_is_done = True

							if SortGUI.number is not None:
								if not self.bubble_bool:
									

									self.bubble_bool_text_thread = False

									bubble_main_thread = threading.Thread(target = self.call_bubble_thread)
									bubble_main_thread.daemon = True
									bubble_main_thread.start()
									bubble_initialize = True

									bubble_ani_x = 215
									bubble_ani_y = 358

								self.bubble_bool = not self.bubble_bool	

							elif SortGUI.number is None:
								no_array_x = 205
								no_array_y = 325
								if self.no_array_sleep != 0:
									self.no_array_sleep -= 50
								self.no_array_bool = True

				if event.type == pygame.USEREVENT:
					if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
						if event.ui_element == self.insertion_button:

							if self.insert_ani_bool:
								insert_is_done = True

							if SortGUI.number is not None:
								if self.insert_bool == False:


									self.insert_bool_text_thread = False

									insert_main_thread = threading.Thread(target = self.call_insert_thread)
									insert_main_thread.daemon = True
									insert_main_thread.start()
									insert_initialize = True

									insert_ani_x = 410
									insert_ani_y = 358

									
								self.insert_bool = not self.insert_bool		

							elif SortGUI.number is None:
								no_array_x = 397
								no_array_y = 325
								if self.no_array_sleep != 0:
									self.no_array_sleep -= 50
								self.no_array_bool = True								

				if event.type == pygame.USEREVENT:
					if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
						if event.ui_element == self.merge_button:

							if self.merge_ani_bool:
								merge_is_done = True


							if SortGUI.number is not None:
								if not self.merge_bool:
									

									self.merge_bool_text_thread = False

									merge_main_thread = threading.Thread(target = self.call_merge_thread)
									merge_main_thread.daemon = True
									merge_main_thread.start()
									merge_initialize = True

									merge_ani_x = 605
									merge_ani_y = 358

								self.merge_bool = not self.merge_bool

							elif SortGUI.number is None:
								no_array_x = 587
								no_array_y = 325
								if self.no_array_sleep != 0:
									self.no_array_sleep -= 50
								self.no_array_bool = True


				#----ARRAY CREATION BUTTONS-----

				if event.type == pygame.USEREVENT:
					if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
						if event.ui_element == self.custom_array_button:
							
							

							
							if self.get_user_input(self.input_box):
								#handle animation time dynamically
								SortGUI.number = self.get_user_input(self.input_box)
								self.no_array_bool = False

								ani_time = 0.1 / (len(SortGUI.number) * 0.015)
								print(ani_time)		
								self.array_created = True
										
							else:
								self.no_input = True
								
							

				if event.type == pygame.USEREVENT:
					if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
						if event.ui_element == self.create_array_button:
							
							self.minValue = self.input_minValue.get_text()
							if self.get_user_input(self.input_minValue):
								self.minValue = int(self.minValue)

								self.maxValue = self.input_maxValue.get_text()
								if self.get_user_input(self.input_maxValue):
									self.maxValue = int(self.maxValue)

									SortGUI.number = self.sort_met.CreateArray(self.minValue, self.maxValue)
									self.no_array_bool = False
									
									ani_time = 0.1 / (len(SortGUI.number) * 0.025)
									print(ani_time)
									self.array_created = True
								else:
									self.no_input = True
									
							else:
								self.no_input = True
																						


							

				self.ui_manager.process_events(event)

			#setup stuff
			self.ui_manager.update(delta_time)
			self.window_surface.blit(self.background, (0, 0))
			self.ui_manager.draw_ui(self.window_surface)	

			#display custom text
			self.window_surface.blit(self.custom_text, (20, 10))
			self.window_surface.blit(self.custom_info, (30, 32))
			
			#display random text
			self.window_surface.blit(self.random_text, (20, 100))
			self.window_surface.blit(self.random_info, (30, 122))

			self.window_surface.blit(self.min_text, (40, 140))
			self.window_surface.blit(self.max_text, (40, 175))

			#display made by text
			self.window_surface.blit(self.made_by_text, (620, 7))



			#if statements for text
			if self.selec_bool and self.selec_bool_text_thread:
				self.window_surface.blit(self.ui_selec_text, (35, 250))

			if self.bubble_bool and self.bubble_bool_text_thread:
				self.window_surface.blit(self.ui_bubble_text, (227, 250))

			if self.insert_bool and self.insert_bool_text_thread:
				self.window_surface.blit(self.ui_insert_text, (419, 250))

			if self.merge_bool and self.merge_bool_text_thread:
				self.window_surface.blit(self.ui_merge_text, (611, 250))

			if self.no_array_bool:
				self.window_surface.blit(self.warn_no_array, (no_array_x, no_array_y))

				self.no_array_sleep += 1
				
				if self.no_array_sleep > 250:
					self.no_array_bool = False
					self.no_array_sleep = 0

			if self.get_user_input(self.input_box) or self.get_user_input(self.input_maxValue) and self.get_user_input(self.input_minValue):
				self.no_input = False

			if self.no_input:
				self.window_surface.blit(self.warn_no_input, (125, 225))

				self.no_input_sleep += 1

				if self.no_input_sleep > 250:
					self.no_input = False
					self.no_input_sleep = 0
			
			if self.array_created:
				self.window_surface.blit(self.array_created_text, (340, 430))

				self.array_created_sleep += 1

				if self.array_created_sleep > 60:
					self.array_created = False
					self.array_created_sleep = 0


			#ANIMATIONS

			#SELECTION LOADING
			if self.selec_sorting_loading_bool:
				self.loading_sort(55, 328)
			if self.selec_creating_loading_bool:
				self.loading_images(25, 328)

			#SELECTION

			if self.selec_ani_bool:

				

				if selec_initialize:
					selec_backward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(selec_ani_x + 3, selec_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#backward_button")
					selec_play_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(selec_ani_x + 46, selec_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#play_button")
					selec_pause_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(selec_ani_x + 89, selec_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#pause_button")
					selec_forward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(selec_ani_x + 132, selec_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#forward_button")
					selec_exit_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(selec_ani_x + 58, selec_ani_y - 30,60, 30), text = 'Close', starting_height = 100, manager = self.ui_manager)

					selec_pause_button.disable()

					selec_modes = {
						"mode": ""
					}

					selec_is_done = False

					selec_check_pause = False

					selec_initialize = False

				if selec_play_button.check_pressed(): 
					selec_modes["mode"] = "play"
				if selec_pause_button.check_pressed():
					selec_modes["mode"] = "pause"
				if selec_forward_button.check_pressed():
					selec_modes["mode"] = "forward"
				if selec_backward_button.check_pressed():
					selec_modes["mode"] = "backward"
				if selec_exit_button.check_pressed():
					selec_is_done = True


				if selec_modes["mode"] == "play":

					if selec_check_pause == False:
						selec_play_button.disable()
						selec_pause_button.enable()
						selec_check_pause = True

					self.current_time_selec += delta_time

					
					if self.current_time_selec >= ani_time:
						self.selec_index += 1
						self.current_time_selec = 0

					if self.selec_index < len(self.selec_imgs):	
						self.window_surface.blit(self.selec_imgs[self.selec_index], (selec_ani_x, selec_ani_y))
						
					else:
						self.selec_index = len(self.selec_imgs) - 1
						self.window_surface.blit(self.selec_imgs[self.selec_index], (selec_ani_x, selec_ani_y))

					if selec_is_done:
						self.selec_index = 0
						self.selec_ani_bool = False

						selec_play_button.kill()
						selec_pause_button.kill()
						selec_forward_button.kill()
						selec_backward_button.kill()
						selec_exit_button.kill()

						self.selec_bool = False




				elif selec_modes["mode"] == "pause":
					if selec_check_pause:
						selec_pause_button.disable()
						selec_play_button.enable()
						selec_check_pause = False

					self.window_surface.blit(self.selec_imgs[self.selec_index], (selec_ani_x, selec_ani_y))

					if selec_is_done:
						self.selec_index = 0
						self.selec_ani_bool = False

						selec_play_button.kill()
						selec_pause_button.kill()
						selec_forward_button.kill()
						selec_backward_button.kill()
						selec_exit_button.kill()

						self.selec_bool = False



				elif selec_modes["mode"] == "forward" and selec_is_done == False:
					if self.selec_index < len(self.selec_imgs) - 1:
						self.selec_index += 1
						self.window_surface.blit(self.selec_imgs[self.selec_index], (selec_ani_x, selec_ani_y))
						selec_modes["mode"] = "pause"

					else:
						selec_is_done = True

				elif selec_modes["mode"] == "backward" and selec_is_done == False:
					if self.selec_index > 0:
						self.selec_index -= 1
						selec_modes["mode"] = "pause"
					self.window_surface.blit(self.selec_imgs[self.selec_index], (selec_ani_x, selec_ani_y))
					


				elif selec_is_done:
					self.selec_index = 0
					self.selec_ani_bool = False

					selec_play_button.kill()
					selec_pause_button.kill()
					selec_forward_button.kill()
					selec_backward_button.kill()
					selec_exit_button.kill()

					self.selec_bool = False

					
				#to start the animation stopped
				else:
					self.window_surface.blit(self.selec_imgs[0], (selec_ani_x, selec_ani_y))



			#BUBBLE

			#BUBBLE LOADING
			if self.bubble_sorting_loading_bool:
				self.loading_sort(247, 328)
			if self.bubble_creating_loading_bool:
				self.loading_images(217, 328)

			if self.bubble_ani_bool:
				

				if bubble_initialize:
					bubble_backward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(bubble_ani_x + 3, bubble_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#backward_button")
					bubble_play_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(bubble_ani_x + 46, bubble_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#play_button")
					bubble_pause_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(bubble_ani_x + 89, bubble_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#pause_button")
					bubble_forward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(bubble_ani_x + 132, bubble_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#forward_button")
					bubble_exit_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(bubble_ani_x + 58, bubble_ani_y - 30,60, 30), text = 'Close', starting_height = 100, manager = self.ui_manager)


					bubble_pause_button.disable()

					bubble_modes = {
						"mode": ""
					}

					bubble_is_done = False

					bubble_check_pause = False

					bubble_initialize = False

				if bubble_play_button.check_pressed(): 
					bubble_modes["mode"] = "play"
				if bubble_pause_button.check_pressed():
					bubble_modes["mode"] = "pause"
				if bubble_forward_button.check_pressed():
					bubble_modes["mode"] = "forward"
				if bubble_backward_button.check_pressed():
					bubble_modes["mode"] = "backward"
				if bubble_exit_button.check_pressed():
					bubble_is_done = True


				if bubble_modes["mode"] == "play":

					if bubble_check_pause == False:
						bubble_play_button.disable()
						bubble_pause_button.enable()
						bubble_check_pause = True

					self.current_time_bubble += delta_time

					
					if self.current_time_bubble >= ani_time:
						self.bubble_index += 1
						self.current_time_bubble = 0

					if self.bubble_index < len(self.bubble_imgs):	
						self.window_surface.blit(self.bubble_imgs[self.bubble_index], (bubble_ani_x, bubble_ani_y))
						
					else:
						self.bubble_index = len(self.bubble_imgs) - 1
						self.window_surface.blit(self.bubble_imgs[self.bubble_index], (bubble_ani_x, bubble_ani_y))

					if bubble_is_done:
						self.bubble_index = 0
						self.bubble_ani_bool = False

						bubble_play_button.kill()
						bubble_pause_button.kill()
						bubble_forward_button.kill()
						bubble_backward_button.kill()
						bubble_exit_button.kill()

						self.bubble_bool = False


				elif bubble_modes["mode"] == "pause":
					if bubble_check_pause:
						bubble_pause_button.disable()
						bubble_play_button.enable()
						bubble_check_pause = False

					self.window_surface.blit(self.bubble_imgs[self.bubble_index], (bubble_ani_x, bubble_ani_y))

					if bubble_is_done:
						self.bubble_index = 0
						self.bubble_ani_bool = False

						bubble_play_button.kill()
						bubble_pause_button.kill()
						bubble_forward_button.kill()
						bubble_backward_button.kill()
						bubble_exit_button.kill()
						self.bubble_bool = False


				elif bubble_modes["mode"] == "forward" and bubble_is_done == False:
					if self.bubble_index < len(self.bubble_imgs) - 1:
						self.bubble_index += 1
						self.window_surface.blit(self.bubble_imgs[self.bubble_index], (bubble_ani_x, bubble_ani_y))
						bubble_modes["mode"] = "pause"

					else:
						bubble_is_done = True

				elif bubble_modes["mode"] == "backward" and bubble_is_done == False:
					if self.bubble_index > 0:
						self.bubble_index -= 1
						bubble_modes["mode"] = "pause"
					self.window_surface.blit(self.bubble_imgs[self.bubble_index], (bubble_ani_x, bubble_ani_y))
					


				elif bubble_is_done:
					self.bubble_index = 0
					self.bubble_ani_bool = False

					bubble_play_button.kill()
					bubble_pause_button.kill()
					bubble_forward_button.kill()
					bubble_backward_button.kill()
					bubble_exit_button.kill()
					self.bubble_bool = False


					
				#to start the animation stopped
				else:
					self.window_surface.blit(self.bubble_imgs[0], (bubble_ani_x, bubble_ani_y))




			#INSERTION

			#INSERTION LOADING
			if self.insert_sorting_loading_bool:
				self.loading_sort(439, 328)
			if self.insert_creating_loading_bool:
				self.loading_images(409, 328)

			if self.insert_ani_bool:
				

				if insert_initialize:
					insert_backward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(insert_ani_x + 3, insert_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#backward_button")
					insert_play_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(insert_ani_x + 46, insert_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#play_button")
					insert_pause_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(insert_ani_x + 89, insert_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#pause_button")
					insert_forward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(insert_ani_x + 132, insert_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#forward_button")
					insert_exit_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(insert_ani_x + 58, insert_ani_y - 30,60, 30), text = 'Close', starting_height = 100, manager = self.ui_manager)


					insert_pause_button.disable()

					insert_modes = {
						"mode": ""
					}

					insert_is_done = False

					insert_check_pause = False

					insert_initialize = False

				if insert_play_button.check_pressed(): 
					insert_modes["mode"] = "play"
				if insert_pause_button.check_pressed():
					insert_modes["mode"] = "pause"
				if insert_forward_button.check_pressed():
					insert_modes["mode"] = "forward"
				if insert_backward_button.check_pressed():
					insert_modes["mode"] = "backward"
				if insert_exit_button.check_pressed():
					insert_is_done = True


				if insert_modes["mode"] == "play":

					if insert_check_pause == False:
						insert_play_button.disable()
						insert_pause_button.enable()
						insert_check_pause = True

					self.current_time_insert += delta_time

					
					if self.current_time_insert >= ani_time:
						self.insert_index += 1
						self.current_time_insert = 0

					if self.insert_index < len(self.insert_imgs):	
						self.window_surface.blit(self.insert_imgs[self.insert_index], (insert_ani_x, insert_ani_y))
						
					else:
						self.insert_index = len(self.insert_imgs) - 1
						self.window_surface.blit(self.insert_imgs[self.insert_index], (insert_ani_x, insert_ani_y))

					if insert_is_done:
						self.insert_index = 0
						self.insert_ani_bool = False

						insert_play_button.kill()
						insert_pause_button.kill()
						insert_forward_button.kill()
						insert_backward_button.kill()
						insert_exit_button.kill()

						self.insert_bool = False


				elif insert_modes["mode"] == "pause":
					if insert_check_pause:
						insert_pause_button.disable()
						insert_play_button.enable()
						insert_check_pause = False

					self.window_surface.blit(self.insert_imgs[self.insert_index], (insert_ani_x, insert_ani_y))

					if insert_is_done:
						self.insert_index = 0
						self.insert_ani_bool = False

						insert_play_button.kill()
						insert_pause_button.kill()
						insert_forward_button.kill()
						insert_backward_button.kill()
						insert_exit_button.kill()

						self.insert_bool = False


				elif insert_modes["mode"] == "forward" and insert_is_done == False:
					if self.insert_index < len(self.insert_imgs) - 1:
						self.insert_index += 1
						self.window_surface.blit(self.insert_imgs[self.insert_index], (insert_ani_x, insert_ani_y))
						insert_modes["mode"] = "pause"

					else:
						insert_is_done = True

				elif insert_modes["mode"] == "backward" and insert_is_done == False:
					if self.insert_index > 0:
						self.insert_index -= 1
						insert_modes["mode"] = "pause"
					self.window_surface.blit(self.insert_imgs[self.insert_index], (insert_ani_x, insert_ani_y))
					


				elif insert_is_done:
					self.insert_index = 0
					self.insert_ani_bool = False

					insert_play_button.kill()
					insert_pause_button.kill()
					insert_forward_button.kill()
					insert_backward_button.kill()
					insert_exit_button.kill()

					self.insert_bool = False

				#to start the animation stopped
				else:
					self.window_surface.blit(self.insert_imgs[0], (insert_ani_x, insert_ani_y))
	


			#MERGE

			#MERGE LOADING
			if self.merge_sorting_loading_bool:
				self.loading_sort(631, 328)
			if self.merge_creating_loading_bool:
				self.loading_images(601, 328)

			if self.merge_ani_bool:
				

				if merge_initialize:
					merge_backward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(merge_ani_x + 3, merge_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#backward_button")
					merge_play_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(merge_ani_x + 46, merge_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#play_button")
					merge_pause_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(merge_ani_x + 89, merge_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#pause_button")
					merge_forward_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(merge_ani_x + 132, merge_ani_y + 180, 40, 40), text = '', manager = self.ui_manager, object_id = "#forward_button")
					merge_exit_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(merge_ani_x + 58, merge_ani_y - 30,60, 30), text = 'Close', starting_height = 100, manager = self.ui_manager)


					merge_pause_button.disable()

					merge_modes = {
						"mode": ""
					}

					merge_is_done = False

					merge_check_pause = False

					merge_initialize = False

				if merge_play_button.check_pressed(): 
					merge_modes["mode"] = "play"
				if merge_pause_button.check_pressed():
					merge_modes["mode"] = "pause"
				if merge_forward_button.check_pressed():
					merge_modes["mode"] = "forward"
				if merge_backward_button.check_pressed():
					merge_modes["mode"] = "backward"
				if merge_exit_button.check_pressed():
					merge_is_done = True


				if merge_modes["mode"] == "play":

					if merge_check_pause == False:
						merge_play_button.disable()
						merge_pause_button.enable()
						merge_check_pause = True

					self.current_time_merge += delta_time

					
					if self.current_time_merge >= ani_time:
						self.merge_index += 1
						self.current_time_merge = 0

					if self.merge_index < len(self.merge_imgs):	
						self.window_surface.blit(self.merge_imgs[self.merge_index], (merge_ani_x, merge_ani_y))
						
					else:
						self.merge_index = len(self.merge_imgs) - 1
						self.window_surface.blit(self.merge_imgs[self.merge_index], (merge_ani_x, merge_ani_y))

					if merge_is_done:
						self.merge_index = 0
						self.merge_ani_bool = False

						merge_play_button.kill()
						merge_pause_button.kill()
						merge_forward_button.kill()
						merge_backward_button.kill()
						merge_exit_button.kill()

						self.merge_bool = False

				elif merge_modes["mode"] == "pause":
					if merge_check_pause:
						merge_pause_button.disable()
						merge_play_button.enable()
						merge_check_pause = False

					self.window_surface.blit(self.merge_imgs[self.merge_index], (merge_ani_x, merge_ani_y))

					if merge_is_done:
						self.merge_index = 0
						self.merge_ani_bool = False

						merge_play_button.kill()
						merge_pause_button.kill()
						merge_forward_button.kill()
						merge_backward_button.kill()
						merge_exit_button.kill()

						self.merge_bool = False



				elif merge_modes["mode"] == "forward" and merge_is_done == False:
					if self.merge_index < len(self.merge_imgs) - 1:
						self.merge_index += 1
						self.window_surface.blit(self.merge_imgs[self.merge_index], (merge_ani_x, merge_ani_y))
						merge_modes["mode"] = "pause"

					else:
						merge_is_done = True

				elif merge_modes["mode"] == "backward" and merge_is_done == False:
					if self.merge_index > 0:
						self.merge_index -= 1
						merge_modes["mode"] = "pause"
					self.window_surface.blit(self.merge_imgs[self.merge_index], (merge_ani_x, merge_ani_y))
					


				elif merge_is_done:
					self.merge_index = 0
					self.merge_ani_bool = False

					merge_play_button.kill()
					merge_pause_button.kill()
					merge_forward_button.kill()
					merge_backward_button.kill()
					merge_exit_button.kill()

					self.merge_bool = False


					
				#to start the animation stopped
				else:
					self.window_surface.blit(self.merge_imgs[0], (merge_ani_x, merge_ani_y))




			pygame.display.update()

if __name__ == "__main__":

	app = SortGUI()

	app.run()