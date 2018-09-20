#!/usr/bin/env python
import ROOT
import re
from array import array

obs = "#tau1 p_{T} [GeV]"
file=ROOT.TFile("final_nominal.root","r")
cate={"ttOS_0jetR":"0jet","ttOS_boostedR":"1jet","ttOS_vbfR":"2jets"}
majors=["ZTT","QCD"]
minors=["ZL","ZJ","TTT","TTJ","W","VVT","VVJ"]
signals=["SMH","ggH125","VBF125","WH125","ZH125"]
# Colors
mypalette=["#ffbcfe","#f9cd66","#9feff2","#544e56"]
adapt=ROOT.gROOT.GetColor(12)
new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)


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

def add_cate(category):
    categ  = ROOT.TPaveText(0.21, 0.5+0.013, 0.43, 0.70+0.155, "NDC")
    categ.SetBorderSize(   0 )
    categ.SetFillStyle(    0 )
    categ.SetTextAlign(   12 )
    categ.SetTextSize ( 0.06 )
    categ.SetTextColor(    1 )
    categ.SetTextFont (   41 )
    categ.AddText(category)
    return categ

def make_canvas(hight,c_name):
    c=ROOT.TCanvas(c_name,"",0,0,600,hight)
    return c

def set_padMargin(pad,left,right,top,bottom):
    pad.SetLeftMargin(left)
    pad.SetRightMargin(right)
    pad.SetTopMargin(top)
    pad.SetBottomMargin(bottom)

def make_stackPad(y_low,y_high):
    padStack = ROOT.TPad("padStack","padStack",0,y_low,1,y_high)
    padStack.SetFillColor(0)
    padStack.SetBorderMode(0)
    padStack.SetBorderSize(10)
    padStack.SetTickx(1)
    padStack.SetTicky(1)
    padStack.SetLeftMargin(0.18)
    padStack.SetRightMargin(0.05)
    padStack.SetTopMargin(0.122)
    padStack.SetBottomMargin(0.0)
    padStack.SetFrameFillStyle(0)
    padStack.SetFrameLineStyle(0)
    padStack.SetFrameLineWidth(1)
    padStack.SetFrameBorderMode(0)
    padStack.SetFrameBorderSize(10)
    return padStack

def call_histos():
    histos = {"histSig":{},"histBkg":{},"histData":{}}
    for cat in cate.keys():
        histlist=[] # all bkg histograms go into here
        histlist_sig=[] # ggH, VBF and SMH(ggH+VBF+VH) go into here
        ''' Save histograms in the list '''
        # signals
        for signal in signals:
            histlist_sig.append(file.Get(cat).Get(signal))
        # major bkg
        for major in majors:
            histlist.append(file.Get(cat).Get(major))
        # combine minor bkg
        h_minor = file.Get(cat).Get(minors[0])
        for minor in minors:
            if(minor!=minors[0]): 
                h_minor.Add(file.Get(cat).Get(minor),1)
        histlist.append(h_minor)
        # data
        h_data=file.Get(cat).Get("data_obs")
        
        # add histograms into dictionary histos
        histos["histSig"][cate[cat]]=histlist_sig
        histos["histBkg"][cate[cat]]=histlist
        histos["histData"][cate[cat]]=h_data
    return histos

def set_dataStyle():
    for cat in cate.keys():
        Data = histoAll["histData"][cate[cat]]
        Data.GetXaxis().SetTitle("")
        Data.GetXaxis().SetLabelSize(0)
        Data.GetXaxis().SetTitleSize(0)
        Data.GetXaxis().SetNdivisions(505)
        Data.GetYaxis().SetTitle("Events/bin")    
        Data.GetYaxis().SetTitleSize(1)
        Data.GetYaxis().SetTitleOffset(0.0)
        Data.GetYaxis().SetLabelFont(42)
        Data.GetYaxis().SetLabelOffset(0.01)
        Data.GetYaxis().SetLabelSize(0.03)#0.06
        Data.SetTitle("")
        Data.SetMarkerStyle(20)
        Data.SetLineColor(1)
        Data.SetMarkerSize(1)
        Data.SetMaximum(Data.GetMaximum()*1.60)#,stack.GetMaximum()*1.20))
        Data.SetMinimum(0)

def make_stack(category):
    stack=ROOT.THStack("","")
    #errorBand=histoAll["histBkg"][cat].Clone() 
    c_index = 0
    for h_bkg in histoAll["histBkg"][category]:
        h_bkg.SetLineWidth(2)
        h_bkg.SetLineColor(1)
        h_bkg.SetFillColor(ROOT.TColor.GetColor(mypalette[c_index]))
        c_index+=1
        stack.Add(h_bkg)
    stack.SetMaximum(stack.GetMaximum()*1.60)
    return stack

