############################################################################
##
## Copyright (C) 2006-2007 University of Utah. All rights reserved.
##
## This file is part of VisTrails.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following to ensure GNU General Public
## Licensing requirements will be met:
## http://www.opensource.org/licenses/gpl-license.php
##
## If you are unsure which license is appropriate for your use (for
## instance, you are interested in developing a commercial derivative
## of VisTrails), please contact us at vistrails@sci.utah.edu.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
############################################################################
""" This modules builds a widget to interact with vistrail diff
operation """
from PyQt4 import QtCore, QtGui
from core.utils.color import ColorByName
from gui.pipeline_view import QPipelineView
from gui.theme import CurrentTheme
import copy

################################################################################

class QFunctionItemModel(QtGui.QStandardItemModel):
    """
    QFunctionItemModel is a item model that will allow item to be
    show as a disabled one on the table
    
    """
    def __init__(self, row, col, parent=None):
        """ QFunctionItemModel(row: int, col: int, parent: QWidget)
                              -> QFunctionItemModel                             
        Initialize with a number of rows and columns
        
        """
        QtGui.QStandardItemModel.__init__(self, row, col, parent)
        self.disabledRows = {}

    def flags(self, index):
        """ flags(index: QModelIndex) -> None
        Return the current flags of the item with the index 'index'
        
        """
        if index.isValid() and self.disabledRows.has_key(index.row()):
            return (QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled |
                    QtCore.Qt.ItemIsSelectable)
        return QtGui.QStandardItemModel.flags(self,index)

    def clearList(self):
        """ clearList() -> None
        Clear all items including the disabled ones
        
        """
        self.disabledRows = {}
        self.removeRows(0,self.rowCount())

    def disableRow(self,row):
        """ disableRow(row: int) -> None
        Disable a specific row on the table
        
        """
        self.disabledRows[row] = None

class QParamTable(QtGui.QTableView):
    """
    QParamTable is a widget represents a diff between two version
    as side-by-side comparisons
    
    """
    def __init__(self, v1Name=None, v2Name=None, parent=None):
        """ QParamTable(v1Name: str, v2Name: str, parent: QWidget)
                       -> QParamTable
        Initialize the table with two version names on the header view
        
        """
        QtGui.QTableView.__init__(self, parent)
        itemModel = QFunctionItemModel(0, 2, self)
        itemModel.setHeaderData(0, QtCore.Qt.Horizontal,
                                QtCore.QVariant(v1Name))
        itemModel.setHeaderData(1, QtCore.Qt.Horizontal,
                                QtCore.QVariant(v2Name))
        self.setModel(itemModel)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)        
        self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)        
        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)        
        self.setFont(CurrentTheme.VISUAL_DIFF_PARAMETER_FONT)
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        

class QParamInspector(QtGui.QWidget):
    """
    QParamInspector is a widget acting as an inspector vistrail modules
    in diff mode. It consists of a function inspector and annotation
    inspector
    
    """
    def __init__(self, v1Name='', v2Name='',
                 parent=None, f=QtCore.Qt.WindowFlags()):
        """ QParamInspector(v1Name: str, v2Name: str,
                            parent: QWidget, f: WindowFlags)
                            -> QParamInspector
        Construct a widget containing tabs: Functions and Annotations,
        each of them is in turn a table of two columns for two
        corresponding versions.
        
        """
        QtGui.QWidget.__init__(self, parent, f | QtCore.Qt.Tool)
        self.setWindowTitle('Parameter Inspector - None')
        self.firstTime = True        
        self.boxLayout = QtGui.QVBoxLayout()
        self.boxLayout.setMargin(0)
        self.boxLayout.setSpacing(0)
        self.tabWidget = QtGui.QTabWidget()
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.functionsTab = QParamTable(v1Name, v2Name)
        self.tabWidget.addTab(self.functionsTab, 'Functions')        
        self.annotationsTab = QParamTable(v1Name, v2Name)
        self.annotationsTab.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.annotationsTab, 'Annotations')        
        self.boxLayout.addWidget(self.tabWidget)
        self.boxLayout.addWidget(QtGui.QSizeGrip(self))
        self.setLayout(self.boxLayout)

    def closeEvent(self, e):
        """ closeEvent(e: QCloseEvent) -> None        
        Doesn't allow the QParamInspector widget to close, but just hide
        instead
        
        """
        e.ignore()
        self.parent().showInspectorAction.setChecked(False)
        

