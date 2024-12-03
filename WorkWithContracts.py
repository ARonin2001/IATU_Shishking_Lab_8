from ContractForAdditionalEducation import AbstractContractEducation
import validate

class WorkWithContracts:
	__contracts = set()
	__segment_contracts = {}

	def __init__(self, contracts):
		validate.validate_type(contracts, set, "Параметр: contracts не является допустимым типом <dict>")
		self.__contracts = contracts

	def add_contract(self, contract):
		validate.validate_type(contract, AbstractContractEducation, f"Договор: { contract } не является допустимым типом")
		self.__contracts.add(contract)

	def remove_contract(self, contract):
		try:
			self.__contract.remove(course)
		except:
			print(f"Данного договора не существует {contract} не существует")

	def set_contracts(self, contracts):
		validate.validate_type(contracts, set, "Параметр: contracts не является допустимым типом <dict>")
		self.__contracts = contracts

	def segment_contracts(self):
		courses = set()
		for con in self.__contracts:
			courses.add(con.get_courses)

		#TODO реализовать сегментация договоров		
		return self.__segment_contracts

	def remove_contract():
		self.remove()