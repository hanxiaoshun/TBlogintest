import wx 
import time 
from threading import Thread
from wx.lib.pubsub import pub


# 发布/订阅者模式
# 线程实例化时立即启动
class TestThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.start()
    
    def run(self):
        # 线程执行的代码
        for i in range(101):
            time.sleep(0.03)
            wx.CallAfter(pub.sendMessage, "update", msg=i)
            time.sleep(0.5)


class MyForm(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, 
                          title='aaa.xy.com',
                          pos=wx.DefaultPosition,
                          size=wx.Size(-1, -1), 
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        gSizer2 = wx.GridSizer(0, 3, 0, 0)
        
        self.m_button2 = wx.Button(self, 
                                   wx.ID_ANY,
                                   label="执行教程", 
                                   pos=wx.DefaultPosition,
                                   size=wx.DefaultSize)
        gSizer2.Add(self.m_button2,
                    0,
                    wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 
                    5)
        self.m_staticText2 = wx.StaticText(self, 
                                           wx.ID_ANY,
                                           "MyLabel",
                                           wx.DefaultPosition,
                                           wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)
        gSizer2.Add(self.m_staticText2, 
                    0,
                    wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
                    5)
        # 设定一个 Gauge 计量器，总数是100
        self.m_gauge1 = wx.Gauge(self, 
                                 wx.ID_ANY, 
                                 100, 
                                 wx.DefaultPosition,
                                 wx.DefaultSize,
                                 wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        gSizer2.Add(self.m_gauge1,
                    0,
                    wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTRE_VERTICAL,
                    5)
        self.SetSizer(gSizer2)
        self.Layout()
        gSizer2.Fit(self)
        
        self.Centre(wx.BOTH)
        self.m_button2.Bind(wx.EVT_BUTTON, self.onButton)
        pub.subscribe(self.updateDisplay, 'update')
        
    def updateDisplay(self, msg):
        t = msg
        if isinstance(t, int):
            self.m_staticText2.SetLabel('%s%%' % t)
            self.m_gauge1.SetValue(t)
        else:
            self.m_staticText2.SetLabel('%s' % t)
            self.m_button2.Enabled()
            
    def onButton(self, event):
        TestThread()
        self.m_staticText2.SetLabel('线程开始')
        event.GetEventObject().Disable()
        
        
if __name__ == "__main__":
    app = wx.App()
    MyForm(None).Show()
    app.MainLoop()