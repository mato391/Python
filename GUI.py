import wx
from Log import *
class Window(wx.Frame):

   def __init__(self, parent, title, size):
        super(Window, self).__init__(parent, title=title, size=size)
        self.InitUI()

   def InitUI(self):

        self.menubar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.fitem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.menubar.Append(self.fileMenu, '&File')
        self.SetMenuBar(self.menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)

        self.Centre()
        self.Show(True)

   def OnQuit(self, e):
        try:
            LOGGER.logging("Input signal exit app ", "INFO")
            self.Close()
        except(e):
            LOGGER.logging("CALLTRACE " + str(e), "ERROR")