from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class Diagram:
	def create_pie_chart_from_dict(self, root, data, figsize = (8, 8)):
		labels = list(data.keys())
		sizes = list(data.values())

		fig, ax = plt.subplots(figsize=figsize)
		ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
		ax.axis('equal')
		ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.17))	

		canvas = FigureCanvasTkAgg(fig, master=root)
		canvas.draw()
		canvas.get_tk_widget().pack()