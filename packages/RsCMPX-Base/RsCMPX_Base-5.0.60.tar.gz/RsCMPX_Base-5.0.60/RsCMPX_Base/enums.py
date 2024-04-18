from enum import Enum


# noinspection SpellCheckingInspection
class AdjustStatus(Enum):
	"""2 Members, ADJust ... NADJust"""
	ADJust = 0
	NADJust = 1


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
class BaseAdjState(Enum):
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
class BoxNumber(Enum):
	"""9 Members, BOX1 ... NAV"""
	BOX1 = 0
	BOX2 = 1
	BOX3 = 2
	BOX4 = 3
	BOX5 = 4
	BOX6 = 5
	BOX7 = 6
	BOX8 = 7
	NAV = 8


# noinspection SpellCheckingInspection
class ByteOrder(Enum):
	"""2 Members, NORMal ... SWAPped"""
	NORMal = 0
	SWAPped = 1


# noinspection SpellCheckingInspection
class CatalogFormat(Enum):
	"""2 Members, ALL ... WTIMe"""
	ALL = 0
	WTIMe = 1


# noinspection SpellCheckingInspection
class CmwCurrentStatus(Enum):
	"""6 Members, ERRor ... STBY"""
	ERRor = 0
	MCCNconnected = 1
	MCMW = 2
	PCINconnected = 3
	SALone = 4
	STBY = 5


# noinspection SpellCheckingInspection
class CmwMode(Enum):
	"""3 Members, GENerator ... STANdalone"""
	GENerator = 0
	LISTener = 1
	STANdalone = 2


# noinspection SpellCheckingInspection
class CmwSetStatus(Enum):
	"""3 Members, MCMW ... STBY"""
	MCMW = 0
	SALone = 1
	STBY = 2


# noinspection SpellCheckingInspection
class ColorSet(Enum):
	"""1 Members, DEF ... DEF"""
	DEF = 0


# noinspection SpellCheckingInspection
class CorrResult(Enum):
	"""4 Members, FAIL ... PASS"""
	FAIL = 0
	IPR = 1
	NCAP = 2
	PASS = 3


# noinspection SpellCheckingInspection
class DataFormat(Enum):
	"""8 Members, ASCii ... UINTeger"""
	ASCii = 0
	BINary = 1
	HEXadecimal = 2
	INTeger = 3
	OCTal = 4
	PACKed = 5
	REAL = 6
	UINTeger = 7


# noinspection SpellCheckingInspection
class DefaultUnitAngle(Enum):
	"""3 Members, DEG ... RAD"""
	DEG = 0
	GRAD = 1
	RAD = 2


# noinspection SpellCheckingInspection
class DefaultUnitCapacity(Enum):
	"""13 Members, AF ... UF"""
	AF = 0
	EXF = 1
	F = 2
	FF = 3
	GF = 4
	KF = 5
	MF = 6
	MIF = 7
	NF = 8
	PEF = 9
	PF = 10
	TF = 11
	UF = 12


# noinspection SpellCheckingInspection
class DefaultUnitCharge(Enum):
	"""13 Members, AC ... UC"""
	AC = 0
	C = 1
	EXC = 2
	FC = 3
	GC = 4
	KC = 5
	MC = 6
	MIC = 7
	NC = 8
	PC = 9
	PEC = 10
	TC = 11
	UC = 12


# noinspection SpellCheckingInspection
class DefaultUnitConductance(Enum):
	"""13 Members, ASIE ... USIE"""
	ASIE = 0
	EXSie = 1
	FSIE = 2
	GSIE = 3
	KSIE = 4
	MISie = 5
	MSIE = 6
	NSIE = 7
	PESie = 8
	PSIE = 9
	SIE = 10
	TSIE = 11
	USIE = 12


