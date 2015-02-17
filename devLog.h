#ifndef __DEVLOG_H__
#define __DEVLOG_H__

/*******************************************************************************
**
** FILE         :  devLog.h
**
** CREATED      :  PEKRI, 2007-01-08
**
** DESCRIPTION  :  
**
** COPYRIGHT    :  2007 TC.GROUP
**
*******************************************************************************/
//#include "scoretypes.h"

//#include "Shared/Params/Fw_New/log_ext_conf.h"


#ifndef NUM_CHANNELS
#define NUM_CHANNELS 4
#endif

typedef enum 
{
  E_LOG_FLASH_ERROR,
  E_LOG_ASSERT,
  E_LOG_RESERVED_ERROR
} eLogValueType;

typedef struct tagDvcServBits
{
#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int  ucRes2        :8;  
  unsigned int  ucRes1        :8;  
  unsigned int  ucRes0        :8;  
#ifdef P51_PSUMON
/// P51MONDATA
  unsigned int   unNeedsService       :4;  //The PSU needs service. A Power cycle is needed to recover if possible.
                                  //  0  -  No error, normal mode
                                  //  1  -  The PSU did not get the PFC state OK signal after turning on the PFC in three attempts
                                  //  2  -  The PSU did not get the DC state OK signal after turning on the DC/DC in three attempts
                                  //  3  -  The PFC output voltage did not reach the level where the DC/DC should be turned on within the required time
                                  //  4  -  Communication with DICO was lost during 1.5 seconds
                                  //  5  -  The PSU A/D interrupts are not running 
                                  //  6  -  Sensor fault is detected on a PSU temp sensor
                                  //  7  -  Board Id Fault
                                  // 8-15 -  TBD
#else
  unsigned int   bRes7           :1;
  unsigned int   bRes6           :1;  
  unsigned int   bRes5           :1;
  unsigned int   bRes4          :1;
#endif
  unsigned int   bRes3          :1;  
  unsigned int   bRes2          :1;
  unsigned int   bRes1          :1;
  unsigned int   bPsmFault      :1;// Power failure
#else
  unsigned int   bPsmFault      :1;
  unsigned int   bRes1          :1;
  unsigned int   bRes2          :1;
  unsigned int   bRes3          :1;  

#ifdef P51_PSUMON
/// P51MONDATA
  unsigned int   unNeedsService       :4;  //The PSU needs service. A Power cycle is needed to recover if possible.
#else
  unsigned int   bRes4          :1;
  unsigned int   bRes5           :1;
  unsigned int   bRes6           :1;  
  unsigned int   bRes7           :1;
#endif
  unsigned int  ucRes0        :8;  
  unsigned int  ucRes1        :8;  
  unsigned int  ucRes2        :8;  
#endif
} DvcServBits;

typedef struct tagChServBits
{

#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int  ucRes2        :8;
  unsigned int  ucRes1        :8;  
  unsigned int  ucRes0        :8;    
  unsigned int   bRes7           :1;  
  unsigned int   bRes6           :1;  
  unsigned int   bRes5           :1;
  unsigned int   bRes4          :1;
  unsigned int   bRes3          :1;  
  unsigned int  bRes8          :1;
  unsigned int   bDac          :1;// DAC config at bootup failed
  unsigned int  bFuse          :1;// Fuse blown    
#else  
  unsigned int  bFuse          :1;  
  unsigned int   bDac          :1;
  unsigned int  bRes8          :1;
  unsigned int   bRes3          :1;  
  unsigned int   bRes4          :1;
  unsigned int   bRes5           :1;
  unsigned int   bRes6           :1;  
  unsigned int   bRes7           :1;//_
  unsigned int  ucRes0        :8;  
  unsigned int  ucRes1        :8;  
  unsigned int  ucRes2        :8;    
#endif
} ChServBits;

