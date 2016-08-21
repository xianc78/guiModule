# Module for simple GUI functions. ONLY WORKS IN WINDOWS
import ctypes

def MessageBox(message, title):
	ctypes.windll.user32.MessageBoxA(0, message, title, 0)
	
def YesNo(message, title):
	if ctypes.windll.user32.MessageBoxA(0, message, title, 4) == 6:
		return True
	else:
		return False
		
def OkCancel(message, title):
	if ctypes.windll.user32.MessageBoxA(0, message, title, 1) == 1:
		return True
	else:
		return False
		
def YesNoCancel(message, title):
	if ctypes.windll.user32.MessageBoxA(0, message, title, 3) == 6:
		return "Yes"
	elif ctypes.windll.user32.MessageBoxA(0, message, title, 3) == 7:
		return "No"
	else:
		return "Cancel"