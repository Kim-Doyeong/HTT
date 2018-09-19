
from subprocess import Popen 
from sys import argv, exit, stdout, stderr    

import ROOT
import numpy 
from array import array   

import plotRocCurve_def 

# So things don't look like crap.    
ROOT.gROOT.SetStyle("Plain")
ROOT.gROOT.SetBatch(True)   
ROOT.gStyle.SetOptStat(0)  

######## Load Files ######### 
file_mjj = ROOT.TFile("final_nominal_mjj.root")
file_ggh = ROOT.TFile("final_nominal_normMELAggH.root")
file_vbf = ROOT.TFile("final_nominal_normMELAvbf.root")
file_vbfbyggh = ROOT.TFile("final_nominal_normMELAvbfbyggh.root")
file_gghbyvbf = ROOT.TFile("final_nominal_normMELAgghbyvbf.root")



####### Produce ROC curve #######
plotRocCurve_def.produce_roc_curve( 
    file_mjj,file_ggh,       # input root files
    'ggH125','ggH125_eff',   # 'histogramName' in rootfile, 'legend Title' on the plot (x-axis)
    'ZTT','ZTT_eff',         # 'histogramName' in rootfile, 'legend Title' on the plot (y-axis)
    'mjj','MELA',            # category (legend name)
    'ROC(normMELAggH)',      # output file name is 'ROC(normMELAggH).pdf'
    )

plotRocCurve_def.produce_roc_curve( 
    file_mjj,file_vbf,       # input root files
    'VBF125','VBF125_eff',   # 'histogramName' in rootfile, 'legend Title' on the plot (x-axis)
    'ZTT','ZTT_eff',         # 'histogramName' in rootfile, 'legend Title' on the plot (y-axis)
    'mjj','MELA',            # category (legend name)
    'ROC(normMELAvbf)',      # output file name is 'ROC(normMELAvbf).pdf'
    )



####### Produce MELA obs with ratio #######
plotRocCurve_def.produce_ratio(
    file_vbf,
    'normMELAvbf','vbf',     # 'legend title', 'category' in root file
    'VBF125','ZTT',          # 'signal histo name', 'ztt histo name'
    )
plotRocCurve_def.produce_ratio(
    file_ggh,
    'normMELAggh','vbf',     # 'legend title', 'category' in root file
    'ggH125','ZTT',          # 'signal histo name', 'ztt histo name'
    )
plotRocCurve_def.produce_ratio(
    file_vbfbyggh,
    'normMELAvbf_ggH','vbf',
    'ggH125','VBF125',
    )
plotRocCurve_def.produce_ratio(
    file_gghbyvbf,
    'normMELAggH_vbf','vbf',
    'ggH125','VBF125',
    )
