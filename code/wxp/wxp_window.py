import wx

app = wx.App()
frame = wx.Frame(None, -1, '')
frame.SetToolTip(wx.ToolTip('This is a frame'))
frame.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
frame.SetPosition(wx.Point(100,200))
frame.SetSize(wx.Size(300,200))
frame.SetTitle("BAIBEI.py")
frame.Show()
app.MainLoop()