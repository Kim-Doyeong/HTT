#ifndef THTH_TREE_H
#define	THTH_TREE_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <utility>
#include <map>
#include <string>
#include "TTree.h"
#include "TFile.h"
#include "TSystem.h"
#include "HTauTauTree_mt.h"

using namespace std;


float trackpt_1,trackpt_2, jetPt_1, jetPt_2;
unsigned int run, lumi, evt, NUP = -10;
int gen_match_1, gen_match_2=0;
float mMatchesDoubleTightTau35Path,tMatchesDoubleTightTau35Path,mMatchesDoubleMediumTau40Path,tMatchesDoubleMediumTau40Path,mMatchesDoubleTightTau40Path,tMatchesDoubleTightTau40Path;
float jetpt_1, jetpt_2, jetpt_3;
float met_norecoil;
float npu, rho, npv=-1, puweight, weight;
float againstElectronLooseMVA6_2, againstElectronMediumMVA6_2, againstElectronTightMVA6_2, againstElectronVLooseMVA6_2, againstElectronVTightMVA6_2, againstMuonLoose3_2, againstMuonTight3_2, decayModeFinding_2;
float e_1, px_1, py_1, pz_1, pt_1, phi_1, eta_1, m_1, q_1, d0_1, dZ_1, mt_1, iso_1;
float e_2, px_2, py_2, pz_2, pt_2, phi_2, eta_2, m_2, q_2, d0_2, dZ_2, mt_2, iso_2, t_decayMode;
float id_m_loose_1, id_m_medium_1, id_m_tight_1;
float byCombinedIsolationDeltaBetaCorrRaw3Hits_2, byIsolationMVA3oldDMwLTraw_2, byIsolationMVA3newDMwLTraw_2;
float byVLooseIsolationMVArun2v1DBnewDMwLT_2,  byVLooseIsolationMVArun2v1DBoldDMwLT_2,  byVLooseIsolationMVArun2v1DBdR03oldDMwLT_2;
float byLooseIsolationMVArun2v1DBnewDMwLT_2,  byLooseIsolationMVArun2v1DBoldDMwLT_2,  byLooseIsolationMVArun2v1DBdR03oldDMwLT_2;
float byMediumIsolationMVArun2v1DBnewDMwLT_2,  byMediumIsolationMVArun2v1DBoldDMwLT_2,  byMediumIsolationMVArun2v1DBdR03oldDMwLT_2;
float byTightIsolationMVArun2v1DBnewDMwLT_2,  byTightIsolationMVArun2v1DBoldDMwLT_2,  byTightIsolationMVArun2v1DBdR03oldDMwLT_2;
float byVTightIsolationMVArun2v1DBnewDMwLT_2,  byVTightIsolationMVArun2v1DBoldDMwLT_2,  byVTightIsolationMVArun2v1DBdR03oldDMwLT_2;
float byVVTightIsolationMVArun2v1DBnewDMwLT_2,  byVVTightIsolationMVArun2v1DBoldDMwLT_2,  byVVTightIsolationMVArun2v1DBdR03oldDMwLT_2;
float mjj, jdeta, jdphi, dijetpt, dijetphi, hdijetphi, visjeteta, ptvis;
float mjj_JESDown, jdeta_JESDown,mjj_JESUp,jdeta_JESUp;
int njetingap, njetingap20, nbtag, njets, njetspt20, nbtagL;
int njetingap_JESDown, njetingap20_JESDown, njets_JESDown, njetspt20_JESDown;
int njetingap_JESUp, njetingap20_JESUp, njets_JESUp, njetspt20_JESUp;
float jmass_1, jpt_1, jpx_1, jpy_1, jpz_1, jeta_1, jphi_1, jrawf_1, jmva_1, jpfid_1, jpuid_1, jcsv_1;
float jmass_2, jpx_2, jpy_2, jpz_2, jpt_2, jeta_2, jphi_2, jrawf_2, jmva_2, jpfid_2, jpuid_2, jcsv_2;
float bpt_1, beta_1, bphi_1, bpfid_1, bpuid_1, bcsv_1, bflavor_1;
float bpt_2, beta_2, bphi_2, bpfid_2, bpuid_2, bcsv_2, bflavor_2;
float met, metphi, mvaMet, mvaMetphi, pzetavis, pzetamiss, mvacov00, mvacov01, mvacov11, mvacov10;
float top_reweighting, gen_Higgs_pt, gen_Higgs_mass=1.0;
float  extraelec_veto, extramuon_veto, dilepton_veto=false;
float byLooseCombinedIsolationDeltaBetaCorr3Hits_3, byMediumCombinedIsolationDeltaBetaCorr3Hits_3, byTightCombinedIsolationDeltaBetaCorr3Hits_3;
float byLooseCombinedIsolationDeltaBetaCorr3HitsdR03_3, byMediumCombinedIsolationDeltaBetaCorr3HitsdR03_3, byTightCombinedIsolationDeltaBetaCorr3HitsdR03_3;
float extratau_veto, pt_top1, pt_top2, genweight, dphi_12, dphi_mumet, dphi_taumet;
float aMCatNLO_weight, numGenJets;
float met_px, met_py;
float metSig, metcov00, metcov01, metcov10,metcov11, mvaMetcov00, mvaMetcov01,mvaMetcov10,mvaMetcov11, metcov00_v2, metcov01_v2, metcov10_v2,metcov11_v2;
float met_JESDown,met_UESDown;
float met_JESUp,met_UESUp,met_MESUp;
float metphi_JERDown,metphi_JESDown,metphi_UESDown,metphi_MESDown,metphi_EESDown,metphi_TESDown,metphi_PESDown;
float metphi_JERUp,metphi_JESUp,metphi_UESUp,metphi_MESUp,metphi_EESUp,metphi_TESUp,metphi_PESUp;
float genDR_2;
float byVLooseIsolationRerunMVArun2v1DBoldDMwLT_1, byVTightIsolationRerunMVArun2v1DBoldDMwLT_1, byLooseIsolationRerunMVArun2v1DBoldDMwLT_1, byMediumIsolationRerunMVArun2v1DBoldDMwLT_1, byTightIsolationRerunMVArun2v1DBoldDMwLT_1, byVVTightIsolationRerunMVArun2v1DBoldDMwLT_1,byIsolationRerunMVA3oldDMwLTraw_1;
float byVLooseIsolationRerunMVArun2v1DBoldDMwLT_2, byVTightIsolationRerunMVArun2v1DBoldDMwLT_2, byLooseIsolationRerunMVArun2v1DBoldDMwLT_2, byMediumIsolationRerunMVArun2v1DBoldDMwLT_2, byTightIsolationRerunMVArun2v1DBoldDMwLT_2, byVVTightIsolationRerunMVArun2v1DBoldDMwLT_2,byIsolationRerunMVA3oldDMwLTraw_2;
float mRerunMVArun2v2DBoldDMwLTVVLoose,mRerunMVArun2v2DBoldDMwLTVLoose,mRerunMVArun2v2DBoldDMwLTLoose,mRerunMVArun2v2DBoldDMwLTMedium,mRerunMVArun2v2DBoldDMwLTTight,mRerunMVArun2v2DBoldDMwLTVTight,mRerunMVArun2v2DBoldDMwLTVVTight;
float tRerunMVArun2v2DBoldDMwLTVVLoose,tRerunMVArun2v2DBoldDMwLTVLoose,tRerunMVArun2v2DBoldDMwLTLoose,tRerunMVArun2v2DBoldDMwLTMedium,tRerunMVArun2v2DBoldDMwLTTight,tRerunMVArun2v2DBoldDMwLTVTight,tRerunMVArun2v2DBoldDMwLTVVTight;
float matchIsoMu22eta2p1_2,matchIsoTkMu22eta2p1_2,matchIsoMu22_2,matchIsoTkMu22_2,matchIsoMu24_2,matchIsoTkMu24_2,filterIsoMu22eta2p1_2,filterIsoTkMu22eta2p1_2,filterIsoMu22_2,filterIsoTkMu22_2,filterIsoMu24_2,filterIsoTkMu24_2,filterIsoMu19Tau0_3,filterIsoMu21Tau0_3;
int njets_JetAbsoluteFlavMapDown,njets_JetAbsoluteMPFBiasDown,njets_JetAbsoluteScaleDown,njets_JetAbsoluteStatDown,njets_JetEnDown,njets_JetFlavorQCDDown,njets_JetFragmentationDown,njets_JetPileUpDataMCDown,njets_JetPileUpPtBBDown,njets_JetPileUpPtEC1Down,njets_JetPileUpPtEC2Down,njets_JetPileUpPtHFDown,njets_JetPileUpPtRefDown,njets_JetRelativeBalDown,njets_JetRelativeFSRDown,njets_JetRelativeJEREC1Down,njets_JetRelativeJEREC2Down,njets_JetRelativeJERHFDown,njets_JetRelativePtBBDown,njets_JetRelativePtEC1Down,njets_JetRelativePtEC2Down,njets_JetRelativePtHFDown,njets_JetRelativeStatECDown,njets_JetRelativeStatFSRDown,njets_JetRelativeStatHFDown,njets_JetSinglePionECALDown,njets_JetSinglePionHCALDown,njets_JetTimePtEtaDown;
int njets_JetAbsoluteFlavMapUp,njets_JetAbsoluteMPFBiasUp,njets_JetAbsoluteScaleUp,njets_JetAbsoluteStatUp,njets_JetEnUp,njets_JetFlavorQCDUp,njets_JetFragmentationUp,njets_JetPileUpDataMCUp,njets_JetPileUpPtBBUp,njets_JetPileUpPtEC1Up,njets_JetPileUpPtEC2Up,njets_JetPileUpPtHFUp,njets_JetPileUpPtRefUp,njets_JetRelativeBalUp,njets_JetRelativeFSRUp,njets_JetRelativeJEREC1Up,njets_JetRelativeJEREC2Up,njets_JetRelativeJERHFUp,njets_JetRelativePtBBUp,njets_JetRelativePtEC1Up,njets_JetRelativePtEC2Up,njets_JetRelativePtHFUp,njets_JetRelativeStatECUp,njets_JetRelativeStatFSRUp,njets_JetRelativeStatHFUp,njets_JetSinglePionECALUp,njets_JetSinglePionHCALUp,njets_JetTimePtEtaUp;
float mjj_JetAbsoluteFlavMapDown,mjj_JetAbsoluteMPFBiasDown,mjj_JetAbsoluteScaleDown,mjj_JetAbsoluteStatDown,mjj_JetEnDown,mjj_JetFlavorQCDDown,mjj_JetFragmentationDown,mjj_JetPileUpDataMCDown,mjj_JetPileUpPtBBDown,mjj_JetPileUpPtEC1Down,mjj_JetPileUpPtEC2Down,mjj_JetPileUpPtHFDown,mjj_JetPileUpPtRefDown,mjj_JetRelativeBalDown,mjj_JetRelativeFSRDown,mjj_JetRelativeJEREC1Down,mjj_JetRelativeJEREC2Down,mjj_JetRelativeJERHFDown,mjj_JetRelativePtBBDown,mjj_JetRelativePtEC1Down,mjj_JetRelativePtEC2Down,mjj_JetRelativePtHFDown,mjj_JetRelativeStatECDown,mjj_JetRelativeStatFSRDown,mjj_JetRelativeStatHFDown,mjjJetSinglePionECALDown,mjj_JetSinglePionHCALDown,mjj_JetTimePtEtaDown, mjj_JetSinglePionECALDown;
float mjj_JetAbsoluteFlavMapUp,mjj_JetAbsoluteMPFBiasUp,mjj_JetAbsoluteScaleUp,mjj_JetAbsoluteStatUp,mjj_JetEnUp,mjj_JetFlavorQCDUp,mjj_JetFragmentationUp,mjj_JetPileUpDataMCUp,mjj_JetPileUpPtBBUp,mjj_JetPileUpPtEC1Up,mjj_JetPileUpPtEC2Up,mjj_JetPileUpPtHFUp,mjj_JetPileUpPtRefUp,mjj_JetRelativeBalUp,mjj_JetRelativeFSRUp,mjj_JetRelativeJEREC1Up,mjj_JetRelativeJEREC2Up,mjj_JetRelativeJERHFUp,mjj_JetRelativePtBBUp,mjj_JetRelativePtEC1Up,mjj_JetRelativePtEC2Up,mjj_JetRelativePtHFUp,mjj_JetRelativeStatECUp,mjj_JetRelativeStatFSRUp,mjj_JetRelativeStatHFUp,mjj_JetSinglePionECALUp,mjj_JetSinglePionHCALUp,mjj_JetTimePtEtaUp;
float passDoubleMu;
float passDoubleTau35, matchDoubleTau35_1, matchDoubleTau35_2,filterDoubleTau35_1,filterDoubleTau35_2,passDoubleTauCmbIso35,matchDoubleTauCmbIso35_1,matchDoubleTauCmbIso35_2,filterDoubleTauCmbIso35_1,filterDoubleTauCmbIso35_2;
float genM,genpT,genpX,genpY,vispX,vispY, b_vispX;
float genEta, genPhi, genHTT, genMass;
float type1_pfMet_shiftedPt_UnclusteredEnUp,type1_pfMet_shiftedPt_UnclusteredEnDown,type1_pfMet_shiftedPhi_UnclusteredEnUp,type1_pfMet_shiftedPhi_UnclusteredEnDown,type1_pfMet_shiftedPt_JetEnUp,type1_pfMet_shiftedPt_JetEnDown,type1_pfMet_shiftedPhi_JetEnUp,type1_pfMet_shiftedPhi_JetEnDown;
float mGenCharge,mGenDecayMode,mGenEnergy,mGenEta,mGenIsPrompt,mGenJetEta,mGenJetPt,mGenMotherEnergy,mGenMotherEta,mGenMotherPdgId,mGenMotherPhi,mGenMotherPt,mGenPdgId,mGenPhi,mGenPt,mGenStatus,mZTTGenDR,mZTTGenEta,mZTTGenMatching,mZTTGenPhi,mZTTGenPt;
float tGenCharge,tGenDecayMode,tGenEnergy,tGenEta,tGenIsPrompt,tGenJetEta,tGenJetPt,tGenMotherEnergy,tGenMotherEta,tGenMotherPdgId,tGenMotherPhi,tGenMotherPt,tGenPdgId,tGenPhi,tGenPt,tGenStatus,tZTTGenDR,tZTTGenEta,tZTTGenMatching,tZTTGenPhi,tZTTGenPt;
float trg_doubletau, trg_singlemuon, trg_mutaucross;
float chargedIsoPtSum_1, chargedIsoPtSum_2, neutralIsoPtSum_1, neutralIsoPtSum_2, puCorrPtSum_1, puCorrPtSum_2;

