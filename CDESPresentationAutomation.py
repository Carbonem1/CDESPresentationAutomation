#!/usr/bin/env python
import wx
import re
from name_to_group import *

class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(700, 200))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.input_txt = wx.TextCtrl(self.panel, -1, size=(300,200), style= wx.TE_MULTILINE)
        self.input_txt.SetValue('Input')
        self.output_txt = wx.TextCtrl(self.panel, -1, size=(300,200), style= wx.TE_MULTILINE)
        self.output_txt.SetValue('Output')
        self.btn = wx.Button(self.panel, -1, "Convert")
        self.Bind(wx.EVT_BUTTON, self.Convert, self.btn)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.input_txt)
        sizer.Add(self.output_txt)
        sizer.Add(self.btn)

        self.panel.SetSizer(sizer)
        self.Show()

    def findGroup(self, person):
        #if (person == "Harding, Robert" or person == "Jain, Shweta" or person == "Percy, John" or person == "Savilonis, Daniel" or person == "Schulz, Edward" or person == "shubel, paul" or person == "Silvestri Jr, Victor" or person == "Soltis, Edward"  or person == "troung, thuan" or person == "Carbone, Michael"):
        #    return "CDES"
        #if (person == "" or person == "" or person == "" or person == ""):
        #    return ""
        #if (person == "" or person == "" or person == "" or person == ""):
        #    return ""
        #if (person == "" or person == "" or person == "" or person == ""):
        #    return ""
        try:
            return name_to_group[person]
        except KeyError:
            return "Can't find group"


    def Convert(self, event):
        total_count = 0
        cdes_count = 0
        ghe_count = 0
        game_count = 0
        isd_count = 0
        sqa_count = 0
        midrange_count = 0
        dd_systems_count = 0
        other_count = 0

        input_text = self.input_txt.GetValue()
        input_text = input_text.split('\n')

        for line in input_text:
            if (line == ""):
                continue
            count = re.findall('(\s+\d+)', line)
            total_count += int(count[0])

            print line
            name = re.findall('(\w+,*\s\w+)', line)
            print name[0]
            count = re.findall('(\s+\d+)', line)
            print count[0]

            group = self.findGroup(name[0])
            print group
            if (group == "CDES"):
                cdes_count += int(count[0])
            elif (group == "GHE"):
                ghe_count += int(count[0])
            elif (group == "GAME"):
                game_count += int(count[0])
            elif (group == "ISD"):
                isd_count += int(count[0])
            elif (group == "SQA"):
                sqa_count += int(count[0])
            elif (group == "MIDRANGE"):
                midrange_count += int(count[0])
            elif (group == "DD_SYSTEMS"):
                dd_systems_count += int(count[0])
            else:
                other_count += int(count[0])

            #print float(count[0])/total_count

        print "TOTAL: " + str(total_count)
        print "CDES: " + str(float(cdes_count)/total_count)
        print "GHE: " + str(float(ghe_count)/total_count)
        print "GAME: " + str(float(game_count)/total_count)
        print "ISD: " + str(float(isd_count)/total_count)
        print "SQA: " + str(float(sqa_count)/total_count)
        print "MIDRANGE: " + str(float(midrange_count)/total_count)
        print "DD_SYSTEMS: " + str(float(dd_systems_count)/total_count)
        print "OTHER: " + str(float(other_count)/total_count)

        self.output_txt.SetValue("CDES: " + str(round((float(cdes_count)/total_count)* 100, 2)) + "%\n" +
                                    "GHE: " + str(round((float(ghe_count)/total_count)* 100, 2)) + "%\n" +
                                    "GAME: " + str(round((float(game_count)/total_count)* 100, 2)) + "%\n" +
                                    "ISD: " + str(round((float(isd_count)/total_count)* 100, 2)) + "%\n" +
                                    "SQA: " + str(round((float(sqa_count)/total_count)* 100, 2)) + "%\n" +
                                    "MIDRANGE: " + str(round((float(midrange_count)/total_count)* 100, 2)) + "%\n" +
                                    "DD_SYSTEMS: " + str(round((float(dd_systems_count)/total_count)* 100, 2)) + "%\n" +
                                    "OTHER: " + str(round((float(other_count)/total_count)* 100, 2)) + "%\n")

        #self.output_txt.SetValue(input_text)

    def OnCloseWindow(self, e):
        self.Destroy()

app = wx.App()
frame = Frame(None, 'CDES Presentation Automation')
app.MainLoop()