typedef struct tagStdHst          
{                              // Example:  
  unsigned int  uiBin0;        // 0 - 20% counter, 50-60%
  unsigned int  uiBin1;        // 20- 40% counter, 60-70%
  unsigned int  uiBin2;        // 40- 60% counter, 70-80%
  unsigned int  uiBin3;        // 60- 80% counter, 80-90%
  unsigned int  uiBin4;        // 80-100% counter, 90-100%
} StdHst;                      // 20 bytes

typedef struct tagDvcMiscBits
{
#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
/*  unsigned int  ucRes2        :8;  
  unsigned int  ucRes1        :8;  
*/
  // ======>
  // #535: New assignment for bit in ucRes0: Sense warning -- When Usense=0 and Isense=0 for all channels in power state on
  // The suspected cause may be that the floating sense ADC supply has a fault
  
#ifdef P51_PSUMON
/// P51MONDATA
  unsigned int   nMainsLowFault  :1;  // Mains under voltage (RMS)
  unsigned int   nMainsHighFault  :1;  // Mains over voltage (RMS)
  unsigned int   nMainsHighFaultPeak  :1;  // Mains over voltage (Peak)
  unsigned int   nPowerProtect  :1;  // Lost HW Power good forced the PSU to turn off
  unsigned int   nUVL  :1;  // Mains current limit due to Mains Under Voltage
  unsigned int   nBEL  :1;  // Mains current limit due to Fuse setting
  unsigned int   nATL  :1;  // Amplifier temperature limit
  unsigned int   nPTL  :1;  // PSU temperature limit

  unsigned int   nPALP51  :1;  // Mains current limit due to input power limit in P51
  unsigned int   nCheckACMains  :1;  // PFC over voltage was tripped
  unsigned int   nPSUSafeMode  :1;  // P51 PSU is in safe mode
  unsigned int   nMainsGlitch  :1;  // Mains voltage glitch
  unsigned int  ucRes1        :4;  

  unsigned int  ucRes0        :6;
  unsigned int   nTempWarn        :1;  // Temp high warning (See bTemp above for PSU Temp high fault)
  
#else
  unsigned int  ucRes2        :8;  
  unsigned int  ucRes1        :8;  
  unsigned int  ucRes0        :7;    
#endif
  unsigned int  bSenseWarning  :1; ///< Active if Usense=0 and Isense=0 for all channels and power state is ON 
  // <======
  unsigned int   bSlotTemp       :1; // Slot/compartment temperature fault
  unsigned int   bPsmStatus     :1;  // Power on/off, user preference not the "real" value
  unsigned int   bAssert         :1; // Assert flag
  unsigned int   bTemp          :1; // PSM Temperature fault
  unsigned int   bPAL          :1; // PAL (ILim PSM)  
  unsigned int   bAudioClk      :1; // Audio clocks lost  
  unsigned int   bAudioNok      :1; // Audio not OK
  unsigned int   bFlash        :1; // Flash failure  
#else  
  unsigned int   bFlash        :1;
  unsigned int   bAudioNok      :1;
  unsigned int   bAudioClk      :1;  
  unsigned int   bPAL          :1;  
  unsigned int   bTemp          :1;
  unsigned int   bAssert         :1;
  unsigned int   bPsmStatus     :1;  
  unsigned int   bSlotTemp       :1; // Slot/compartment temperature fault
  // ======>
  // #535: New assignment for bit 12: Sense warning -- When Usense=0 and Isense=0 for all channels in power state on
  // The suspected cause may be that the floating sense ADC supply has a fault
  unsigned int  bSenseWarning  :1; ///< Active if Usense=0 and Isense=0 for all channels and power state is ON 
#ifdef P51_PSUMON

/// P51MONDATA
  unsigned int   nTempWarn        :1;  // Temp high warning (See bTemp above for PSU Temp high fault)
  unsigned int  ucRes0        :6;

  unsigned int  ucRes1        :4;  
  unsigned int   nMainsGlitch  :1;  // Mains voltage glitch    
  unsigned int   nPSUSafeMode  :1;  // P51 PSU is in safe mode
  unsigned int   nCheckACMains  :1;  // PFC over voltage was tripped
  unsigned int   nPALP51  :1;  // Mains current limit due to input power limit in P51
  
  unsigned int   nPTL  :1;  // PSU temperature limit
  unsigned int   nATL  :1;  // Amplifier temperature limit
  unsigned int   nBEL  :1;  // Mains current limit due to Fuse setting
  unsigned int   nUVL  :1;  // Mains current limit due to Mains Under Voltage
  unsigned int   nPowerProtect  :1;  // Lost HW Power good forced the PSU to turn off
  unsigned int   nMainsHighFaultPeak  :1;  // Mains over voltage (Peak)
  unsigned int   nMainsHighFault  :1;  // Mains over voltage (RMS)
  unsigned int   nMainsLowFault  :1;  // Mains under voltage (RMS)
/////////////////
#else
  unsigned int  ucRes0        :7;  
/// P51MONDATA
  unsigned int  ucRes1        :8;  
  unsigned int  ucRes2        :8;
/////////////////
#endif
/// P51MONDATA
/*  unsigned int  ucRes1        :8;  
  unsigned int  ucRes2        :8;  */
/////////////////
#endif
} DvcMiscBits;

