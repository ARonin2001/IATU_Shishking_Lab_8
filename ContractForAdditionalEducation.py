from abc import ABC, abstractmethod
import validate

class AbstractContractEducation(ABC):
	@abstractmethod
	def add_course(self, course):
		pass

	@abstractmethod
	def remove_course(self, course):
		pass

	@abstractmethod
	def set_courses(self, courses):
		pass

class ContractForAdditionalEducation(AbstractContractEducation):
	__courses = set()

	def __init__(self, courses: set):
		validate.validate_type(courses, set, "Параметр: courses не является допустимым типом <set>")
		self.__courses = courses

	def add_course(self, course):
		self.__courses.add(course)

	def remove_course(self, course):
		try:
			self.__courses.remove(course)
		except:
			print(f"Курса {course} не существует в данном договоре")

	def set_courses(self, courses):
		validate.validate_type(courses, set, "Параметр: courses не является допустимым типом <set>")
		self.__courses = courses

	def get_courses(self):
		return self.__courses