from enum import Enum


# noinspection SpellCheckingInspection
class Band(Enum):
	"""6 Members, B257 ... B262"""
	B257 = 0
	B258 = 1
	B259 = 2
	B260 = 3
	B261 = 4
	B262 = 5


# noinspection SpellCheckingInspection
class BandwidthPart(Enum):
	"""4 Members, BWP0 ... BWP3"""
	BWP0 = 0
	BWP1 = 1
	BWP2 = 2
	BWP3 = 3


# noinspection SpellCheckingInspection
class ChannelBw(Enum):
	"""4 Members, B050 ... B400"""
	B050 = 0
	B100 = 1
	B200 = 2
	B400 = 3


# noinspection SpellCheckingInspection
class ChannelTypeA(Enum):
	"""2 Members, PUCCh ... PUSCh"""
	PUCCh = 0
	PUSCh = 1


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
class DuplexModeB(Enum):
	"""2 Members, FDD ... TDD"""
	FDD = 0
	TDD = 1


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
class Initialization(Enum):
	"""2 Members, CID ... DMRSid"""
	CID = 0
	DMRSid = 1


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
class MappingType(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class MeasCarrier(Enum):
	"""4 Members, CC1 ... CC4"""
	CC1 = 0
	CC2 = 1
	CC3 = 2
	CC4 = 3


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
	"""2 Members, ALL ... UDEF"""
	ALL = 0
	UDEF = 1


# noinspection SpellCheckingInspection
class ModScheme(Enum):
	"""6 Members, BPSK ... QPSK"""
	BPSK = 0
	PHBPsk = 1
	Q16 = 2
	Q256 = 3
	Q64 = 4
	QPSK = 5


# noinspection SpellCheckingInspection
class NsValue(Enum):
	"""99 Members, NS01 ... NSU43"""
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
	NS35 = 33
	NS36 = 34
	NS37 = 35
	NS38 = 36
	NS39 = 37
	NS40 = 38
	NS41 = 39
	NS42 = 40
	NS43 = 41
	NS44 = 42
	NS45 = 43
	NS46 = 44
	NS47 = 45
	NS48 = 46
	NS49 = 47
	NS50 = 48
	NS51 = 49
	NS52 = 50
	NS53 = 51
	NS54 = 52
	NS55 = 53
	NS56 = 54
	NS57 = 55
	NS58 = 56
	NS59 = 57
	NS60 = 58
	NS61 = 59
	NS62 = 60
	NS63 = 61
	NS64 = 62
	NS65 = 63
	NS66 = 64
	NS67 = 65
	NS68 = 66
	NS69 = 67
	NS70 = 68
	NS71 = 69
	NS72 = 70
	NS73 = 71
	NS74 = 72
	NS75 = 73
	NS76 = 74
	NS77 = 75
	NS78 = 76
	NS79 = 77
	NS80 = 78
	NS81 = 79
	NS82 = 80
	NS83 = 81
	NS84 = 82
	NS85 = 83
	NS86 = 84
	NS87 = 85
	NS88 = 86
	NS89 = 87
	NS90 = 88
	NS91 = 89
	NS92 = 90
	NS93 = 91
	NS94 = 92
	NS95 = 93
	NS96 = 94
	NS97 = 95
	NS98 = 96
	NS99 = 97
	NSU43 = 98


# noinspection SpellCheckingInspection
class Path(Enum):
	"""2 Members, NETWork ... STANdalone"""
	NETWork = 0
	STANdalone = 1


# noinspection SpellCheckingInspection
class Periodicity(Enum):
	"""8 Members, MS05 ... MS5"""
	MS05 = 0
	MS0625 = 1
	MS1 = 2
	MS10 = 3
	MS125 = 4
	MS2 = 5
	MS25 = 6
	MS5 = 7


# noinspection SpellCheckingInspection
class PeriodPreamble(Enum):
	"""6 Members, MS01 ... MS20"""
	MS01 = 0
	MS0125 = 1
	MS025 = 2
	MS05 = 3
	MS10 = 4
	MS20 = 5


# noinspection SpellCheckingInspection
class PhaseComp(Enum):
	"""3 Members, CAF ... UDEF"""
	CAF = 0
	OFF = 1
	UDEF = 2


# noinspection SpellCheckingInspection
class PowerClass(Enum):
	"""4 Members, PC1 ... PC4"""
	PC1 = 0
	PC2 = 1
	PC3 = 2
	PC4 = 3


# noinspection SpellCheckingInspection
class PreambleFormat(Enum):
	"""9 Members, A1 ... C2"""
	A1 = 0
	A2 = 1
	A3 = 2
	B1 = 3
	B2 = 4
	B3 = 5
	B4 = 6
	C0 = 7
	C2 = 8


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
	"""2 Members, K120 ... M1"""
	K120 = 0
	M1 = 1


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
	"""3 Members, IFPower ... ON"""
	IFPower = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class RfConverter(Enum):
	"""40 Members, IRX1 ... RX44"""
	IRX1 = 0
	IRX11 = 1
	IRX12 = 2
	IRX13 = 3
	IRX14 = 4
	IRX2 = 5
	IRX21 = 6
	IRX22 = 7
	IRX23 = 8
	IRX24 = 9
	IRX3 = 10
	IRX31 = 11
	IRX32 = 12
	IRX33 = 13
	IRX34 = 14
	IRX4 = 15
	IRX41 = 16
	IRX42 = 17
	IRX43 = 18
	IRX44 = 19
	RX1 = 20
	RX11 = 21
	RX12 = 22
	RX13 = 23
	RX14 = 24
	RX2 = 25
	RX21 = 26
	RX22 = 27
	RX23 = 28
	RX24 = 29
	RX3 = 30
	RX31 = 31
	RX32 = 32
	RX33 = 33
	RX34 = 34
	RX4 = 35
	RX41 = 36
	RX42 = 37
	RX43 = 38
	RX44 = 39


# noinspection SpellCheckingInspection
class RxConnector(Enum):
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
class Scenario(Enum):
	"""1 Members, SAL ... SAL"""
	SAL = 0


# noinspection SpellCheckingInspection
class ScSpacing(Enum):
	"""2 Members, S120k ... S60K"""
	S120k = 0
	S60K = 1


# noinspection SpellCheckingInspection
class Sharing(Enum):
	"""3 Members, FSHared ... OCONnect"""
	FSHared = 0
	NSHared = 1
	OCONnect = 2


# noinspection SpellCheckingInspection
class SignalSlope(Enum):
	"""2 Members, FEDGe ... REDGe"""
	FEDGe = 0
	REDGe = 1


# noinspection SpellCheckingInspection
class StopCondition(Enum):
	"""2 Members, NONE ... SLFail"""
	NONE = 0
	SLFail = 1


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
	"""1 Members, GOO ... GOO"""
	GOO = 0


# noinspection SpellCheckingInspection
class UsedSlots(Enum):
	"""3 Members, DL ... X"""
	DL = 0
	UL = 1
	X = 2