typedef struct tagGlobLogEntry 
{
  // Lifetime logs (28 bytes)
  unsigned int   uiAccLife;    // The total time the device has been powered  
  unsigned int   uiRes1;        // 
  unsigned int   uiAccRst;      // The total number of power cycles
  unsigned int  uiAccEntry;    // Consecutive entry number
  unsigned int  uiAccTFault;  // Total number of temperature faults
  unsigned int  uiAccAssert;  // Total number of asserts
  unsigned int   uiLifeMaxT;    // Lifetime highest temperature 12
  
  // Histograms (40 bytes)
  StdHst        hstPsmT;      // Temperature histogram (not implemented)
  StdHst        hstPwr;        // Power histogram (not implemented)
 
  // Statistical (12 bytes)
#ifdef P51_PSUMON
  #ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int  uiPsuMaxMainsCurr:  8;  // Old PAL0:8 - Max PSU mains RMS input current in percent of max (42A)
  unsigned int  uiPsuMinMainsVolt:  8;  // Old PAL0:8 - Min PSU mains RMS input voltage in Volt
  unsigned int  uiPsuAvgMainsVolt:  8;  // Old PAL0:8 - Average PSU mains RMS input voltage in Volt
  unsigned int  uiPsuMaxMainsVolt:  8;  // Old PAL0:8 - Max PSU mains RMS input voltage in Volt
  unsigned int  uiMaxPLimReduct:    8;  // Old PAL1:8 - Max degree of power limit reduction 0-100%
  unsigned int  uiPfcAvgOutVolt:    8;  // Old PAL1:8 - Average PFC output voltage in percent of max (400V)
  unsigned int  uiPfcMinOutVolt:    8;  // Old PAL1:8 - Min PFC output voltage in percent of max (400V)
  unsigned int  uiPsuAvgMainsCurr:  8;  // Old PAL1:8 - Average PSU mains RMS input current in percent of max (42A)
  unsigned int  uiPsuTempSensor:    8;  // Old PAL2:8 - Highest PSU temperature sensor id
  unsigned int  uiPsuMaxP:          8;  // Old PAL2:8 - Max PSU input power in percent of PeakTotalPower
  unsigned int  uiPsuAvgP:          8;  // Old PAL2:8 - Average PSU input power in percent of AverageTotalPower
  unsigned int  uiAvgPLimReduct:    8;  // Old PAL2:8 - Average degree of power limit reduction 0-100%
  #else  
  unsigned int  uiPsuMaxMainsVolt:  8;
  unsigned int  uiPsuAvgMainsVolt:  8;
  unsigned int  uiPsuMinMainsVolt:  8;
  unsigned int  uiPsuMaxMainsCurr:  8;
  unsigned int  uiPsuAvgMainsCurr:  8;
  unsigned int  uiPfcMinOutVolt:    8;
  unsigned int  uiPfcAvgOutVolt:    8;
  unsigned int  uiMaxPLimReduct:    8;
  unsigned int  uiAvgPLimReduct:    8;
  unsigned int  uiPsuAvgP:          8;
  unsigned int  uiPsuMaxP:          8;
  unsigned int  uiPsuTempSensor:    8;
  #endif  
#else
  unsigned int   uiPAL0;        // Sw-PAL 0
   unsigned int   uiPAL1;        // Sw-PAL 1
   unsigned int   uiPAL2;        // Sw-PAL 2
#endif
  
  // Statistical (4 bytes)

#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int  ucAvgP         :8;// Average power
  unsigned int  ucMaxP         :8;// Maximum power
  unsigned int   ucPsmAvgTemp   :8;// Average PSM temperature    
  unsigned int   ucPsmPeakTemp  :8;// Peak PSM temperature
#else  
  unsigned int   ucPsmPeakTemp  :8;
  unsigned int   ucPsmAvgTemp   :8;  
  unsigned int  ucMaxP         :8;
  unsigned int  ucAvgP         :8;
#endif  

  // Bits (4 bytes)
#ifdef BAJS 
  unsigned int  accWatisar     :8;
  unsigned int  Res            :23;
  unsigned int  bMsrInp        :1;  // Load monitor measurement in progress
#else    
  unsigned int  bMsrInp        :1;
  unsigned int  Res            :23;  
  unsigned int  accWatisar     :8;
#endif
    
  // Service (4 bytes)
  DvcServBits    servBits;
  
  // Misc events (4 bytes)
  DvcMiscBits    miscBits;
  
} GlobLogEntry;              // 96 bytes


