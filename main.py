"""
	Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом. 
	Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции). 
	Ввод данных из файла с контролем правильности ввода. 
	Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами.
 	Для GUI и визуализации использовать библиотеку tkinter.
	
	Вариант 20
	Объекты – договоры на дополнительное образование
	Функции:	сегментация полного списка договоров по названиям курсов
	визуализация предыдущей функции в форме круговой диаграммы
	сегментация полного списка договоров по обучающимся
	визуализация предыдущей функции в форме круговой диаграммы
"""

from ContractForAdditionalEducation import ContractForAdditionalEducation
from WorkWithContracts import WorkWithContracts
from DisplayTkinter import DisplayTkinter
from Diagram import Diagram

def read_courses():
	with open("numbersList.txt") as file:
		stringNumbers = [line.strip() for line in file if line.strip()]

def display_diagram(courses: dict):
	is_diagram_by_courses = False

	contracts = set()
	for item in courses:
		contact = ContractForAdditionalEducation(set(courses[item]), item)
		contracts.add(contact)

	workContracts = WorkWithContracts(contracts)

	segment = workContracts.set_segment_contracts()
	data_for_diagram = {}

	if is_diagram_by_courses:
		for course in segment:
			contractsTitle = ""
			for obj in segment[course]:
				contractsTitle += f" {obj.title},"
			data_for_diagram[f"course: {course} contracts: {contractsTitle}"] = len(segment[course])
			contractsTitle = ""
	else:
		for course in segment:
			for con in segment[course]:
				data_for_diagram[f"student: {con.get_student()} course: {course}"] = len(segment[course])

	window = DisplayTkinter()
	root = window.get_root()

	diagram = Diagram()
	diagram.create_pie_chart_from_dict(root, data_for_diagram)

	window.display()

def read_courses_file(filename="default.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        return None

    result = {}
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                name = parts[0].strip()
                skills = [word.strip() for word in parts[1].split(",")]
                if ',' not in parts[1]:
                    skills = [word.strip() for word in parts[1].split()]
                result[name] = skills
    return result

def main():
	courses = read_courses_file()

	display_diagram(courses)

if __name__ == "__main__":
	main()
