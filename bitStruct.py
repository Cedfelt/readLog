bitStruct = [('uint:8', 'ucTag0', 8),
('uint:8', 'ucTag1', 8),
('uint:8', 'ucTag2', 8),
('uint:8', 'ucChksum', 8),
('uint:32', 'ucVer', 32),
('uint:32', 'uiTimestamp', 32),
('uint:32', 'uiLogType', 32),
('uint:32', 'uiLogPos', 32),
#GlobLogEntry global
  ('uint:32', 'global.uiAccLife', 32),
  ('uint:32', 'global.uiRes1', 32),
  ('uint:32', 'global.uiAccRst', 32),
  ('uint:32', 'global.uiAccEntry', 32),
  ('uint:32', 'global.uiAccTFault', 32),
  ('uint:32', 'global.uiAccAssert', 32),
  ('uint:32', 'global.uiLifeMaxT', 32),
  #StdHst hstPsmT
    ('uint:32', 'global.hstPsmT.uiBin0', 32),
    ('uint:32', 'global.hstPsmT.uiBin1', 32),
    ('uint:32', 'global.hstPsmT.uiBin2', 32),
    ('uint:32', 'global.hstPsmT.uiBin3', 32),
    ('uint:32', 'global.hstPsmT.uiBin4', 32),
  #StdHst hstPwr
    ('uint:32', 'global.hstPwr.uiBin0', 32),
    ('uint:32', 'global.hstPwr.uiBin1', 32),
    ('uint:32', 'global.hstPwr.uiBin2', 32),
    ('uint:32', 'global.hstPwr.uiBin3', 32),
    ('uint:32', 'global.hstPwr.uiBin4', 32),

  ('uint:8', 'global.uiPsuMaxMainsVolt', 8),
  ('uint:8', 'global.uiPsuAvgMainsVolt', 8),
  ('uint:8', 'global.uiPsuMinMainsVolt', 8),
  ('uint:8', 'global.uiPsuMaxMainsCurr', 8),
  ('uint:8', 'global.uiPsuAvgMainsCurr', 8),
  ('uint:8', 'global.uiPfcMinOutVolt', 8),
  ('uint:8', 'global.uiPfcAvgOutVolt', 8),
  ('uint:8', 'global.uiMaxPLimReduct', 8),
  ('uint:8', 'global.uiAvgPLimReduct', 8),
  ('uint:8', 'global.uiPsuAvgP', 8),
  ('uint:8', 'global.uiPsuMaxP', 8),
  ('uint:8', 'global.uiPsuTempSensor', 8),
  ('uint:8', 'global.ucPsmPeakTemp', 8),
  ('uint:8', 'global.ucPsmAvgTemp', 8),
  ('uint:8', 'global.ucMaxP', 8),
  ('uint:8', 'global.ucAvgP', 8),
  ('uint:1', 'global.bMsrInp', 1),
  ('uint:23', 'global.Res', 23),
  ('uint:8', 'global.accWatisar', 8),
  #DvcServBits servBits
    ('uint:1', 'global.servBits.bPsmFault', 1),
    ('uint:1', 'global.servBits.bRes1', 1),
    ('uint:1', 'global.servBits.bRes2', 1),
    ('uint:1', 'global.servBits.bRes3', 1),
    ('uint:4', 'global.servBits.unNeedsService', 4),
    ('uint:8', 'global.servBits.ucRes0', 8),
    ('uint:8', 'global.servBits.ucRes1', 8),
    ('uint:8', 'global.servBits.ucRes2', 8),
  #DvcMiscBits miscBits
    ('uint:1', 'global.miscBits.bFlash', 1),
    ('uint:1', 'global.miscBits.bAudioNok', 1),
    ('uint:1', 'global.miscBits.bAudioClk', 1),
    ('uint:1', 'global.miscBits.bPAL', 1),
    ('uint:1', 'global.miscBits.bTemp', 1),
    ('uint:1', 'global.miscBits.bAssert', 1),
    ('uint:1', 'global.miscBits.bPsmStatus', 1),
    ('uint:1', 'global.miscBits.bSlotTemp', 1),
    ('uint:1', 'global.miscBits.bSenseWarning', 1),
    ('uint:1', 'global.miscBits.nTempWarn', 1),
    ('uint:6', 'global.miscBits.ucRes0', 6),
    ('uint:4', 'global.miscBits.ucRes1', 4),
    ('uint:1', 'global.miscBits.nMainsGlitch', 1),
    ('uint:1', 'global.miscBits.nPSUSafeMode', 1),
    ('uint:1', 'global.miscBits.nCheckACMains', 1),
    ('uint:1', 'global.miscBits.nPALP51', 1),
    ('uint:1', 'global.miscBits.nPTL', 1),
    ('uint:1', 'global.miscBits.nATL', 1),
    ('uint:1', 'global.miscBits.nBEL', 1),
    ('uint:1', 'global.miscBits.nUVL', 1),
    ('uint:1', 'global.miscBits.nPowerProtect', 1),
    ('uint:1', 'global.miscBits.nMainsHighFaultPeak', 1),
    ('uint:1', 'global.miscBits.nMainsHighFault', 1),
    ('uint:1', 'global.miscBits.nMainsLowFault', 1),


#ChLogEntry ch 1 [4]
  ('uint:8', 'ChLogEntry_ChA.ucPeakT', 8),
  ('uint:8', 'ChLogEntry_ChA.ucAvgT', 8),
  ('uint:8', 'ChLogEntry_ChA.ucPeakV', 8),
  ('uint:8', 'ChLogEntry_ChA.ucAvgV', 8),
  ('uint:8', 'ChLogEntry_ChA.ucPeakI', 8),
  ('uint:8', 'ChLogEntry_ChA.ucAvgI', 8),
  ('uint:8', 'ChLogEntry_ChA.ucMaxP', 8),
  ('uint:8', 'ChLogEntry_ChA.ucAvgP', 8),
  ('uint:8', 'ChLogEntry_ChA.ucMaxVC', 8),
  ('uint:8', 'ChLogEntry_ChA.ucAvgVC', 8),
  ('uint:8', 'ChLogEntry_ChA.ucPeakHR', 8),
  ('uint:8', 'ChLogEntry_ChA.ucThermHR', 8),
  ('uint:16', 'ChLogEntry_ChA.usMinLoadZ0', 16),
  ('uint:16', 'ChLogEntry_ChA.usMaxLoadZ0', 16),
  ('uint:1', 'ChLogEntry_ChA.bTemp', 1),
  ('uint:1', 'ChLogEntry_ChA.bVcTemp', 1),
  ('uint:1', 'ChLogEntry_ChA.bSmTemp', 1),
  ('uint:1', 'ChLogEntry_ChA.bNoLoad', 1),
  ('uint:1', 'ChLogEntry_ChA.bVhf', 1),
  ('uint:1', 'ChLogEntry_ChA.bWrongSpkr', 1),
  ('uint:1', 'ChLogEntry_ChA.bFewSpkr', 1),
  ('uint:1', 'ChLogEntry_ChA.bCorrect', 1),
  ('uint:1', 'ChLogEntry_ChA.bModPrecLow', 1),
  ('uint:1', 'ChLogEntry_ChA.bTempW1', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes11', 1),
  ('uint:1', 'ChLogEntry_ChA.bMoreSpkr', 1),
  ('uint:1', 'ChLogEntry_ChA.bVcTempW', 1),
  ('uint:1', 'ChLogEntry_ChA.bSmTempW', 1),
  ('uint:1', 'ChLogEntry_ChA.bUncLoad', 1),
  ('uint:1', 'ChLogEntry_ChA.bNotvLoad', 1),
  ('uint:1', 'ChLogEntry_ChA.bNoLdPrst', 1),
  ('uint:1', 'ChLogEntry_ChA.bULim', 1),
  ('uint:1', 'ChLogEntry_ChA.bILim', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes13', 1),
  ('uint:1', 'ChLogEntry_ChA.bACL', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes12', 1),
  ('uint:1', 'ChLogEntry_ChA.bShortc', 1),
  ('uint:1', 'ChLogEntry_ChA.bLoadPilotActive', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes3', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes4', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes5', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes6', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes7', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes8', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes9', 1),
  ('uint:1', 'ChLogEntry_ChA.bRes10', 1),
  #ChServBits servBits
    ('uint:1', 'ChLogEntry_ChA.servBits.bFuse', 1),
    ('uint:1', 'ChLogEntry_ChA.servBits.bDac', 1),
    ('uint:1', 'ChLogEntry_ChA.servBits.bRes8', 1),
    ('uint:1', 'ChLogEntry_ChA.servBits.bRes3', 1),
    ('uint:1', 'ChLogEntry_ChA.servBits.bRes4', 1),
    ('uint:1', 'ChLogEntry_ChA.servBits.bRes5', 1),
    ('uint:1', 'ChLogEntry_ChA.servBits.bRes6', 1),
    ('uint:1', 'ChLogEntry_ChA.servBits.bRes7', 1),
    ('uint:8', 'ChLogEntry_ChA.servBits.ucRes0', 8),
    ('uint:8', 'ChLogEntry_ChA.servBits.ucRes1', 8),
    ('uint:8', 'ChLogEntry_ChA.servBits.ucRes2', 8),
  ('uint:32', 'ChLogEntry_ChA.uiAccWh', 32),
  ('uint:32', 'ChLogEntry_ChA.uiAccTFault', 32),
  #StdHst hstPsmT
    ('uint:32', 'ChLogEntry_ChA.hstPsmT.uiBin0', 32),
    ('uint:32', 'ChLogEntry_ChA.hstPsmT.uiBin1', 32),
    ('uint:32', 'ChLogEntry_ChA.hstPsmT.uiBin2', 32),
    ('uint:32', 'ChLogEntry_ChA.hstPsmT.uiBin3', 32),
    ('uint:32', 'ChLogEntry_ChA.hstPsmT.uiBin4', 32),
  #StdHst hstPwr
    ('uint:32', 'ChLogEntry_ChA.hstPwr.uiBin0', 32),
    ('uint:32', 'ChLogEntry_ChA.hstPwr.uiBin1', 32),
    ('uint:32', 'ChLogEntry_ChA.hstPwr.uiBin2', 32),
    ('uint:32', 'ChLogEntry_ChA.hstPwr.uiBin3', 32),
    ('uint:32', 'ChLogEntry_ChA.hstPwr.uiBin4', 32),
  ('uint:16', 'ChLogEntry_ChA.usMinLoadZ1', 16),
  ('uint:16', 'ChLogEntry_ChA.usMaxLoadZ1', 16),
  ('uint:32', 'ChLogEntry_ChA.Res1', 32),

#ChLogEntry ch B [4]
  ('uint:8', 'ChLogEntry_ChB.ucPeakT', 8),
  ('uint:8', 'ChLogEntry_ChB.ucAvgT', 8),
  ('uint:8', 'ChLogEntry_ChB.ucPeakV', 8),
  ('uint:8', 'ChLogEntry_ChB.ucAvgV', 8),
  ('uint:8', 'ChLogEntry_ChB.ucPeakI', 8),
  ('uint:8', 'ChLogEntry_ChB.ucAvgI', 8),
  ('uint:8', 'ChLogEntry_ChB.ucMaxP', 8),
  ('uint:8', 'ChLogEntry_ChB.ucAvgP', 8),
  ('uint:8', 'ChLogEntry_ChB.ucMaxVC', 8),
  ('uint:8', 'ChLogEntry_ChB.ucAvgVC', 8),
  ('uint:8', 'ChLogEntry_ChB.ucPeakHR', 8),
  ('uint:8', 'ChLogEntry_ChB.ucThermHR', 8),
  ('uint:16', 'ChLogEntry_ChB.usMinLoadZ0', 16),
  ('uint:16', 'ChLogEntry_ChB.usMaxLoadZ0', 16),
  ('uint:1', 'ChLogEntry_ChB.bTemp', 1),
  ('uint:1', 'ChLogEntry_ChB.bVcTemp', 1),
  ('uint:1', 'ChLogEntry_ChB.bSmTemp', 1),
  ('uint:1', 'ChLogEntry_ChB.bNoLoad', 1),
  ('uint:1', 'ChLogEntry_ChB.bVhf', 1),
  ('uint:1', 'ChLogEntry_ChB.bWrongSpkr', 1),
  ('uint:1', 'ChLogEntry_ChB.bFewSpkr', 1),
  ('uint:1', 'ChLogEntry_ChB.bCorrect', 1),
  ('uint:1', 'ChLogEntry_ChB.bModPrecLow', 1),
  ('uint:1', 'ChLogEntry_ChB.bTempW1', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes11', 1),
  ('uint:1', 'ChLogEntry_ChB.bMoreSpkr', 1),
  ('uint:1', 'ChLogEntry_ChB.bVcTempW', 1),
  ('uint:1', 'ChLogEntry_ChB.bSmTempW', 1),
  ('uint:1', 'ChLogEntry_ChB.bUncLoad', 1),
  ('uint:1', 'ChLogEntry_ChB.bNotvLoad', 1),
  ('uint:1', 'ChLogEntry_ChB.bNoLdPrst', 1),
  ('uint:1', 'ChLogEntry_ChB.bULim', 1),
  ('uint:1', 'ChLogEntry_ChB.bILim', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes13', 1),
  ('uint:1', 'ChLogEntry_ChB.bACL', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes12', 1),
  ('uint:1', 'ChLogEntry_ChB.bShortc', 1),
  ('uint:1', 'ChLogEntry_ChB.bLoadPilotActive', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes3', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes4', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes5', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes6', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes7', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes8', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes9', 1),
  ('uint:1', 'ChLogEntry_ChB.bRes10', 1),
  #ChServBits servBits
    ('uint:1', 'ChLogEntry_ChB.servBits.bFuse', 1),
    ('uint:1', 'ChLogEntry_ChB.servBits.bDac', 1),
    ('uint:1', 'ChLogEntry_ChB.servBits.bRes8', 1),
    ('uint:1', 'ChLogEntry_ChB.servBits.bRes3', 1),
    ('uint:1', 'ChLogEntry_ChB.servBits.bRes4', 1),
    ('uint:1', 'ChLogEntry_ChB.servBits.bRes5', 1),
    ('uint:1', 'ChLogEntry_ChB.servBits.bRes6', 1),
    ('uint:1', 'ChLogEntry_ChB.servBits.bRes7', 1),
    ('uint:8', 'ChLogEntry_ChB.servBits.ucRes0', 8),
    ('uint:8', 'ChLogEntry_ChB.servBits.ucRes1', 8),
    ('uint:8', 'ChLogEntry_ChB.servBits.ucRes2', 8),
  ('uint:32', 'ChLogEntry_ChB.uiAccWh', 32),
  ('uint:32', 'ChLogEntry_ChB.uiAccTFault', 32),
  #StdHst hstPsmT
    ('uint:32', 'ChLogEntry_ChB.hstPsmT.uiBin0', 32),
    ('uint:32', 'ChLogEntry_ChB.hstPsmT.uiBin1', 32),
    ('uint:32', 'ChLogEntry_ChB.hstPsmT.uiBin2', 32),
    ('uint:32', 'ChLogEntry_ChB.hstPsmT.uiBin3', 32),
    ('uint:32', 'ChLogEntry_ChB.hstPsmT.uiBin4', 32),
  #StdHst hstPwr
    ('uint:32', 'ChLogEntry_ChB.hstPwr.uiBin0', 32),
    ('uint:32', 'ChLogEntry_ChB.hstPwr.uiBin1', 32),
    ('uint:32', 'ChLogEntry_ChB.hstPwr.uiBin2', 32),
    ('uint:32', 'ChLogEntry_ChB.hstPwr.uiBin3', 32),
    ('uint:32', 'ChLogEntry_ChB.hstPwr.uiBin4', 32),
  ('uint:16', 'ChLogEntry_ChB.usMinLoadZ1', 16),
  ('uint:16', 'ChLogEntry_ChB.usMaxLoadZ1', 16),
  ('uint:32', 'ChLogEntry_ChB.Res1', 32),

#ChLogEntry ch C [4]
  ('uint:8', 'ChLogEntry_ChC.ucPeakT', 8),
  ('uint:8', 'ChLogEntry_ChC.ucAvgT', 8),
  ('uint:8', 'ChLogEntry_ChC.ucPeakV', 8),
  ('uint:8', 'ChLogEntry_ChC.ucAvgV', 8),
  ('uint:8', 'ChLogEntry_ChC.ucPeakI', 8),
  ('uint:8', 'ChLogEntry_ChC.ucAvgI', 8),
  ('uint:8', 'ChLogEntry_ChC.ucMaxP', 8),
  ('uint:8', 'ChLogEntry_ChC.ucAvgP', 8),
  ('uint:8', 'ChLogEntry_ChC.ucMaxVC', 8),
  ('uint:8', 'ChLogEntry_ChC.ucAvgVC', 8),
  ('uint:8', 'ChLogEntry_ChC.ucPeakHR', 8),
  ('uint:8', 'ChLogEntry_ChC.ucThermHR', 8),
  ('uint:16', 'ChLogEntry_ChC.usMinLoadZ0', 16),
  ('uint:16', 'ChLogEntry_ChC.usMaxLoadZ0', 16),
  ('uint:1', 'ChLogEntry_ChC.bTemp', 1),
  ('uint:1', 'ChLogEntry_ChC.bVcTemp', 1),
  ('uint:1', 'ChLogEntry_ChC.bSmTemp', 1),
  ('uint:1', 'ChLogEntry_ChC.bNoLoad', 1),
  ('uint:1', 'ChLogEntry_ChC.bVhf', 1),
  ('uint:1', 'ChLogEntry_ChC.bWrongSpkr', 1),
  ('uint:1', 'ChLogEntry_ChC.bFewSpkr', 1),
  ('uint:1', 'ChLogEntry_ChC.bCorrect', 1),
  ('uint:1', 'ChLogEntry_ChC.bModPrecLow', 1),
  ('uint:1', 'ChLogEntry_ChC.bTempW1', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes11', 1),
  ('uint:1', 'ChLogEntry_ChC.bMoreSpkr', 1),
  ('uint:1', 'ChLogEntry_ChC.bVcTempW', 1),
  ('uint:1', 'ChLogEntry_ChC.bSmTempW', 1),
  ('uint:1', 'ChLogEntry_ChC.bUncLoad', 1),
  ('uint:1', 'ChLogEntry_ChC.bNotvLoad', 1),
  ('uint:1', 'ChLogEntry_ChC.bNoLdPrst', 1),
  ('uint:1', 'ChLogEntry_ChC.bULim', 1),
  ('uint:1', 'ChLogEntry_ChC.bILim', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes13', 1),
  ('uint:1', 'ChLogEntry_ChC.bACL', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes12', 1),
  ('uint:1', 'ChLogEntry_ChC.bShortc', 1),
  ('uint:1', 'ChLogEntry_ChC.bLoadPilotActive', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes3', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes4', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes5', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes6', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes7', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes8', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes9', 1),
  ('uint:1', 'ChLogEntry_ChC.bRes10', 1),
  #ChServBits servBits
    ('uint:1', 'ChLogEntry_ChC.servBits.bFuse', 1),
    ('uint:1', 'ChLogEntry_ChC.servBits.bDac', 1),
    ('uint:1', 'ChLogEntry_ChC.servBits.bRes8', 1),
    ('uint:1', 'ChLogEntry_ChC.servBits.bRes3', 1),
    ('uint:1', 'ChLogEntry_ChC.servBits.bRes4', 1),
    ('uint:1', 'ChLogEntry_ChC.servBits.bRes5', 1),
    ('uint:1', 'ChLogEntry_ChC.servBits.bRes6', 1),
    ('uint:1', 'ChLogEntry_ChC.servBits.bRes7', 1),
    ('uint:8', 'ChLogEntry_ChC.servBits.ucRes0', 8),
    ('uint:8', 'ChLogEntry_ChC.servBits.ucRes1', 8),
    ('uint:8', 'ChLogEntry_ChC.servBits.ucRes2', 8),
  ('uint:32', 'ChLogEntry_ChC.uiAccWh', 32),
  ('uint:32', 'ChLogEntry_ChC.uiAccTFault', 32),
  #StdHst hstPsmT
    ('uint:32', 'ChLogEntry_ChC.hstPsmT.uiBin0', 32),
    ('uint:32', 'ChLogEntry_ChC.hstPsmT.uiBin1', 32),
    ('uint:32', 'ChLogEntry_ChC.hstPsmT.uiBin2', 32),
    ('uint:32', 'ChLogEntry_ChC.hstPsmT.uiBin3', 32),
    ('uint:32', 'ChLogEntry_ChC.hstPsmT.uiBin4', 32),
  #StdHst hstPwr
    ('uint:32', 'ChLogEntry_ChC.hstPwr.uiBin0', 32),
    ('uint:32', 'ChLogEntry_ChC.hstPwr.uiBin1', 32),
    ('uint:32', 'ChLogEntry_ChC.hstPwr.uiBin2', 32),
    ('uint:32', 'ChLogEntry_ChC.hstPwr.uiBin3', 32),
    ('uint:32', 'ChLogEntry_ChC.hstPwr.uiBin4', 32),
  ('uint:16', 'ChLogEntry_ChC.usMinLoadZ1', 16),
  ('uint:16', 'ChLogEntry_ChC.usMaxLoadZ1', 16),
  ('uint:32', 'ChLogEntry_ChC.Res1', 32),

#ChLogEntry ch D [4]
  ('uint:8', 'ChLogEntry_ChD.ucPeakT', 8),
  ('uint:8', 'ChLogEntry_ChD.ucAvgT', 8),
  ('uint:8', 'ChLogEntry_ChD.ucPeakV', 8),
  ('uint:8', 'ChLogEntry_ChD.ucAvgV', 8),
  ('uint:8', 'ChLogEntry_ChD.ucPeakI', 8),
  ('uint:8', 'ChLogEntry_ChD.ucAvgI', 8),
  ('uint:8', 'ChLogEntry_ChD.ucMaxP', 8),
  ('uint:8', 'ChLogEntry_ChD.ucAvgP', 8),
  ('uint:8', 'ChLogEntry_ChD.ucMaxVC', 8),
  ('uint:8', 'ChLogEntry_ChD.ucAvgVC', 8),
  ('uint:8', 'ChLogEntry_ChD.ucPeakHR', 8),
  ('uint:8', 'ChLogEntry_ChD.ucThermHR', 8),
  ('uint:16', 'ChLogEntry_ChD.usMinLoadZ0', 16),
  ('uint:16', 'ChLogEntry_ChD.usMaxLoadZ0', 16),
  ('uint:1', 'ChLogEntry_ChD.bTemp', 1),
  ('uint:1', 'ChLogEntry_ChD.bVcTemp', 1),
  ('uint:1', 'ChLogEntry_ChD.bSmTemp', 1),
  ('uint:1', 'ChLogEntry_ChD.bNoLoad', 1),
  ('uint:1', 'ChLogEntry_ChD.bVhf', 1),
  ('uint:1', 'ChLogEntry_ChD.bWrongSpkr', 1),
  ('uint:1', 'ChLogEntry_ChD.bFewSpkr', 1),
  ('uint:1', 'ChLogEntry_ChD.bCorrect', 1),
  ('uint:1', 'ChLogEntry_ChD.bModPrecLow', 1),
  ('uint:1', 'ChLogEntry_ChD.bTempW1', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes11', 1),
  ('uint:1', 'ChLogEntry_ChD.bMoreSpkr', 1),
  ('uint:1', 'ChLogEntry_ChD.bVcTempW', 1),
  ('uint:1', 'ChLogEntry_ChD.bSmTempW', 1),
  ('uint:1', 'ChLogEntry_ChD.bUncLoad', 1),
  ('uint:1', 'ChLogEntry_ChD.bNotvLoad', 1),
  ('uint:1', 'ChLogEntry_ChD.bNoLdPrst', 1),
  ('uint:1', 'ChLogEntry_ChD.bULim', 1),
  ('uint:1', 'ChLogEntry_ChD.bILim', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes13', 1),
  ('uint:1', 'ChLogEntry_ChD.bACL', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes12', 1),
  ('uint:1', 'ChLogEntry_ChD.bShortc', 1),
  ('uint:1', 'ChLogEntry_ChD.bLoadPilotActive', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes3', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes4', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes5', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes6', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes7', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes8', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes9', 1),
  ('uint:1', 'ChLogEntry_ChD.bRes10', 1),
  #ChServBits servBits
    ('uint:1', 'ChLogEntry_ChD.servBits.bFuse', 1),
    ('uint:1', 'ChLogEntry_ChD.servBits.bDac', 1),
    ('uint:1', 'ChLogEntry_ChD.servBits.bRes8', 1),
    ('uint:1', 'ChLogEntry_ChD.servBits.bRes3', 1),
    ('uint:1', 'ChLogEntry_ChD.servBits.bRes4', 1),
    ('uint:1', 'ChLogEntry_ChD.servBits.bRes5', 1),
    ('uint:1', 'ChLogEntry_ChD.servBits.bRes6', 1),
    ('uint:1', 'ChLogEntry_ChD.servBits.bRes7', 1),
    ('uint:8', 'ChLogEntry_ChD.servBits.ucRes0', 8),
    ('uint:8', 'ChLogEntry_ChD.servBits.ucRes1', 8),
    ('uint:8', 'ChLogEntry_ChD.servBits.ucRes2', 8),
  ('uint:32', 'ChLogEntry_ChD.uiAccWh', 32),
  ('uint:32', 'ChLogEntry_ChD.uiAccTFault', 32),
  #StdHst hstPsmT
    ('uint:32', 'ChLogEntry_ChD.hstPsmT.uiBin0', 32),
    ('uint:32', 'ChLogEntry_ChD.hstPsmT.uiBin1', 32),
    ('uint:32', 'ChLogEntry_ChD.hstPsmT.uiBin2', 32),
    ('uint:32', 'ChLogEntry_ChD.hstPsmT.uiBin3', 32),
    ('uint:32', 'ChLogEntry_ChD.hstPsmT.uiBin4', 32),
  #StdHst hstPwr
    ('uint:32', 'ChLogEntry_ChD.hstPwr.uiBin0', 32),
    ('uint:32', 'ChLogEntry_ChD.hstPwr.uiBin1', 32),
    ('uint:32', 'ChLogEntry_ChD.hstPwr.uiBin2', 32),
    ('uint:32', 'ChLogEntry_ChD.hstPwr.uiBin3', 32),
    ('uint:32', 'ChLogEntry_ChD.hstPwr.uiBin4', 32),
  ('uint:16', 'ChLogEntry_ChD.usMinLoadZ1', 16),
  ('uint:16', 'ChLogEntry_ChD.usMaxLoadZ1', 16),
  ('uint:32', 'ChLogEntry_ChD.Res1', 32),


#DvcDebug debug
  ('uint:1', 'debug.bWriteFailure', 1),
  ('uint:1', 'debug.bInvalidChksum', 1),
  ('uint:1', 'debug.bMissingTag', 1),
  ('uint:1', 'debug.bRes3', 1),
  ('uint:1', 'debug.bRes4', 1),
  ('uint:1', 'debug.bRes5', 1),
  ('uint:1', 'debug.bRes6', 1),
  ('uint:1', 'debug.bRes7', 1),
  ('uint:8', 'debug.ucRes1', 8),
  ('uint:8', 'debug.ucRes2', 8),
  ('uint:8', 'debug.ucRes3', 8),
('uint:32', 'uiCritPos', 32),
('uint:32', 'uiServPos', 32)]

bitStructIter = iter(bitStruct)
# print type(bitStruct)
# print type(bitStructIter)