def make_sig(category,sig,color,style,scale):
    h_sig = file.Get(category).Get(sig).Clone()
    h_sig.SetLineColor(ROOT.kBlue)
    h_sig.SetMarkerStyle(0)
    h_sig.SetLineWidth(4)
    h_sig.SetLineStyle(style)
    h_sig.Scale(scale)
    return h_sig

def make_errorBand(category):
    errorBand=histoAll["histBkg"][category][0].Clone()
    for h_bkg in histoAll["histBkg"][category]:
        if h_bkg is not histoAll["histBkg"][category][0]:
            errorBand.Add(h_bkg)
    errorBand.SetMarkerSize(0)
    errorBand.SetFillColor(new_idx)
    errorBand.SetFillStyle(3001)
    errorBand.SetLineWidth(0)
    return errorBand

def make_dividedHisto(num,deno,min,max,title):
    h_ratio = num.Clone()
    h_ratio.Divide(deno)
    h_ratio.Sumw2()
    if min is not max:
        h_ratio.SetMaximum(max)
        h_ratio.SetMinimum(min)
    else:
        h_ratio.SetMaximum(h_ratio.GetMaximum()*1.4)
        h_ratio.SetMinimum(h_ratio.GetMinimum()*0.6)
    h_ratio.SetMarkerStyle(21)
    h_ratio.SetLineStyle(0)
    h_ratio.SetLineColor(1)
    h_ratio.SetLineWidth(2)
    h_ratio.GetYaxis().SetTitle(title)
    h_ratio.GetYaxis().SetTitleOffset(0.4)
    h_ratio.GetXaxis().SetNdivisions(505)
    h_ratio.GetYaxis().SetNdivisions(5, True)
    h_ratio.GetXaxis().SetTitleSize(0.15)
    h_ratio.GetYaxis().SetTitleSize(0.17)
    h_ratio.GetXaxis().SetLabelSize(0.11)
    h_ratio.GetYaxis().SetLabelSize(0.15)
    h_ratio.GetXaxis().SetTitleFont(42)
    h_ratio.GetYaxis().SetTitleFont(42)
    return h_ratio

def make_ratioErr(error):
    h_error = error.Clone()
    h_error1 = error.Clone()
    for i in range (1, h_error1.GetSize()-2):
        h_error1.SetBinError(i,0)
    h_error.Sumw2()
    h_error.Divide(h_error1)
    return h_error

def make_titleTag():
    obsPave = ROOT.TPaveText(0.5, 0.1, 0.95, 0.9, "NDC")
    obsPave.SetBorderSize(   0 )
    obsPave.SetFillStyle(    0 )
    obsPave.SetTextAlign(   31 )
    obsPave.SetTextSize (  0.5 )
    obsPave.SetTextColor(    1 )
    obsPave.SetTextFont (   42 )
    obsPave.AddText(obs)
    return obsPave


##########################
##     Build Canvas     ##
##########################
ROOT.gStyle.SetFrameLineWidth(1)
ROOT.gStyle.SetLineWidth(1)
ROOT.gStyle.SetOptStat(0)

histoAll = call_histos()
set_dataStyle()


