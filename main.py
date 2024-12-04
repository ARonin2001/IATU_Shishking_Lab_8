from ContractForAdditionalEducation import ContractForAdditionalEducation
from WorkWithContracts import WorkWithContracts
from DisplayTkinter import DisplayTkinter
from Diagram import Diagram

def display_diagram():
	is_diagram_by_courses = True

	courses = set({"Japanese", "Stingler", "English", "Frontend"})
	contract = ContractForAdditionalEducation(courses, "suck some dick", "Alex")
	courses2 = set({"Japanese", "Backend"})
	contract2 = ContractForAdditionalEducation(courses2, "suck 2", "Simon")

	contracts = set({contract, contract2})
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

def main():
	display_diagram()

if __name__ == "__main__":
	main()