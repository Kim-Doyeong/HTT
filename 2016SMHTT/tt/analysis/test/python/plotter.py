#!/usr/bin/env python
import ROOT
import re
from array import array

def add_lumi():
    lowX=0.58
    lowY=0.835
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.05)
    lumi.SetTextFont (   42 )
    lumi.AddText("2016, 35.9 fb^{-1} (13 TeV)")
    return lumi

def add_CMS():
    lowX=0.21
    lowY=0.70
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.08)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi

def add_Preliminary():
    lowX=0.21
    lowY=0.63
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(52)
    lumi.SetTextSize(0.06)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("Preliminary")
    return lumi

def make_legend():
        output = ROOT.TLegend(0.60, 0.55, 0.95, 0.83, "", "brNDC")
        #output = ROOT.TLegend(0.2, 0.1, 0.47, 0.65, "", "brNDC")
        output.SetLineWidth(0)
        output.SetLineStyle(0)
        output.SetFillStyle(0)
        output.SetBorderSize(0)
        output.SetMargin(0.3)
        output.SetTextFont(62)
        return output

ROOT.gStyle.SetFrameLineWidth(1)
ROOT.gStyle.SetLineWidth(1)
ROOT.gStyle.SetOptStat(0)

c=ROOT.TCanvas("canvas","",0,0,600,1000)
c.cd()

file=ROOT.TFile("final_nominal.root","r")

adapt=ROOT.gROOT.GetColor(12)
new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)
categories=["ttOS_0jetR","ttOS_boostedR","ttOS_vbfR"]
categories2=["0jet","1jet","2jets"]
majors=["ZTT","QCD"]
minors=["ZL","ZJ","TTT","TTJ","W","VVT","VVJ"]
signals=["ggH125","VBF125"]#,"WH125","ZH125","SMH"]
mypalette=["#ffbcfe","#f9cd66","#9feff2","#544e56"]
ncat = 3

