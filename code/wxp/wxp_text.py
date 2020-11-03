import wx


class MyText():
    """
    自定文本框
    """

    def __init__(self, parent, pos, size=(80, 60), readOnly=False):
        self.defaultFontSize = 10  # 默认字体大小
        self.TextCtrColor = 'white'
        self.defaultBorderColor = '#EAEAEA'
        
        self.TextCtr, self.border, self.bg = self.__CreateTextCtrl(parent,
                                                                   pos,
                                                                   size,
                                                                   self.defaultBorderColor,
                                                                   readOnly)

    def __CreateTextCtrl(self,
                         parent,
                         pos,
                         size,
                         borderColor,
                         readOnly=True,
                         borderSize=1):
        """创建文本框
        """
        # 创建边框
        self.border = wx.StaticText(parent, -1, '', size=size, pos=pos)
        # 设置边框要展现的颜色
        self.border.SetBackgroundColour(borderColor)
        self.bg = wx.StaticText(self.border, -1, '',
                                size=((size[0] - borderSize * 2),
                                      (size[1] - borderSize * 2)),
                                pos=(borderSize, borderSize))
        if readOnly:
            style = wx.TE_READONLY | wx.NO_BORDER
        else:
            style = wx.NO_BORDER
        
        self.textCtrl = wx.TextCtrl(self.bg, -1,
                                    size=((size[0] - 10), 
                                          self.defaultFontSize * 2),
                                    pos=(5, 
                                         (size[1] - 2 * self.defaultFontSize - borderSize * 2) / 2),
                                    style=style)
        font = wx.Font(self.defaultFontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, '微软雅黑')
        self.textCtrl.SetFont(font)
        
        if readOnly:
            self.bg.SetBackgroundColour('rgb(240,240,240)')
            self.TextCtrColor = 'rgb(240, 240, 240)'
        else:
            self.bg.SetBackgroundColour(self.textCtrl.GetBackgroundColour())
            self.TextCtrColor = self.textCtrl.GetBackgroundColour()
        self.bg.Bind(wx.EVT_LEFT_UP, self.__ClickEvent)
        return self.textCtrl, self.border, self.bg
    
    def __ClickEvent(self, event):
        """点击时焦点设置在文本框上
        """
        self.textCtrl.SetFocus()
        
    def SetValue(self, value):
        if not value:
            value = ''
        self.textCtrl.SetValue(value)
    
    def GetValue(self):
        return self.textCtrl.GetValue()
    
    def SetBorderColor(self, color):
        self.border.SetBackgroundColour(color)
        self.border.Refresh()
 
    def SetFontColor(self, color):
        self.textCtrl.SetForegroundColour(color)
        self.textCtrl.SetBackgroundColour(self.TextCtrlColor)
    
    def SetFont(self, font):
        self.textCtrl.SetFont(font)
    
    def SetBackgroundColour(self, color):
        self.bg.SetBackgroundColour(color)
        self.textCtrl.SetBackgroundColour(color)
        self.textCtrl.Refresh()

        
app = wx.App()
frame = wx.Frame(None,
                title='Gui test editor',
                pos=(1000, 200), size=(500, 400))
panel = wx.Panel(frame)

path_text = wx.TextCtrl(panel, size=(260, 36))
my_text = MyText(panel, pos=(10, 50),
                 size=(260, 36))
my_text1 = MyText(panel,
                  pos=(10, 100),
                  size=(260, 36), readOnly=True)

my_text.SetBorderColor('red')
frame.Show()
app.MainLoop()