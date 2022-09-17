def type_check(self, type_info):
	try:
		int(type_info)
	except ValueError as e:
		print(f"{e} / Please enter again...")
		return False
	except TypeError as e:
		print(f"{e} / Please enter again...")
		return False
	return True

