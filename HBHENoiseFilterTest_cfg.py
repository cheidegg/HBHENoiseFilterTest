import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("TEST")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

##____________________________________________________________________________||
process.load("CommonTools/RecoAlgos.HBHENoiseFilterResultProducer_cfi")
#process.load("CommonTools/RecoAlgos.HBHENoiseFilterResultProducer_cfi", defaultDecision = "HBHENoiseFilterResultRun2Loose")
#process.load("CommonTools/RecoAlgos.HBHENoiseFilterResultProducer_cfi", defaultDecision = "HBHENoiseFilterResultRun2Tight")

##____________________________________________________________________________||
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/MCRUN2_74_V7-v1/00000/704718B7-77D4-E411-BC8C-003048FFD7D4.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/MCRUN2_74_V7-v1/00000/920178CC-58D4-E411-9620-0026189437EC.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/MCRUN2_74_V7-v1/00000/FA77C69A-76D4-E411-B22F-003048FFCB74.root",

       "/store/relval/CMSSW_7_4_0_pre9_ROOT6/JetHT/RECO/GR_R_74_V8_1Apr_RelVal_jht2012D-v1/00000/00D54B37-5BD9-E411-9BC0-002618943807.root", 
       "/store/relval/CMSSW_7_4_0_pre9_ROOT6/JetHT/RECO/GR_R_74_V8_1Apr_RelVal_jht2012D-v1/00000/026F987A-41DB-E411-A714-0025905A60B6.root", 
       "/store/relval/CMSSW_7_4_0_pre9_ROOT6/JetHT/RECO/GR_R_74_V8_1Apr_RelVal_jht2012D-v1/00000/02BAF09A-23DB-E411-A674-0025905A48D0.root", 
       "/store/relval/CMSSW_7_4_0_pre9_ROOT6/JetHT/RECO/GR_R_74_V8_1Apr_RelVal_jht2012D-v1/00000/045D5B9E-D4DA-E411-B2D1-0025905A607E.root", 
       "/store/relval/CMSSW_7_4_0_pre9_ROOT6/JetHT/RECO/GR_R_74_V8_1Apr_RelVal_jht2012D-v1/00000/04A85887-43DB-E411-A6F2-0025905A48D6.root", 
       
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/06F0BC5D-7FD4-E411-942F-0026189438DD.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/2E9707F3-4DD4-E411-B87E-0025905A48BC.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/5405F51B-53D4-E411-8C0D-0025905A611C.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/7436EF05-55D4-E411-A5DC-0025905A605E.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/78112D06-5BD4-E411-AA11-0025905A60C6.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/9EB83C69-7FD4-E411-8B38-0025905A497A.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/A24E0250-57D4-E411-94A8-0025905A607E.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/CA8CBFD0-7BD4-E411-B44B-0025905A6084.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/DAEA5E07-5BD4-E411-8363-0025905A6118.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/EA53FE74-52D4-E411-AC51-00261894380D.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU25ns_MCRUN2_74_V7-v1/00000/EC7FE840-55D4-E411-84E0-0025905A605E.root",

       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V6-v1/00000/82C64875-E9D3-E411-8C2F-003048FFCC1E.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V6-v1/00000/9A67A875-E9D3-E411-B8A4-0025905A497A.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V6-v1/00000/B2F70BC2-E6D3-E411-8B72-0025905B858E.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V6-v1/00000/B4802AC3-E6D3-E411-B23A-0025905964A6.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V6-v1/00000/C2AC80C4-E6D3-E411-B69F-0025905A6132.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V6-v1/00000/C615391D-E6D3-E411-A394-0025905A6082.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V6-v1/00000/CE47F11B-E6D3-E411-B1AC-002354EF3BE1.root",
       #"/store/relval/CMSSW_7_4_0_pre9/RelValTTbar_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V6-v1/00000/F6EFCDC5-E4D3-E411-8ECF-0025905B858A.root"
       )
    )

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('HBHENoiseFilter.root'),
    #SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_*_*_TEST'
        )
    )

##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 500
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

##____________________________________________________________________________||
#process.pfMetWithSignificance = process.pfMet.clone(
#    calculateSignificance = cms.bool(True),
#    srcJets = cms.InputTag("ak4PFJets"),
#    srcLeptons = cms.VInputTag("selectedElectrons", "selectedMuons", "selectedPhotons"),
#    parameters = process.METSignificanceParams
#    )

##____________________________________________________________________________||
process.p = cms.Path(
    process.HBHENoiseFilterResultProducer
    )

process.e1 = cms.EndPath(
    process.out
    )

##____________________________________________________________________________||
