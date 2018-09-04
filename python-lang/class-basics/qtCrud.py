import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dmanage import DatabaseManager
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.startUI()
        self.table_name = ''
        self.column_data = {}
    def startUI(self):
        self.resize(900,600)
        self.move(300,100)
        self.setWindowTitle("MySQL CRUD")
        self.setWindowIcon(QIcon('factory.png'))
        # Main Window main layout
        mainvlayout = QVBoxLayout(self)
        self.setLayout(mainvlayout)
        # title
        title = QLabel("<b>MySQL CRUD Basics</b>",self)
        mainvlayout.addWidget(title)
        test_data = ["shahid", "zahid", "isna"]

        # Groupbox for databases, button and table
        groupBox1 = QGroupBox("All Databases and Tables: Select a database and click '>>'",self)
        gb1_layout = QGridLayout()
        groupBox1.setLayout(gb1_layout)
        self.db_combo = QComboBox(self)
        # add all databases to db_combo
        self.config = {"user":"shahid",
              "password": "102mspass",
              "host":"127.0.0.1"
             }
        self.dm = DatabaseManager(self.config)
        # getting all databases
        dbs = self.dm.show_databases()
        databases = [item[0] for item in dbs]
        self.db_combo.addItems(databases)
        # this button will get the selected db and display its tables in tcombo
        db_button = QPushButton(">>",self)
        db_button.clicked.connect(self.handle_db_button)
        self.t_combo = QComboBox(self)
        t_button = QPushButton("Go", self)
        t_button.clicked.connect(self.handle_go_button)
        self.detail_label = QLabel(self)
        ## add all databases to
        gb1_layout.addWidget(self.db_combo, 0,0,1,4)
        gb1_layout.addWidget(db_button, 0,4)
        gb1_layout.addWidget(self.t_combo,0,5,1,4)
        gb1_layout.addWidget(t_button,0,9)
        gb1_layout.addWidget(self.detail_label,1,0,1,10)
        # Groupbox grid layout for input etc
        groupBox2 = QGroupBox("Inputs",self)
        groupBox2layout = QGridLayout()
        groupBox2.setLayout(groupBox2layout)
        # Create Table Label
        l1 = QLabel("Create Table: ", self)
        # Input for table name
        self.table_name_input = QLineEdit(self)
        # Create Column Label
        column_name = QLabel("Column Name ")
        # Column Type Label
        type_combo_label = QLabel("Type ")
        # Column Type Combo
        self.type_combo = QComboBox(self)
        type_combo_items = ["str","int","float"]
        # Column Name Input, we add one column at a time
        self.column_name_input = QLineEdit(self)
        # Add Column Button
        add_column_button = QPushButton("Add Column",self)
        add_column_button.clicked.connect(self.handle_add_column)
        # Add Table Button
        add_table_button = QPushButton("Create Table",self)
        add_table_button.clicked.connect(self.handle_add_table)
        # Details Label
        self.details_label = QLabel()
        # add items to type_combo combobox
        self.type_combo.addItems(type_combo_items)
        # trying to add vertical line
        vertical_line = QFrame()
        vertical_line.setFrameShape(QFrame.VLine)
        vertical_line.setFrameShadow(QFrame.Sunken)
        # Test label
        second_gbox = QGroupBox("Data Insertion")
        second_gbox_layout = QGridLayout()
        second_gbox.setLayout(second_gbox_layout)

        second_gbox_label = QLabel("Insert Data into table, Enter comma (,) separated values below")
        second_gbox_layout.addWidget(second_gbox_label,0,0)
        second_gbox_input = QLineEdit()
        second_gbox_layout.addWidget(second_gbox_input,1,0)
        second_gbox_button = QPushButton("Insert")
        second_gbox_layout.addWidget(second_gbox_button,2,0)
        # layout various widgets 
        groupBox2layout.addWidget(l1,0,0,1,1)
        groupBox2layout.addWidget(self.table_name_input,0,1,1,2)
        groupBox2layout.addWidget(type_combo_label,2,0,1,1)
        groupBox2layout.addWidget(self.type_combo,2,1,1,1)
        groupBox2layout.addWidget(column_name,1,0,1,1)
        groupBox2layout.addWidget(self.column_name_input,1,1,1,2)
        groupBox2layout.addWidget(add_column_button,2,2,1,1)
        groupBox2layout.addWidget(self.details_label,3,0,1,5)
        groupBox2layout.addWidget(add_table_button,4,2,1,1)
        groupBox2layout.addWidget(vertical_line,0,3,5,1)
        groupBox2layout.addWidget(second_gbox,0,4,3,3)

        # another groupbox grid layout for output etc
        groupBox3 = QGroupBox("Results", self)
        groupBox3layout = QGridLayout()
        groupBox3.setLayout(groupBox3layout)
        self.select_all_checkbox = QCheckBox("Select All")
        show_results_button = QPushButton("Show Results")
        show_results_button.clicked.connect(self.handle_show_results)
        columns_label = QLabel("Add Columns")
        self.columns_input = QLineEdit("Add ',' separated columns")
        # text browser
        self.browser = QTextBrowser(self)
        # add widgetst to layout
        groupBox3layout.addWidget(self.select_all_checkbox,0,0,1,1)
        groupBox3layout.addWidget(show_results_button,0,4,1,1)
        groupBox3layout.addWidget(self.browser,1,0,1,5)
        groupBox3layout.addWidget(columns_label,0,1,1,1)
        groupBox3layout.addWidget(self.columns_input,0,2,1,1)
        # last input section Hbox

        custom_line = QWidget(self)
        custom_line_layout = QHBoxLayout()
        custom_line.setLayout(custom_line_layout)

        custom_label = QLabel("Custom SQL >>", self)
        self.custom_input = QLineEdit(self)
        custom_button = QPushButton("Execute", self)
        custom_button.clicked.connect(self.handle_custom_button)
        custom_line_layout.addWidget(custom_label)
        custom_line_layout.addWidget(self.custom_input)
        custom_line_layout.addWidget(custom_button)

        # add widgets to main layout
        mainvlayout.addWidget(groupBox1)
        mainvlayout.addWidget(groupBox2)
        mainvlayout.addWidget(groupBox3)
        mainvlayout.addWidget(custom_line)
        self.show()
    def handle_db_button(self):
        self.selected_db = str(self.db_combo.currentText()).strip()
        # use selected db
        self.dm.use_database(self.selected_db)
        # now fetch its tables
        tbls = self.dm.show_tables()
        tables = []
        tables = [item[0] for item in tbls]
        self.t_combo.clear()
        self.t_combo.addItems(tables)
    def handle_go_button(self):
        ## lets get which table is selected
        self.selected_table = str(self.t_combo.currentText()).strip()
        self.detail_label.setText("Database selected: <b>{}</b>, Table selected <b>{}</b> ".format(self.selected_db, self.selected_table))
    def handle_add_column(self):
        print("Adding Column\n")
        # get column name
        column_name = str(self.column_name_input.text()).strip()
        # get column type
        column_type = str(self.type_combo.currentText()).strip()
        #store column_name:column_type in the dictionary
        if len(column_name) >=1 and len(column_type) >=1:
            self.column_data[column_name] = column_type
        print(self.column_data)

    def handle_add_table(self):
        # get table name
        self.table_name = str(self.table_name_input.text()).strip()
        print("Table Name \n")
        print(self.table_name)

        # access column_data
        print("Column Data\n")
        print(self.column_data)

        # do database query using the interface
        query =  self.dm.create_table(self.table_name, self.column_data)
        self.details_label.setText("<small style='color:green'>Executing {}</small>".format(query))
        # clear column_data
        self.column_data.clear()
    def handle_show_results(self):
        # check the checkbox state
        self.browser.clear()
        if self.select_all_checkbox.isChecked():
            data = self.dm.select_all(self.selected_table)
            for count, item in enumerate(data):
                self.browser.append("{} {}".format(count+1,str(item)))
        else:
            self.browser.clear()
            input_data = str(self.columns_input.text()).strip()
            if len(input_data) >= 1:
                splitted_data = input_data.split(',')
                columns = [item.strip() for item in splitted_data]
                results = self.dm.select_cols(columns, self.selected_table)
                for count, item in enumerate(results):
                    self.browser.append("{} {}".format(count+1, str(item)))
            self.columns_input.setText("")
    def handle_custom_button(self):
        # clear browser
        query = str(self.custom_input.text()).strip()
        self.browser.clear()
        results = self.dm.custom_sql(query)
        for key, item in enumerate(results):
            self.browser.append("{} {}".format(key, str(item)))
        # clear custom input line
        self.custom_input.setText("")

    def closeEvent(self, event):
        msg = QMessageBox.question(self, "Message",
                                   "Are you sure to quit?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if msg == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
