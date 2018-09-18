# Plotting distribution

## Instruction :
Checkout the repository and change branch for plot.
```
git clone https://github.com/dykim1/HTT.git
cd HTT
git checkout feature-plot
```

One need to copy input ntuples into this place.

```2016SMHTT/tt/analysis/test/Aug30/```

Ntuples are here : https://www.dropbox.com/sh/a5f5itv565t7phb/AAC48NbYLeC8StJhZWpVxRLTa?dl=0

Or from the Wisconsin machine(@login.wisc.hep.edu) 
```/hdfs/store/user/doyeong/SMHTT_CONDOR/tautau/myskims/Aug30/skims_sv_mela/```

To compile analyzer,
```
cd 2016SMHTT/tt/analysis/src
./Make.sh tt_analyzer.cc
```

To run the analyzer and make the distribution plots,
```
cd ../test
source do_nominalRuns.sh
```

---
### How to change observable
One need to modify ```tt_analyzer.cc``` to make other observable distributions. 

1. Set what you want to plots in this line.

https://github.com/dykim1/HTT/blob/feature-plot/2016SMHTT/tt/analysis/src/tt_analyzer.cc#L761

2. Choose the proper binning from here.

https://github.com/dykim1/HTT/blob/feature-plot/2016SMHTT/tt/analysis/src/tt_analyzer.cc#L223-L225

Where 0, 1, and 2 means 0jet, 1jet and 2 or more jets category. One can modify binning of each category independently. 

3. If you would like to change the definiton of category, modifiy these lines.

https://github.com/dykim1/HTT/blob/feature-plot/2016SMHTT/tt/analysis/src/tt_analyzer.cc#L738-L739

https://github.com/dykim1/HTT/blob/feature-plot/2016SMHTT/tt/analysis/src/tt_analyzer.cc#L735

