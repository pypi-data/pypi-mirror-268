from enum import Enum


# noinspection SpellCheckingInspection
class All(Enum):
	"""1 Members, ALL ... ALL"""
	ALL = 0


# noinspection SpellCheckingInspection
class Amplification(Enum):
	"""4 Members, HIGH ... MEDium"""
	HIGH = 0
	LOW = 1
	MAXimum = 2
	MEDium = 3


# noinspection SpellCheckingInspection
class ArbFile(Enum):
	"""3 Members, ABSPath ... TRUTh"""
	ABSPath = 0
	DEF = 1
	TRUTh = 2


# noinspection SpellCheckingInspection
class ArbSegmentsMode(Enum):
	"""3 Members, AUTO ... CSEamless"""
	AUTO = 0
	CONTinuous = 1
	CSEamless = 2


# noinspection SpellCheckingInspection
class AveragingMode(Enum):
	"""2 Members, LINear ... LOGarithmic"""
	LINear = 0
	LOGarithmic = 1


# noinspection SpellCheckingInspection
class BasebandMode(Enum):
	"""3 Members, ARB ... DTONe"""
	ARB = 0
	CW = 1
	DTONe = 2


# noinspection SpellCheckingInspection
class CcdfMode(Enum):
	"""2 Members, POWer ... STATistic"""
	POWer = 0
	STATistic = 1


# noinspection SpellCheckingInspection
class Detector(Enum):
	"""6 Members, AUTopeak ... SAMPle"""
	AUTopeak = 0
	AVERage = 1
	MAXPeak = 2
	MINPeak = 3
	RMS = 4
	SAMPle = 5


# noinspection SpellCheckingInspection
class DetectorBasic(Enum):
	"""2 Members, PEAK ... RMS"""
	PEAK = 0
	RMS = 1


# noinspection SpellCheckingInspection
class DeviceMode(Enum):
	"""3 Members, M2X2 ... NONE"""
	M2X2 = 0
	M4X4 = 1
	NONE = 2


# noinspection SpellCheckingInspection
class DeviceType(Enum):
	"""2 Members, NONE ... Z24"""
	NONE = 0
	Z24 = 1


# noinspection SpellCheckingInspection
class DigitalFilterType(Enum):
	"""5 Members, BANDpass ... WCDMa"""
	BANDpass = 0
	CDMA = 1
	GAUSs = 2
	TDSCdma = 3
	WCDMa = 4


# noinspection SpellCheckingInspection
class ExtPwrSensorAvgMode(Enum):
	"""3 Members, MANual ... RES"""
	MANual = 0
	NSR = 1
	RES = 2


# noinspection SpellCheckingInspection
class FileSave(Enum):
	"""3 Members, OFF ... ONLY"""
	OFF = 0
	ON = 1
	ONLY = 2


# noinspection SpellCheckingInspection
class FilterCriteria(Enum):
	"""1 Members, LOSupport ... LOSupport"""
	LOSupport = 0


# noinspection SpellCheckingInspection
class FilterType(Enum):
	"""5 Members, B10Mhz ... NYQuist"""
	B10Mhz = 0
	B1MHz = 1
	GAUSs = 2
	NY1Mhz = 3
	NYQuist = 4


# noinspection SpellCheckingInspection
class GeneratorState(Enum):
	"""8 Members, ADJusted ... RDY"""
	ADJusted = 0
	AUTonomous = 1
	COUPled = 2
	INValid = 3
	OFF = 4
	ON = 5
	PENDing = 6
	RDY = 7


# noinspection SpellCheckingInspection
class IncTransition(Enum):
	"""6 Members, IMMediate ... WMA4"""
	IMMediate = 0
	RMARker = 1
	WMA1 = 2
	WMA2 = 3
	WMA3 = 4
	WMA4 = 5


# noinspection SpellCheckingInspection
class InstrumentType(Enum):
	"""2 Members, PROTocol ... SIGNaling"""
	PROTocol = 0
	SIGNaling = 1


# noinspection SpellCheckingInspection
class IqFormat(Enum):
	"""2 Members, IQ ... RPHI"""
	IQ = 0
	RPHI = 1


