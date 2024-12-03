def validate_type(value, type, message = "Недопустимый тип данных { vlaue_type }"):
	if not isinstance(value, type):
		raise TypeError(message.format(value_type=type(value).__name__))
