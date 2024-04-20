from enum import Enum


# noinspection SpellCheckingInspection
class AllocatedSlots(Enum):
	"""1 Members, ALL ... ALL"""
	ALL = 0


# noinspection SpellCheckingInspection
class Band(Enum):
	"""60 Members, OB1 ... OB99"""
	OB1 = 0
	OB100 = 1
	OB101 = 2
	OB104 = 3
	OB12 = 4
	OB13 = 5
	OB14 = 6
	OB18 = 7
	OB2 = 8
	OB20 = 9
	OB24 = 10
	OB25 = 11
	OB255 = 12
	OB256 = 13
	OB26 = 14
	OB28 = 15
	OB3 = 16
	OB30 = 17
	OB34 = 18
	OB38 = 19
	OB39 = 20
	OB40 = 21
	OB41 = 22
	OB46 = 23
	OB47 = 24
	OB48 = 25
	OB5 = 26
	OB50 = 27
	OB51 = 28
	OB53 = 29
	OB65 = 30
	OB66 = 31
	OB7 = 32
	OB70 = 33
	OB71 = 34
	OB74 = 35
	OB75 = 36
	OB76 = 37
	OB77 = 38
	OB78 = 39
	OB79 = 40
	OB8 = 41
	OB80 = 42
	OB81 = 43
	OB82 = 44
	OB83 = 45
	OB84 = 46
	OB85 = 47
	OB86 = 48
	OB89 = 49
	OB90 = 50
	OB91 = 51
	OB92 = 52
	OB93 = 53
	OB94 = 54
	OB95 = 55
	OB96 = 56
	OB97 = 57
	OB98 = 58
	OB99 = 59


# noinspection SpellCheckingInspection
class BandwidthPart(Enum):
	"""1 Members, BWP0 ... BWP0"""
	BWP0 = 0


# noinspection SpellCheckingInspection
class CarrierComponent(Enum):
	"""2 Members, CC1 ... CC2"""
	CC1 = 0
	CC2 = 1


# noinspection SpellCheckingInspection
class CarrierPosition(Enum):
	"""2 Members, LONR ... RONR"""
	LONR = 0
	RONR = 1


# noinspection SpellCheckingInspection
class ChannelBwidth(Enum):
	"""15 Members, B005 ... B100"""
	B005 = 0
	B010 = 1
	B015 = 2
	B020 = 3
	B025 = 4
	B030 = 5
	B035 = 6
	B040 = 7
	B045 = 8
	B050 = 9
	B060 = 10
	B070 = 11
	B080 = 12
	B090 = 13
	B100 = 14


# noinspection SpellCheckingInspection
class ChannelBwidthB(Enum):
	"""4 Members, B005 ... B020"""
	B005 = 0
	B010 = 1
	B015 = 2
	B020 = 3


# noinspection SpellCheckingInspection
class ChannelTypeA(Enum):
	"""2 Members, PUCCh ... PUSCh"""
	PUCCh = 0
	PUSCh = 1


# noinspection SpellCheckingInspection
class ChannelTypeB(Enum):
	"""4 Members, OFF ... PUSCh"""
	OFF = 0
	ON = 1
	PUCCh = 2
	PUSCh = 3


# noinspection SpellCheckingInspection
class CmwsConnector(Enum):
	"""48 Members, R11 ... RB8"""
	R11 = 0
	R12 = 1
	R13 = 2
	R14 = 3
	R15 = 4
	R16 = 5
	R17 = 6
	R18 = 7
	R21 = 8
	R22 = 9
	R23 = 10
	R24 = 11
	R25 = 12
	R26 = 13
	R27 = 14
	R28 = 15
	R31 = 16
	R32 = 17
	R33 = 18
	R34 = 19
	R35 = 20
	R36 = 21
	R37 = 22
	R38 = 23
	R41 = 24
	R42 = 25
	R43 = 26
	R44 = 27
	R45 = 28
	R46 = 29
	R47 = 30
	R48 = 31
	RA1 = 32
	RA2 = 33
	RA3 = 34
	RA4 = 35
	RA5 = 36
	RA6 = 37
	RA7 = 38
	RA8 = 39
	RB1 = 40
	RB2 = 41
	RB3 = 42
	RB4 = 43
	RB5 = 44
	RB6 = 45
	RB7 = 46
	RB8 = 47


