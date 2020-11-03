import wx
def main():
    app = wx.App()
    frame = wx.Frame(None,-1,'爱你宝贝',wx.DefaultPosition,wx.Size(350,300))
    frame.SetIcon(wx.Icon('D:/PycharmProjects/taobaolive/code/wxp/Tipi2.ico',wx.BITMAP_TYPE_ICO))
    frame.Center()
    frame.Show()
    app.MainLoop()
if __name__ == "__main__":
    main()
