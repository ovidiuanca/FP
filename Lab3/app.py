from UI import *
from Repository import *
from Controller import *

def main():
	my_Repository = Repository()
	my_Controller = Controller(my_Repository)

	my_UI = UI(my_Controller)
	my_UI.do_menu()

if (__name__ == '__main__'):
	main()