# noinspection SpellCheckingInspection
class DefaultUnitCurrent(Enum):
	"""18 Members, A ... UA"""
	A = 0
	AA = 1
	DBA = 2
	DBMA = 3
	DBNA = 4
	DBPA = 5
	DBUA = 6
	EXA = 7
	FA = 8
	GA = 9
	KA = 10
	MA = 11
	MAA = 12
	NA = 13
	PA = 14
	PEA = 15
	TA = 16
	UA = 17


# noinspection SpellCheckingInspection
class DefaultUnitEnergy(Enum):
	"""13 Members, AJ ... UJ"""
	AJ = 0
	EXJ = 1
	FJ = 2
	GJ = 3
	J = 4
	KJ = 5
	MIJ = 6
	MJ = 7
	NJ = 8
	PEJ = 9
	PJ = 10
	TJ = 11
	UJ = 12


# noinspection SpellCheckingInspection
class DefaultUnitFrequency(Enum):
	"""13 Members, AHZ ... UHZ"""
	AHZ = 0
	EXHZ = 1
	FHZ = 2
	GHZ = 3
	HZ = 4
	KHZ = 5
	MHZ = 6
	MIHZ = 7
	NHZ = 8
	PEHZ = 9
	PHZ = 10
	THZ = 11
	UHZ = 12


# noinspection SpellCheckingInspection
class DefaultUnitLenght(Enum):
	"""13 Members, AM ... UM"""
	AM = 0
	EXM = 1
	FM = 2
	GM = 3
	KM = 4
	M = 5
	MAM = 6
	MM = 7
	NM = 8
	PEM = 9
	PM = 10
	TM = 11
	UM = 12


# noinspection SpellCheckingInspection
class DefaultUnitPower(Enum):
	"""19 Members, AW ... W"""
	AW = 0
	DBC = 1
	DBMW = 2
	DBNW = 3
	DBPW = 4
	DBUW = 5
	DBW = 6
	EXW = 7
	FW = 8
	GW = 9
	KW = 10
	MIW = 11
	MW = 12
	NW = 13
	PEW = 14
	PW = 15
	TW = 16
	UW = 17
	W = 18


# noinspection SpellCheckingInspection
class DefaultUnitResistor(Enum):
	"""13 Members, AOHM ... UOHM"""
	AOHM = 0
	EXOHm = 1
	FOHM = 2
	GOHM = 3
	KOHM = 4
	MIOHm = 5
	MOHM = 6
	NOHM = 7
	OHM = 8
	PEOHm = 9
	POHM = 10
	TOHM = 11
	UOHM = 12


# noinspection SpellCheckingInspection
class DefaultUnitTemperature(Enum):
	"""6 Members, C ... KEL"""
	C = 0
	CEL = 1
	F = 2
	FAR = 3
	K = 4
	KEL = 5


# noinspection SpellCheckingInspection
class DefaultUnitTime(Enum):
	"""18 Members, AS ... US"""
	AS = 0
	EXS = 1
	FS = 2
	GS = 3
	H = 4
	HOUR = 5
	KS = 6
	M = 7
	MAS = 8
	MIN = 9
	MS = 10
	NS = 11
	PES = 12
	PS = 13
	S = 14
	SEC = 15
	TS = 16
	US = 17


# noinspection SpellCheckingInspection
class DefaultUnitVoltage(Enum):
	"""18 Members, AV ... V"""
	AV = 0
	DBMV = 1
	DBNV = 2
	DBPV = 3
	DBUV = 4
	DBV = 5
	EXV = 6
	FV = 7
	GV = 8
	KV = 9
	MAV = 10
	MV = 11
	NV = 12
	PEV = 13
	PV = 14
	TV = 15
	UV = 16
	V = 17


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
class DiagLoggigMode(Enum):
	"""3 Members, DETailed ... SIMPle"""
	DETailed = 0
	OFF = 1
	SIMPle = 2


# noinspection SpellCheckingInspection
class DiagLoggingDevice(Enum):
	"""3 Members, ALL ... MEMory"""
	ALL = 0
	DEBug = 1
	MEMory = 2


