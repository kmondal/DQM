import FWCore.ParameterSet.Config as cms
from DQM.TrackingMonitorSource.StandaloneTrackMonitor_cfi import *
#from DQM.TrackingMonitor.V0Monitor_cfi import *

# Primary Vertex Selector
selectedPrimaryVertices = cms.EDFilter("VertexSelector",
    src = cms.InputTag('offlinePrimaryVertices'),
    cut = cms.string("!isFake && ndof >= 4 && abs(z) < 24 && abs(position.Rho) < 2.0"),
    filter = cms.bool(True)
)

# Track Selector
selectedTracks = cms.EDFilter("TrackSelector",
    src = cms.InputTag('generalTracks'),
    cut = cms.string("pt > 1.0"),
    filter = cms.bool(True)
)

# HLT path selector
hltPathFilter = cms.EDFilter("HLTPathSelector",
    processName = cms.string("HLT"),
    hltPathsOfInterest = cms.vstring("HLT_ZeroBias_v"),
    triggerResults = cms.untracked.InputTag("TriggerResults","","HLT"),
    triggerEvent = cms.untracked.InputTag("hltTriggerSummaryAOD","","HLT")
)
# Z->MuMu event selector
ztoMMEventSelector = cms.EDFilter("ZtoMMEventSelector")
muonTracks = cms.EDProducer("MuonTrackProducer")
# Z->ee event selector
ztoEEEventSelector = cms.EDFilter("ZtoEEEventSelector")
electronTracks = cms.EDProducer("ElectronTrackProducer")

# Added module for V0Monitoring for Ks only
#KshortMonitor = v0Monitor.clone()
#KshortMonitor.FolderName = cms.string("Tracking/V0Monitoring/Ks")
#KshortMonitor.v0         = cms.InputTag('generalV0Candidates:Kshort')
#KshortMonitor.histoPSet.massPSet = cms.PSet(
#   nbins = cms.int32 ( 100 ),
#   xmin  = cms.double( 0.400),
#   xmax  = cms.double( 0.600),
#)

standaloneTrackMonitorMC = standaloneTrackMonitor.clone(
    puScaleFactorFile = cms.untracked.string("PileupScaleFactor_302572_wrt_nVertex_ZtoMM.root"),
    doPUCorrection    = cms.untracked.bool(True),
    isMC              = cms.untracked.bool(True)
    )

standaloneTrackMonitorElec = standaloneTrackMonitor.clone(
    folderName = cms.untracked.string("ElectronTracks"),
    trackInputTag = cms.untracked.InputTag('electronTracks'),
    )

standaloneTrackMonitorElecMC = standaloneTrackMonitor.clone(
    folderName = cms.untracked.string("ElectronTracks"),
    trackInputTag = cms.untracked.InputTag('electronTracks'),
    puScaleFactorFile = cms.untracked.string("PileupScaleFactor_302572_wrt_nVertex_ZtoEE.root"),
    doPUCorrection    = cms.untracked.bool(True),
    isMC              = cms.untracked.bool(True)
    )

standaloneValidationElec = cms.Sequence(
    selectedTracks
    * selectedPrimaryVertices
    * ztoEEEventSelector
    * electronTracks
    * standaloneTrackMonitorElec   
    * standaloneTrackMonitor)
standaloneValidationElecMC = cms.Sequence(
    selectedTracks
    * selectedPrimaryVertices
    * ztoEEEventSelector
    * electronTracks
    * standaloneTrackMonitorElecMC   
    * standaloneTrackMonitorMC)


standaloneTrackMonitorMuon = standaloneTrackMonitor.clone(
    folderName = cms.untracked.string("MuonTracks"),
    trackInputTag = cms.untracked.InputTag('muonTracks'),
    )

standaloneTrackMonitorMuonMC = standaloneTrackMonitor.clone(
    folderName = cms.untracked.string("MuonTracks"),
    trackInputTag = cms.untracked.InputTag('muonTracks'),
    puScaleFactorFile = cms.untracked.string("PileupScaleFactor_302572_wrt_nVertex_ZtoMM.root"),
    doPUCorrection    = cms.untracked.bool(True),
    isMC              = cms.untracked.bool(True)
    )

standaloneValidationMuon = cms.Sequence(
    selectedTracks
    * selectedPrimaryVertices
    * ztoMMEventSelector
    * muonTracks
    * standaloneTrackMonitorMuon 
    * standaloneTrackMonitor)
standaloneValidationMuonMC = cms.Sequence(
    selectedTracks
    * selectedPrimaryVertices
    * ztoMMEventSelector
    * muonTracks
    * standaloneTrackMonitorMuonMC 
    * standaloneTrackMonitorMC)

standaloneValidationMinbias = cms.Sequence(
    hltPathFilter
    * selectedTracks
    * selectedPrimaryVertices
    * standaloneTrackMonitor)
standaloneValidationMinbiasMC = cms.Sequence(
    hltPathFilter
    * selectedTracks
    * selectedPrimaryVertices
    * standaloneTrackMonitorMC)

