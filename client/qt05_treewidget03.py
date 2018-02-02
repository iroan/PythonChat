import sys
from PyQt5.QtWidgets import *

'''
该类的功能：
	1. 提供一次加载全部用户的功能
	2. 提供选中一项数据的执行指定函数的功能
'''
class TreeWidgetDemo(QWidget):   
	def __init__(self,parent=None):
		super(TreeWidgetDemo,self).__init__(parent)

		self.tree = QTreeWidget(self)
        # 设置列数
		self.tree.setColumnCount(2)

        # 设置头的标题
		self.tree.setHeaderLabels(['昵称','姓名','状态'])

		root= QTreeWidgetItem(self.tree)
		root.setText(0,'XX公司')

		'''
		加载数据：
			1. 加载部门
			2. 加载部门下的员工
		'''

		child1 = QTreeWidgetItem(self.tree)
		child1.setText(0,'child1')
		child1.setText(1,'1')
		print(child1.text(1))
		
		child2 = QTreeWidgetItem(root)
		child2.setText(0,'child2')
		child2.setText(1,'2')
		
		child3 = QTreeWidgetItem(root)
		child3.setText(0,'child3')
		child3.setText(1,'3')		
		
		child4 = QTreeWidgetItem(child3)
		child4.setText(0,'child4')
		child4.setText(1,'4')

		child5 = QTreeWidgetItem(child3)
		child5.setText(0,'child5')
		child5.setText(1,'5')
        
		self.tree.addTopLevelItem(root)
		self.tree.clicked.connect( self.onTreeClicked )
        		
		mainLayout = QVBoxLayout(self);
		mainLayout.addWidget(self.tree);
		self.setLayout(mainLayout)		

	def onTreeClicked(self, qmodelindex):
		item = self.tree.currentItem()
		print("key=%s ,value=%s" % (item.text(0), item.text(1)))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	tree = TreeWidgetDemo()
	tree.show()
	sys.exit(app.exec_())