# noinspection SpellCheckingInspection
class DirectionHv(Enum):
	"""2 Members, HORizontal ... VERTical"""
	HORizontal = 0
	VERTical = 1


# noinspection SpellCheckingInspection
class DirectionIo(Enum):
	"""2 Members, IN ... OUT"""
	IN = 0
	OUT = 1


# noinspection SpellCheckingInspection
class DisplayLanguage(Enum):
	"""14 Members, AR ... ZH"""
	AR = 0
	CS = 1
	DA = 2
	DE = 3
	EN = 4
	ES = 5
	FR = 6
	IT = 7
	JA = 8
	KO = 9
	RU = 10
	SV = 11
	TR = 12
	ZH = 13


# noinspection SpellCheckingInspection
class DisplayMode(Enum):
	"""2 Members, AUTomatic ... MANual"""
	AUTomatic = 0
	MANual = 1


# noinspection SpellCheckingInspection
class DisplayStrategy(Enum):
	"""2 Members, BYLayout ... OFF"""
	BYLayout = 0
	OFF = 1


# noinspection SpellCheckingInspection
class Execution(Enum):
	"""2 Members, CONCurrent ... SEQuential"""
	CONCurrent = 0
	SEQuential = 1


# noinspection SpellCheckingInspection
class ExpertSetup(Enum):
	"""101 Members, BBG1 ... SUW7"""
	BBG1 = 0
	BBG2 = 1
	BBG3 = 2
	BBG4 = 3
	BBG5 = 4
	BBG6 = 5
	BBG7 = 6
	BBM1 = 7
	BBM2 = 8
	BBM3 = 9
	BBM4 = 10
	BBM5 = 11
	BBM6 = 12
	BBM7 = 13
	INValid = 14
	PANY = 15
	PI1 = 16
	PI2 = 17
	PO1 = 18
	PO2 = 19
	R11 = 20
	R118 = 21
	R11Ci = 22
	R11Co = 23
	R11O = 24
	R12 = 25
	R12Ci = 26
	R12Co = 27
	R13 = 28
	R13Ci = 29
	R13Co = 30
	R13O = 31
	R14 = 32
	R14Ci = 33
	R14Co = 34
	R15 = 35
	R16 = 36
	R17 = 37
	R18 = 38
	R1CI = 39
	R1CO = 40
	R1O = 41
	R21Ci = 42
	R21Co = 43
	R21O = 44
	R22Ci = 45
	R22Co = 46
	R23Ci = 47
	R23Co = 48
	R23O = 49
	R24Ci = 50
	R24Co = 51
	R2CI = 52
	R2CO = 53
	R31Ci = 54
	R31Co = 55
	R31O = 56
	R32Ci = 57
	R32Co = 58
	R33Ci = 59
	R33Co = 60
	R33O = 61
	R34Ci = 62
	R34Co = 63
	R3CI = 64
	R3CO = 65
	R3O = 66
	R41Ci = 67
	R41Co = 68
	R41O = 69
	R42Ci = 70
	R42Co = 71
	R43Ci = 72
	R43Co = 73
	R43O = 74
	R44Ci = 75
	R44Co = 76
	R4CI = 77
	R4CO = 78
	RRX1 = 79
	RRX2 = 80
	RRX3 = 81
	RRX4 = 82
	RTX1 = 83
	RTX2 = 84
	RTX3 = 85
	RTX4 = 86
	SUU1 = 87
	SUU2 = 88
	SUU3 = 89
	SUU4 = 90
	SUU5 = 91
	SUU6 = 92
	SUU7 = 93
	SUW1 = 94
	SUW2 = 95
	SUW3 = 96
	SUW4 = 97
	SUW5 = 98
	SUW6 = 99
	SUW7 = 100


# noinspection SpellCheckingInspection
class ExpressionMode(Enum):
	"""2 Members, REGex ... STRing"""
	REGex = 0
	STRing = 1


