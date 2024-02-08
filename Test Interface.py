
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
from TestBackend import GraphicsTools

class MainWindow(QMainWindow): # Class that will create UI, will inhertant all the methods from QMainWindow
    def __init__(self): # The constructor for this class that will always be called when first created
        super().__init__() # Call the constructor of the parent clas and return a object of the parent
        self.setGeometry(0, 0, 1000, 1000) # Set spawn position of window and inital size
        self.setWindowTitle("INSIGHT")
        self.createWindow() # In constructor call another method
        self.start = GraphicsTools()
        
    def createWindow(self):
        # region Window Widget and Layout Creation
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.canvas = QWidget() # a blank widget that will only hold the main layout for widgets, gets color from stylesheet     
        self.mainLayout = QHBoxLayout() # As we add stuff it will be placed horizatonally
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
        
        # region Window Content
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # region Main Nodes Section
        #========================================
        # region Main Nodes Section Widget and Layout Creation
        #----------------------------------------
        # The Second Main Struture
        self.nodeContainer = QGroupBox("Nodes") # Contains all node related things, will contain the nodeLayout
        self.nodeContainer.setFixedWidth(550) # Has same coloring as MainWindow Widget
        
        # The Second Main Layout
        self.nodeLayout = QVBoxLayout()  # Every Primary Widget will be added here, goes downwards, two Primaries Note and Response
        self.nodeLayout.setSpacing(4) # The space inbetween widgets in node layout
        self.nodeLayout.setContentsMargins(6,0,6,6) # The space inbetween the ends of the groupbox and the widgets inside
        #----------------------------------------
        # endregion
        
        # region Main Nodes Section Content
        #----------------------------------------
        # region Primary Node Note
        #****************************************
        self.createInfoLabel("Enter a node's position as x,y.") # Creates a widget called noteCotainer 
        #****************************************
        # endregion
            
        # region Primary Node Response
        #****************************************
        # region Primary Node Response Widget and Layout Creation
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # The Node Response Main Struture
        self.nodeResponseContainer = QFrame() # Contains all the reponses and heading, will contain the nodeResponseLayout
 
        # The Node Response Main Layout
        self.nodeResponseLayout = QVBoxLayout() # Every Major Widget will be added here, goes downwards, three Major Widgets Label, Input Area, and add button
        self.nodeResponseLayout.setSpacing(0)  
        self.nodeResponseLayout.setContentsMargins(0,0,0,6)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Node Response Content
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # region Major Node Label 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Node Label Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Node Label Main Struture
        self.labelContainer = QWidget() # Contains all the info labels, will contain the nodeLabelLayout
        self.labelContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
       
        # The Node Label Main Layout
        self.labelLayout = QHBoxLayout() # Every Minor Widget will be added here, goes sideways, formatting
        self.labelLayout.setSpacing(0) 
        self.labelLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Node Label Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Minor Widgets
        self.indexLabel = QLabel("#")
        self.indexLabel.setStyleSheet("""
                                       min-width: 2em;
                                       max-width: 2em;
                                       
                                       background-color: rgba(0,0,0,0);""")
        
        self.positionLabel = QLabel("Position")
        self.positionLabel.setStyleSheet("""
                                       min-width: 5em;
                                       max-width: 5em;
                              
                                       background-color: rgba(0,0,0,0);
        
                                       qproperty-alignment: AlignLeft;""")        
        
        self.symmetricLabel = QLabel("Sym.")
        self.symmetricLabel.setStyleSheet("""
                                       min-width: 2em;
                                       max-width: 2em;
                                    
                                       background-color: rgba(0,0,0,0);""")
        
        self.deleteLabel = QLabel("Delete")
        self.deleteLabel.setStyleSheet("""
                                       min-width: 2.35em;
                                       max-width: 2.35em;
                                 
                                       background-color: rgba(0,0,0,0);""")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Node Label Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Node Label Main Layout
        self.labelLayout.addWidget(self.indexLabel)
        self.labelLayout.addWidget(self.positionLabel)
        self.labelLayout.addWidget(self.symmetricLabel)
        self.labelLayout.addWidget(self.deleteLabel)
        
        # Note: I have no idea why this line works
        #self.labelLayout.setAlignment(self.indexLabel, Qt.AlignLeft)
        self.labelLayout.setAlignment(self.positionLabel, Qt.AlignLeft)
        self.labelLayout.setAlignment(self.symmetricLabel, Qt.AlignCenter)
        self.labelLayout.setAlignment(self.deleteLabel, Qt.AlignCenter) 
        
        # Setting the Node Label Main Layout to the Node Label Main Struture
        self.labelContainer.setLayout(self.labelLayout)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Node Input Area 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Node Input Area Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Node Input Area Main Struture
        self.nodeInputScorllArea = QScrollArea() # Controls the Scroll Area for the Widget that contains all the inputs
        self.nodeInputScorllArea.setWidgetResizable(True)
        self.nodeInputScorllArea.setMinimumHeight(45)
        self.nodeInputScorllArea.setStyleSheet("""border-color: rgba(0,0,0,0);
                                                  background-color: black;""")
        
        # The Node Input Area Main Sub-Struture
        self.nodeInputScrollAreaWidget = QWidget() # Widget that will hold all inputs, will be the central widget for nodeInputScrollArea, will contain the nodeInputScrollAreaWidgetLayout
        self.nodeInputScrollAreaWidget.setContentsMargins(0,0,0,0)
        self.nodeInputScrollAreaWidget.setStyleSheet("""border: none;
                                   background-color: rgba(0,0,0,0);""")
        
        # The Node Input Area Main Sub-Layout
        self.nodeInputScrollAreaWidgetLayout = QVBoxLayout() # Every addition input will be added here, Minor Widget will be added here, goes downwards, one Minor Widget Input, non formatting
        self.nodeInputScrollAreaWidgetLayout.setSpacing(0)
        self.nodeInputScrollAreaWidgetLayout.setContentsMargins(0,0,0,0) 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Node Input Area Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # region Minor Node Input 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # region Minor Node Input Widget and Layout Creation
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # The Node Input Main Struture
        self.nodeInputContainer = QWidget() # Contains input, will contain the nodeInputLayout, add to nodeInputScrollAreaWidgetLayout once done
        #self.rowWidget.setMinimumHeight(1) dont need it since the widgets inside already have a min height size
        
        #The Node Input Main Layout
        self.nodeInputLayout = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
        self.nodeInputLayout.setSpacing(0)
        self.nodeInputLayout.setContentsMargins(0,0,0,3)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Node Input Content
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Tiny Widgets
        self.indexNumber = QLabel("1")
        self.indexNumber.setStyleSheet("""
                                       min-width: 2em;
                                       max-width: 2em; """)
        
        self.genericInput = QLineEdit()
        self.genericInput.editingFinished.connect(lambda: self.onTextFinal(1)) #textChanged
        self.genericInput.setAlignment(Qt.AlignCenter)
        self.genericInput.setStyleSheet("background-color: white;")
        
        self.symmetric = QCheckBox()

        self.delete = QRadioButton()
        self.delete.setDisabled(True)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Node Input addition and layout
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Adding Tiny to The Node Input Main Layout
        self.nodeInputLayout.addWidget(self.indexNumber)
        self.nodeInputLayout.addWidget(self.genericInput)
        self.nodeInputLayout.addWidget(self.symmetric)
        self.nodeInputLayout.addWidget(self.delete)
        
        self.nodeInputLayout.setAlignment(self.genericInput, Qt.AlignCenter)
        self.nodeInputLayout.setAlignment(self.symmetric, Qt.AlignCenter)
        self.nodeInputLayout.setAlignment(self.delete, Qt.AlignCenter) 
        
        # Setting the Node Input Main Layout to the Node Input Main Struture
        self.nodeInputContainer.setLayout(self.nodeInputLayout)
        
        self.list_of_widgets = []
        self.list_of_widgets.append(self.nodeInputContainer)
        
        self.list_of_widgets_previous_text = []
        self.list_of_widgets_previous_text.append("0,0") # first always there 
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # endregion
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
       
        # region Major Node Input Area Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Node Input Area Main Sub-Layout
        self.nodeInputScrollAreaWidgetLayout.addWidget(self.nodeInputContainer)
        
        # Setting the Node Input Area Main Sub-Layout to the Node Input Area Main Sub-Struture
        self.nodeInputScrollAreaWidget.setLayout(self.nodeInputScrollAreaWidgetLayout)

        # Setting the Node Input Area Main Sub-Struture to the Node Input Area Main Struture
        self.nodeInputScorllArea.setWidget(self.nodeInputScrollAreaWidget)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Add Node Button Sub-Sub-Section
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Add Node Button Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # None needed since it will be added to bottom and centered 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Node Button Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.addNodeButton = QPushButton()
        self.addNodeButton.setText("Add Node")
        self.addNodeButton.clicked.connect(lambda: self.onClick())
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Node Button addition and actualization
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # none needed since already widget and so will be added directly to node response layout 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Node Response Content addition and Actualization
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Adding Major to Node Response Main Layout
        self.nodeResponseLayout.addWidget(self.labelContainer)
        self.nodeResponseLayout.addWidget(self.nodeInputScorllArea) # chnge it back here
        self.nodeResponseLayout.addWidget(self.addNodeButton)
        
        self.nodeResponseLayout.setAlignment(self.addNodeButton, Qt.AlignCenter)

        # Setting the Node Response Main Layout to the Node Response Main Struture
        self.nodeResponseContainer.setLayout(self.nodeResponseLayout) 
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion
        #****************************************
        # endregion 
        #----------------------------------------
        # endregion
        
        # region Main Nodes Section addition and layout
        #----------------------------------------
        # Adding Primary to Second Main Layout
        self.nodeLayout.addWidget(self.noteContainer) # Added to Super Container Layout
        self.nodeLayout.addWidget(self.nodeResponseContainer) # Change this back if fails

        # Setting the Second Main Layout to the Second Main Struture 
        self.nodeContainer.setLayout(self.nodeLayout) # This will be added to MainLayout
        #----------------------------------------
        # endregion
        #========================================
        # endregion 
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
        
        # region Window addition, layout, and Actualization
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.mainLayout.addWidget(self.nodeContainer) # First Column
        
        self.canvas.setLayout(self.mainLayout) 
        
        self.setCentralWidget(self.canvas)
   
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
             
    def createInfoLabel(self, message):
        self.noteContainer = QFrame() # To get outline of note
        self.noteContainer.setFixedHeight(100) # On frame min and max
        self.noteLayout = QVBoxLayout() # Add things up to down
        self.noteLayout.setSpacing(0)

        self.note = QLabel("Note:") # look at master style sheet
        self.note.setStyleSheet("qproperty-alignment: AlignLeft;")
        
        self.genericInfo = QLabel(message) # look at master style sheet
        # by default Q label text is centered in master style sheet
        
        self.noteLayout.addWidget(self.note)
        self.noteLayout.addWidget(self.genericInfo)
        
        self.noteContainer.setLayout(self.noteLayout) # returns this, to be added to layout
        
    def createMinorNodeResponse(self, number):
        # region Minor Node Response Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.genericRowWidget = QWidget()
        self.genericRowWidget.setMinimumHeight(45)
        self.genericHorizationalLayout = QHBoxLayout()
        self.genericHorizationalLayout.setSpacing(0)
        self.genericHorizationalLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Minor Node Response Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.indexNumber_1 = QLabel(f"{number}")
        self.indexNumber_1.setStyleSheet("""
                                       min-width: 2em;
                                       max-width: 2em;
                                       """)
        
        self.genericInput_1 = QLineEdit()
        self.genericInput_1.setAlignment(Qt.AlignCenter)
        self.genericInput_1.setStyleSheet("background-color: white;")
        
        self.symmetric_1 = QCheckBox()
        #self.symmetric.setStyleSheet("""QCheckBox::indicator:hover{background-color: green;}""")
        
        self.delete_1 = QRadioButton()
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Minor Node Response addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.genericHorizationalLayout.addWidget(self.indexNumber_1)
        self.genericHorizationalLayout.addWidget(self.genericInput_1)
        self.genericHorizationalLayout.addWidget(self.symmetric_1)
        self.genericHorizationalLayout.addWidget(self.delete_1)
        
        self.genericHorizationalLayout.setAlignment(self.genericInput_1, Qt.AlignCenter)
        self.genericHorizationalLayout.setAlignment(self.symmetric_1, Qt.AlignCenter)
        self.genericHorizationalLayout.setAlignment(self.delete_1, Qt.AlignCenter)
        
        self.genericRowWidget.setLayout(self.genericHorizationalLayout)
        
        # important here for numbers
        self.list_of_widgets.append(self.genericRowWidget) # now added to list so official counted
        self.list_of_widgets_previous_text.append("0,0") #store preivous good text
        
        self.genericInput_1.editingFinished.connect(lambda: self.onTextFinal(number)) #textChanged
        
        self.nodeInputScrollAreaWidgetLayout.addWidget(self.genericRowWidget)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
    
    def onTextChanged(self, text):
        print(f"current text {text}") 
        
    def onTextFinal(self,number):
        print(f" Number of nodes is {len(self.list_of_widgets)}.")
        yo = self.list_of_widgets[number - 1] # gives button based on current total number like 20
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list
        hi = yo.findChildren(QLabel) # finds all QLineEdits in second button (there is only one) and give them in a list
        
        print(f"Line {number} has text {hey[0].text()}") # go to the first QLineEdit in the list and grab the text from it
        print(f"Number in label is {hi[0].text()}")
        print("node creation started-")
        self.lineParsing(hey[0].text(), int(hi[0].text())) # if number and label are same then can just replace with number
        
    def cleartext(self, number):
        yo = self.list_of_widgets[number - 1] # gives button based on current total number like 20
        
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list
        hey[0].clear()
               
        print(f"Line {number} has been cleared.") # go to the first QLineEdit in the list and grab the text from it
        
        hey[0].setText(self.list_of_widgets_previous_text[number - 1])
            
    def lineParsing(self, text, number):
        try:
            i,j = text.split(",") # Grab the text and break it into two parts
            
            # since no forces at the moment then us assocuted method
            self.start.node_creation(float(i), float(j), number)
                 
            # list_of_nodes.append(node_position)
            # number_of_nodes += 1
            
            # if k == None:
                
            # print("Null")
                
            # if k.lower() == "true":
            #     make_symmetric = True
            #     node_position = node_creation(-1*float(i), float(j), number_of_nodes)
            #     list_of_nodes.append(node_position)  
            #     number_of_nodes += 1
                
            # elif k.lower() == "false":
            #     make_symmetric = False
                
            # elif make_symmetric:
            #     make_symmetric = True
            #     node_position = node_creation(-1*float(i), float(j), number_of_nodes)
            #     list_of_nodes.append(node_position)  
            #     number_of_nodes += 1
                
            print("node created successfully")
            
            self.list_of_widgets_previous_text[number - 1] = text # replace zeros with good number
            print("=======================")
        except:
            print("node created unsuccessfully")
            print("format was not followed")
            self.cleartext(number)
            print("=======================")
       
    def onClick(self):    
        self.createMinorNodeResponse(len(self.list_of_widgets) + 1) # before node gets added
        
        self.repaint()
                            
