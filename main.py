from tkinter import *

class ContractForAdditionalEducation:
	self.__contracts = {}

	def __init__(self, contracts):
		self.contracts = contracts

	def set_contracts(self, contracts):
		self.__contracts = contracts

	def addContract(self, contract):
		self.contracts[contract] = 

		return self.contracts

	def get_contracts(self):
		return self.contracts

	def getContractByName(self, name):
		return self.contracts.get(name)

	def removeContractByName(self, name):
		del self.contracts[name]

		return self.contracts

	def editContract(self, name, value):
		self.contracts[name] = value

		return self.contracts


def main():
	root = Tk()
	root.title("Lab №8")
	root.mainloop()

if __name__ == "__main__":
	main()