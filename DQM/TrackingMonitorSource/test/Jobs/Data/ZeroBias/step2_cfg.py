# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test_11_b_1 -s HARVESTING:dqmHarvesting --conditions auto:com10 --data --filein file:step1_DQM.root --scenario pp --no_exec --python_filename=test_step2.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('HARVESTING')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EDMtoMEAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring([
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_1.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_101.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_11.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_111.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_121.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_131.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_21.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_31.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_41.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_51.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_61.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_71.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_81.root",
"file:/afs/cern.ch/work/k/kmondal/public/DatavsMC/September18_2017/CMSSW_9_3_0/src/DQM/TrackingMonitorSource/test/Jobs/Run302572/ZeroBias/step1_output/step1_DQM_91.root"
    ]),
    processingMode = cms.untracked.string('RunsAndLumis')
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('FULLMERGE')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('test_11_b_1 nevts:1'),
    name = cms.untracked.string('Applications')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v9', '')

# Path and EndPath definitions
process.edmtome_step = cms.Path(process.EDMtoME)
process.validationprodHarvesting = cms.Path(process.hltpostvalidation_prod+process.postValidation_gen)
process.validationHarvesting = cms.Path(process.postValidation+process.hltpostvalidation+process.postValidation_gen)
process.dqmHarvestingPOGMC = cms.Path(process.DQMOffline_SecondStep_PrePOGMC)
process.validationpreprodHarvesting = cms.Path(process.postValidation_preprod+process.hltpostvalidation_preprod+process.postValidation_gen)
process.validationHarvestingHI = cms.Path(process.postValidationHI)
process.genHarvesting = cms.Path(process.postValidation_gen)
process.dqmHarvestingPOG = cms.Path(process.DQMOffline_SecondStep_PrePOG)
process.alcaHarvesting = cms.Path()
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(process.edmtome_step,process.dqmsave_step)
