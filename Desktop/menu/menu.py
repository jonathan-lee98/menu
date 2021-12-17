import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class MenuBarDemo(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('menu')
		self.resize(600, 500)

		self.menuBar = self.menuBar()

		fileMenu = self.menuBar.addMenu('File')
		editMenu = self.menuBar.addMenu('Edit')


		exit_action = QAction('Exit App', self)
		exit_action.setShortcut('Ctrl+Q')
		exit_action.triggered.connect(lambda:QApplication.quit())

		fileMenu.addAction(exit_action)



if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = MenuBarDemo()
	demo.show()

	sys.exit(app.exec_())