class QLegendBox(QtGui.QFrame):
    """
    QLegendBox is just a rectangular box with a solid color
    
    """
    def __init__(self, brush, size, parent=None, f=QtCore.Qt.WindowFlags()):
        """ QLegendBox(color: QBrush, size: (int,int), parent: QWidget,
                      f: WindowFlags) -> QLegendBox
        Initialize the widget with a color and fixed size
        
        """
        QtGui.QFrame.__init__(self, parent, f)
        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.setAttribute(QtCore.Qt.WA_PaintOnScreen)
        self.setAutoFillBackground(True)
        self.palette().setBrush(QtGui.QPalette.Window, brush)
        self.setFixedSize(*size)        

class QLegendWindow(QtGui.QWidget):
    """
    QLegendWindow contains a list of QLegendBox and its description
    
    """
    def __init__(self, v1Name='', v2Name= None, parent='',
                 f=QtCore.Qt.WindowFlags()):
        """ QLegendWindow(v1Name: str, v2Name: str,
                          parent: QWidget, f: WindowFlags)
                          -> QLegendWindow
        Construct a window by default with 4 QLegendBox and 4 QLabels
        
        """
        QtGui.QWidget.__init__(self, parent,
                               f | QtCore.Qt.Tool )
        self.setWindowTitle('Visual Diff Legend')
        self.firstTime = True
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setMargin(10)
        self.gridLayout.setSpacing(10)
        self.setFont(CurrentTheme.VISUAL_DIFF_LEGEND_FONT)
        
        parent = self.parent()
        
        self.legendV1Box = QLegendBox(
            CurrentTheme.VISUAL_DIFF_FROM_VERSION_BRUSH,
            CurrentTheme.VISUAL_DIFF_LEGEND_SIZE,
            self)        
        self.gridLayout.addWidget(self.legendV1Box, 0, 0)
        self.legendV1 = QtGui.QLabel("Version '" + v1Name + "'", self)
        self.gridLayout.addWidget(self.legendV1, 0, 1)
        
        self.legendV2Box = QLegendBox(
            CurrentTheme.VISUAL_DIFF_TO_VERSION_BRUSH,            
            CurrentTheme.VISUAL_DIFF_LEGEND_SIZE,
            self)        
        self.gridLayout.addWidget(self.legendV2Box, 1, 0)
        self.legendV2 = QtGui.QLabel("Version '" + v2Name + "'", self)
        self.gridLayout.addWidget(self.legendV2, 1, 1)
        
        self.legendV12Box = QLegendBox(CurrentTheme.VISUAL_DIFF_SHARED_BRUSH,
                                       CurrentTheme.VISUAL_DIFF_LEGEND_SIZE,
                                       self)
        self.gridLayout.addWidget(self.legendV12Box, 2, 0)
        self.legendV12 = QtGui.QLabel("Shared", self)
        self.gridLayout.addWidget(self.legendV12, 2, 1)
        
        self.legendParamBox = QLegendBox(
            CurrentTheme.VISUAL_DIFF_PARAMETER_CHANGED_BRUSH,
            CurrentTheme.VISUAL_DIFF_LEGEND_SIZE,
            self)
        self.gridLayout.addWidget(self.legendParamBox,3,0)
        self.legendParam = QtGui.QLabel("Parameter Changes", self)
        self.gridLayout.addWidget(self.legendParam,3,1)
        self.adjustSize()
        
    def closeEvent(self,e):
        """ closeEvent(e: QCloseEvent) -> None
        Doesn't allow the Legend widget to close, but just hide
        instead
        
        """
        e.ignore()
        self.parent().showLegendsAction.setChecked(False)
        

