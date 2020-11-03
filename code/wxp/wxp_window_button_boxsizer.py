import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, wx_id, title):
        wx.Frame.__init__(self, parent, wx_id, title)
        panel = wx.Panel(self, -1)
        
        button1 = wx.Button(panel, -1, 'button 1')
        button2 = wx.Button(panel, -1, 'button 2')
        button3 = wx.Button(panel, -1, 'button 3')
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(button1, 1, wx.LEFT)
        vbox.Add(button2, 1, wx.RIGHT)
        vbox.Add(button3, 1)
        panel.SetSizer(vbox)
        self.Center()
        
class Myapp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'vBox_panel.py')
        frame.Show()
        return True
    
    
app = Myapp()
app.MainLoop()