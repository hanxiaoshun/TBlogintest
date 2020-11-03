import wx
from pip._internal.utils.outdated import SelfCheckState

class MyFrame(wx.Frame):
    def __init__(self, parent, wx_id, title):
        wx.Frame.__init__(self, parent, wx_id, title)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # 只能在windows 上使用
        panel1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        panel2 = wx.Panel(self, -1, style=wx.RAISED_BORDER)
        panel3 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        panel4 = wx.Panel(self, -1, style=wx.DOUBLE_BORDER)
        panel5 = wx.Panel(self, -1, style=wx.STATIC_BORDER)
        panel6 = wx.Panel(self, -1, style=wx.NO_BORDER)

        hbox1.Add(panel1, 1, wx.EXPAND | wx.ALL, 3)
        hbox1.Add(panel2, 1, wx.EXPAND | wx.ALL, 3)
        hbox1.Add(panel3, 1, wx.EXPAND | wx.ALL, 3)
        
        hbox2.Add(panel4, 1, wx.EXPAND | wx.ALL, 3)
        hbox2.Add(panel5, 1, wx.EXPAND | wx.ALL, 3)
        hbox2.Add(panel6, 1, wx.EXPAND | wx.ALL, 3)
        
        vbox.Add(hbox1, 1, wx.EXPAND)
        vbox.Add(hbox2, 1, wx.EXPAND)
        self.SetSizer(vbox)
        self.Centre()
        
        
class MyApp(wx.App):
    
    def OnInit(self):
        # return wx.App.OnInit(self, *args, **kwargs)
        frame = MyFrame(None, -1, 'border.py')
        frame.Show(True)
        return True

app= MyApp(0)
app.MainLoop()
    