# noinspection SpellCheckingInspection
class IqRecBypass(Enum):
	"""3 Members, BIT ... ON"""
	BIT = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class ListIncrement(Enum):
	"""5 Members, ACYCles ... USER"""
	ACYCles = 0
	DTIMe = 1
	MEASurement = 2
	TRIGger = 3
	USER = 4


# noinspection SpellCheckingInspection
class ListSubMode(Enum):
	"""6 Members, AUTO ... STEP"""
	AUTO = 0
	BBGenerator = 1
	BBMeasurement = 2
	OTHer = 3
	SINGle = 4
	STEP = 5


# noinspection SpellCheckingInspection
class LoLevel(Enum):
	"""3 Members, CORRect ... LOW"""
	CORRect = 0
	HIGH = 1
	LOW = 2


# noinspection SpellCheckingInspection
class LowHigh(Enum):
	"""2 Members, HIGH ... LOW"""
	HIGH = 0
	LOW = 1


# noinspection SpellCheckingInspection
class MagnitudeUnit(Enum):
	"""2 Members, RAW ... VOLT"""
	RAW = 0
	VOLT = 1


# noinspection SpellCheckingInspection
class MeasMode(Enum):
	"""3 Members, CCALibration ... OSHort"""
	CCALibration = 0
	OOPen = 1
	OSHort = 2


# noinspection SpellCheckingInspection
class MeasScenario(Enum):
	"""5 Members, CSPath ... UNDefined"""
	CSPath = 0
	MAIQ = 1
	MAPR = 2
	SALone = 3
	UNDefined = 4


# noinspection SpellCheckingInspection
class MeasurementMode(Enum):
	"""2 Members, NORMal ... TALignment"""
	NORMal = 0
	TALignment = 1


# noinspection SpellCheckingInspection
class NameStyle(Enum):
	"""3 Members, FQName ... NAME"""
	FQName = 0
	LNAMe = 1
	NAME = 2


# noinspection SpellCheckingInspection
class OffsetMode(Enum):
	"""2 Members, FIXed ... VARiable"""
	FIXed = 0
	VARiable = 1


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class PwrSensorResolution(Enum):
	"""4 Members, PD0 ... PD3"""
	PD0 = 0
	PD1 = 1
	PD2 = 2
	PD3 = 3


# noinspection SpellCheckingInspection
class Range(Enum):
	"""2 Members, FULL ... SUB"""
	FULL = 0
	SUB = 1


# noinspection SpellCheckingInspection
class RbwFilterType(Enum):
	"""2 Members, BANDpass ... GAUSs"""
	BANDpass = 0
	GAUSs = 1


# noinspection SpellCheckingInspection
class Repeat(Enum):
	"""2 Members, CONTinuous ... SINGleshot"""
	CONTinuous = 0
	SINGleshot = 1


# noinspection SpellCheckingInspection
class RepeatMode(Enum):
	"""2 Members, CONTinuous ... SINGle"""
	CONTinuous = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class ResourceState(Enum):
	"""8 Members, ACTive ... RUN"""
	ACTive = 0
	ADJusted = 1
	INValid = 2
	OFF = 3
	PENDing = 4
	QUEued = 5
	RDY = 6
	RUN = 7


# noinspection SpellCheckingInspection
class ResultStatus2(Enum):
	"""10 Members, DC ... ULEU"""
	DC = 0
	INV = 1
	NAV = 2
	NCAP = 3
	OFF = 4
	OFL = 5
	OK = 6
	UFL = 7
	ULEL = 8
	ULEU = 9


