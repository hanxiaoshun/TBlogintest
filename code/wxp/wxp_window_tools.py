import wx
tipi = 'D:/PycharmProjects/taobaolive/code/wxp/Tipi2.ico'

class MyToolBar(wx.Frame):
    def __init__( self, parent, ID, title ):  
        wx.Frame.__init__( self, parent, ID, title, wx.DefaultPosition, wx.Size( 350, 250 ) )  

        # 垂直
        vbox = wx.BoxSizer(wx.VERTICAL)
        toolbar = wx.ToolBar(self,-1,style=wx.TB_HORIZONTAL|wx.NO_BORDER )
        toolbar.AddSimpleTool(1,wx.Image('D:/PycharmProjects/taobaolive/code/wxp/555.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),'new.','')
        toolbar.AddSimpleTool(2,wx.Image('D:/PycharmProjects/taobaolive/code/wxp/555.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),'open','')
        toolbar.AddSimpleTool(3,wx.Image('D:/PycharmProjects/taobaolive/code/wxp/555.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),'save','')
        toolbar.AddSeparator()
        toolbar.AddSimpleTool(4,wx.Image('D:/PycharmProjects/taobaolive/code/wxp/555.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),'exit','')
        # 用来显示工具栏
        toolbar.Realize()
        vbox.Add(toolbar,0,border=5)
        self.SetSizer(vbox)
        self.statusbar = self.CreateStatusBar()
        self.Centre()
        
        wx.EVT_TOOL(self,1,self.OnNew)
        wx.EVT_TOOL(self,2,self.OnOpen)
        wx.EVT_TOOL(self,3,self.OnSave)
        wx.EVT_TOOL(self,4,self.OnExit)
        
    def OnNew(self,event):
        self.statusbar.SetStatusText('New Command')
    def OnOpen(self,event):
        self.statusbar.SetStatusText('Open Command')
            
    def OnSave(self,event):
        self.statusbar.SetStatusText('Save Command')
    def OnExit(self,event):
        self.Close()
        
        
class MyApp(wx.App):
    def OnInit(self):
        # return wx.App.OnInit(self, *args, **kwargs)
        frame = MyToolBar(None,-1,'toobar.py')
        frame.Show(True)
        return True
    
app = MyApp(0)
app.MainLoop()