#c1=ROOT.TCanvas("canvas1","",0,0,600,1000)
for cat in cate.keys():
    print cate[cat]+' is processing...'

    ''' Making main histogram pad '''
    # Open new canvas
    p_histoStack = make_canvas(500,"p_histoStack")
    p_histoStack.cd()
    # Draw data
    Data = histoAll["histData"][cate[cat]]
    Data.Draw("e")
    # Draw bkg
    stack = make_stack(cate[cat])
    stack.Draw("HIST")
    # Draw error band
    error = make_errorBand(cate[cat])
    error.Draw("e2same")
    # Draw sig - flexible!
    SMH = make_sig(cat,"SMH",0,7,30)
    SMH.Draw("esame HIST")
    ggH = make_sig(cat,"ggH125",0,7,30)
    VBF = make_sig(cat,"VBF125",0,7,30)
    WH = make_sig(cat,"WH125",0,7,30)
    ZH = make_sig(cat,"ZH125",0,7,30)
    Data.Draw("esame")
    # Draw Legend
    legende = make_legend()
    legende.AddEntry(Data,"Data","elp")    
    legende.AddEntry(SMH,"ggH Higgs(125)x30.0","l")
    legende.AddEntry(histoAll["histBkg"][cate[cat]][0],"Z#rightarrow#tau#tau","f")
    legende.AddEntry(histoAll["histBkg"][cate[cat]][1],"QCD","f")
    legende.AddEntry(histoAll["histBkg"][cate[cat]][2],"others","f")
    legende.Draw()
    # Draw miscellaneous
    lumi = add_lumi()
    lumi.Draw("same")
    cms = add_CMS()
    cms.Draw("same")
    prelim = add_Preliminary()
    prelim.Draw("same")
    categ = add_cate(cate[cat])
    categ.Draw("same")
    p_histoStack.RedrawAxis()
    p_histoStack.SetFillColor(0)
    p_histoStack.SetBorderMode(0)
    p_histoStack.SetBorderSize(10)
    p_histoStack.SetTickx(1)
    p_histoStack.SetTicky(1)
    p_histoStack.SetFrameFillStyle(0)
    p_histoStack.SetFrameLineStyle(0)
    p_histoStack.SetFrameLineWidth(1)
    p_histoStack.SetFrameBorderMode(0)
    p_histoStack.SetFrameBorderSize(10)
    set_padMargin(p_histoStack,0.18,0.05,0.122,0.0)

    ''' Making ratio pads '''
    # ratio[1] : Data/MC
    p_ratio_DataMC = make_canvas(150,"p_ratio_DataMC")
    p_ratio_DataMC.cd()
    p_ratio_DataMC.SetGridy()
    h_ratio_DataMC = make_dividedHisto(Data,error,0.5,1.5,"Data / MC")
    h_ratio_DataMC.Draw("e0p")
    h_ratioErr_DataMC = make_ratioErr(error)
    h_ratioErr_DataMC.Draw("e2same")
    set_padMargin(p_ratio_DataMC,0.18,0.05,0.0,0.0)
    # ratio[2] : Sig/sqrt(S+B)
    p_ratio_SigBkg = make_canvas(150,"p_ratio_SigBkg")
    p_ratio_SigBkg.cd()
    p_ratio_SigBkg.SetGridy()
    
    h_ratio_SigBkg = make_dividedHisto(SMH,error,0,0,"Sig/sqrt(S+B)")
    h_ratio_SigBkg.Draw("e0p")
    set_padMargin(p_ratio_SigBkg,0.18,0.05,0.0,0.0)
    # ratio[3] : VBF/ggH
    p_ratio_VBFggH = make_canvas(150,"p_ratio")
    p_ratio_VBFggH.cd()
    p_ratio_VBFggH.SetGridy()
    h_ratio_VBFggH = make_dividedHisto(VBF,ggH,0,0,"VBF/ggH")
    h_ratio_VBFggH.Draw("e0p")
    set_padMargin(p_ratio_VBFggH,0.18,0.05,0.0,0.0)



    ########################################################################
    ##                                                                    ##
    ##  Plot[1]                                                           ##
    ##  1. Main histogram                                                 ##
    ##  2. Data/MC                                                        ##
    ##  3. S/sqrt(S+B)    : To see discriminating power btw sig and bkg   ##
    ##  4. VBF/ggH        : To see if we can separate VBF and ggH         ##
    ##                                                                    ##
    ########################################################################

    # Make canvas
    plot1 = make_canvas(1000,"plot1")
    # Stick main histogram pad
    plot1.cd()
    pad_Main = make_stackPad(0.5,1.0)
    pad_Main.Draw()
    pad_Main.cd()
    p_histoStack.DrawClonePad()    
    SMH.Draw("esame HIST")
    # Stick ratio Data/MC
    plot1.cd()
    pad_DataMC = make_stackPad(0.36,0.5)
    pad_DataMC.Draw()
    pad_DataMC.cd()
    p_ratio_DataMC.DrawClonePad()
    # Stick ratio S/sqrt(S+B)
    plot1.cd()
    pad_SigBkg = make_stackPad(0.22,0.36)
    pad_SigBkg.Draw()
    pad_SigBkg.cd()
    p_ratio_SigBkg.DrawClonePad() 
    # Stick ratio VBF/ggH
    plot1.cd()
    pad_VBFggH = make_stackPad(0.08,0.22)
    pad_VBFggH.Draw()
    pad_VBFggH.cd()
    p_ratio_VBFggH.DrawClonePad() 
    # Stick title of the plot
    plot1.cd()
    pad_obs = make_stackPad(0,0.08)
    pad_obs.Draw()
    pad_obs.cd()
    set_padMargin(pad_obs,0,0,0,0)
    obsPave = make_titleTag()
    obsPave.Draw()

    # Save plot
    plot1.SaveAs("plots/testPlotter1_"+cate[cat]+".pdf")
    

    