class UI(): # This class will hold the method that will be called in a different file to start UI
    def start():
        App = QApplication([]) # Start up the UI system
        
        # This will set the default style for all widgets created in this window QCheckBox::indicator:checked{background-color: lightgreen; color : black;}
        App.setStyleSheet("""
                        QWidget {font-family: Times New Roman;
                        font-size: 50px;
                        color: black;}
                        
                        QMainWindow{background-color: #161219;}
                        
                        QCheckBox::indicator:unchecked:hover{background-color: rgba(0,255,0, 75);}
                        
                        QCheckBox::indicator:checked:hover{background-color: rgba(255,0,0,100);}
                        
                        QCheckBox::indicator:checked:pressed{background-color: rgba(255,0,0,100);}
                        
                        QRadioButton::indicator:unchecked:hover{background-color: rgba(255,0,0,100);}
                        
                        QFrame{border: 1px;
                        border-radius: 25px;
                        border-color: white;
                        border-style: solid;
                        background-color: black;
                        min-width: 8.75em;}
                        
                        QLabel {color: white;
                        font-size: 35px;
                        padding: 0px;
                        spacing: 0px;
                        border: none;
                        background-color: black;
                        selection-color: black;
                        selection-background-color: white;
                        min-width: 7em;
                        max-height: 1em;
                        min-height: 1em;
                        
                        qproperty-alignment: AlignCenter;}
                        
                        QLineEdit{font-size: 35px;
                        max-width: 5em;
                        max-height: 1em;
                        min-height: 1em;}
                        
                        
                        QPushButton{background-color: black;
                        border-color: #a868d9;
                        border-style: outset;
                        border-width: 1px;
                        border-radius: 10px;
                        font: bold 35px;
                        color: white;
                        min-width: 6em;
                        max-height: 0.7em;
                        min-height: 0.7em;}
                      
                        QPushButton::hover{background-color: #734c91;
                        color: white;}
                        
                        QTextEdit{color: white;
                        font-size: 35px;
                        padding: 10px;
                        border-color: white; 
                        border-style: solid;
                        border-width: 1px;
                        border-radius: 20px;
                        background-color: black;
                        selection-color: black;
                        selection-background-color: white;
                        min-width: 7em;}
                        
                        QGroupBox{color: white;}
                        
                        QScrollBar {color: white;}
                        """)
        
        window = MainWindow() # Create a instance of the MainWindow Class
        window.show()
        
        sys.exit(App.exec())
        
ex = UI.start()