void fillTree(TTree *Run_Tree, HTauTauTree_mt *tree, int entry_tree, bool ismc){
    tree->GetEntry(entry_tree);
    // Event ID variables 
    run = tree->run;
    lumi = tree->lumi;
    evt =tree->evt;
    aMCatNLO_weight = tree->GenWeight;
    // Extra lepton vetos
    dilepton_veto=((tree->dimuonVeto>0));
    extraelec_veto=((tree->eVetoZTTp001dxyzR0>0));
    extramuon_veto=((tree->muVetoZTTp001dxyzR0>1));
    // Trigger flags
    trg_singlemuon = (tree->IsoMu24Group || tree->IsoMu24Pass || tree->IsoMu24Prescale);//|| tree->IsoMu27Group || tree->IsoMu27Pass || tree->IsoMu27Prescale;
    //trg_mutaucross = ; // FIXME - FSA doesn't have cross trg branches.

    TLorentzVector mu, tau, mymet;
    mu.SetPtEtaPhiM(tree->mPt,tree->mEta,tree->mPhi,tree->mMass);
    tau.SetPtEtaPhiM(tree->tPt,tree->tEta,tree->tPhi,tree->tMass);
    mymet.SetPtEtaPhiM(tree->type1_pfMetEt,0,tree->type1_pfMetPhi,0);
    met_norecoil=tree->type1_pfMetEt;
    float pfmetcorr_ex=mymet.Px();
    float pfmetcorr_ey=mymet.Py();
    mymet.SetPxPyPzE(pfmetcorr_ex,pfmetcorr_ey,0,sqrt(pfmetcorr_ex*pfmetcorr_ex+pfmetcorr_ey*pfmetcorr_ey));
    /*

    if (ismc && tree->tDecayMode==0) tau=tau*0.982;
    else if (ismc && tree->tDecayMode==1) tau=tau*1.010;
    else if (ismc && tree->tDecayMode==10) tau=tau*1.004;

    */

    /*
    if (ismc && tree->mDecayMode==0 && tree->tDecayMode==0) mymet=mymet+(mu+tau)-0.982*(mu+tau);
    else if (ismc && tree->mDecayMode==0 && tree->tDecayMode==1) mymet=mymet+(mu+tau)-0.982*mu-1.010*tau;
    else if (ismc && tree->mDecayMode==0 && tree->tDecayMode==10) mymet=mymet+(mu+tau)-0.982*mu-1.004*tau;
    else if (ismc && tree->mDecayMode==1 && tree->tDecayMode==0) mymet=mymet+(mu+tau)-1.010*mu-1.010*tau;
    else if (ismc && tree->mDecayMode==1 && tree->tDecayMode==1) mymet=mymet+(mu+tau)-1.010*(mu+tau);
    else if (ismc && tree->mDecayMode==1 && tree->tDecayMode==10) mymet=mymet+(mu+tau)-1.010*mu-1.004*tau;
    else if (ismc && tree->mDecayMode==10 && tree->tDecayMode==1) mymet=mymet+(mu+tau)-1.004*mu-1.010*tau;
    else if (ismc && tree->mDecayMode==10 && tree->tDecayMode==0) mymet=mymet+(mu+tau)-1.004*mu-1.004*tau;
    else if (ismc && tree->mDecayMode==10 && tree->tDecayMode==10) mymet=mymet+(mu+tau)-1.004*(mu+tau);
    */

    // Leg1
    pt_1 = mu.Pt();
    px_1 = mu.Px();
    py_1 = mu.Py();
    pz_1 = mu.Pz();
    phi_1 = mu.Phi();
    eta_1 = mu.Eta();
    m_1 = mu.M();
    e_1 = mu.E();
    q_1 = tree->mCharge;
    d0_1 = tree->mPVDXY;
    dZ_1 = tree->mPVDZ;
    mt_1 = sqrt(2*mu.Pt()*mymet.Pt()*(1-cos(mu.DeltaPhi(mymet))));    
    iso_1 = tree->mRelPFIsoDBDefaultR04;
    gen_match_1=tree->mZTTGenMatching;
    id_m_loose_1 = tree->mPFIDLoose;
    id_m_medium_1 = tree->mPFIDMedium;
    id_m_tight_1 = tree->mPFIDTight;
    // Leg2
    pt_2 = tau.Pt();
    px_2 = tau.Px();
    py_2 = tau.Py();
    pz_2 = tau.Pz();
    phi_2 = tau.Phi();
    eta_2 = tau.Eta();
    m_2 = tau.M();
    if (tree->tDecayMode==0) m_2=tree->tMass;
    e_2 = tau.E();
    q_2 = tree->tCharge;
    d0_2 = tree->tPVDXY;
    dZ_2 = tree->tPVDZ;
    mt_2 = sqrt(2*tau.Pt()*mymet.Pt()*(1-cos(tau.DeltaPhi(mymet))));
    iso_2 = tree->tRerunMVArun2v2DBoldDMwLTraw;
    gen_match_2=tree->tZTTGenMatching;
    againstElectronVLooseMVA6_2 = tree->tAgainstElectronVLooseMVA6;
    againstElectronLooseMVA6_2 = tree->tAgainstElectronLooseMVA6;
    againstElectronMediumMVA6_2 = tree->tAgainstElectronMediumMVA6;
    againstElectronTightMVA6_2 = tree->tAgainstElectronTightMVA6;
    againstElectronVTightMVA6_2 = tree->tAgainstElectronVTightMVA6;
    againstMuonTight3_2 = tree->tAgainstMuonTight3;
    againstMuonLoose3_2 = tree->tAgainstMuonLoose3;
    byCombinedIsolationDeltaBetaCorrRaw3Hits_2=tree->tByCombinedIsolationDeltaBetaCorrRaw3Hits;
    byIsolationMVA3oldDMwLTraw_2=tree->tRerunMVArun2v2DBoldDMwLTraw;
    byIsolationMVA3newDMwLTraw_2=tree->tByIsolationMVArun2v1DBnewDMwLTraw;  // FIXME
    chargedIsoPtSum_2 = tree->tChargedIsoPtSum; 
    neutralIsoPtSum_2 = tree->tNeutralIsoPtSum;
    decayModeFinding_2=tree->tDecayModeFinding;
    t_decayMode=tree->tDecayMode;
    // MET
    met=mymet.Pt();
    metphi=mymet.Phi();
    metSig=tree->metSig;
    metcov00=tree->metcov00;
    metcov01=tree->metcov01;
    metcov10=tree->metcov10;
    metcov11=tree->metcov11;
    met_px=mymet.Px();
    met_py=mymet.Py();
    // VBF system : Only fill if njetspt20>=2
    njetspt20=tree->jetVeto20;
    TLorentzVector jet1, jet2, dijet;
    if (tree->jetVeto20 > 0 && jpt_1>0)
      jet1.SetPtEtaPhiM(jpt_1,jeta_1,jphi_1,0);
    if (tree->jetVeto20 > 1 && jpt_2>0) {
      jet2.SetPtEtaPhiM(jpt_2,jeta_2,jphi_2,0);
      dijet=jet1+jet2;
      mjj = dijet.M();
      jdeta=tree->vbfDeta;
      if(tree->jetVeto30>1) njetingap=tree->vbfJetVeto30;
      njetingap20=tree->vbfJetVeto20;
      jdphi = jet1.DeltaPhi(jet2); 
      dijetpt = dijet.Pt();
      dijetphi=dijet.Phi();
    }
    else{
      /*
      mjj=-10000;
      jdeta=-10000;
      njetingap=-10000;
      njetingap20=-10000;
      jdphi=-10000;
      dijetpt=-10000;
      dijetphi=-10000;
      */
    }
    // additional jets
    nbtag = tree->bjetCISVVeto20Medium;
    nbtagL = tree->bjetCISVVeto20Loose;
    njets = tree->jetVeto30;
    njets_JESDown = tree->jetVeto30_JetEnDown;
    njetspt20_JESDown=tree->jetVeto20_JetEnDown;
    njets_JESUp = tree->jetVeto30_JetEnUp;
    njetspt20_JESUp=tree->jetVeto20_JetEnUp;
    jpt_1=tree->j1pt;
    jeta_1=tree->j1eta;
    jphi_1=tree->j1phi;
    jcsv_1=tree->j1csv;
    jpt_2=tree->j2pt;
    jeta_2=tree->j2eta;
    jphi_2=tree->j2phi;
    jcsv_2=tree->j2csv;
    bpt_1=tree->jb1pt;
    beta_1=tree->jb1eta;
    bphi_1=tree->jb1phi;
    bcsv_1=tree->jb1csv;
    bflavor_1=tree->jb1hadronflavor;
    bpt_2=tree->jb2pt;
    beta_2=tree->jb2eta;
    bphi_2=tree->jb2phi;
    bcsv_2=tree->jb2csv;
    bflavor_2=tree->jb2hadronflavor;
    // Generator Variables
    NUP=tree->NUP;
    // Pile Up
    npv=tree->nvtx;
    npu=tree->nTruePU;
    rho=tree->rho;



    genpX=tree->genpX;
    genpY=tree->genpY;
    genpT=tree->genpT;
    genM=tree->genM;
    vispX=tree->vispX;
    vispY=tree->vispY;

    genEta=tree->genEta;
    genPhi=tree->genPhi;
    genHTT=tree->genHTT;
    genMass=tree->genMass;

    /*
    mGenCharge=tree->mGenCharge;
    mGenEnergy=tree->mGenEnergy;
    mGenEta=tree->mGenEta;
    mGenIsPrompt=tree->mGenIsPrompt;
    mGenPdgId=tree->mGenPdgId;
    mGenPhi=tree->mGenPhi;
    mGenPt=tree->mGenPt;
    mGenStatus=tree->mGenStatus;
    mZTTGenDR=tree->mZTTGenDR;
    mZTTGenEta=tree->mZTTGenEta;
    mZTTGenMatching=tree->mZTTGenMatching;
    mZTTGenPhi=tree->mZTTGenPhi;
    mZTTGenPt=tree->mZTTGenPt;

    tGenCharge=tree->tGenCharge;
    tGenDecayMode=tree->tGenDecayMode;
    tGenEnergy=tree->tGenEnergy;
    tGenEta=tree->tGenEta;
    tGenIsPrompt=tree->tGenIsPrompt;
    tGenJetEta=tree->tGenJetEta;
    tGenJetPt=tree->tGenJetPt;
    tGenMotherEnergy=tree->tGenMotherEnergy;
    tGenMotherEta=tree->tGenMotherEta;
    tGenMotherPdgId=tree->tGenMotherPdgId;
    tGenMotherPhi=tree->tGenMotherPhi;
    tGenMotherPt=tree->tGenMotherPt;
    tGenPdgId=tree->tGenPdgId;
    tGenPhi=tree->tGenPhi;
    tGenPt=tree->tGenPt;
    tGenStatus=tree->tGenStatus;
    tZTTGenDR=tree->tZTTGenDR;
    tZTTGenEta=tree->tZTTGenEta;
    tZTTGenMatching=tree->tZTTGenMatching;
    tZTTGenPhi=tree->tZTTGenPhi;
    tZTTGenPt=tree->tZTTGenPt;
    */

    pt_top1=tree->topQuarkPt1;
    pt_top2=tree->topQuarkPt2;
    numGenJets=tree->numGenJets;



    jetPt_1 = tree->mJetPt;


    
     // rereun iso
    //tRerunMVArun2v2DBoldDMwLTVVLoose = tree->tRerunMVArun2v2DBoldDMwLTVVLoose;
    tRerunMVArun2v2DBoldDMwLTVLoose = tree->tRerunMVArun2v2DBoldDMwLTVLoose;
    tRerunMVArun2v2DBoldDMwLTLoose = tree->tRerunMVArun2v2DBoldDMwLTLoose;    
    tRerunMVArun2v2DBoldDMwLTMedium = tree->tRerunMVArun2v2DBoldDMwLTMedium;
    tRerunMVArun2v2DBoldDMwLTTight = tree->tRerunMVArun2v2DBoldDMwLTTight;
    tRerunMVArun2v2DBoldDMwLTVTight = tree->tRerunMVArun2v2DBoldDMwLTVTight;
    tRerunMVArun2v2DBoldDMwLTVVTight = tree->tRerunMVArun2v2DBoldDMwLTVVTight;
    //

    trackpt_2 = tree->tLeadTrackPt;
    jetPt_2 = tree->tJetPt;


    byVLooseIsolationMVArun2v1DBoldDMwLT_2 = tree->tByVLooseIsolationMVArun2v1DBoldDMwLT;
    byLooseIsolationMVArun2v1DBoldDMwLT_2 = tree->tByLooseIsolationMVArun2v1DBoldDMwLT;
    byMediumIsolationMVArun2v1DBoldDMwLT_2 = tree->tByMediumIsolationMVArun2v1DBoldDMwLT;
    byTightIsolationMVArun2v1DBoldDMwLT_2 = tree->tByTightIsolationMVArun2v1DBoldDMwLT;
    byVTightIsolationMVArun2v1DBoldDMwLT_2 = tree->tByVTightIsolationMVArun2v1DBoldDMwLT;
    byVVTightIsolationMVArun2v1DBoldDMwLT_2 = tree->tByVVTightIsolationMVArun2v1DBoldDMwLT;

    //byIsolationMVA3oldDMwoLTraw_2=tree->tByIsolationMVArun2v1DBoldDMwLTraw;
   

   /*
   if (njetspt20_JESUp > 1){
      njetingap20_JESUp=tree->vbfJetVeto20_JetEnUp;
      njetingap_JESUp=tree->vbfJetVeto30_JetEnUp;
      mjj_JESUp=tree->vbfMass_JetEnUp;
      jdeta_JESUp=tree->vbfDeta_JetEnUp;
   }
   else{
      jdeta_JESUp=-10000;
      mjj_JESUp=-10000;
      njetingap20_JESUp=-10000;
      njetingap_JESUp=-100000;
   }
   if (njetspt20_JESDown > 1){
      njetingap20_JESDown=tree->vbfJetVeto20_JetEnDown;
      njetingap_JESDown=tree->vbfJetVeto30_JetEnDown;
      mjj_JESDown=tree->vbfMass_JetEnDown;
      jdeta_JESDown=tree->vbfDeta_JetEnDown;
   }
   else{
      jdeta_JESDown=-10000;
      mjj_JESDown=-10000;
      njetingap20_JESDown=-10000;
      njetingap_JESDown=-100000;
   }
   */
        
    extratau_veto=tree->tauVetoPt20Loose3HitsVtx;
    Run_Tree->Fill();
}

#endif


