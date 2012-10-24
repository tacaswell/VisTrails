from core.modules.vistrails_module import Module
from core.modules.module_registry import get_module_registry
from core.modules.basic_modules import String, Variant, List

from ipython_set import IPythonSet, QWarningDialog, QAddEnginesDialog
ipythonSet = None
profile_dir = None

from map import Map

def initialize(*args,**keywords):
    reg = get_module_registry()

    reg.add_module(Map)
    reg.add_input_port(Map, 'FunctionPort', (Module, ""))
    reg.add_input_port(Map, 'InputList', (List, ""))
    reg.add_input_port(Map, 'InputPort', (List, ""))
    reg.add_input_port(Map, 'OutputPort', (List, ""))
    reg.add_output_port(Map, 'Result', (Variant, ""))
    
#################################################################################

def start_local_controller():
    """
    Starts a local IPython controller.
    """
    global ipythonSet, profile_dir
    
    if not ipythonSet:
        ipythonSet = IPythonSet()
        profile_dir = ipythonSet.profile_dir
    else:
        warning_widget = QWarningDialog('A local controller is already running. Would you like to restart it?')
        if warning_widget.exec_():
            if warning_widget.is_ok():
                ipythonSet.restart_controller()
        

def add_local_engines():
    """
    Adds local engines in the IPython set.
    """
    global ipythonSet, profile_dir, type_engines
    
    def add_engines():
        n_engines = 0
        engines_widget = QAddEnginesDialog()
        if engines_widget.exec_():
            try:
                n_engines = int(engines_widget.get_number())
            except:
                 warning_widget = QWarningDialog("Invalid number of engines: '%s'" %engines_widget.get_number(),
                                                 button_cancel=False)
                 warning_widget.exec_()
            ipythonSet.add_engines(n_engines)
    
    if not ipythonSet:
        warning_widget = QWarningDialog('No local controller was found. Would you like to start a local controller and add local engines?')
        if warning_widget.exec_():
            if warning_widget.is_ok():
                ipythonSet = IPythonSet()
                profile_dir = ipythonSet.profile_dir
                add_engines()
    else:
        if (ipythonSet.engine_type != 'local') and (ipythonSet.engine_type != None):
            warning_widget = QWarningDialog("Existing engines are of type '%s'." %ipythonSet.engine_type,
                                            button_cancel=False)
            warning_widget.exec_()
        else:
            add_engines()
       
       
def add_ssh_engines():
    """
    Adds SSH engines in the IPython set.
    """
    pass


def restart_controller():
    """
    Restarts the controller.
    Note that restarting the controller also restarts the engines!
    """
    global ipythonSet, profile_dir
    
    if not ipythonSet:
        warning_widget = QWarningDialog('No local controller was found. Would you like to start a local controller?')
        if warning_widget.exec_():
            if warning_widget.is_ok():
                ipythonSet = IPythonSet()
                profile_dir = ipythonSet.profile_dir
    else:
        ipythonSet.restart_controller()
        ipythonSet.restart_engines()
        
        
def restart_engines():
    """
    Restarts the engines.
    """
    global ipythonSet, profile_dir
    
    if not ipythonSet:
        warning_widget = QWarningDialog('No local controller was found. Would you like to start a local controller and add local engines?')
        if warning_widget.exec_():
            if warning_widget.is_ok():
                ipythonSet = IPythonSet()
                profile_dir = ipythonSet.profile_dir
                add_local_engines()
    else:
        ipythonSet.restart_engines()
        
    
# TODO: how to stop controller, before VT closes, if user does not close it?
def stop_controller():
    """
    Stops the controller.
    Note that stopping the controller also stops the engines and clear the set!
    """
    global ipythonSet, profile_dir
    
    if not ipythonSet:
        warning_widget = QWarningDialog('No local controller was found.',
                                        button_cancel=False)
        warning_widget.exec_()
    else:
        ipythonSet.stop_engines()
        ipythonSet.stop_controller()
        ipythonSet = None
        profile_dir = None
        

def menu_items():
    """menu_items() -> tuple of (str,function)
    It returns a list of pairs containing text for the menu and a
    callback function that will be executed when that menu item is selected.
    
    """
    lst = []
    lst.append(("Start Local Controller", start_local_controller))
    lst.append(("Add Local Engines", add_local_engines))
    lst.append(("Add SSH Engines", add_ssh_engines))
    lst.append(("Restart Controller", restart_controller))
    lst.append(("Restart Engines", restart_engines))
    lst.append(("Stop Controller", stop_controller))
    return tuple(lst)