for i in range (0,ncat):
    print categories2[i]
    histlist=[] # all bkg histograms go into here
    histlist_sig=[] # ggH, VBF and SMH(ggH+VBF+VH) go into here
    ''' Save histograms in the list '''
    # major bkg
    for major in majors:
        histlist.append(file.Get(categories[i]).Get(major))
    # combine minor bkg
    h_minor = file.Get(categories[i]).Get(minors[0])
    for minor in minors:
        if(minor!=minors[0]): 
            h_minor.Add(file.Get(categories[i]).Get(minor),1)
    histlist.append(h_minor)
    # signals
    h_sig = file.Get(categories[i]).Get("SMH").Clone()
    h_vbf = file.Get(categories[i]).Get("VBF125").Clone()
    h_ggH = file.Get(categories[i]).Get("ggH125").Clone()
    for signal in signals:
        histlist_sig.append(file.Get(categories[i]).Get(signal))
    # data
    Data=file.Get(categories[i]).Get("data_obs")
    Data.GetXaxis().SetTitle("")
    Data.GetXaxis().SetTitleSize(0)
    Data.GetXaxis().SetNdivisions(505)
    Data.GetYaxis().SetLabelFont(42)
    Data.GetYaxis().SetLabelOffset(0.01)
    Data.GetYaxis().SetLabelSize(0.03)#0.06
    Data.GetYaxis().SetTitleSize(0.075)
    Data.GetYaxis().SetTitleOffset(1.04)
    Data.SetTitle("")
    Data.GetYaxis().SetTitle("Events/bin")    
    Data.SetMarkerStyle(20)
    Data.SetLineColor(1)
    Data.SetMarkerSize(1)

    ''' Making errorBand and stack. + Setting histogram styles '''
    errorBand=file.Get(categories[i]).Get(majors[0]).Clone()    
    stack=ROOT.THStack("stack","stack")
    for x in range(0,len(histlist)):
        histlist[x].SetFillColor(ROOT.TColor.GetColor(mypalette[x]))
        histlist[x].SetLineWidth(2)
        histlist[x].SetLineColor(1)
        if x is not 0:
            errorBand.Add(histlist[x])
        stack.Add(histlist[x])

    errorBand.SetMarkerSize(0)
    errorBand.SetFillColor(new_idx)
    errorBand.SetFillStyle(3001)
    errorBand.SetLineWidth(0)

    ''' Setting signal lines styles '''
    for hist in histlist_sig:
        hist.Scale(20)
        hist.SetLineStyle(7)
        hist.SetMarkerStyle(0)
        hist.SetLineWidth(4)
    histlist_sig[0].SetLineColor(ROOT.kBlue)
    histlist_sig[1].SetLineColor(ROOT.kRed)
    #histlist_sig[2].SetLineColor(ROOT.kMagenta+3)
    #histlist_sig[3].SetLineColor(ROOT.kBlack)
    #histlist_sig[4].SetLineColor(ROOT.kRed)
    
    # Setting pad1
    pad1 = ROOT.TPad("pad1","pad1",0,0.50,1,1)
    pad1.Draw()
    pad1.cd()
    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetBorderSize(10)
    pad1.SetTickx(1)
    pad1.SetTicky(1)
    pad1.SetLeftMargin(0.18)
    pad1.SetRightMargin(0.05)
    pad1.SetTopMargin(0.122)
    pad1.SetBottomMargin(0.0)
    pad1.SetFrameFillStyle(0)
    pad1.SetFrameLineStyle(0)
    pad1.SetFrameLineWidth(1)
    pad1.SetFrameBorderMode(0)
    pad1.SetFrameBorderSize(10)
    
    Data.GetXaxis().SetLabelSize(0)
    Data.SetMaximum(max(Data.GetMaximum()*1.20,stack.GetMaximum()*1.20)) #32000
    for k in range(1,Data.GetSize()-1):
        s=histlist_sig[0].GetBinContent(k)
        data1=Data.GetBinContent(k)
        #b=VV.GetBinContent(k)+Fake.GetBinContent(k)
        #b=ZZ.GetBinContent(k)+Fake.GetBinContent(k)+WZ.GetBinContent(k)
        #if (b<0):
        #    b=0.000001
        #if (s/(0.00001+0.2*s+b)**0.5 > 0.8):
        #    Data.SetBinContent(k,-1)
        #    Data.SetBinError(k,-1)


    ''' Draw '''
    # data
    Data.SetMinimum(0)
    Data.SetMaximum(1.3*Data.GetMaximum()) #1.3
    Data.Draw("e")
    # bkg
    stack.Draw("histsame")
    # signal
    for hist in histlist_sig:
        hist.Draw("histsame")
    Data.Draw("esame")
    # errorband
    errorBand.Draw("e2same")
    # legend
    legende=make_legend()
    #legende.SetHeader("[ "+categories2[i]+" ]","C")
    legende.AddEntry(Data,"Data","elp")    
    legende.AddEntry(histlist_sig[0],"ggH Higgs(125)x20.0","l")
    legende.AddEntry(histlist_sig[1],"VBF Higgs(125)x20.0","l")
    #legende.AddEntry(histlist_sig[2],"WH Higgs(125)x20.0","l")
    #legende.AddEntry(histlist_sig[3],"ZH Higgs(125)x20.0","l")
    #legende.AddEntry(histlist_sig[5],"SM Higgs(125)x20.0","elp")
    legende.AddEntry(histlist[0],"Z#rightarrow#tau#tau","f")
    legende.AddEntry(histlist[1],"QCD","f")
    legende.AddEntry(histlist[2],"others","f")
    legende.AddEntry(errorBand,"Uncertainty","f")
    legende.Draw()
    # miscellaneous
    l1=add_lumi()
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    pad1.RedrawAxis()
    categ  = ROOT.TPaveText(0.21, 0.5+0.013, 0.43, 0.70+0.155, "NDC")
    categ.SetBorderSize(   0 )
    categ.SetFillStyle(    0 )
    categ.SetTextAlign(   12 )
    categ.SetTextSize ( 0.06 )
    categ.SetTextColor(    1 )
    categ.SetTextFont (   41 )
    categ.AddText(categories2[i])
    categ.Draw()


    ''' Making ratio [1]Data/MC'''    
    # Setting up pad
    c.cd()
    pad2 = ROOT.TPad("pad2","pad2",0,0.35,1,0.50);
    pad2.SetTopMargin(0.00);
    pad2.SetBottomMargin(0.0);
    pad2.SetLeftMargin(0.18);
    pad2.SetRightMargin(0.05);
    pad2.SetTickx(1)
    pad2.SetTicky(1)
   #pad2.SetFrameLineWidth(3)
   #pad2.SetGridx()
    pad2.SetGridy()
    pad2.Draw()
    pad2.cd()
    # Making the ratio histogram
    h1=Data.Clone()
    h1.SetMaximum(1.5)#FIXME(1.5)
    h1.SetMinimum(0.5)#FIXME(0.5)
    h1.SetMarkerStyle(21)
    h3=errorBand.Clone()
    hwoE=errorBand.Clone()
    for iii in range (1,hwoE.GetSize()-2):
        hwoE.SetBinError(iii,0)
    h3.Sumw2()
    h1.Sumw2()
    h1.SetStats(0)
    h1.Divide(hwoE)
    h3.Divide(hwoE)
    #h1.GetXaxis().SetTitle("M_{jj} [GeV]")#M_{jj} [GeV]")#"M_{#tau#tau} [GeV]")
    #   h1.GetXaxis().SetTitle("Higgs p_{t} [GeV]")#M_{jj} [GeV]")#"M_{#tau#tau} [GeV]")
           #"Higgs p_{T} [GeV]")#1:well matched, 3:sub is not from H, 4:leading is not from W")#("p_{T,vis} (GeV)")#("p_{T}(#mu_{2}) (GeV)")
   #("m_{vis} (GeV)")#(#vec{p_{T}}(#tau_{1})+#vec{p_{T}}(#tau_{2}))/(p_{T}(#tau_{1})+p_{T}(#tau_{2}))")#("m_{vis} (GeV)")#(#vec{p_{T}(#mu)}+#vec{p_{T}(#tau)})/(p_{T}(#mu)+p_{T}(#tau))")
   #if (i+1==1 or i+1==2 or i+1==7 or i+1==8):
   #	h1.GetXaxis().SetTitle("Electron p_{T} (GeV)")
   #if (i+1==4 or i+1==10):
   #     h1.GetXaxis().SetTitle("Muon p_{T} (GeV)")
   #if (i+1==6 or i+1==12 or i+1==3 or i+1==5 or i+1==9 or i+1==11):
   #     h1.GetXaxis().SetTitle("Tau p_{T} (GeV)")
    h1.GetXaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetTitle("Data / MC")
    h1.GetXaxis().SetNdivisions(505)
    h1.GetYaxis().SetNdivisions(5, True)
    
    h1.GetXaxis().SetTitleSize(0.15)
    h1.GetYaxis().SetTitleSize(0.15)#(0.15)
    h1.GetYaxis().SetTitleOffset(0.25*1.5)
   #h1.GetXaxis().SetTitleOffset(1.04)
    h1.GetXaxis().SetLabelSize(0.11)
    h1.GetYaxis().SetLabelSize(0.11)
    h1.GetXaxis().SetTitleFont(42)
    h1.GetYaxis().SetTitleFont(42)
    
    h1.Draw("e0p")
    h3.Draw("e2same")
    
    c.cd()
    pad3 = ROOT.TPad("pad3","pad3",0,0.20,1,0.35);
    pad3.SetTopMargin(0.00);
    pad3.SetBottomMargin(0.00);
    pad3.SetLeftMargin(0.18);
    pad3.SetRightMargin(0.05);
    pad3.SetTickx(1)
    pad3.SetTicky(1)
   #pad3.SetFrameLineWidth(3)
   #pad3.SetGridx()
    pad3.SetGridy()
    pad3.Draw()
    pad3.cd()

    h_sig.SetLineStyle(0)
    h_sig.SetMarkerStyle(21)
    h_sig.Sumw2()
    #h_sig.SetStates(0)
    h_sig.Divide(hwoE)
    #h_sig.GetXaxis().SetTitle("tau_{1} p_{T} [GeV]")
    h_sig.SetMaximum(h_sig.GetMaximum()*1.4)
    h_sig.SetMinimum(h_sig.GetMinimum()*0.6)
    
    h_sig.GetXaxis().SetLabelSize(0.08)
    h_sig.GetYaxis().SetLabelSize(0.08)
    h_sig.GetYaxis().SetTitle("Sig / Bkg")
    h_sig.GetXaxis().SetNdivisions(505)
    h_sig.GetYaxis().SetNdivisions(5, True)
    
    h_sig.GetXaxis().SetTitleSize(0.15)
    h_sig.GetYaxis().SetTitleSize(0.15)#(0.15)
    h_sig.GetYaxis().SetTitleOffset(0.25*1.5)
   #h1.GetXaxis().SetTitleOffset(1.04)
    h_sig.GetXaxis().SetLabelSize(0.11)
    h_sig.GetYaxis().SetLabelSize(0.11)
    h_sig.GetXaxis().SetTitleFont(42)
    h_sig.GetYaxis().SetTitleFont(42)
    
    h_sig.Draw("e0p")
    #h3.Draw("e2same")


    c.cd()
    pad4 = ROOT.TPad("pad4","pad4",0,0,1,0.20);
    pad4.SetTopMargin(0.00);
    pad4.SetBottomMargin(0.3);
    pad4.SetLeftMargin(0.18);
    pad4.SetRightMargin(0.05);
    pad4.SetTickx(1)
    pad4.SetTicky(1)
   #pad3.SetFrameLineWidth(3)
   #pad3.SetGridx()
    pad4.SetGridy()
    pad4.Draw()
    pad4.cd()

    h_vbf.Divide(h_ggH)
    h_vbf.SetLineStyle(0)
    #if h_ggH.GetMinimum() is not 0:
    #    if h_ggH.GetMaximum() is not 0:
    #        h_vbf.SetMaximum(1.4*max(h_vbf.GetMinimum()/h_ggH.GetMinimum(),(h_vbf.GetMinimum()/h_ggH.GetMaximum())))
    #else:
    h_vbf.SetMaximum(h_vbf.GetMaximum()*1.4)
    h_vbf.SetMinimum(h_vbf.GetMinimum()*0.6)
    h_vbf.SetMarkerStyle(21)
    #h_sig.SetStates(0)

    h_vbf.GetXaxis().SetTitle("H p_{T} - pt_sv [GeV]")
    
    h_vbf.GetXaxis().SetLabelSize(0.08)
    h_vbf.GetYaxis().SetLabelSize(0.08)
    h_vbf.GetYaxis().SetTitle("VBF / ggH")
    h_vbf.GetXaxis().SetNdivisions(505)
    h_vbf.GetYaxis().SetNdivisions(5, True)
    
    h_vbf.GetXaxis().SetTitleSize(0.15)
    h_vbf.GetYaxis().SetTitleSize(0.12)#(0.15)
    h_vbf.GetYaxis().SetTitleOffset(0.25*1.5)
   #h1.GetXaxis().SetTitleOffset(1.04)
    h_vbf.GetXaxis().SetLabelSize(0.11)
    h_vbf.GetYaxis().SetLabelSize(0.11)
    h_vbf.GetXaxis().SetTitleFont(42)
    h_vbf.GetYaxis().SetTitleFont(42)
    
    h_vbf.Draw("e0p")
    #h_ggH.Draw("e2same")



   #print "integral : ", h3.Integral(9,10)

    c.cd()
    pad1.Draw()
    
    ROOT.gPad.RedrawAxis()
    
    c.Modified()
    c.SaveAs("plots/htt_"+categories2[i]+".pdf")
   #c.SaveAs("htt_"+categories[i]+".png")