# noinspection SpellCheckingInspection
class ConfigType(Enum):
	"""2 Members, T1 ... T2"""
	T1 = 0
	T2 = 1


# noinspection SpellCheckingInspection
class CyclicPrefix(Enum):
	"""2 Members, EXTended ... NORMal"""
	EXTended = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class DmrsInit(Enum):
	"""2 Members, CID ... DID"""
	CID = 0
	DID = 1


# noinspection SpellCheckingInspection
class DmrsPort(Enum):
	"""3 Members, ALL ... P1001"""
	ALL = 0
	P1000 = 1
	P1001 = 2


# noinspection SpellCheckingInspection
class DuplexModeB(Enum):
	"""2 Members, FDD ... TDD"""
	FDD = 0
	TDD = 1


# noinspection SpellCheckingInspection
class Generator(Enum):
	"""2 Members, DID ... PHY"""
	DID = 0
	PHY = 1


# noinspection SpellCheckingInspection
class GhopingInit(Enum):
	"""2 Members, CID ... HID"""
	CID = 0
	HID = 1


# noinspection SpellCheckingInspection
class GroupHopping(Enum):
	"""3 Members, DISable ... NEITher"""
	DISable = 0
	ENABle = 1
	NEITher = 2


# noinspection SpellCheckingInspection
class Ktc(Enum):
	"""3 Members, N2 ... N8"""
	N2 = 0
	N4 = 1
	N8 = 2


# noinspection SpellCheckingInspection
class Lagging(Enum):
	"""3 Members, MS05 ... OFF"""
	MS05 = 0
	MS25 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class Leading(Enum):
	"""2 Members, MS25 ... OFF"""
	MS25 = 0
	OFF = 1


# noinspection SpellCheckingInspection
class ListMode(Enum):
	"""2 Members, ONCE ... SEGMent"""
	ONCE = 0
	SEGMent = 1


# noinspection SpellCheckingInspection
class LowHigh(Enum):
	"""2 Members, HIGH ... LOW"""
	HIGH = 0
	LOW = 1