# noinspection SpellCheckingInspection
class RfConnector(Enum):
	"""163 Members, I11I ... RH8"""
	I11I = 0
	I13I = 1
	I15I = 2
	I17I = 3
	I21I = 4
	I23I = 5
	I25I = 6
	I27I = 7
	I31I = 8
	I33I = 9
	I35I = 10
	I37I = 11
	I41I = 12
	I43I = 13
	I45I = 14
	I47I = 15
	IFI1 = 16
	IFI2 = 17
	IFI3 = 18
	IFI4 = 19
	IFI5 = 20
	IFI6 = 21
	IQ1I = 22
	IQ3I = 23
	IQ5I = 24
	IQ7I = 25
	R10D = 26
	R11 = 27
	R11C = 28
	R11D = 29
	R12 = 30
	R12C = 31
	R12D = 32
	R12I = 33
	R13 = 34
	R13C = 35
	R14 = 36
	R14C = 37
	R14I = 38
	R15 = 39
	R16 = 40
	R17 = 41
	R18 = 42
	R21 = 43
	R21C = 44
	R22 = 45
	R22C = 46
	R22I = 47
	R23 = 48
	R23C = 49
	R24 = 50
	R24C = 51
	R24I = 52
	R25 = 53
	R26 = 54
	R27 = 55
	R28 = 56
	R31 = 57
	R31C = 58
	R32 = 59
	R32C = 60
	R32I = 61
	R33 = 62
	R33C = 63
	R34 = 64
	R34C = 65
	R34I = 66
	R35 = 67
	R36 = 68
	R37 = 69
	R38 = 70
	R41 = 71
	R41C = 72
	R42 = 73
	R42C = 74
	R42I = 75
	R43 = 76
	R43C = 77
	R44 = 78
	R44C = 79
	R44I = 80
	R45 = 81
	R46 = 82
	R47 = 83
	R48 = 84
	RA1 = 85
	RA2 = 86
	RA3 = 87
	RA4 = 88
	RA5 = 89
	RA6 = 90
	RA7 = 91
	RA8 = 92
	RB1 = 93
	RB2 = 94
	RB3 = 95
	RB4 = 96
	RB5 = 97
	RB6 = 98
	RB7 = 99
	RB8 = 100
	RC1 = 101
	RC2 = 102
	RC3 = 103
	RC4 = 104
	RC5 = 105
	RC6 = 106
	RC7 = 107
	RC8 = 108
	RD1 = 109
	RD2 = 110
	RD3 = 111
	RD4 = 112
	RD5 = 113
	RD6 = 114
	RD7 = 115
	RD8 = 116
	RE1 = 117
	RE2 = 118
	RE3 = 119
	RE4 = 120
	RE5 = 121
	RE6 = 122
	RE7 = 123
	RE8 = 124
	RF1 = 125
	RF1C = 126
	RF2 = 127
	RF2C = 128
	RF2I = 129
	RF3 = 130
	RF3C = 131
	RF4 = 132
	RF4C = 133
	RF4I = 134
	RF5 = 135
	RF5C = 136
	RF6 = 137
	RF6C = 138
	RF7 = 139
	RF7C = 140
	RF8 = 141
	RF8C = 142
	RF9C = 143
	RFAC = 144
	RFBC = 145
	RFBI = 146
	RG1 = 147
	RG2 = 148
	RG3 = 149
	RG4 = 150
	RG5 = 151
	RG6 = 152
	RG7 = 153
	RG8 = 154
	RH1 = 155
	RH2 = 156
	RH3 = 157
	RH4 = 158
	RH5 = 159
	RH6 = 160
	RH7 = 161
	RH8 = 162


# noinspection SpellCheckingInspection
class SelectMode(Enum):
	"""4 Members, EVAL ... SHORt"""
	EVAL = 0
	MATCh = 1
	OPEN = 2
	SHORt = 3


# noinspection SpellCheckingInspection
class SignalDirection(Enum):
	"""3 Members, RX ... TX"""
	RX = 0
	RXTX = 1
	TX = 2


# noinspection SpellCheckingInspection
class SignalSlope(Enum):
	"""2 Members, FEDGe ... REDGe"""
	FEDGe = 0
	REDGe = 1


# noinspection SpellCheckingInspection
class SignalSlopeExt(Enum):
	"""4 Members, FALLing ... RISing"""
	FALLing = 0
	FEDGe = 1
	REDGe = 2
	RISing = 3


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class SpanMode(Enum):
	"""2 Members, FSWeep ... ZSPan"""
	FSWeep = 0
	ZSPan = 1


# noinspection SpellCheckingInspection
class Statistic(Enum):
	"""4 Members, AVERage ... MINimum"""
	AVERage = 0
	CURRent = 1
	MAXimum = 2
	MINimum = 3


# noinspection SpellCheckingInspection
class TargetStateA(Enum):
	"""3 Members, OFF ... RUN"""
	OFF = 0
	RDY = 1
	RUN = 2