class QVisualDiff(QtGui.QMainWindow):
    """
    QVisualDiff is a main widget for Visual Diff containing a GL
    Widget to draw the pipeline
    
    """
    def __init__(self, vistrail, v1, v2,
                 parent=None, f=QtCore.Qt.WindowFlags()):
        """ QVisualDiff(vistrail: Vistrail, v1: str, v2: str,
                        parent: QWidget, f: WindowFlags) -> QVisualDiff
        Initialize with all
        
        """
        # Set up the version name correctly
        v1Name = vistrail.getVersionName(v1)
        if not v1Name: v1Name = 'Version %d' % v1
        v2Name = vistrail.getVersionName(v2)        
        if not v2Name: v2Name = 'Version %d' % v2
        
        # Actually perform the diff and store its result
        self.diff = vistrail.getPipelineDiff(v1, v2)

        # Create the top-level Visual Diff window
        visDiffParent = QtCore.QCoreApplication.instance().visDiffParent
        windowDecors = f | QtCore.Qt.Dialog |QtCore.Qt.WindowMaximizeButtonHint
        QtGui.QMainWindow.__init__(self, visDiffParent,
                                   )
        self.setWindowTitle('Visual Diff - %s vs. %s' % (v1Name, v2Name))
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                             QtGui.QSizePolicy.Expanding))
        self.createPipelineView()
        self.createToolBar()
        self.createToolWindows(v1Name, v2Name)

    def createPipelineView(self):
        """ createPipelineView() -> None        
        Create a center pipeline view for Visual Diff and setup the
        view based on the diff result self.diff
        
        """
        # Initialize the shape engine
        self.pipelineView = QPipelineView()
        self.setCentralWidget(self.pipelineView)

        # Add all the shapes into the view
        self.createDiffPipeline()

        # Hook shape selecting functions
        self.connect(self.pipelineView.scene(), QtCore.SIGNAL("moduleSelected"),
                     self.moduleSelected)

    def createToolBar(self):
        """ createToolBar() -> None        
        Create the default toolbar of Visual Diff window with two
        buttons to toggle the Parameter Inspector and Legend window
        
        """
        # Initialize the Visual Diff toolbar
        self.toolBar = self.addToolBar('Visual Diff Toolbar')
        self.toolBar.setMovable(False)

        # Add the Show Parameter Inspector action
        self.showInspectorAction = self.toolBar.addAction(
            CurrentTheme.VISUAL_DIFF_SHOW_PARAM_ICON,
            'Show Parameter Inspector window')
        self.showInspectorAction.setCheckable(True)
        self.connect(self.showInspectorAction, QtCore.SIGNAL("toggled(bool)"),
                     self.toggleShowInspector)
        
        # Add the Show Legend window action
        self.showLegendsAction = self.toolBar.addAction(
            CurrentTheme.VISUAL_DIFF_SHOW_LEGEND_ICON,
            'Show Legends')
        self.showLegendsAction.setCheckable(True)
        self.connect(self.showLegendsAction, QtCore.SIGNAL("toggled(bool)"),
                     self.toggleShowLegend)

    def createToolWindows(self, v1Name, v2Name):
        """ createToolWindows(v1Name: str, v2Name: str) -> None
        Create Inspector and Legend window

        """
        self.inspector = QParamInspector(v1Name, v2Name, self)
        self.inspector.resize(QtCore.QSize(
            *CurrentTheme.VISUAL_DIFF_PARAMETER_WINDOW_SIZE))
        self.legendWindow = QLegendWindow(v1Name, v2Name,self)

    def moduleSelected(self, id, selectedItems):
        """ moduleSelected(id: int, selectedItems: [QGraphicsItem]) -> None
        When the user click on a module, display its parameter changes
        in the Inspector
        
        """
        if len(selectedItems)!=1 or id==-1:
            self.moduleUnselected()
            return
        
        # Interprete the diff result and setup item models
        (p1, p2, v1Andv2, v1Only, v2Only, paramChanged) = self.diff

        # Set the window title
        if id>self.maxId1:
            self.inspector.setWindowTitle('Parameter Changes - %s' %
                                          p2.modules[id-self.maxId1-1].name)
        else:
            self.inspector.setWindowTitle('Parameter Changes - %s' %
                                          p1.modules[id].name)
            
        # Clear the old inspector
        functions = self.inspector.functionsTab.model()
        annotations = self.inspector.annotationsTab.model()
        functions.clearList()
        annotations.clearList()

        # Find the parameter changed module
        matching = None
        for ((m1id, m2id), paramMatching) in paramChanged:
            if m1id==id:
                matching = paramMatching
                break

        # If the module has no parameter changed, just display nothing
        if not matching:          
            return
        
        # Else just layout the diff on a table
        functions.insertRows(0,len(matching))
        currentRow = 0
        for (f1, f2) in matching:
            if f1[0]!=None:
                functions.setData(
                    functions.index(currentRow, 0),
                    QtCore.QVariant('%s(%s)' % (f1[0],
                                                ','.join(v[1] for v in f1[1]))))
            if f2[0]!=None:
                functions.setData(
                    functions.index(currentRow, 1),
                    QtCore.QVariant('%s(%s)' % (f2[0],
                                                ','.join(v[1] for v in f2[1]))))
            if f1==f2:                
                functions.disableRow(currentRow)
            currentRow += 1

        self.inspector.functionsTab.resizeRowsToContents()
        self.inspector.annotationsTab.resizeRowsToContents()

    def moduleUnselected(self):
        """ moduleUnselected() -> None
        When a user selects nothing, make sure to display nothing as well
        
        """
        self.inspector.annotationsTab.model().clearList()
        self.inspector.functionsTab.model().clearList()
        self.inspector.setWindowTitle('Parameter Changes - None')

    def toggleShowInspector(self):
        """ toggleShowInspector() -> None
        Show/Hide the inspector when toggle this button
        
        """
        if self.inspector.firstTime:
            self.inspector.move(self.pos().x()+self.frameSize().width(),
                                self.pos().y())
            self.inspector.firstTime = False
        self.inspector.setVisible(self.showInspectorAction.isChecked())
            
    def toggleShowLegend(self):
        """ toggleShowLegend() -> None
        Show/Hide the legend window when toggle this button
        
        """
        if self.legendWindow.firstTime:
            self.legendWindow.move(self.pos().x()+self.frameSize().width()-
                                   self.legendWindow.frameSize().width(),
                                   self.pos().y())
        self.legendWindow.setVisible(self.showLegendsAction.isChecked())
        if self.legendWindow.firstTime:
            self.legendWindow.firstTime = False
            self.legendWindow.setFixedSize(self.legendWindow.size())            
                
    def createDiffPipeline(self):
        """ createDiffPipeline() -> None        
        Actually walk through the self.diff result and add all modules
        into the pipeline view
        
        """

        # Interprete the diff result
        (p1, p2, v1Andv2, v1Only, v2Only, paramChanged) = self.diff

        scene = self.pipelineView.scene()
        scene.clearItems()

        # Find the max version id from v1 and start the adding process
        self.maxId1 = 0
        for m1id in p1.modules.keys():
            if m1id>self.maxId1:
                self.maxId1 = m1id
        shiftId = self.maxId1 + 1

        # First add all shared modules, just use v1 module id
        for (m1id, m2id) in v1Andv2:
            scene.addModule(p1.modules[m1id],            
                            CurrentTheme.VISUAL_DIFF_SHARED_BRUSH)
            
        # Then add parameter changed version
        for ((m1id, m2id), matching) in paramChanged:
            scene.addModule(p1.modules[m1id],
                            CurrentTheme.VISUAL_DIFF_PARAMETER_CHANGED_BRUSH)

        # Now add the ones only applicable for v1, still using v1 ids
        for m1id in v1Only:
            scene.addModule(p1.modules[m1id],
                            CurrentTheme.VISUAL_DIFF_FROM_VERSION_BRUSH)

        # Now add the ones for v2 only but must shift the ids away from v1
        for m2id in v2Only:
            p2.modules[m2id].id = m2id + shiftId
            scene.addModule(p2.modules[m2id],
                            CurrentTheme.VISUAL_DIFF_TO_VERSION_BRUSH)

        # Create a mapping between share modules between v1 and v2
        v1Tov2 = {}
        v2Tov1 = {}
        for (m1id, m2id) in v1Andv2:
            v1Tov2[m1id] = m2id
            v2Tov1[m2id] = m1id
        for ((m1id, m2id), matching) in paramChanged:
            v1Tov2[m1id] = m2id
            v2Tov1[m2id] = m1id

        # Next we're going to add connections, only connections of
        # v2Only need to shift their ids
        if p1.connections.keys():
            connectionShift = max(p1.connections.keys())+1
        else:
            connectionShift = 0
        allConnections = copy.copy(p1.connections)
        sharedConnections = []
        v2OnlyConnections = []        
        for (cid2, connection2) in copy.copy(p2.connections.items()):
            if connection2.sourceId in v2Only:
                connection2.sourceId += shiftId
            else:
                connection2.sourceId = v2Tov1[connection2.sourceId]
                
            if connection2.destinationId in v2Only:
                connection2.destinationId += shiftId
            else:
                connection2.destinationId = v2Tov1[connection2.destinationId]

            # Is this connection also shared by p1?
            shared = False
            for (cid1, connection1) in p1.connections.items():
                if (connection1.sourceId==connection2.sourceId and
                    connection1.destinationId==connection2.destinationId and
                    connection1.source.name==connection2.source.name and
                    connection1.destination.name==connection2.destination.name):
                    sharedConnections.append(cid1)
                    shared = True
                    break
            if not shared:
                allConnections[cid2+connectionShift] = connection2
                connection2.id = cid2+connectionShift
                v2OnlyConnections.append(cid2+connectionShift)

        connectionItems = []
        for c in allConnections.values():
            connectionItems.append(scene.addConnection(c))

        # Color Code connections
        for c in connectionItems:
            if c.id in sharedConnections:
                pass
            elif c.id in v2OnlyConnections:
                pen = QtGui.QPen(CurrentTheme.CONNECTION_PEN)
                pen.setBrush(CurrentTheme.VISUAL_DIFF_TO_VERSION_BRUSH)
                c.connectionPen = pen
            else:
                pen = QtGui.QPen(CurrentTheme.CONNECTION_PEN)
                pen.setBrush(CurrentTheme.VISUAL_DIFF_FROM_VERSION_BRUSH)
                c.connectionPen = pen

        scene.updateSceneBoundingRect()
        scene.fitToView(self.pipelineView)