typedef struct tagChLogEntry
{
  // Statistical (16 bytes)
#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int  ucAvgV      :8;// Average voltage
  unsigned int  ucPeakV      :8;// Peak voltage
  unsigned int  ucAvgT      :8;// Average temperature
  unsigned int  ucPeakT      :8;// Peak temperature

  unsigned int  ucAvgP       :8;// Average power
  unsigned int  ucMaxP       :8;// Max power
  unsigned int  ucAvgI       :8;// Average current
  unsigned int  ucPeakI     :8;// Peak current

  unsigned int  ucThermHR   :8;// Thermal headroom
  unsigned int  ucPeakHR     :8;// Peak thermal headroom
#ifdef USE_LML_SPEAKERSAFE
  unsigned int  ucAvgVC     :8;// Average voice coil temperature
  unsigned int  ucMaxVC     :8;// Max voice coil temperature

  unsigned int  ucAvgMag    :8;// Average magnet temperature
  unsigned int  ucMaxMag    :8;// Max magnet temperature
#else
  unsigned int  ucAvgVC_unused :8;// Average voice coil temperature
  unsigned int  ucMaxVC_unused :8;// Max voice coil temperature

  unsigned int  ucMinAvgZ_H :8;// Upper word of minimum average impedance.  Scaled up by 10.
  unsigned int  ucMaxAvgZ_H :8;// Upper word of maximum average impedance.  Scaled up by 10.
#endif
  unsigned int  ucMinAvgZ   :8;// Minimum average impedance. Scaled up by 10.
  unsigned int  ucMaxAvgZ   :8;// Maximum average impedance. Scaled up by 10.
#else
  unsigned int  ucPeakT      :8;
  unsigned int  ucAvgT      :8;
  unsigned int  ucPeakV      :8;
  unsigned int  ucAvgV      :8;

  unsigned int  ucPeakI     :8;
  unsigned int  ucAvgI       :8;
  unsigned int  ucMaxP       :8;
  unsigned int  ucAvgP       :8;

#ifdef USE_LML_SPEAKERSAFE
  unsigned int  ucMaxVC     :8;
  unsigned int  ucAvgVC     :8;
#else
  unsigned int  ucMaxVC_unused     :8;
  unsigned int  ucAvgVC_unused     :8;
#endif
  unsigned int  ucPeakHR     :8;
  unsigned int  ucThermHR   :8;

  unsigned int  ucMaxAvgZ   :8;
  unsigned int  ucMinAvgZ   :8;
#ifdef USE_LML_SPEAKERSAFE
  unsigned int  ucMaxMag    :8;
  unsigned int  ucAvgMag    :8;
#else
  unsigned int  ucMaxAvgZ_H :8;
  unsigned int  ucMinAvgZ_H :8;
#endif // USE_LML_SPEAKERSAFE
#endif
#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int  bRes10          :1;  
  unsigned int  bRes9            :1;
  unsigned int  bRes8            :1;
  unsigned int  bRes7            :1;
  unsigned int  bRes6            :1;
  unsigned int  bRes5            :1;
  unsigned int  bRes4            :1;    
  unsigned int  bRes3            :1;    
  
  unsigned int  bLoadPilotActive  :1;
  unsigned int  bShortc          :1;// Short circuit
  unsigned int  bRes12          :1;// Sw-PAL
  unsigned int  bACL            :1;
  unsigned int  bRes13          :1;
  unsigned int  bILim            :1;// I Limiter
  unsigned int  bULim            :1;// U Limiter  
  unsigned int  bNoLdPrst        :1;// No load monitor preset

  unsigned int  bNotvLoad        :1;// Load not verified 
  unsigned int  bUncLoad        :1;// Uncertain about load
#ifdef USE_LML_SPEAKERSAFE
  unsigned int  bSmTempW        :1;// Speaker magnet temperature warning
  unsigned int  bVcTempW        :1;// Voice coil temperature warning
#else
  unsigned int  bSpkrShortedW        :1;// Speaker shorted
  unsigned int  bSpkrDamagedW        :1;// Speaker damaged
#endif
  unsigned int  bMoreSpkr        :1;// More speakers
  unsigned int  bRes11          :1;// Former Amplifier temperature warning level 2
  unsigned int  bTempW1          :1;// Amplifier temperature warning  
  unsigned int  bModPrecLow      :1;// Model precision low
  
  unsigned int  bCorrect        :1;// Correct speakers
  unsigned int  bFewSpkr        :1;// Fewer speakers
  unsigned int  bWrongSpkr      :1;// Wrong type of speaker
  unsigned int  bVhf            :1;// Vhf fault
  unsigned int  bNoLoad          :1;// Channel has no load 
  unsigned int  bSmTemp          :1;// Speaker magnet temperature fault
  unsigned int  bVcTemp          :1;// Voice coil temperature fault
  unsigned int  bTemp            :1;// Amplifier temperature fault

#else    
  unsigned int  bTemp            :1;
  unsigned int  bVcTemp          :1;
  unsigned int  bSmTemp          :1;
  unsigned int  bNoLoad          :1;
  unsigned int  bVhf            :1;
  unsigned int  bWrongSpkr      :1;
  unsigned int  bFewSpkr        :1;
  unsigned int  bCorrect        :1;//_
  unsigned int  bModPrecLow      :1;
  unsigned int  bTempW1          :1;
  unsigned int  bRes11          :1;
  unsigned int  bMoreSpkr        :1;
#ifdef USE_LML_SPEAKERSAFE
  unsigned int  bVcTempW        :1;
  unsigned int  bSmTempW        :1;
#else
  unsigned int  bSpkrDamagedW        :1;
  unsigned int  bSpkrShortedW        :1;
#endif
  unsigned int  bUncLoad        :1;
  unsigned int  bNotvLoad        :1;//_
  unsigned int  bNoLdPrst        :1;
  unsigned int  bULim            :1;
  unsigned int  bILim            :1;
  unsigned int  bRes13          :1;
  unsigned int  bACL            :1;
  unsigned int  bRes12          :1;
  unsigned int  bShortc          :1;
  unsigned int  bLoadPilotActive  :1;//_
  unsigned int  bRes3            :1;
  unsigned int  bRes4            :1;
  unsigned int  bRes5            :1;
  unsigned int  bRes6            :1;
  unsigned int  bRes7            :1;
  unsigned int  bRes8            :1;
  unsigned int  bRes9            :1;
  unsigned int  bRes10          :1;   // 4 bytes
#endif
  
  // Service (4 bytes)
  ChServBits    servBits;    // Channel needs service
    
  // Lifetime logs (8 bytes)
  unsigned int  uiAccWh;     // Total lifetime energy (Wh) 
  unsigned int  uiAccTFault;// Total temperature faults
    
  // Histograms (40 bytes)
  StdHst        hstPsmT;     // Temperature histogram (not implemented)
  StdHst        hstPwr;       // Power histogram (not implemented)
  
  // PTG implementation changes - Need a new impedance reading that supports at least the range 1-600 ohm
//  unsigned int  Res0;
#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int  usPtgZ0          :16;  // Measured load impedance  where 1-60000 corresponds to 0.1-6000.0 ohm
  unsigned int  usPtgZ1          :16;
#else
  unsigned int  usPtgZ1          :16;
  unsigned int  usPtgZ0          :16;  // Measured load impedance  where 1-60000 corresponds to 0.1-6000.0 ohm
#endif
  unsigned int  Res1;
} ChLogEntry;                // 80 bytes


