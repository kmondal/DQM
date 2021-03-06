import FWCore.ParameterSet.Config as cms
from HLTriggerOffline.Btag.hltBtagJetMCTools_cff import *

#denominator trigger
hltBtagTriggerSelection = cms.EDFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring(
      "HLT_PFMET120_* OR HLT_HT300PT30_QuadJet_75_60_45_40_v* OR HLT_PFHT380_SixJet32_DoubleBTagCSV_* OR HLT_Ele28_eta2p1_WPTight_Gsf_HT150_* OR HLT_IsoMu24_eta2p1_*"),
    hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
#    l1tResults = cms.InputTag( "simGtDigis" ),
    l1tResults = cms.InputTag( "" ),
    throw = cms.bool( False )
)

#correct the jet used for the matching
hltBtagJetsbyRef.jets = cms.InputTag("ak4GenJetsNoNu")

#define HltVertexValidationVertices for the vertex DQM validation
HltVertexValidationVertices= cms.EDAnalyzer("HLTVertexPerformanceAnalyzer",
        SimVertexCollection = cms.InputTag("g4SimHits"),
	TriggerResults = cms.InputTag('TriggerResults','',"HLT"),
	HLTPathNames =cms.vstring(
	'HLT_PFMET120_',
	'HLT_PFMET120_',
	'HLT_PFMET120_',
	'HLT_HT300PT30_QuadJet_75_60_45_40_v',
	'HLT_HT300PT30_QuadJet_75_60_45_40_v',
	'HLT_HT300PT30_QuadJet_75_60_45_40_v',
	'HLT_PFHT380_SixJet32_DoubleBTagCSV_',
	'HLT_PFHT380_SixJet32_DoubleBTagCSV_',
	'HLT_PFHT380_SixJet32_DoubleBTagCSV_',
	'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_',
	'HLT_IsoMu24_eta2p1_'
	),
	Vertex = cms.VInputTag(
		cms.InputTag("hltVerticesL3"), 
		cms.InputTag("hltFastPrimaryVertex"), 
		cms.InputTag("hltFastPVPixelVertices"),
		cms.InputTag("hltVerticesPF"), 
	)
)

#define bTagValidation for the b-tag DQM validation (distribution plot)
hltbTagValidation = cms.EDAnalyzer("HLTBTagPerformanceAnalyzer",
	TriggerResults = cms.InputTag('TriggerResults','','HLT'),
	HLTPathNames =cms.vstring(
	'HLT_PFMET120_',
	'HLT_HT300PT30_QuadJet_75_60_45_40_v',
	'HLT_PFHT380_SixJet32_DoubleBTagCSV_',
	'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_',
	'HLT_IsoMu24_eta2p1_'
	),
	JetTag = cms.VInputTag(
		cms.InputTag("hltCombinedSecondaryVertexBJetTagsCalo"),
		cms.InputTag("hltCombinedSecondaryVertexBJetTagsCalo"),
		cms.InputTag("hltCombinedSecondaryVertexBJetTagsCalo"),
		cms.InputTag("hltCombinedSecondaryVertexBJetTagsPF"),
		cms.InputTag("hltCombinedSecondaryVertexBJetTagsPF"),
		),
	MinJetPT = cms.double(20),
	mcFlavours = cms.PSet(
		light = cms.vuint32(1, 2, 3, 21), # udsg
		c = cms.vuint32(4),
		b = cms.vuint32(5),
		g = cms.vuint32(21),
		uds = cms.vuint32(1, 2, 3)
	),
	mcPartons = cms.InputTag("hltBtagJetsbyValAlgo")
)

#put all in a path
hltbtagValidationSequence = cms.Sequence(
#	remove noisy warnings
#	hltBtagTriggerSelection +
	hltBtagJetMCTools +
	HltVertexValidationVertices +
	hltbTagValidation
)

# fastsim customs
from Configuration.Eras.Modifier_fastSim_cff import fastSim
if fastSim.isChosen():
    HltVertexValidationVertices.SimVertexCollection = cms.InputTag("famosSimHits")
    # are these customs actually needed?
    #HltVertexValidationVertices.HLTPathNames =cms.vstring(
    #'HLT_PFMET120_NoiseCleaned_BTagCSV07_v',
    #'HLT_PFMET120_NoiseCleaned_BTagCSV07_v',
    #	'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_',
    #	'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_',
    #	'HLT_QuadPFJet_VBF',
    #	'HLT_QuadPFJet_VBF',
    #	'HLT_Ele32_eta2p1_',
    #	'HLT_IsoMu24_eta2p1_')
    #HltVertexValidationVertices.Vertex = cms.VInputTag(
    #    cms.InputTag("hltVerticesL3"), 
    #    cms.InputTag("hltFastPVPixelVertices"),
    #    cms.InputTag("hltVerticesPF"), 
    #)

