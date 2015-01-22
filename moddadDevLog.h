typedef enum
{
  E_LOG_FLASH_ERROR,
  E_LOG_ASSERT,
  E_LOG_RESERVED_ERROR
} eLogValueType;
typedef struct tagDvcServBits
{
  unsigned int bPsmFault :1;
  unsigned int bRes1 :1;
  unsigned int bRes2 :1;
  unsigned int bRes3 :1;
  unsigned int bRes4 :1;
  unsigned int bRes5 :1;
  unsigned int bRes6 :1;
  unsigned int bRes7 :1;
  unsigned int ucRes0 :8;
  unsigned int ucRes1 :8;
  unsigned int ucRes2 :8;
} DvcServBits;
typedef struct tagChServBits
{
  unsigned int bFuse :1;
  unsigned int bDac :1;
  unsigned int bRes8 :1;
  unsigned int bRes3 :1;
  unsigned int bRes4 :1;
  unsigned int bRes5 :1;
  unsigned int bRes6 :1;
  unsigned int bRes7 :1;
  unsigned int ucRes0 :8;
  unsigned int ucRes1 :8;
  unsigned int ucRes2 :8;
} ChServBits;
typedef struct tagStdHst
{
  unsigned int uiBin0;
  unsigned int uiBin1;
  unsigned int uiBin2;
  unsigned int uiBin3;
  unsigned int uiBin4;
} StdHst;
typedef struct tagDvcMiscBits
{
  unsigned int bFlash :1;
  unsigned int bAudioNok :1;
  unsigned int bAudioClk :1;
  unsigned int bPAL :1;
  unsigned int bTemp :1;
  unsigned int bAssert :1;
  unsigned int bPsmStatus :1;
  unsigned int bSlotTemp :1;
  unsigned int bSenseWarning :1;
  unsigned int ucRes0 :7;
  unsigned int ucRes1 :8;
  unsigned int ucRes2 :8;
} DvcMiscBits;
typedef struct tagGlobLogEntry
{
  unsigned int uiAccLife;
  unsigned int uiRes1;
  unsigned int uiAccRst;
  unsigned int uiAccEntry;
  unsigned int uiAccTFault;
  unsigned int uiAccAssert;
  unsigned int uiLifeMaxT;
  StdHst hstPsmT;
  StdHst hstPwr;
  unsigned int uiPAL0;
   unsigned int uiPAL1;
   unsigned int uiPAL2;
  unsigned int ucPsmPeakTemp :8;
  unsigned int ucPsmAvgTemp :8;
  unsigned int ucMaxP :8;
  unsigned int ucAvgP :8;
  unsigned int bMsrInp :1;
  unsigned int Res :31;
  DvcServBits servBits;
  DvcMiscBits miscBits;
} GlobLogEntry;
typedef struct tagChLogEntry
{
  unsigned int ucPeakT :8;
  unsigned int ucAvgT :8;
  unsigned int ucPeakV :8;
  unsigned int ucAvgV :8;
  unsigned int ucPeakI :8;
  unsigned int ucAvgI :8;
  unsigned int ucMaxP :8;
  unsigned int ucAvgP :8;
  unsigned int ucMaxVC :8;
  unsigned int ucAvgVC :8;
  unsigned int ucPeakHR :8;
  unsigned int ucThermHR :8;
  unsigned int ucMaxAvgZ :8;
  unsigned int ucMinAvgZ :8;
  unsigned int ucMaxMag :8;
  unsigned int ucAvgMag :8;
  unsigned int bTemp :1;
  unsigned int bVcTemp :1;
  unsigned int bSmTemp :1;
  unsigned int bNoLoad :1;
  unsigned int bVhf :1;
  unsigned int bWrongSpkr :1;
  unsigned int bFewSpkr :1;
  unsigned int bCorrect :1;
  unsigned int bModPrecLow :1;
  unsigned int bTempW1 :1;
  unsigned int bRes11 :1;
  unsigned int bMoreSpkr :1;
  unsigned int bVcTempW :1;
  unsigned int bSmTempW :1;
  unsigned int bUncLoad :1;
  unsigned int bNotvLoad :1;
  unsigned int bNoLdPrst :1;
  unsigned int bULim :1;
  unsigned int bILim :1;
  unsigned int bRes13 :1;
  unsigned int bACL :1;
  unsigned int bRes12 :1;
  unsigned int bShortc :1;
  unsigned int bLiveNotStarted :1;
  unsigned int bRes3 :1;
  unsigned int bRes4 :1;
  unsigned int bRes5 :1;
  unsigned int bRes6 :1;
  unsigned int bRes7 :1;
  unsigned int bRes8 :1;
  unsigned int bRes9 :1;
  unsigned int bRes10 :1;
  ChServBits servBits;
  unsigned int uiAccWh;
  unsigned int uiAccTFault;
  StdHst hstPsmT;
  StdHst hstPwr;
  unsigned int usRes0 :16;
  unsigned int usPtgZ :16;
  unsigned int Res1;
} ChLogEntry;
typedef struct tagDvcDebug
{
  unsigned int bWriteFailure :1;
  unsigned int bInvalidChksum :1;
  unsigned int bMissingTag :1;
  unsigned int bRes3 :1;
  unsigned int bRes4 :1;
  unsigned int bRes5 :1;
  unsigned int bRes6 :1;
  unsigned int bRes7 :1;
  unsigned int ucRes1 :8;
  unsigned int ucRes2 :8;
  unsigned int ucRes3 :8;
} DvcDebug;
typedef struct tagLogEntry
{
  unsigned int ucTag0 :8;
  unsigned int ucTag1 :8;
  unsigned int ucTag2 :8;
  unsigned int ucChksum :8;
  uint32_t ucVer;
  uint32_t uiTimestamp;
  uint32_t uiLogType;
  uint32_t uiLogPos;
  GlobLogEntry global;
  ChLogEntry ch[4];
  DvcDebug debug;
  uint32_t uiCritPos;
  uint32_t uiServPos;
} LogEntry;
int LOG_Scheduler(void* pThis);
void LOG_Init(void* pThis);
void LOG_ForceEntry(void* pThis);
void LOG_SetUpdateRate(unsigned int uiUpdateRate, void* pThis);
void LOG_SetTime(unsigned int uiTime);
void LOG_SetValue(eLogValueType logValueType, unsigned int uiLogValue);
void LOG_CreateServiceTag(void);