# noinspection SpellCheckingInspection
class MappingType(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class MaxLength(Enum):
	"""2 Members, DOUBle ... SINGle"""
	DOUBle = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class MeasFilter(Enum):
	"""2 Members, BANDpass ... GAUSs"""
	BANDpass = 0
	GAUSs = 1


# noinspection SpellCheckingInspection
class MeasurementMode(Enum):
	"""2 Members, MELMode ... NORMal"""
	MELMode = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class MeasureSlot(Enum):
	"""6 Members, ALL ... UDEF"""
	ALL = 0
	MS0 = 1
	MS1 = 2
	MS2 = 3
	MS3 = 4
	UDEF = 5


# noinspection SpellCheckingInspection
class MevLimit(Enum):
	"""2 Members, STD ... UDEF"""
	STD = 0
	UDEF = 1


# noinspection SpellCheckingInspection
class Modulation(Enum):
	"""6 Members, BPSK ... QPSK"""
	BPSK = 0
	BPWS = 1
	Q16 = 2
	Q256 = 3
	Q64 = 4
	QPSK = 5


# noinspection SpellCheckingInspection
class ModulationScheme(Enum):
	"""7 Members, AUTO ... QPSK"""
	AUTO = 0
	BPSK = 1
	BPWS = 2
	Q16 = 3
	Q256 = 4
	Q64 = 5
	QPSK = 6


# noinspection SpellCheckingInspection
class ModulationSchemeB(Enum):
	"""4 Members, Q16 ... QPSK"""
	Q16 = 0
	Q256 = 1
	Q64 = 2
	QPSK = 3


# noinspection SpellCheckingInspection
class NbTrigger(Enum):
	"""4 Members, M010 ... M080"""
	M010 = 0
	M020 = 1
	M040 = 2
	M080 = 3


# noinspection SpellCheckingInspection
class NetworkSigVal(Enum):
	"""103 Members, NS01 ... NSU43"""
	NS01 = 0
	NS02 = 1
	NS03 = 2
	NS04 = 3
	NS05 = 4
	NS06 = 5
	NS07 = 6
	NS08 = 7
	NS09 = 8
	NS10 = 9
	NS100 = 10
	NS11 = 11
	NS12 = 12
	NS13 = 13
	NS14 = 14
	NS15 = 15
	NS16 = 16
	NS17 = 17
	NS18 = 18
	NS19 = 19
	NS20 = 20
	NS21 = 21
	NS22 = 22
	NS23 = 23
	NS24 = 24
	NS25 = 25
	NS26 = 26
	NS27 = 27
	NS28 = 28
	NS29 = 29
	NS30 = 30
	NS31 = 31
	NS32 = 32
	NS33 = 33
	NS34 = 34
	NS35 = 35
	NS36 = 36
	NS37 = 37
	NS38 = 38
	NS39 = 39
	NS40 = 40
	NS41 = 41
	NS42 = 42
	NS43 = 43
	NS44 = 44
	NS45 = 45
	NS46 = 46
	NS47 = 47
	NS48 = 48
	NS49 = 49
	NS50 = 50
	NS51 = 51
	NS52 = 52
	NS53 = 53
	NS54 = 54
	NS55 = 55
	NS56 = 56
	NS57 = 57
	NS58 = 58
	NS59 = 59
	NS60 = 60
	NS61 = 61
	NS62 = 62
	NS63 = 63
	NS64 = 64
	NS65 = 65
	NS66 = 66
	NS67 = 67
	NS68 = 68
	NS69 = 69
	NS70 = 70
	NS71 = 71
	NS72 = 72
	NS73 = 73
	NS74 = 74
	NS75 = 75
	NS76 = 76
	NS77 = 77
	NS78 = 78
	NS79 = 79
	NS80 = 80
	NS81 = 81
	NS82 = 82
	NS83 = 83
	NS84 = 84
	NS85 = 85
	NS86 = 86
	NS87 = 87
	NS88 = 88
	NS89 = 89
	NS90 = 90
	NS91 = 91
	NS92 = 92
	NS93 = 93
	NS94 = 94
	NS95 = 95
	NS96 = 96
	NS97 = 97
	NS98 = 98
	NS99 = 99
	NSU03 = 100
	NSU05 = 101
	NSU43 = 102


# noinspection SpellCheckingInspection
class NumberSymbols(Enum):
	"""7 Members, N1 ... N8"""
	N1 = 0
	N10 = 1
	N12 = 2
	N14 = 3
	N2 = 4
	N4 = 5
	N8 = 6


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class Periodicity(Enum):
	"""9 Members, MS05 ... MS5"""
	MS05 = 0
	MS1 = 1
	MS10 = 2
	MS125 = 3
	MS2 = 4
	MS25 = 5
	MS3 = 6
	MS4 = 7
	MS5 = 8


# noinspection SpellCheckingInspection
class PeriodPreamble(Enum):
	"""3 Members, MS05 ... MS20"""
	MS05 = 0
	MS10 = 1
	MS20 = 2


# noinspection SpellCheckingInspection
class PhaseComp(Enum):
	"""3 Members, CAF ... UDEF"""
	CAF = 0
	OFF = 1
	UDEF = 2


# noinspection SpellCheckingInspection
class PreambleFormat(Enum):
	"""13 Members, PF0 ... PFC2"""
	PF0 = 0
	PF1 = 1
	PF2 = 2
	PF3 = 3
	PFA1 = 4
	PFA2 = 5
	PFA3 = 6
	PFB1 = 7
	PFB2 = 8
	PFB3 = 9
	PFB4 = 10
	PFC0 = 11
	PFC2 = 12


# noinspection SpellCheckingInspection
class PucchFormat(Enum):
	"""5 Members, F0 ... F4"""
	F0 = 0
	F1 = 1
	F2 = 2
	F3 = 3
	F4 = 4


# noinspection SpellCheckingInspection
class RbwA(Enum):
	"""3 Members, K030 ... PC1"""
	K030 = 0
	M1 = 1
	PC1 = 2


# noinspection SpellCheckingInspection
class RbwB(Enum):
	"""6 Members, K030 ... PC2"""
	K030 = 0
	K100 = 1
	K400 = 2
	M1 = 3
	PC1 = 4
	PC2 = 5


# noinspection SpellCheckingInspection
class RbwC(Enum):
	"""3 Members, K030 ... M1"""
	K030 = 0
	K400 = 1
	M1 = 2


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
class RestrictedSet(Enum):
	"""1 Members, URES ... URES"""
	URES = 0


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
class RetriggerFlag(Enum):
	"""4 Members, IFPNarrowband ... ON"""
	IFPNarrowband = 0
	IFPower = 1
	OFF = 2
	ON = 3


# noinspection SpellCheckingInspection
class Sharing(Enum):
	"""3 Members, FSHared ... OCONnection"""
	FSHared = 0
	NSHared = 1
	OCONnection = 2


# noinspection SpellCheckingInspection
class SignalPath(Enum):
	"""2 Members, NETWork ... STANdalone"""
	NETWork = 0
	STANdalone = 1


# noinspection SpellCheckingInspection
class SignalSlope(Enum):
	"""2 Members, FEDGe ... REDGe"""
	FEDGe = 0
	REDGe = 1


# noinspection SpellCheckingInspection
class SignalType(Enum):
	"""2 Members, SL ... UL"""
	SL = 0
	UL = 1


# noinspection SpellCheckingInspection
class SrsPeriodicity(Enum):
	"""17 Members, SL1 ... SL80"""
	SL1 = 0
	SL10 = 1
	SL1280 = 2
	SL16 = 3
	SL160 = 4
	SL2 = 5
	SL20 = 6
	SL2560 = 7
	SL32 = 8
	SL320 = 9
	SL4 = 10
	SL40 = 11
	SL5 = 12
	SL64 = 13
	SL640 = 14
	SL8 = 15
	SL80 = 16


# noinspection SpellCheckingInspection
class StopCondition(Enum):
	"""2 Members, NONE ... SLFail"""
	NONE = 0
	SLFail = 1


# noinspection SpellCheckingInspection
class SubCarrSpacing(Enum):
	"""3 Members, S15K ... S60K"""
	S15K = 0
	S30K = 1
	S60K = 2


# noinspection SpellCheckingInspection
class SubCarrSpacingB(Enum):
	"""5 Members, S15K ... S60K"""
	S15K = 0
	S1K2 = 1
	S30K = 2
	S5K = 3
	S60K = 4


# noinspection SpellCheckingInspection
class SubChanSize(Enum):
	"""8 Members, RB10 ... RB75"""
	RB10 = 0
	RB100 = 1
	RB12 = 2
	RB15 = 3
	RB20 = 4
	RB25 = 5
	RB50 = 6
	RB75 = 7


# noinspection SpellCheckingInspection
class SyncMode(Enum):
	"""4 Members, ENHanced ... NSSLot"""
	ENHanced = 0
	ESSLot = 1
	NORMal = 2
	NSSLot = 3


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
class TimeMask(Enum):
	"""3 Members, GOO ... SBLanking"""
	GOO = 0
	PPSRs = 1
	SBLanking = 2


# noinspection SpellCheckingInspection
class TraceSelect(Enum):
	"""3 Members, AVERage ... MAXimum"""
	AVERage = 0
	CURRent = 1
	MAXimum = 2
