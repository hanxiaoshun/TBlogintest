"""
Hello World, but with more meat.
"""

import wx

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)
        

        
        # put some text with a larger bold font on it
        # st = wx.StaticText(pnl, label="淘宝直播中控台数据处理系统")
        # font = st.GetFont()
        # font.PointSize += 10
        # font = font.Bold()
        # st.SetFont(font)
        


        # and create a sizer to manage the layout of child widgets
        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        # pnl.SetSizer(sizer)

        # create a menu bar
        # self.makeMenuBar()

        # and a status bar
        # self.CreateStatusBar()
        # self.SetStatusText("Welcome to wxPython!")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)
        
class Page1(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        v_box_sizer = wx.BoxSizer(wx.VERTICAL)
        v_box_sizer.Add(wx.StaticText(self,label='小封面'), proportion=0, flag=wx.EXPAND)
        v_box_sizer.Add(wx.StaticText(self,label='大封面'), proportion=1, flag=wx.EXPAND)
        v_box_sizer.Add(wx.StaticText(self,label='视频地址'), proportion=1, flag=wx.EXPAND)
        v_box_sizer.Add(wx.StaticText(self,label='直播标题'), proportion=1, flag=wx.EXPAND)
        self.SetSizer(v_box_sizer)

class Page2(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self,label='Page Two2')

class Page3(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self,label='Page Three3')

class Page4(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self,label='Page Three3')


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    # app = wx.App()
    # frame = HelloFrame(None, title='淘宝直播中控台数据处理系统')
    # app = wx.App(False)
    # frame = wx.Frame(None, title="淘宝直播中控台数据处理系统")
    # # 添加Tab效果
    nb = wx.Notebook(frame)
    nb.AddPage(Page1(nb), "发布预告")
    nb.AddPage(Page2(nb), "辅助工具")
    nb.AddPage(Page3(nb), "评论")
    nb.AddPage(Page4(nb), "主播间用户采集")
    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(nb, True)
    # panel = wx.Panel(frame)
    btn = wx.Button(panel,100,"click Me") 
    vbox.Add(btn,0, wx.ALIGN_CENTER) 
    #   self.btn.Bind(wx.EVT_BUTTON,self.OnClicked) 
         
    #   self.tbtn = wx.ToggleButton(panel , -1, "click to on") 
    #   vbox.Add(self.tbtn,0,wx.EXPAND|wx.ALIGN_CENTER) 
    #   self.tbtn.Bind(wx.EVT_TOGGLEBUTTON,self.OnToggle) 
         
    #   hbox = wx.BoxSizer(wx.HORIZONTAL) 
         
    #   bmp = wx.Bitmap("NEW.BMP", wx.BITMAP_TYPE_BMP) 
    #   self.bmpbtn = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp,
    #      size = (bmp.GetWidth()+10, bmp.GetHeight()+10)) 
			
    #   hbox.Add(self.bmpbtn,0,wx.ALIGN_CENTER) 
    #   self.bmpbtn.Bind(wx.EVT_BUTTON,self.OnClicked) 
    #   self.bmpbtn.SetLabel("NEW") //原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：https://www.yiibai.com/wxpython/wxpython_buttons.html#
    # panel = wx.Panel(frame) 
    # vbox = wx.BoxSizer(wx.VERTICAL) 
    # nb.btn = wx.Button(panel,100,"click Me") 
    # vbox.Add(nb.btn,0,wx.ALIGN_CENTER) 
    
    frame.Show()
    app.MainLoop()