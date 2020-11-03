import wx

class MyMenu(wx.Frame):
    def __init__(self, parent,ID,title):
        wx.Frame.__init__(self,parent,-1,title,wx.DefaultPosition,wx.Size(200,200))
        menubar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        edit.Append(201,'check item1','',kind=wx.ITEM_CHECK)
        edit.Append(202,'check item2','',kind=wx.ITEM_CHECK)
        submenu = wx.Menu()
        submenu.Append(301,'radio item1',kind = wx.ITEM_RADIO)
        submenu.Append(302,'radio item2',kind = wx.ITEM_RADIO)
        edit.AppendMenu(203,'submenu',submenu)
        help = wx.Menu()
        file.Append(101, "&打开",  "就是打开一个文件吗")
        file.AppendSeparator()
        file.Append(102, "&保存", "保存一个文件")
        quit = wx.MenuItem(file,105,"&Quit",'退出')
        quit.SetBitmap(wx.Image('D:/PycharmProjects/taobaolive/code/wxp/Tipi2.ico',wx.BITMAP_TYPE_ICO).ConvertToBitmap())
        file.Append(quit)
        menubar.Append(file,"&file")
        menubar.Append(edit, "&edit")
        menubar.Append(help,"&help")
        self.SetMenuBar(menubar)
        
        wx.EVT_MENU(self, 105, self.OnQuit)
        
    def OnQuit(self,event):
        print("quit----")
        self.Close()
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyMenu(None,-1,'menu.py')
        frame.Show(True)
        return True
    
app=MyApp()
app.MainLoop()
