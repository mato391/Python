import wx
from Log import *
class Window(wx.Frame):

   def __init__(self, parent, title, size):
        super(Window, self).__init__(parent, title=title, size=size)
        self.InitUI()

   def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        self.Centre()
        self.Show(True)

   def OnQuit(self, e):
        try:
            LOGGER.logging("Input signal exit app ", "INFO")
            self.Close()
        except(e):
            LOGGER.logging("CALLTRACE " + str(e), "ERROR")