import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, wx_id, title):
        wx.Frame.__init__(self, parent, wx_id, title)
        penal = wx.Panel(self, -1)
        wx.Button(penal, -1, 'Button 1', (0, 0))
        wx.Button(penal, -1, 'Button 2', (80, 0))
        wx.Button(penal, -1, 'Button 3', (160, 0))
        
        
class MyApp(wx.App):
    def OnInit(self):
        # return wx.App.OnInit(self, *args, **kwargs)
        frame = MyFrame(None, -1, 'button_test')
        frame.Show(True)
        frame.Center()
        
        return True
        
        
app = MyApp(0)
app.MainLoop()