typedef struct tagDvcDebug
{
#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int  ucRes3            :8;  
  unsigned int  ucRes2            :8;  
  unsigned int  ucRes1            :8;  
  unsigned int   bRes7               :1;
  unsigned int   bRes6               :1;  
  unsigned int   bRes5               :1;
  unsigned int   bRes4              :1;
  unsigned int   bRes3              :1;  
  unsigned int   bMissingTag        :1;// Misc debug info  
  unsigned int   bInvalidChksum    :1;
  unsigned int   bWriteFailure      :1;
#else
  unsigned int   bWriteFailure      :1;
  unsigned int   bInvalidChksum    :1;
  unsigned int   bMissingTag        :1;  
  unsigned int   bRes3              :1;  
  unsigned int   bRes4              :1;
  unsigned int   bRes5               :1;
  unsigned int   bRes6               :1;  
  unsigned int   bRes7               :1;
  unsigned int  ucRes1            :8;
  unsigned int  ucRes2            :8;
  unsigned int  ucRes3            :8;
#endif
} DvcDebug;                  // 4 bytes


typedef struct tagLogEntry
{
#ifdef BAJS // Bit fields is interpreted differently in WIN32 and SHARC environment
  unsigned int ucChksum  :8;  // Checksum
  unsigned int ucTag2    :8;  // 'G'
  unsigned int ucTag1    :8;  // 'O'
  unsigned int ucTag0    :8;  // 'L'
#else
  unsigned int ucTag0    :8;  //  L
  unsigned int ucTag1    :8;  //  O
  unsigned int ucTag2    :8;  //  G
  unsigned int ucChksum  :8;  //  4 bytes
#endif
  uint32_t     ucVer;       //  Log version - 4 bytes
  uint32_t     uiTimestamp; //  Timestamp   - 4 bytes
  uint32_t     uiLogType;    //  NORMAL(1) CRITICAL(2) SERVICE(4)
  uint32_t     uiLogPos;    // Header 20 bytes
  GlobLogEntry global;      // 96  bytes
  ChLogEntry   ch[NUM_CHANNELS];          // 80  bytes * 4
  DvcDebug     debug;        // 4    bytes
  uint32_t     uiCritPos;    // 4    bytes 
  uint32_t     uiServPos;    // 4    bytes
} LogEntry;                  // 448 bytes in total


void LOG_Init(void* pThis);
void LOG_ForceEntry(void* pThis);
void LOG_SetUpdateRate(unsigned int uiUpdateRate, void* pThis);
void LOG_SetTime(unsigned int uiTime);
void LOG_SetValue(eLogValueType logValueType, unsigned int uiLogValue);
void LOG_CreateServiceTag(void);

#ifdef P51_PSUMON
void LOG_DisableSessionLogging();
#endif

#endif //__DEVLOG_H__

