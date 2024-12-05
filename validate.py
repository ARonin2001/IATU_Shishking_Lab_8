def validate_type(value, type, message = "Недопустимый тип данных "):
	if not isinstance(value, type):
		raise TypeError(message)