# noinspection SpellCheckingInspection
class TargetStateB(Enum):
	"""3 Members, OFF ... STOP"""
	OFF = 0
	RUN = 1
	STOP = 2


# noinspection SpellCheckingInspection
class TargetSyncState(Enum):
	"""2 Members, ADJusted ... PENDing"""
	ADJusted = 0
	PENDing = 1


# noinspection SpellCheckingInspection
class TimeSource(Enum):
	"""2 Members, MANual ... NTP"""
	MANual = 0
	NTP = 1


# noinspection SpellCheckingInspection
class Timing(Enum):
	"""2 Members, CENTered ... STEP"""
	CENTered = 0
	STEP = 1


# noinspection SpellCheckingInspection
class TransferMode(Enum):
	"""2 Members, ENABlemode ... REQuestmode"""
	ENABlemode = 0
	REQuestmode = 1


# noinspection SpellCheckingInspection
class Trigger(Enum):
	"""3 Members, CLEarlist ... OFF"""
	CLEarlist = 0
	GENeratelist = 1
	OFF = 2


# noinspection SpellCheckingInspection
class TriggerPowerMode(Enum):
	"""4 Members, ALL ... SWEep"""
	ALL = 0
	ONCE = 1
	PRESelect = 2
	SWEep = 3


# noinspection SpellCheckingInspection
class TriggerSequenceMode(Enum):
	"""2 Members, ONCE ... PRESelect"""
	ONCE = 0
	PRESelect = 1


# noinspection SpellCheckingInspection
class TxConnector(Enum):
	"""86 Members, I12O ... RH18"""
	I12O = 0
	I14O = 1
	I16O = 2
	I18O = 3
	I22O = 4
	I24O = 5
	I26O = 6
	I28O = 7
	I32O = 8
	I34O = 9
	I36O = 10
	I38O = 11
	I42O = 12
	I44O = 13
	I46O = 14
	I48O = 15
	IFO1 = 16
	IFO2 = 17
	IFO3 = 18
	IFO4 = 19
	IFO5 = 20
	IFO6 = 21
	IQ2O = 22
	IQ4O = 23
	IQ6O = 24
	IQ8O = 25
	R10D = 26
	R118 = 27
	R1183 = 28
	R1184 = 29
	R11C = 30
	R11D = 31
	R11O = 32
	R11O3 = 33
	R11O4 = 34
	R12C = 35
	R12D = 36
	R13C = 37
	R13O = 38
	R14C = 39
	R214 = 40
	R218 = 41
	R21C = 42
	R21O = 43
	R22C = 44
	R23C = 45
	R23O = 46
	R24C = 47
	R258 = 48
	R318 = 49
	R31C = 50
	R31O = 51
	R32C = 52
	R33C = 53
	R33O = 54
	R34C = 55
	R418 = 56
	R41C = 57
	R41O = 58
	R42C = 59
	R43C = 60
	R43O = 61
	R44C = 62
	RA18 = 63
	RB14 = 64
	RB18 = 65
	RC18 = 66
	RD18 = 67
	RE18 = 68
	RF18 = 69
	RF1C = 70
	RF1O = 71
	RF2C = 72
	RF3C = 73
	RF3O = 74
	RF4C = 75
	RF5C = 76
	RF6C = 77
	RF7C = 78
	RF8C = 79
	RF9C = 80
	RFAC = 81
	RFAO = 82
	RFBC = 83
	RG18 = 84
	RH18 = 85


# noinspection SpellCheckingInspection
class TxiMode(Enum):
	"""2 Members, IREPetition ... LENTry"""
	IREPetition = 0
	LENTry = 1


# noinspection SpellCheckingInspection
class UserDebugMode(Enum):
	"""2 Members, DEBug ... USER"""
	DEBug = 0
	USER = 1


# noinspection SpellCheckingInspection
class YesNoStatus(Enum):
	"""2 Members, NO ... YES"""
	NO = 0
	YES = 1


# noinspection SpellCheckingInspection
class ZeroingState(Enum):
	"""2 Members, FAILed ... PASSed"""
	FAILed = 0
	PASSed = 1
