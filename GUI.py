import wx
from Log import *
class Window(wx.Frame):

   def __init__(self, parent, title, size):
        '''Constructor creating Frame
        :param parent: Parent item for Frame
        :param title: title of window
        :param size: window's size
        :return: None
        '''
        super(Window, self).__init__(parent, title=title, size=size)
        self.InitUI()

   def InitUI(self):
        '''
        Creating GUI ,menus, buttons and events
        :return: None
        '''
        self.menubar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.fitem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.menubar.Append(self.fileMenu, '&File')
        self.SetMenuBar(self.menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)

        self.Centre()
        self.Show(True)

   def OnQuit(self, e):
        '''
        OnQuit Operation called by menu item
        :param e: Exception
        :return: None
        '''
        try:
            LOGGER.logging("Input signal exit app ", "INFO")
            self.Close()
        except(e):
            LOGGER.logging("CALLTRACE " + str(e), "ERROR")