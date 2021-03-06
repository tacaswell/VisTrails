###############################################################################
##
## Copyright (C) 2006-2011, University of Utah. 
## All rights reserved.
## Contact: contact@vistrails.org
##
## This file is part of VisTrails.
##
## "Redistribution and use in source and binary forms, with or without 
## modification, are permitted provided that the following conditions are met:
##
##  - Redistributions of source code must retain the above copyright notice, 
##    this list of conditions and the following disclaimer.
##  - Redistributions in binary form must reproduce the above copyright 
##    notice, this list of conditions and the following disclaimer in the 
##    documentation and/or other materials provided with the distribution.
##  - Neither the name of the University of Utah nor the names of its 
##    contributors may be used to endorse or promote products derived from 
##    this software without specific prior written permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
## AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
## THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
## PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
## CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
## EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
## PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
## OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
## WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
## OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
## ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
###############################################################################

import matplotlib
import pylab
import urllib

from matplotlib.backend_bases import FigureCanvasBase

from vistrails.core.modules.basic_modules import CodeRunnerMixin
from vistrails.core.modules.vistrails_module import Module, NotCacheable, ModuleError

################################################################################

class MplProperties(Module):
    def compute(self, artist):
        pass

    class Artist(object):
        def update_sub_props(self, objs):
            # must implement in subclass
            pass

#base class for 2D plots
class MplPlot(NotCacheable, Module):
    def __init__(self):
        Module.__init__(self)
        self.figInstance = None

    def set_figure(self, fig):
        if self.figInstance is None:
            self.figInstance = fig
        else:
            raise ModuleError(self,
                              "matplotlib plots can only be in one figure")

    def compute(self):
        matplotlib.pyplot.figure(self.figInstance.number)

class MplSource(CodeRunnerMixin, MplPlot):
    """
    MplSource is a module similar to PythonSource. The user can enter
    Matplotlib code into this module. This will then get connected to
    MplFigure to draw the figure. Please note that, codes entered in
    this module should limit to subplot() scope only. Using
    Figure-level commands, e.g. figure() or show(), the result will be
    unknown
    
    """
    _input_ports = [('source', '(basic:String)')]
    _output_ports = [('value', '(MplSource)')]

    def compute(self):
        """ compute() -> None
        """
        source = self.get_input('source')
        s = ('from pylab import *\n'
             'from numpy import *\n' +
             'figure(%d)\n' % self.figInstance.number +
             urllib.unquote(source))

        self.run_code(s, use_input=True, use_output=True)
        self.set_output('value', None)

class MplFigure(Module):
    _input_ports = [("addPlot", "(MplPlot)"),
                    ("axesProperties", "(MplAxesProperties)"),
                    ("figureProperties", "(MplFigureProperties)"),
                    ("setLegend", "(MplLegend)")]

    _output_ports = [("self", "(MplFigure)")]

    def __init__(self):
        Module.__init__(self)
        self.figInstance = None

    def update_upstream(self):
        # Create a figure
        if self.figInstance is None:
            self.figInstance = pylab.figure()
        pylab.hold(True)

        # Set it on the plots
        connectorList = self.inputPorts.get('addPlot', [])
        connectorList.extend(self.inputPorts.get('setLegend', []))
        for connector in connectorList:
            connector.obj.set_figure(self.figInstance)

        # Now we can run upstream modules
        super(MplFigure, self).update_upstream()

    def compute(self):
        plots = self.get_input_list("addPlot")

        if self.has_input("figureProperties"):
            figure_props = self.get_input("figureProperties")
            figure_props.update_props(self.figInstance)
        if self.has_input("axesProperties"):
            axes_props = self.get_input("axesProperties")
            axes_props.update_props(self.figInstance.gca())
        if self.has_input("setLegend"):
            legend = self.get_input("setLegend")
            self.figInstance.gca().legend()


        self.set_output("self", self)

class MplFigureToFile(Module):
    _input_ports = [('figure', 'MplFigure'),
                    ('format', 'basic:String', {"defaults": ["pdf"]}),
                    ('width', 'basic:Integer', {"defaults": ["800"]}),
                    ('height', 'basic:Integer', {"defaults": ["600"]})]
    _output_ports = [('imageFile', 'basic:File')]

    def compute(self):
        figure = self.get_input('figure')
        format = self.get_input('format')
        width = self.get_input('width')
        height = self.get_input('height')
        imageFile = self.interpreter.filePool.create_file(suffix=".%s" % format)

        fig = figure.figInstance
        w_inches = width / 72.0
        h_inches = height / 72.0

        previous_size = tuple(fig.get_size_inches())
        fig.set_size_inches(w_inches, h_inches)
        canvas = FigureCanvasBase(fig)
        canvas.print_figure(imageFile.name, dpi=72, format=format)
        fig.set_size_inches(previous_size[0],previous_size[1])
        canvas.draw()

        self.set_output('imageFile', imageFile)

class MplContourSet(Module):
    pass

class MplQuadContourSet(MplContourSet):
    pass
        
_modules = [(MplProperties, {'abstract': True}),
            (MplPlot, {'abstract': True}), 
            (MplSource, {'configureWidgetType': \
                             ('vistrails.packages.matplotlib.widgets',
                              'MplSourceConfigurationWidget')}),
            MplFigure,
            MplFigureToFile,
            MplContourSet,
            MplQuadContourSet]
