#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):

    def __init__(self, parent, wx_id, title):
        wx.Frame.__init__(self, parent, wx_id, title, size=(600, 300))
        # 创建面版
        panel = wx.Panel(self)
        # 在Panel上创建button
        button = wx.Button(panel, label='关闭', pos=(150, 60), size=(100, 50))
        # 给button 绑定事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)

    def OnCloseMe(self, event):
        dialog = wx.MessageDialog(None, '消息对话框', '标题信息', wx.YES_NO | wx.ICON_QUESTION)
        if dialog.ShowModal() == wx.ID_YES:
            self.Close()
        dialog.Destroy()

        
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(parent=None, wx_id=-1, title='测试对话框')
    frame.Show()
    app.MainLoop()