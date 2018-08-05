#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
ZetCode wxPython tutorial

In this example we create a Go To class
layout with wx.BoxSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)


        hbox = wx.BoxSizer(wx.HORIZONTAL)               #Create Main Horizontal sixer

        #First column sizer
        vbox1 = wx.BoxSizer(wx.VERTICAL)                #First column sizer

        #Adding first static box
        contactsStaticBox = wx.StaticBox(panel, label="Contacts")
        contactsBoxSizer = wx.StaticBoxSizer(contactsStaticBox, wx.VERTICAL)

        vbox1.Add(contactsBoxSizer, wx.VERTICAL)

        contact1Btn = wx.Button(panel, label='Contact 1', size=(170, 50))
        contactsBoxSizer.Add(contact1Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)

        contact2Btn = wx.Button(panel, label='Contact 2', size=(170, 50))
        contactsBoxSizer.Add(contact2Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)

        contact3Btn = wx.Button(panel, label='Contact 3', size=(170, 50))
        contactsBoxSizer.Add(contact3Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)



        #Adding second static box
        miscStaticBox = wx.StaticBox(panel, label="Misc")
        miscBoxSizer = wx.StaticBoxSizer(miscStaticBox, wx.VERTICAL)

        vbox1.Add(miscBoxSizer, wx.VERTICAL)

        misc1Btn = wx.Button(panel, label='Misc 1', size=(170, 50))
        miscBoxSizer.Add(misc1Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)

        misc2Btn = wx.Button(panel, label='Misc 2', size=(170, 50))
        miscBoxSizer.Add(misc2Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)

        misc3Btn = wx.Button(panel, label='Misc 3', size=(170, 50))
        miscBoxSizer.Add(misc3Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)



        hbox.Add(vbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        hbox.Add((-1, 10))



        #Second column sizer
        vbox2 = wx.BoxSizer(wx.VERTICAL)  # Second column sizer

        #Adding first static box
        junkStaticBox = wx.StaticBox(panel, label="Junk")
        junkBoxSizer = wx.StaticBoxSizer(junkStaticBox, wx.VERTICAL)

        vbox2.Add(junkBoxSizer, wx.VERTICAL)

        junk1Btn = wx.Button(panel, label='Junk 1', size=(170, 50))
        junkBoxSizer.Add(junk1Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)

        junk2Btn = wx.Button(panel, label='Junk 2', size=(170, 50))
        junkBoxSizer.Add(junk2Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)

        junk3Btn = wx.Button(panel, label='Junk 3', size=(170, 50))
        junkBoxSizer.Add(junk3Btn, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)

        hbox.Add(vbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox.Add((-1, 10))

        panel.SetSizer(hbox)
        hbox.Fit(self)
"""
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Matching Classes')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        vbox.Add((-1, 25))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(panel, label='Case Sensitive')
        cb1.SetFont(font)
        hbox4.Add(cb1)
        cb2 = wx.CheckBox(panel, label='Nested Classes')
        cb2.SetFont(font)
        hbox4.Add(cb2, flag=wx.LEFT, border=10)
        cb3 = wx.CheckBox(panel, label='Non-Project classes')
        cb3.SetFont(font)
        hbox4.Add(cb3, flag=wx.LEFT, border=10)
        vbox.Add(hbox4, flag=wx.LEFT, border=10)

        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
"""
        #panel.SetSizer(hbox)




def main():

    app = wx.App()
    ex = Example(None, title='Control Panel')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()