# noinspection SpellCheckingInspection
class FanMode(Enum):
	"""3 Members, HIGH ... NORMal"""
	HIGH = 0
	LOW = 1
	NORMal = 2


# noinspection SpellCheckingInspection
class FilterCriteria(Enum):
	"""1 Members, LOSupport ... LOSupport"""
	LOSupport = 0


# noinspection SpellCheckingInspection
class FontType(Enum):
	"""2 Members, DEF ... LRG"""
	DEF = 0
	LRG = 1


# noinspection SpellCheckingInspection
class HardcopyArea(Enum):
	"""3 Members, AWINdow ... MWINdow"""
	AWINdow = 0
	FSCReen = 1
	MWINdow = 2


# noinspection SpellCheckingInspection
class JoinAction(Enum):
	"""3 Members, CTASk ... STASk"""
	CTASk = 0
	DONE = 1
	STASk = 2


# noinspection SpellCheckingInspection
class LowHigh(Enum):
	"""2 Members, HIGH ... LOW"""
	HIGH = 0
	LOW = 1


# noinspection SpellCheckingInspection
class MutexAction(Enum):
	"""2 Members, DONothing ... RELock"""
	DONothing = 0
	RELock = 1


# noinspection SpellCheckingInspection
class MutexState(Enum):
	"""3 Members, LOCKed ... UNLocked"""
	LOCKed = 0
	NEWLocked = 1
	UNLocked = 2


# noinspection SpellCheckingInspection
class NameStyle(Enum):
	"""3 Members, FQName ... NAME"""
	FQName = 0
	LNAMe = 1
	NAME = 2


# noinspection SpellCheckingInspection
class OperationMode(Enum):
	"""2 Members, LOCal ... REMote"""
	LOCal = 0
	REMote = 1


# noinspection SpellCheckingInspection
class OscillatorType(Enum):
	"""2 Members, OCXO ... TCXO"""
	OCXO = 0
	TCXO = 1


# noinspection SpellCheckingInspection
class ProductType(Enum):
	"""6 Members, ALL ... SWPackage"""
	ALL = 0
	FWA = 1
	HWOPtion = 2
	LHWoption = 3
	SWOPtion = 4
	SWPackage = 5


# noinspection SpellCheckingInspection
class RemoteTraceEnable(Enum):
	"""4 Members, ANALysis ... ON"""
	ANALysis = 0
	LIVE = 1
	OFF = 2
	ON = 3


# noinspection SpellCheckingInspection
class RemoteTraceFileFormat(Enum):
	"""2 Members, ASCii ... XML"""
	ASCii = 0
	XML = 1


# noinspection SpellCheckingInspection
class RemoteTraceStartMode(Enum):
	"""2 Members, AUTO ... EXPLicit"""
	AUTO = 0
	EXPLicit = 1


# noinspection SpellCheckingInspection
class RemoteTraceStopMode(Enum):
	"""4 Members, AUTO ... EXPLicit"""
	AUTO = 0
	BUFFerfull = 1
	ERRor = 2
	EXPLicit = 3


# noinspection SpellCheckingInspection
class Repeat(Enum):
	"""2 Members, CONTinuous ... SINGleshot"""
	CONTinuous = 0
	SINGleshot = 1


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
class RfConverterInPath(Enum):
	"""4 Members, RF1 ... RF4"""
	RF1 = 0
	RF2 = 1
	RF3 = 2
	RF4 = 3


# noinspection SpellCheckingInspection
class RollkeyMode(Enum):
	"""3 Members, CURSors ... ZIGZag"""
	CURSors = 0
	VERTical = 1
	ZIGZag = 2


# noinspection SpellCheckingInspection
class RxTxDirection(Enum):
	"""3 Members, RX ... TX"""
	RX = 0
	RXTX = 1
	TX = 2


