from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from TestBackend import GraphicsTools

import sys

class MainWindow(QMainWindow): # Class that will create UI, will inhertant all the methods from QMainWindow
    def __init__(self): # The constructor for this class that will always be called when first created
        super().__init__() # Call the constructor of the parent clas and return a object of the parent
        self.setGeometry(1420, 50, 100, 100) # Set spawn position of window and inital size
        self.setMaximumWidth(100)
        self.setMaximumHeight(1500)
        self.setWindowTitle("INSIGHT")
        self.createWindow() # In constructor call another method
        self.start = GraphicsTools()
        
    def createWindow(self):
        # region Window Widget and Layout Creation
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.canvas = QWidget() # a blank widget that will only hold the primary layout for widgets        
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
        self.indexLabelNode = QLabel("#")
        self.indexLabelNode.setStyleSheet("""
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
        self.labelLayout.addWidget(self.indexLabelNode)
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
        self.indexNumberNode = QLabel("1")
        self.indexNumberNode.setStyleSheet("""
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
        self.nodeInputLayout.addWidget(self.indexNumberNode)
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
         
        # region Main Force Section
        #========================================
        # region Main Force Section Widget and Layout Creation
        #----------------------------------------
        # The Second Main Struture
        self.forceContainer = QGroupBox("Forces") # Contains all force related things, will contain the forceLayout
        self.forceContainer.setFixedWidth(550) # Has same coloring as MainWindow Widget
        
        # The Second Main Layout
        self.forceLayout = QVBoxLayout()  # Every Primary Widget will be added here, goes downwards, three Primaries Note and Response
        self.forceLayout.setSpacing(4) # The space inbetween widgets in the force layout
        self.forceLayout.setContentsMargins(6,0,6,6) # The space inbetween the ends of the groupbox and the widgets inside
        #----------------------------------------
        # endregion
        
        # region Main Force Section Content
        #----------------------------------------
        # region Primary Force Note
        #****************************************
        self.createInfoLabel("Enter a force as magnitude,angle.") # Creates a widget called noteCotainer 
        #****************************************
        # endregion
            
        # region Primary Force Response
        #****************************************
        # region Primary Force Response Widget and Layout Creation
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # The Force Response Main Struture
        self.forceResponseContainer = QFrame() # Contains all the reponses and heading, will contain the forceResponseLayout
        # QFrame has black as background coloring with layout having no color

        # The Force Response Main Layout
        self.forceResponseLayout = QVBoxLayout() # Every Major Widget will be added here, goes downwards, three Major Widgets Label, Input Area, and Next button
        self.forceResponseLayout.setSpacing(0)
        self.forceResponseLayout.setContentsMargins(0,0,0,6)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Force Response Content
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # region Major Force Label 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Force Label Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Force Label Main Struture
        self.forceLabelContainer = QWidget() # Contains all the info labels, will contain the forceLabelLayout
        self.forceLabelContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
        
        # The Force Label Main Layout
        self.forceLabelLayout = QHBoxLayout() # Every Minor Widget will be added here, goes sideways, two Minor Widgets Force and Symmetric, formatting
        self.forceLabelLayout.setSpacing(0) 
        self.forceLabelLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Force Label Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Minor Widgets
        self.indexLabelForce = QLabel("#")
        self.indexLabelForce.setStyleSheet("""
                                       min-width: 2em;
                                       max-width: 2em;
                                       
                                       background-color: rgba(0,0,0,0);""")
        
        self.forceLabel = QLabel("Force")
        self.forceLabel.setStyleSheet("""
                                       min-width: 3.8em;
                                       max-width: 3.8em;
                                       
                                       background-color: rgba(0,0,0,0);
                                       qproperty-alignment: AlignLeft;""")
        
        self.forceSymmetricLabel = QLabel("Symmetric")
        self.forceSymmetricLabel.setStyleSheet("""
                                       min-width: 4em;
                                       max-width: 4em;
                                    
                                       background-color: rgba(0,0,0,0);""")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Force Label Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Force Label Main Layout
        self.forceLabelLayout.addWidget(self.indexLabelForce)
        self.forceLabelLayout.addWidget(self.forceLabel)
        self.forceLabelLayout.addWidget(self.forceSymmetricLabel)
        
        self.forceLabelLayout.setAlignment(self.forceLabel, Qt.AlignLeft)
        self.forceLabelLayout.setAlignment(self.forceSymmetricLabel, Qt.AlignCenter)

        # Setting the Force Label Main Layout to the Force Label Main Struture
        self.forceLabelContainer.setLayout(self.forceLabelLayout)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Force Input Area 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Force Input Area Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Force Input Area Main Struture
        self.forceInputScorllArea = QScrollArea() # Controls the Scroll Area for the Widget that contains all the inputs
        self.forceInputScorllArea.setWidgetResizable(True)
        self.forceInputScorllArea.setMinimumHeight(45)
        self.forceInputScorllArea.setStyleSheet("""background-color: black;
                                                border-color: rgba(0,0,0,0);""")
        
        # The Force Input Area Main Sub-Struture
        self.forceInputScrollAreaWidget = QWidget() # Widget that will hold all inputs, will be the central widget for forceInputScrollArea, will contain the forceInputScrollAreaWidgetLayout
        self.forceInputScrollAreaWidget.setContentsMargins(0,0,0,0)
        self.forceInputScrollAreaWidget.setStyleSheet("""background-color: rgba(0,0,0,0);
                                   border: none;""")
        
        # The Force Input Area Main Sub-Layout
        self.forceInputScrollAreaWidgetLayout = QVBoxLayout() #  Every addition input will be added here, Minor Widget will be added here, goes downwards, one Minor Widget Input, non formatting
        self.forceInputScrollAreaWidgetLayout.setSpacing(0)
        self.forceInputScrollAreaWidgetLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Force Input Area Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # region Minor Force Input 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # region Minor Force Input Widget and Layout Creation
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # The Force Input Main Struture
        self.forceInputContainer = QWidget() # Contains input, will contain the forceInputLayout, add to forceInputScrollAreaWidgetLayout once done
        #self.rowWidget.setMinimumHeight(1) dont need it since the widgets inside already have a min height size
        
        #The Force Input Main Layout
        self.forceInputLayout = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
        self.forceInputLayout.setSpacing(0)
        self.forceInputLayout.setContentsMargins(0,0,0,3)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Force Input Content
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Tiny Widgets
        self.indexNumberForce = QLabel("1")
        self.indexNumberForce.setStyleSheet("""
                                            min-width: 2em;
                                            max-width: 2em; """)
        
        self.genericInputF = QLineEdit()
        self.genericInputF.editingFinished.connect(lambda: self.onTextFinalF(1)) #textChanged
        self.genericInputF.setAlignment(Qt.AlignCenter)
        self.genericInputF.setStyleSheet("background-color: white;")
        
        self.symmetric = QCheckBox()
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Force Input addition and layout
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Adding Tiny to The Force Input Main Layout
        self.forceInputLayout.addWidget(self.indexNumberForce)
        self.forceInputLayout.addWidget(self.genericInputF)
        self.forceInputLayout.addWidget(self.symmetric)
        
        self.forceInputLayout.setAlignment(self.genericInputF, Qt.AlignLeft)
        self.forceInputLayout.setAlignment(self.symmetric, Qt.AlignCenter)

        # Setting the Force Input Main Layout to the Force Input Main Struture
        self.forceInputContainer.setLayout(self.forceInputLayout)
        
        self.list_of_widgets_previous_textF = []
        self.list_of_widgets_previous_textF.append("0,0")
        
        self.list_of_widgetsF = []
        self.list_of_widgetsF.append(self.forceInputContainer)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # endregion
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Force Input Area Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Force Input Area Main Sub-Layout
        self.forceInputScrollAreaWidgetLayout.addWidget(self.forceInputContainer)
        
        # Setting the Force Input Area Main Sub-Layout to the Force Input Area Main Sub-Struture
        self.forceInputScrollAreaWidget.setLayout(self.forceInputScrollAreaWidgetLayout)
        
        # Setting the Force Input Area Main Sub-Struture to the Force Input Area Main Struture
        self.forceInputScorllArea.setWidget(self.forceInputScrollAreaWidget)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
              
        # region Major Next Force Button 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Next Force Button Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # None needed since it will be added to bottom and centered 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Next Force Button Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.nextForceButton = QPushButton()
        self.nextForceButton.setText("Next >>>")
        self.nextForceButton.clicked.connect(lambda: self.onClickNext())
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Force Button addition and actualization
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # none needed since already widget and so will be added directly to forceResponseLayout 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion     
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Force Response Content addition and Actualization
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Adding Major to Force Response Main Layout
        self.forceResponseLayout.addWidget(self.forceLabelContainer)
        self.forceResponseLayout.addWidget(self.forceInputScorllArea)
        self.forceResponseLayout.addWidget(self.nextForceButton)
        
        self.forceResponseLayout.setAlignment(self.nextForceButton, Qt.AlignCenter)
        
        # Setting the Force Response Main Layout to the Force Response Main Struture
        self.forceResponseContainer.setLayout(self.forceResponseLayout) # This contains a layout, added to Major Layout
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion
        #****************************************
        # endregion 
        #----------------------------------------
        # endregion
        
        # region Main Force Section addition and layout
        #----------------------------------------
        # Adding Primary to Second Main Layout
        self.forceLayout.addWidget(self.noteContainer) 
        self.forceLayout.addWidget(self.forceResponseContainer)
        
        # Setting the Second Main Layout to the Second Main Struture
        self.forceContainer.setLayout(self.forceLayout) 
        #----------------------------------------
        # endregion
        #========================================
        # endregion 
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
        
        # region Window addition, layout, and Actualization
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.mainLayout.addWidget(self.nodeContainer) # First Column
        self.mainLayout.addWidget(self.forceContainer) # Second Column
        
        self.canvas.setLayout(self.mainLayout) 
        
        self.setCentralWidget(self.canvas)
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
             
    def createInfoLabel(self, message):
        # region Info Label Widget and Layout Creation
        #(((((((((((((((((((())))))))))))))))))))
        self.noteContainer = QFrame() # To get outline of note
        self.noteContainer.setFixedHeight(100) # On frame min and max
        self.noteLayout = QVBoxLayout() # Add things up to down
        self.noteLayout.setSpacing(0)
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
        # region Info Label Content
        #(((((((((((((((((((())))))))))))))))))))
        self.note = QLabel("Note:") # look at master style sheet
        self.note.setStyleSheet("qproperty-alignment: AlignLeft;")
        
        self.genericInfo = QLabel(message) # look at master style sheet
        # by default Q label text is centered in master style sheet
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
        # region Info Label addition and layout
        #(((((((((((((((((((())))))))))))))))))))
        self.noteLayout.addWidget(self.note)
        self.noteLayout.addWidget(self.genericInfo)
        
        self.noteContainer.setLayout(self.noteLayout) # returns this, to be added to layout
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
    def createMinorNodeResponse(self, number):
        # region Minor Node Response Widget and Layout Creation
        #(((((((((((((((((((())))))))))))))))))))
        self.genericRowWidget = QWidget()
        self.genericRowWidget.setMinimumHeight(45)
        self.genericHorizationalLayout = QHBoxLayout()
        self.genericHorizationalLayout.setSpacing(0)
        self.genericHorizationalLayout.setContentsMargins(0,0,0,0)
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
        # region Minor Node Response Content
        #(((((((((((((((((((())))))))))))))))))))
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
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
        # region Minor Node Response addition and layout
        #(((((((((((((((((((())))))))))))))))))))
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
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
          
    def createMinorForceResponse(self, number):
        # region Minor Force Input Widget and Layout Creation
        #(((((((((((((((((((())))))))))))))))))))
        # The Force Input Main Struture
        self.forceInputContainer_1 = QWidget() # Contains input, will contain the forceInputLayout, add to forceInputScrollAreaWidgetLayout once done
        self.forceInputContainer_1.setMinimumHeight(45)
        #self.rowWidget.setMinimumHeight(1) dont need it since the widgets inside already have a min height size
        
        #The Force Input Main Layout
        self.forceInputLayout_1 = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
        self.forceInputLayout_1.setSpacing(0)
        self.forceInputLayout_1.setContentsMargins(0,0,0,0)
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
        # region Minor Force Input Content
        #(((((((((((((((((((())))))))))))))))))))
        # Tiny Widgets
        self.indexNumber_2 = QLabel(f"{number}")
        self.indexNumber_2.setStyleSheet("""
                                       min-width: 2em;
                                       max-width: 2em;
                                       """)
        self.genericInput_2 = QLineEdit()
        self.genericInput_2.setAlignment(Qt.AlignCenter)
        self.genericInput_2.setStyleSheet("background-color: white;")
        
        self.symmetric_2 = QCheckBox()
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
        # region Minor Force Input addition and layout
        #(((((((((((((((((((())))))))))))))))))))
        # Adding Tiny to The Force Input Main Layout
        self.forceInputLayout_1.addWidget(self.indexNumber_2)
        self.forceInputLayout_1.addWidget(self.genericInput_2)
        self.forceInputLayout_1.addWidget(self.symmetric_2)

        self.forceInputLayout_1.setAlignment(self.genericInput_2, Qt.AlignLeft)
        self.forceInputLayout_1.setAlignment(self.symmetric_2, Qt.AlignCenter)

        # Setting the Force Input Main Layout to the Force Input Main Struture
        self.forceInputContainer_1.setLayout(self.forceInputLayout_1)   
        
        # important for numbers
        self.list_of_widgetsF.append(self.forceInputContainer_1)
        self.list_of_widgets_previous_textF.append("0,0") # store preivous good text
        
        self.genericInput_2.editingFinished.connect(lambda: self.onTextFinalF(number))
        
        self.forceInputScrollAreaWidgetLayout.addWidget(self.forceInputContainer_1) 
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
    
    def onTextFinal(self,number):
        print(f"Number of nodes is {len(self.list_of_widgets)}.")
        yo = self.list_of_widgets[number - 1] # gives button based on current total number like 20
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list
        
        #hi = yo.findChildren(QLabel) # finds all QLineEdits in second button (there is only one) and give them in a list
        #print(f"Number in label is {hi[0].text()}") # good for checking node creation
        
        print(f"Line {number} has text {hey[0].text()}") # go to the first QLineEdit in the list and grab the text from it
        
        print("Node creation started-") # the process really starts from here
        self.lineParsing(hey[0].text(), number) # if number and label are same then can just replace with number
        
    def onTextFinalF(self,number):
        #print(f" Number of nodes is {len(self.list_of_widgets)}.") # good for checking force creation
        yo = self.list_of_widgetsF[number - 1] # gives button based on current total number like 20
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list

        print(f"Line {number} has text {hey[0].text()}") # go to the first QLineEdit in the list and grab the text from it

        print("Force creation started-") # the process really starts from here
        self.lineParsingF(hey[0].text(), number) # letsss goooo
                   
    def cleartext(self, number):
        yo = self.list_of_widgets[number - 1] # gives button based on current total number like 20
        
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list
        hey[0].clear()
               
        print(f"Line {number} has been cleared.") # go to the first QLineEdit in the list and grab the text from it
        
        hey[0].setText(self.list_of_widgets_previous_text[number - 1])
            
    def lineParsing(self, text, number):
        try:
            i,j = text.split(",") # Grab the text and break it into two parts
            f,a = self.list_of_widgets_previous_textF[number - 1].split(",") # Grab force pair text and break it into two parts
            
            if self.list_of_widgets_previous_textF[number - 1] != "0,0": # if the node has been maunally assigned a force
                self.start.node_creation_with_force(float(i), float(j), number, float(f), float(a)) # then use the method that takes in a force as well as node
                
            else: # if the node has default force
                self.start.node_creation(float(i), float(j), number) # then use node only method
                        
            self.list_of_widgets_previous_text[number - 1] = text # replace zeros with good number
            print("=======================")
            
        except:
            print("node created unsuccessfully")
            print("format was not followed")
            self.cleartext(number)
            print("=======================")
  
    def lineParsingF(self, text, number):
        try:
            i,j = text.split(",") # Grab the text and break it into two parts
            
            # if node not made yet the position info come from the default vaule
            # but an error will occur when force is being created, this is fine 

            x,y = self.list_of_widgets_previous_text[number - 1].split(",")
            # since no forces at the moment then us assocuted method
            self.start.node_creation_with_force(float(x), float(y), number, float(i), float(j))
                 
            # if successfully then store the value, so it can be retrieved later
            self.list_of_widgets_previous_textF[number - 1] = text # replace zeros with good number
            print("=======================")
        except:
            print("force created unsuccessfully")
            print("format was not followed")
            #self.cleartext(number)
            print("=======================")
  
    def nextPage(self):
        self.elementWindow = ElementWindow(self.start)
        self.elementWindow.show()
        self.start.calculate_number_of_equations() # First required calculation
        
    def onClick(self):    
        self.createMinorNodeResponse(len(self.list_of_widgets) + 1) # before node gets added
        self.createMinorForceResponse(len(self.list_of_widgets))
        
        self.repaint()
 
    def onClickNext(self):    
        # call method
        self.nextPage()
    
    def elementWindow(self):
        pass

class ElementWindow(QMainWindow):
    def __init__(self, bah): # The constructor for this class that will always be called when first created
        super().__init__() # Call the constructor of the parent class and return a object of the parent
        self.setGeometry(1420, 50, 100, 100) # Set spawn position of window and inital size
        self.setMaximumWidth(100)
        self.setMaximumHeight(1500)
        self.setWindowTitle("INSIGHT")
        self.createElementWindow() # In constructor call another method
        self.Graphics = bah
        
    def createElementWindow(self):
        # region Window Widget and Layout Creation
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.canvas = QWidget() # a blank widget that will only hold the primary layout for widgets        
        self.mainLayout = QHBoxLayout() # As we add stuff it will be placed horizatonally
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
        
        # region Window Content
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # region Main Element Section
        #========================================
        # region Main Element Section Widget and Layout Creation
        #----------------------------------------
        # The Second Main Struture
        self.ElementContainer = QGroupBox("Elements") # Contains all node related things, will contain the nodeLayout
        self.ElementContainer.setFixedWidth(550) # Has same coloring as MainWindow Widget
        
        # The Second Main Layout
        self.ElementLayout = QVBoxLayout()  # Every Primary Widget will be added here, goes downwards, two Primaries Note and Response
        self.ElementLayout.setSpacing(4) # The space inbetween widgets in node layout
        self.ElementLayout.setContentsMargins(6,0,6,6) # The space inbetween the ends of the groupbox and the widgets inside
        #----------------------------------------
        # endregion
        
        # region Main Element Section Content
        #----------------------------------------
        # region Primary Element Note
        #****************************************
        self.createInfoLabel("Enter an element as int,int.") # Creates a widget called noteCotainer 
        #****************************************
        # endregion
            
        # region Primary Element Response
        #****************************************
        # region Primary Element Response Widget and Layout Creation
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # The Element Response Main Struture
        self.ElementResponseContainer = QFrame() # Contains all the reponses and heading, will contain the nodeResponseLayout

        # The Element Response Main Layout
        self.ElementResponseLayout = QVBoxLayout() # Every Major Widget will be added here, goes downwards, three Major Widgets Label, Input Area, and add button
        self.ElementResponseLayout.setSpacing(0)  
        self.ElementResponseLayout.setContentsMargins(0,0,0,6)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Element Response Content
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # region Major Element Label 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Element Label Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Element Label Main Struture
        self.labelContainer = QWidget() # Contains all the info labels, will contain the elementLabelLayout
        self.labelContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
    
        # The Element Label Main Layout
        self.labelLayout = QHBoxLayout() # Every Minor Widget will be added here, goes sideways, formatting
        self.labelLayout.setSpacing(0) 
        self.labelLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Element Label Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Minor Widgets
        self.indexLabelElement = QLabel("#")
        self.indexLabelElement.setStyleSheet("""
                                    min-width: 2em;
                                    max-width: 2em;
                                    
                                    background-color: rgba(0,0,0,0);""")
        
        self.positionLabel = QLabel("Element")
        self.positionLabel.setStyleSheet("""
                                    min-width: 5em;
                                    max-width: 5em;
                            
                                    background-color: rgba(0,0,0,0);
        
                                    qproperty-alignment: AlignLeft;""")        
        
        self.deleteLabel = QLabel("Delete")
        self.deleteLabel.setStyleSheet("""
                                    min-width: 2.35em;
                                    max-width: 2.35em;
                                
                                    background-color: rgba(0,0,0,0);""")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Element Label Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Node Label Main Layout
        self.labelLayout.addWidget(self.indexLabelElement)
        self.labelLayout.addWidget(self.positionLabel)
        self.labelLayout.addWidget(self.deleteLabel)
        
        # Note: I have no idea why this line works
        #self.labelLayout.setAlignment(self.indexLabel, Qt.AlignLeft)
        self.labelLayout.setAlignment(self.positionLabel, Qt.AlignLeft)
        self.labelLayout.setAlignment(self.deleteLabel, Qt.AlignCenter) 
        
        # Setting the Node Label Main Layout to the Node Label Main Struture
        self.labelContainer.setLayout(self.labelLayout)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Element Input Area 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Element Input Area Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Element Input Area Main Struture
        self.ElementInputScorllArea = QScrollArea() # Controls the Scroll Area for the Widget that contains all the inputs
        self.ElementInputScorllArea.setWidgetResizable(True)
        self.ElementInputScorllArea.setMinimumHeight(45)
        self.ElementInputScorllArea.setStyleSheet("""border-color: rgba(0,0,0,0);
                                                background-color: black;""")
        
        # The Node Input Area Main Sub-Struture
        self.ElementInputScrollAreaWidget = QWidget() # Widget that will hold all inputs, will be the central widget for nodeInputScrollArea, will contain the nodeInputScrollAreaWidgetLayout
        self.ElementInputScrollAreaWidget.setContentsMargins(0,0,0,0)
        self.ElementInputScrollAreaWidget.setStyleSheet("""border: none;
                                background-color: rgba(0,0,0,0);""")
        
        # The Node Input Area Main Sub-Layout
        self.ElementInputScrollAreaWidgetLayout = QVBoxLayout() # Every addition input will be added here, Minor Widget will be added here, goes downwards, one Minor Widget Input, non formatting
        self.ElementInputScrollAreaWidgetLayout.setSpacing(0)
        self.ElementInputScrollAreaWidgetLayout.setContentsMargins(0,0,0,0) 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Element Input Area Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # region Minor Element Input 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # region Minor Element Input Widget and Layout Creation
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # The Element Input Main Struture
        self.ElementInputContainer = QWidget() # Contains input, will contain the nodeInputLayout, add to nodeInputScrollAreaWidgetLayout once done

        #The Elmenet Input Main Layout
        self.ElementInputLayout = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
        self.ElementInputLayout.setSpacing(0)
        self.ElementInputLayout.setContentsMargins(0,0,0,3)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Element Input Content
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Tiny Widgets
        self.indexNumberElement = QLabel("1")
        self.indexNumberElement.setStyleSheet("""
                                    min-width: 2em;
                                    max-width: 2em; """)
        
        self.genericInput = QLineEdit()
        self.genericInput.editingFinished.connect(lambda: self.onTextFinal(1)) #textChanged
        self.genericInput.setAlignment(Qt.AlignCenter)
        self.genericInput.setStyleSheet("background-color: white;")
        
        self.delete = QRadioButton()
        self.delete.setDisabled(True)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Element Input addition and layout
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Adding Tiny to The Node Input Main Layout
        self.ElementInputLayout.addWidget(self.indexNumberElement)
        self.ElementInputLayout.addWidget(self.genericInput)
        self.ElementInputLayout.addWidget(self.delete)
        
        self.ElementInputLayout.setAlignment(self.genericInput, Qt.AlignLeft)
        self.ElementInputLayout.setAlignment(self.delete, Qt.AlignCenter) 
        
        # Setting the Node Input Main Layout to the Node Input Main Struture
        self.ElementInputContainer.setLayout(self.ElementInputLayout)
        
        self.list_of_widgets = []
        self.list_of_widgets.append(self.ElementInputContainer)
        
        self.list_of_widgets_previous_text = []
        self.list_of_widgets_previous_text.append("0,0") # first always there 
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # endregion
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
    
        # region Major Element Input Area Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Element Input Area Main Sub-Layout
        self.ElementInputScrollAreaWidgetLayout.addWidget(self.ElementInputContainer)
        
        # Setting the Element Input Area Main Sub-Layout to the Element Input Area Main Sub-Struture
        self.ElementInputScrollAreaWidget.setLayout(self.ElementInputScrollAreaWidgetLayout)

        # Setting the Element Input Area Main Sub-Struture to the Element Input Area Main Struture
        self.ElementInputScorllArea.setWidget(self.ElementInputScrollAreaWidget)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Add Element Button Sub-Sub-Section
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Add Element Button Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(0) 
        self.buttonsLayout.setContentsMargins(0,0,0,0)
        
        self.buttonsContainer = QWidget()
        self.buttonsContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
        
        # None needed since it will be added to bottom and centered 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Element Button Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.addBackButton = QPushButton()
        self.addBackButton.setText("Back")
        self.addBackButton.setStyleSheet("""
                                            min-width: 3em;
                                            max-width: 3em;
                                                """)
        self.addBackButton.clicked.connect(lambda: self.onClickB())
        
        
        self.addElementButton = QPushButton()
        self.addElementButton.setText("Add Element")
        self.addElementButton.setStyleSheet("""
                                            min-width: 5.3em;
                                            max-width: 5.3em;
                                                """)
        self.addElementButton.clicked.connect(lambda: self.onClick())
        
        self.addCalcuateButton = QPushButton()
        self.addCalcuateButton.setText("Calcuate")
        self.addCalcuateButton.setStyleSheet("""
                                            min-width: 3.8em;
                                            max-width: 3.8em;
                                            
                                            background-color: #734c91;
                                            color: white;
                                                """)
        self.addCalcuateButton.clicked.connect(lambda: self.onClickC())
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Element Button addition and actualization
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.buttonsLayout.addWidget(self.addBackButton)
        self.buttonsLayout.addWidget(self.addElementButton)
        self.buttonsLayout.addWidget(self.addCalcuateButton)
        
        self.buttonsContainer.setLayout(self.buttonsLayout)
        # none needed since already widget and so will be added directly to node response layout 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Element Response Content addition and Actualization
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Adding Major to Element Response Main Layout
        self.ElementResponseLayout.addWidget(self.labelContainer)
        self.ElementResponseLayout.addWidget(self.ElementInputScorllArea) # chnge it back here
        self.ElementResponseLayout.addWidget(self.buttonsContainer)
        
        
        # Setting the Element Response Main Layout to the ELement Response Main Struture
        self.ElementResponseContainer.setLayout(self.ElementResponseLayout) 
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion
        #****************************************
        # endregion 
        #----------------------------------------
        # endregion
        
        # region Main Element Section addition and layout
        #----------------------------------------
        # Adding Primary to Second Main Layout
        self.ElementLayout.addWidget(self.noteContainer) # Added to Super Container Layout
        self.ElementLayout.addWidget(self.ElementResponseContainer)

        # Setting the Second Main Layout to the Second Main Struture 
        self.ElementContainer.setLayout(self.ElementLayout) # This will be added to MainLayout
        #----------------------------------------
        # endregion
        #========================================
        # endregion 
        
        # region Main Engineering Supports Section
        #========================================
        # region Main Engineering Supports Section Widget and Layout Creation
        #----------------------------------------
        # The Second Main Struture
        self.ESContainer = QGroupBox("Supports") # Contains all support related things, will contain the ESLayout
        self.ESContainer.setFixedWidth(550) # Has same coloring as MainWindow Widget
        
        # The Second Main Layout
        self.ESLayout = QVBoxLayout()  # Every Primary Widget will be added here, goes downwards, two Primaries Note and Response
        self.ESLayout.setSpacing(4) # The space inbetween widgets in ESLayout
        self.ESLayout.setContentsMargins(6,0,6,6) # The space inbetween the ends of the groupbox and the widgets inside
        #----------------------------------------
        # endregion
        
        # region Main Engineering Supports Section Content
        #----------------------------------------
        # region Primary Engineering Supports Note
        #****************************************
        self.createInfoLabel("Enter node as integer.") # Creates a widget called noteCotainer 
        #****************************************
        # endregion
            
        # region Primary Roller Response
        #****************************************
        # region Primary Roller Response Widget and Layout Creation
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # The Engineering Supports Response Main Struture
        self.ESResponseContainer = QFrame() # Contains all the reponses and heading, will contain the ESResponseLayout

        # The Engineering Supports Response Main Layout
        self.ESResponseLayout = QVBoxLayout() # Every Major Widget will be added here, goes downwards, three Major Widgets Label, Input Area, and add button
        self.ESResponseLayout.setSpacing(0)  
        self.ESResponseLayout.setContentsMargins(0,0,0,6)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Roller Supports Response Content
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # region Major Engineering Supports Label 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Engineering Supports Label Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Engineering Supports Label Main Struture
        self.ESlabelContainer = QWidget() # Contains all the info labels, will contain the elementLabelLayout
        self.ESlabelContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
    
        # The Engineering Supports Label Main Layout
        self.ESlabelLayout = QHBoxLayout() # Every Minor Widget will be added here, goes sideways, formatting
        self.ESlabelLayout.setSpacing(0) 
        self.ESlabelLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Engineering SupportsElement Label Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Minor Widgets
        self.indexLabelES = QLabel("#")
        self.indexLabelES.setStyleSheet("""
                                    min-width: 2em;
                                    max-width: 2em;
                                    
                                    background-color: rgba(0,0,0,0);""")
        
        self.nodeLabelES = QLabel("Roller")
        self.nodeLabelES.setStyleSheet("""
                                    min-width: 5em;
                                    max-width: 5em;
                            
                                    background-color: rgba(0,0,0,0);
        
                                    qproperty-alignment: AlignLeft;""")        
        
        self.deleteLabelES = QLabel("Delete")
        self.deleteLabelES.setStyleSheet("""
                                    min-width: 2.35em;
                                    max-width: 2.35em;
                                
                                    background-color: rgba(0,0,0,0);""")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Engineering Supports Label Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Node Label Main Layout
        self.ESlabelLayout.addWidget(self.indexLabelES)
        self.ESlabelLayout.addWidget(self.nodeLabelES)
        self.ESlabelLayout.addWidget(self.deleteLabelES)
        
        #self.labelLayout.setAlignment(self.indexLabel, Qt.AlignLeft)
        self.ESlabelLayout.setAlignment(self.nodeLabelES, Qt.AlignLeft)
        self.ESlabelLayout.setAlignment(self.deleteLabelES, Qt.AlignCenter) 
        
        # Setting the Node Label Main Layout to the Node Label Main Struture
        self.ESlabelContainer.setLayout(self.ESlabelLayout)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Engineering Supports Input Area 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Engineering Supports Input Area Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Engineering Supports Input Area Main Struture
        self.ESInputScorllArea = QScrollArea() # Controls the Scroll Area for the Widget that contains all the inputs
        self.ESInputScorllArea.setWidgetResizable(True)
        self.ESInputScorllArea.setMinimumHeight(45)
        self.ESInputScorllArea.setStyleSheet("""border-color: rgba(0,0,0,0);
                                                background-color: black;""")
        
        # The Engineering Supports Input Area Main Sub-Struture
        self.ESInputScrollAreaWidget = QWidget() # Widget that will hold all inputs, will be the central widget for nodeInputScrollArea, will contain the nodeInputScrollAreaWidgetLayout
        self.ESInputScrollAreaWidget.setContentsMargins(0,0,0,0)
        self.ESInputScrollAreaWidget.setStyleSheet("""border: none;
                                background-color: rgba(0,0,0,0);""")
        
        # The Engineering Supports Input Area Main Sub-Layout
        self.ESInputScrollAreaWidgetLayout = QVBoxLayout() # Every addition input will be added here, Minor Widget will be added here, goes downwards, one Minor Widget Input, non formatting
        self.ESInputScrollAreaWidgetLayout.setSpacing(0)
        self.ESInputScrollAreaWidgetLayout.setContentsMargins(0,0,0,0) 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Engineering Supports Input Area Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # region Minor Engineering Supports Input 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # region Minor Engineering Supports Input Widget and Layout Creation
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # The Engineering Supports Input Main Struture
        self.ESInputContainer = QWidget() # Contains input, will contain the nodeInputLayout, add to nodeInputScrollAreaWidgetLayout once done

        #The Engineering Supports Input Main Layout
        self.ESInputLayout = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
        self.ESInputLayout.setSpacing(0)
        self.ESInputLayout.setContentsMargins(0,0,0,3)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Engineering Supports Supports Input Content
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Tiny Widgets
        self.indexNumberES = QLabel("1")
        self.indexNumberES.setStyleSheet("""
                                    min-width: 2em;
                                    max-width: 2em; """)
        
        self.genericInputES = QLineEdit()
        self.genericInputES.editingFinished.connect(lambda: self.onTextFinalR(1)) #textChanged
        self.genericInputES.setAlignment(Qt.AlignCenter)
        self.genericInputES.setStyleSheet("background-color: white;")
        
        self.deleteES = QRadioButton()
        self.deleteES.setDisabled(True)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Engineering Supports Supports Input addition and layout
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Adding Tiny to The Node Input Main Layout
        self.ESInputLayout.addWidget(self.indexNumberES)
        self.ESInputLayout.addWidget(self.genericInputES)
        self.ESInputLayout.addWidget(self.deleteES)
        
        self.ESInputLayout.setAlignment(self.genericInputES, Qt.AlignLeft)
        self.ESInputLayout.setAlignment(self.deleteES, Qt.AlignCenter) 
        
        # Setting the Engineering Supports Input Main Layout to the Engineering Supports Input Main Struture
        self.ESInputContainer.setLayout(self.ESInputLayout)
        
        # list of widgets for roller
        self.list_of_widgetsR = []
        self.list_of_widgetsR.append(self.ESInputContainer)
        
        self.list_of_widgets_previous_textR = []
        self.list_of_widgets_previous_textR.append("0,0") # first always there 
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # endregion
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
    
        # region Major Engineering Supports Input Area Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Engineering Supports Input Area Main Sub-Layout
        self.ESInputScrollAreaWidgetLayout.addWidget(self.ESInputContainer)
        
        # Setting the Engineering Supports Input Area Main Sub-Layout to the Engineering Supports Input Area Main Sub-Struture
        self.ESInputScrollAreaWidget.setLayout(self.ESInputScrollAreaWidgetLayout)

        # Setting the Engineering Supports Input Area Main Sub-Struture to the Engineering Supports Input Area Main Struture
        self.ESInputScorllArea.setWidget(self.ESInputScrollAreaWidget)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Add Engineering Supports Button Sub-Sub-Section
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Add Element Button Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.ESbuttonsLayout = QHBoxLayout()
        self.ESbuttonsLayout.setSpacing(0) 
        self.ESbuttonsLayout.setContentsMargins(0,0,0,0)
        
        self.ESbuttonsContainer = QWidget()
        self.ESbuttonsContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
        
        # None needed since it will be added to bottom and centered 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Element Button Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^          
        self.addElementButtonES = QPushButton()
        self.addElementButtonES.setText("Add Roller")
        self.addElementButtonES.setStyleSheet("""
                                            min-width: 5.3em;
                                            max-width: 5.3em;
                                                """)
        self.addElementButtonES.clicked.connect(lambda: self.onClickR())
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Engineering Supports Button addition and actualization
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #self.ESbuttonsLayout.addWidget(self.addElementButtonES)
        
        #self.ESbuttonsContainer.setLayout(self.ESbuttonsLayout)
        # none needed since already widget and so will be added directly to node response layout 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Roller Supports Response Content addition and Actualization
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Adding Major to Engineering Supports Response Main Layout
        self.ESResponseLayout.addWidget(self.ESlabelContainer)
        self.ESResponseLayout.addWidget(self.ESInputScorllArea) # chnge it back here
        self.ESResponseLayout.addWidget(self.addElementButtonES)
        
        self.ESResponseLayout.setAlignment(self.addElementButtonES, Qt.AlignCenter)

        # Setting the Engineering Supports Response Main Layout to the Engineering Supports Response Main Struture
        self.ESResponseContainer.setLayout(self.ESResponseLayout) 
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion
        #****************************************
        # endregion 
        
        # region Primary Pin Response
        #****************************************
        # region Primary Pin Response Widget and Layout Creation
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # The Engineering Supports Response Main Struture
        self.ESPResponseContainer = QFrame() # Contains all the reponses and heading, will contain the ESResponseLayout

        # The Engineering Supports Response Main Layout
        self.ESPResponseLayout = QVBoxLayout() # Every Major Widget will be added here, goes downwards, three Major Widgets Label, Input Area, and add button
        self.ESPResponseLayout.setSpacing(0)  
        self.ESPResponseLayout.setContentsMargins(0,0,0,6)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Pin Supports Response Content
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # region Major Engineering Supports Label 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Engineering Supports Label Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Engineering Supports Label Main Struture
        self.ESPlabelContainer = QWidget() # Contains all the info labels, will contain the elementLabelLayout
        self.ESPlabelContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
    
        # The Engineering Supports Label Main Layout
        self.ESPlabelLayout = QHBoxLayout() # Every Minor Widget will be added here, goes sideways, formatting
        self.ESPlabelLayout.setSpacing(0) 
        self.ESPlabelLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Engineering SupportsElement Label Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Minor Widgets
        self.indexLabelESP = QLabel("#")
        self.indexLabelESP.setStyleSheet("""
                                    min-width: 2em;
                                    max-width: 2em;
                                    
                                    background-color: rgba(0,0,0,0);""")
        
        self.nodeLabelESP = QLabel("Pin")
        self.nodeLabelESP.setStyleSheet("""
                                    min-width: 5em;
                                    max-width: 5em;
                            
                                    background-color: rgba(0,0,0,0);
        
                                    qproperty-alignment: AlignLeft;""")        
        
        self.deleteLabelESP = QLabel("Delete")
        self.deleteLabelESP.setStyleSheet("""
                                    min-width: 2.35em;
                                    max-width: 2.35em;
                                
                                    background-color: rgba(0,0,0,0);""")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Engineering Supports Label Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Node Label Main Layout
        self.ESPlabelLayout.addWidget(self.indexLabelESP)
        self.ESPlabelLayout.addWidget(self.nodeLabelESP)
        self.ESPlabelLayout.addWidget(self.deleteLabelESP)
        
        #self.labelLayout.setAlignment(self.indexLabel, Qt.AlignLeft)
        self.ESPlabelLayout.setAlignment(self.nodeLabelESP, Qt.AlignLeft)
        self.ESPlabelLayout.setAlignment(self.deleteLabelESP, Qt.AlignCenter) 
        
        # Setting the Node Label Main Layout to the Node Label Main Struture
        self.ESPlabelContainer.setLayout(self.ESPlabelLayout)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Engineering Supports Input Area 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Engineering Supports Input Area Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Engineering Supports Input Area Main Struture
        self.ESPInputScorllArea = QScrollArea() # Controls the Scroll Area for the Widget that contains all the inputs
        self.ESPInputScorllArea.setWidgetResizable(True)
        self.ESPInputScorllArea.setMinimumHeight(45)
        self.ESPInputScorllArea.setStyleSheet("""border-color: rgba(0,0,0,0);
                                                background-color: black;""")
        
        # The Engineering Supports Input Area Main Sub-Struture
        self.ESPInputScrollAreaWidget = QWidget() # Widget that will hold all inputs, will be the central widget for nodeInputScrollArea, will contain the nodeInputScrollAreaWidgetLayout
        self.ESPInputScrollAreaWidget.setContentsMargins(0,0,0,0)
        self.ESPInputScrollAreaWidget.setStyleSheet("""border: none;
                                background-color: rgba(0,0,0,0);""")
        
        # The Engineering Supports Input Area Main Sub-Layout
        self.ESPInputScrollAreaWidgetLayout = QVBoxLayout() # Every addition input will be added here, Minor Widget will be added here, goes downwards, one Minor Widget Input, non formatting
        self.ESPInputScrollAreaWidgetLayout.setSpacing(0)
        self.ESPInputScrollAreaWidgetLayout.setContentsMargins(0,0,0,0) 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Engineering Supports Input Area Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # region Minor Engineering Supports Input 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # region Minor Engineering Supports Input Widget and Layout Creation
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # The Engineering Supports Input Main Struture
        self.ESPInputContainer = QWidget() # Contains input, will contain the nodeInputLayout, add to nodeInputScrollAreaWidgetLayout once done

        #The Engineering Supports Input Main Layout
        self.ESPInputLayout = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
        self.ESPInputLayout.setSpacing(0)
        self.ESPInputLayout.setContentsMargins(0,0,0,3)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Engineering Supports Supports Input Content
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Tiny Widgets
        self.indexNumberESP = QLabel("1")
        self.indexNumberESP.setStyleSheet("""
                                    min-width: 2em;
                                    max-width: 2em; """)
        
        self.genericInputESP = QLineEdit()
        self.genericInputESP.editingFinished.connect(lambda: self.onTextFinalRP(1)) #textChanged
        self.genericInputESP.setAlignment(Qt.AlignCenter)
        self.genericInputESP.setStyleSheet("background-color: white;")
        
        self.deleteESP = QRadioButton()
        self.deleteESP.setDisabled(True)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Engineering Supports Supports Input addition and layout
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Adding Tiny to The Node Input Main Layout
        self.ESPInputLayout.addWidget(self.indexNumberESP)
        self.ESPInputLayout.addWidget(self.genericInputESP)
        self.ESPInputLayout.addWidget(self.deleteESP)
        
        self.ESPInputLayout.setAlignment(self.genericInputESP, Qt.AlignLeft)
        self.ESPInputLayout.setAlignment(self.deleteESP, Qt.AlignCenter) 
        
        # Setting the Engineering Supports Input Main Layout to the Engineering Supports Input Main Struture
        self.ESPInputContainer.setLayout(self.ESPInputLayout)
        
        # list of widgets for roller
        self.list_of_widgetsRP = []
        self.list_of_widgetsRP.append(self.ESPInputContainer)
        
        self.list_of_widgets_previous_textRP = []
        self.list_of_widgets_previous_textRP.append("0,0") # first always there 
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # endregion
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
    
        # region Major Engineering Supports Input Area Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Engineering Supports Input Area Main Sub-Layout
        self.ESPInputScrollAreaWidgetLayout.addWidget(self.ESPInputContainer)
        
        # Setting the Engineering Supports Input Area Main Sub-Layout to the Engineering Supports Input Area Main Sub-Struture
        self.ESPInputScrollAreaWidget.setLayout(self.ESPInputScrollAreaWidgetLayout)

        # Setting the Engineering Supports Input Area Main Sub-Struture to the Engineering Supports Input Area Main Struture
        self.ESPInputScorllArea.setWidget(self.ESPInputScrollAreaWidget)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Add Engineering Supports Button Sub-Sub-Section
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Add Element Button Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.ESPbuttonsLayout = QHBoxLayout()
        self.ESPbuttonsLayout.setSpacing(0) 
        self.ESPbuttonsLayout.setContentsMargins(0,0,0,0)
        
        self.ESPbuttonsContainer = QWidget()
        self.ESPbuttonsContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
        
        # None needed since it will be added to bottom and centered 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Element Button Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^          
        self.addElementButtonESP = QPushButton()
        self.addElementButtonESP.setText("Add Pin")
        self.addElementButtonESP.setStyleSheet("""
                                            min-width: 5.3em;
                                            max-width: 5.3em;
                                                """)
        self.addElementButtonESP.clicked.connect(lambda: self.onClickRP())
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Engineering Supports Button addition and actualization
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #self.ESbuttonsLayout.addWidget(self.addElementButtonES)
        
        #self.ESbuttonsContainer.setLayout(self.ESbuttonsLayout)
        # none needed since already widget and so will be added directly to node response layout 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Pin Supports Response Content addition and Actualization
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Adding Major to Engineering Supports Response Main Layout
        self.ESPResponseLayout.addWidget(self.ESPlabelContainer)
        self.ESPResponseLayout.addWidget(self.ESPInputScorllArea) # chnge it back here
        self.ESPResponseLayout.addWidget(self.addElementButtonESP)
        
        self.ESPResponseLayout.setAlignment(self.addElementButtonESP, Qt.AlignCenter)

        # Setting the Engineering Supports Response Main Layout to the Engineering Supports Response Main Struture
        self.ESPResponseContainer.setLayout(self.ESPResponseLayout) 
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion
        #****************************************
        # endregion
        #----------------------------------------
        # endregion
        
        # region Main Engineering Supports Section addition and layout
        #----------------------------------------
        # Adding Primary to Second Main Layout
        self.ESLayout.addWidget(self.noteContainer) # Added to Super Container Layout
        self.ESLayout.addWidget(self.ESResponseContainer)
        self.ESLayout.addWidget(self.ESPResponseContainer)

        # Setting the Second Main Layout to the Second Main Struture 
        self.ESContainer.setLayout(self.ESLayout) # This will be added to MainLayout
        #----------------------------------------
        # endregion
        #========================================
        # endregion
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
        
        # region Window addition, layout, and Actualization
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.mainLayout.addWidget(self.ElementContainer) # First Column
        self.mainLayout.addWidget(self.ESContainer)

        self.canvas.setLayout(self.mainLayout) 
        
        self.setCentralWidget(self.canvas)
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
    
    def createInfoLabel(self, message):
        # region Info Label Widget and Layout Creation
        #(((((((((((((((((((())))))))))))))))))))
        self.noteContainer = QFrame() # To get outline of note
        self.noteContainer.setFixedHeight(100) # On frame min and max
        self.noteLayout = QVBoxLayout() # Add things up to down
        self.noteLayout.setSpacing(0)
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
        # region Info Label Content
        #(((((((((((((((((((())))))))))))))))))))
        self.note = QLabel("Note:") # look at master style sheet
        self.note.setStyleSheet("qproperty-alignment: AlignLeft;")
        
        self.genericInfo = QLabel(message) # look at master style sheet
        # by default Q label text is centered in master style sheet
        #(((((((((((((((((((())))))))))))))))))))
        # endregion
        
        # region Info Label addition and layout
        #(((((((((((((((((((())))))))))))))))))))
        self.noteLayout.addWidget(self.note)
        self.noteLayout.addWidget(self.genericInfo)
        
        self.noteContainer.setLayout(self.noteLayout) # returns this, to be added to layout
        #(((((((((((((((((((())))))))))))))))))))
        # endregion

    def onClick(self):    
        self.createMinorElementResponse(len(self.list_of_widgets) + 1) # before element gets added         
        self.repaint()
        
    def onClickB(self):
        print("going back")
        
    def onClickC(self):
        self.Graphics.solve_matrix()
        
    def onClickR(self):
        self.createMinorRollerResponse(len(self.list_of_widgetsR) + 1) # before element gets added         
        self.repaint()
        
    def onClickRP(self):
        self.createMinorPinResponse(len(self.list_of_widgetsRP) + 1)
        self.repaint()
        
    def createMinorElementResponse(self, number):
            # region Minor Element Response Widget and Layout Creation
            #(((((((((((((((((((())))))))))))))))))))
            self.genericRowWidget = QWidget()
            self.genericRowWidget.setMinimumHeight(45)
            self.genericHorizationalLayout = QHBoxLayout()
            self.genericHorizationalLayout.setSpacing(0)
            self.genericHorizationalLayout.setContentsMargins(0,0,0,0)
            #(((((((((((((((((((())))))))))))))))))))
            # endregion
            
            # region Minor Element Response Content
            #(((((((((((((((((((())))))))))))))))))))
            self.indexNumber_1 = QLabel(f"{number}")
            self.indexNumber_1.setStyleSheet("""
                                        min-width: 2em;
                                        max-width: 2em;
                                        """)
            
            self.genericInput_1 = QLineEdit()
            self.genericInput_1.setAlignment(Qt.AlignCenter)
            self.genericInput_1.setStyleSheet("background-color: white;")
            
            self.delete_1 = QRadioButton()
            #(((((((((((((((((((())))))))))))))))))))
            # endregion
            
            # region Minor Element Response addition and layout
            #(((((((((((((((((((())))))))))))))))))))
            self.genericHorizationalLayout.addWidget(self.indexNumber_1)
            self.genericHorizationalLayout.addWidget(self.genericInput_1)
            self.genericHorizationalLayout.addWidget(self.delete_1)
            
            self.genericHorizationalLayout.setAlignment(self.genericInput_1, Qt.AlignLeft)
            self.genericHorizationalLayout.setAlignment(self.delete_1, Qt.AlignCenter)
            
            self.genericRowWidget.setLayout(self.genericHorizationalLayout)
            
            # important here for numbers
            self.list_of_widgets.append(self.genericRowWidget) # now added to list so official counted
            self.list_of_widgets_previous_text.append("0,0") #store preivous good text
            
            self.genericInput_1.editingFinished.connect(lambda: self.onTextFinal(number)) #textChanged
            
            self.ElementInputScrollAreaWidgetLayout.addWidget(self.genericRowWidget)
            #(((((((((((((((((((())))))))))))))))))))
            # endregion
    
    def createMinorRollerResponse(self, number):
            # region Minor Engineering Supports Input Widget and Layout Creation
            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            # The Engineering Supports Input Main Struture
            self.ESInputContainerG = QWidget() # Contains input, will contain the nodeInputLayout, add to nodeInputScrollAreaWidgetLayout once done

            #The Engineering Supports Input Main Layout
            self.ESInputLayoutG = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
            self.ESInputLayoutG.setSpacing(0)
            self.ESInputLayoutG.setContentsMargins(0,0,0,3)
            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            # endregion
            
            # region Minor Engineering Supports Supports Input Content
            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            # Tiny Widgets
            self.indexNumberESG = QLabel(f'{number}')
            self.indexNumberESG.setStyleSheet("""
                                        min-width: 2em;
                                        max-width: 2em; """)
            
            self.genericInputESG = QLineEdit()
            self.genericInputESG.setAlignment(Qt.AlignCenter)
            self.genericInputESG.setStyleSheet("background-color: white;")
            
            self.deleteESG = QRadioButton()
            self.deleteESG.setDisabled(True)
            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            # endregion
            
            # region Minor Engineering Supports Supports Input addition and layout
            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            # Adding Tiny to The Node Input Main Layout
            self.ESInputLayoutG.addWidget(self.indexNumberESG)
            self.ESInputLayoutG.addWidget(self.genericInputESG)
            self.ESInputLayoutG.addWidget(self.deleteESG)
            
            self.ESInputLayoutG.setAlignment(self.genericInputESG, Qt.AlignLeft)
            self.ESInputLayoutG.setAlignment(self.deleteESG, Qt.AlignCenter) 
            
            # Setting the Engineering Supports Input Main Layout to the Engineering Supports Input Main Struture
            self.ESInputContainerG.setLayout(self.ESInputLayoutG)
            
            # list of widgets for roller
            self.list_of_widgetsR.append(self.ESInputContainerG)
            self.list_of_widgets_previous_textR.append("0,0") #store preivous good text
            
            self.genericInputESG.editingFinished.connect(lambda: self.onTextFinalR(number)) #textChanged
            
            self.ESInputScrollAreaWidgetLayout.addWidget(self.ESInputContainerG)
            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            # endregion

    def createMinorPinResponse(self, number):
        # region Minor Engineering Supports Input Widget and Layout Creation
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # The Engineering Supports Input Main Struture
        self.ESPInputContainerG = QWidget() # Contains input, will contain the nodeInputLayout, add to nodeInputScrollAreaWidgetLayout once done

        #The Engineering Supports Input Main Layout
        self.ESPInputLayoutG = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
        self.ESPInputLayoutG.setSpacing(0)
        self.ESPInputLayoutG.setContentsMargins(0,0,0,3)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Engineering Supports Supports Input Content
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Tiny Widgets
        self.indexNumberESGP = QLabel(f'{number}')
        self.indexNumberESGP.setStyleSheet("""
                                    min-width: 2em;
                                    max-width: 2em; """)
        
        self.genericInputESGP = QLineEdit()
        self.genericInputESGP.setAlignment(Qt.AlignCenter)
        self.genericInputESGP.setStyleSheet("background-color: white;")
        
        self.deleteESGP = QRadioButton()
        self.deleteESGP.setDisabled(True)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Engineering Supports Supports Input addition and layout
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Adding Tiny to The Node Input Main Layout
        self.ESPInputLayoutG.addWidget(self.indexNumberESGP)
        self.ESPInputLayoutG.addWidget(self.genericInputESGP)
        self.ESPInputLayoutG.addWidget(self.deleteESGP)
        
        self.ESPInputLayoutG.setAlignment(self.genericInputESGP, Qt.AlignLeft)
        self.ESPInputLayoutG.setAlignment(self.deleteESGP, Qt.AlignCenter) 
        
        # Setting the Engineering Supports Input Main Layout to the Engineering Supports Input Main Struture
        self.ESPInputContainerG.setLayout(self.ESPInputLayoutG)
        
        # list of widgets for roller
        self.list_of_widgetsRP.append(self.ESPInputContainerG)
        self.list_of_widgets_previous_textRP.append("0,0") #store preivous good text
        
        self.genericInputESGP.editingFinished.connect(lambda: self.onTextFinalRP(number)) #textChanged
        
        self.ESPInputScrollAreaWidgetLayout.addWidget(self.ESPInputContainerG)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion

    def onTextFinal(self,number):
        print(f"Number of elements are {len(self.list_of_widgets)}.")
        yo = self.list_of_widgets[number - 1] # gives button based on current total number like 20
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list
        
        print(f"Line {number} has text {hey[0].text()}") # go to the first QLineEdit in the list and grab the text from it
        
        print("Element creation started-") # the process really starts from here
        print("------------")
        self.lineParsing(hey[0].text(), number) # if number and label are same then can just replace with number
    
    def onTextFinalR(self, number):
        print(f"Number of rollers are {len(self.list_of_widgetsR)}.")
        yo = self.list_of_widgetsR[number - 1] # gives button based on current total number like 20
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list
        
        print(f"Line {number} has text {hey[0].text()}") # go to the first QLineEdit in the list and grab the text from it
        
        print("Roller process started-") # the process really starts from here
        print("------------")
        self.lineParsingR(hey[0].text(), number) # if number and label are same then can just replace with number

    def onTextFinalRP(self, number):
        print(f"Number of pins are {len(self.list_of_widgetsRP)}.")
        yo = self.list_of_widgetsRP[number - 1] # gives button based on current total number like 20
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list
        
        print(f"Line {number} has text {hey[0].text()}") # go to the first QLineEdit in the list and grab the text from it
        
        print("Pin process started-") # the process really starts from here
        print("------------")
        self.lineParsingRP(hey[0].text(), number) # if number and label are same then can just replace with number

    def lineParsing(self, text, number):
        try:
            i,j = text.split(",") # Grab the text and break it into two parts

            self.Graphics.element_check(number, int(i), int(j))
                        
            self.list_of_widgets_previous_text[number - 1] = text # replace zeros with good number
            print("=======================")
            
        except:
            print("node created unsuccessfully")
            print("format was not followed")
            self.cleartext(number)
            print("=======================")
            
    def lineParsingR(self, text, number):
        try:
            self.Graphics.roller_check(int(text), number)
                        
            self.list_of_widgets_previous_textR[number - 1] = text # replace zeros with good number
            print("Roller process completed-")
            print("=======================")
            
        except:
            print("------------")
            print("Roller process failed-")
            print("Format was not followed")
            self.cleartext(number)
            print("=======================")
    
    def lineParsingRP(self, text, number):
        try:
            self.Graphics.pin_check(int(text), number)
                        
            self.list_of_widgets_previous_textRP[number - 1] = text # replace zeros with good number
            print("Pin process completed-")
            print("=======================")
            
        except:
            print("------------")
            print("Pin process failed-")
            print("Format was not followed")
            self.cleartext(number)
            print("=======================")
         
    def cleartext(self, number):
        yo = self.list_of_widgets[number - 1] # gives button based on current total number like 20
        
        hey = yo.findChildren(QLineEdit) # finds all QLineEdits in second button (there is only one) and give them in a list
        hey[0].clear()
            
        print(f"Line {number} has been cleared.") # go to the first QLineEdit in the list and grab the text from it
        
        hey[0].setText(self.list_of_widgets_previous_text[number - 1])
    
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
                        
                        qproperty-alignment: AlignCenter;}
                        
                        QLineEdit{font-size: 35px;
                        max-width: 5em;
                        max-height: 1em;}
                        
                        QScrollBar {
                            color: white;}
                        
                        QPushButton{background-color: black;
                        border-color: #a868d9;
                        border-style: outset;
                        border-width: 1px;
                        border-radius: 10px;
                        font: bold 35px;
                        color: white;
                        min-width: 6em;
                        max-height: 0.7em;}
                      
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
                        """)
        window = MainWindow() # Create a instance of the MainWindow Class
        window.show()
       
        sys.exit(App.exec())
        
ex = UI.start()