# noinspection SpellCheckingInspection
class Salignment(Enum):
	"""6 Members, FAILed ... SKIPped"""
	FAILed = 0
	INValid = 1
	NAV = 2
	PASSed = 3
	PROGress = 4
	SKIPped = 5


# noinspection SpellCheckingInspection
class SalignmentMode(Enum):
	"""5 Members, FLEVel ... VIQ"""
	FLEVel = 0
	IQ = 1
	LEVel = 2
	NAV = 3
	VIQ = 4


# noinspection SpellCheckingInspection
class ScreenshotFormat(Enum):
	"""3 Members, BMP ... PNG"""
	BMP = 0
	JPG = 1
	PNG = 2


# noinspection SpellCheckingInspection
class Segment(Enum):
	"""3 Members, A ... C"""
	A = 0
	B = 1
	C = 2


# noinspection SpellCheckingInspection
class SelftestSpecMode(Enum):
	"""2 Members, NONE ... UCS"""
	NONE = 0
	UCS = 1


# noinspection SpellCheckingInspection
class SelftestStopCondition(Enum):
	"""2 Members, NONE ... SOF"""
	NONE = 0
	SOF = 1


# noinspection SpellCheckingInspection
class SelftestSumState(Enum):
	"""5 Members, FAILed ... SKIPped"""
	FAILed = 0
	INPRogress = 1
	INValid = 2
	PASSed = 3
	SKIPped = 4


# noinspection SpellCheckingInspection
class SignalSlope(Enum):
	"""2 Members, FEDGe ... REDGe"""
	FEDGe = 0
	REDGe = 1


# noinspection SpellCheckingInspection
class SocketProtocol(Enum):
	"""3 Members, AGILent ... RAW"""
	AGILent = 0
	IEEE1174 = 1
	RAW = 2


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class SourceIntExt(Enum):
	"""3 Members, EINTernal ... INTernal"""
	EINTernal = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class StatRegFormat(Enum):
	"""4 Members, ASCii ... OCTal"""
	ASCii = 0
	BINary = 1
	HEXadecimal = 2
	OCTal = 3


# noinspection SpellCheckingInspection
class SyncPolling(Enum):
	"""2 Members, NPOLling ... POLLing"""
	NPOLling = 0
	POLLing = 1


# noinspection SpellCheckingInspection
class SyncResult(Enum):
	"""5 Members, DSTask ... TOUT"""
	DSTask = 0
	NRDY = 1
	NSTask = 2
	RDY = 3
	TOUT = 4


# noinspection SpellCheckingInspection
class TargetStateA(Enum):
	"""3 Members, OFF ... RUN"""
	OFF = 0
	RDY = 1
	RUN = 2


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
class TriggerSource(Enum):
	"""4 Members, EXTernal ... IFPower"""
	EXTernal = 0
	FREerun = 1
	IF = 2
	IFPower = 3


# noinspection SpellCheckingInspection
class Type(Enum):
	"""4 Members, CALibration ... UCORrection"""
	CALibration = 0
	FSCorrection = 1
	OGCal = 2
	UCORrection = 3


# noinspection SpellCheckingInspection
class UserRole(Enum):
	"""5 Members, ADMin ... USER"""
	ADMin = 0
	DEVeloper = 1
	SERVice = 2
	UEXTended = 3
	USER = 4


# noinspection SpellCheckingInspection
class ValidityScope(Enum):
	"""4 Members, ALL ... VALid"""
	ALL = 0
	CLICense = 1
	FUNCtional = 2
	VALid = 3


# noinspection SpellCheckingInspection
class ValidityScopeA(Enum):
	"""2 Members, GLOBal ... INSTrument"""
	GLOBal = 0
	INSTrument = 1


# noinspection SpellCheckingInspection
class ValidityScopeB(Enum):
	"""2 Members, INSTrument ... SYSTem"""
	INSTrument = 0
	SYSTem = 1
