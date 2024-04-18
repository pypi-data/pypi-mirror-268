from enum import Enum


# noinspection SpellCheckingInspection
class AddressType(Enum):
	"""2 Members, PUBLic ... RANDom"""
	PUBLic = 0
	RANDom = 1


# noinspection SpellCheckingInspection
class AutoManualMode(Enum):
	"""2 Members, AUTO ... MANual"""
	AUTO = 0
	MANual = 1


# noinspection SpellCheckingInspection
class BaudRate(Enum):
	"""24 Members, B110 ... B96K"""
	B110 = 0
	B115k = 1
	B12K = 2
	B14K = 3
	B19K = 4
	B1M = 5
	B1M5 = 6
	B234k = 7
	B24K = 8
	B28K = 9
	B2M = 10
	B300 = 11
	B38K = 12
	B3M = 13
	B3M5 = 14
	B460k = 15
	B48K = 16
	B4M = 17
	B500k = 18
	B576k = 19
	B57K = 20
	B600 = 21
	B921k = 22
	B96K = 23


# noinspection SpellCheckingInspection
class BrEdrChannelsRange(Enum):
	"""2 Members, CH21 ... CH79"""
	CH21 = 0
	CH79 = 1


# noinspection SpellCheckingInspection
class BrPacketType(Enum):
	"""3 Members, DH1 ... DH5"""
	DH1 = 0
	DH3 = 1
	DH5 = 2


# noinspection SpellCheckingInspection
class BurstType(Enum):
	"""4 Members, BR ... QHSL"""
	BR = 0
	EDR = 1
	LE = 2
	QHSL = 3


# noinspection SpellCheckingInspection
class CmwSingleConnector(Enum):
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
class CodingScheme(Enum):
	"""2 Members, S2 ... S8"""
	S2 = 0
	S8 = 1


# noinspection SpellCheckingInspection
class CommProtocol(Enum):
	"""2 Members, HCI ... TWO"""
	HCI = 0
	TWO = 1


# noinspection SpellCheckingInspection
class CtePacketType(Enum):
	"""5 Members, AOA1us ... AOD2us"""
	AOA1us = 0
	AOA2us = 1
	AOAus = 2
	AOD1us = 3
	AOD2us = 4


# noinspection SpellCheckingInspection
class CteType(Enum):
	"""3 Members, AOA ... AOD2"""
	AOA = 0
	AOD1 = 1
	AOD2 = 2


# noinspection SpellCheckingInspection
class DataBits(Enum):
	"""2 Members, D7 ... D8"""
	D7 = 0
	D8 = 1


# noinspection SpellCheckingInspection
class DetectedPatternType(Enum):
	"""4 Members, ALTernating ... P44"""
	ALTernating = 0
	OTHer = 1
	P11 = 2
	P44 = 3


# noinspection SpellCheckingInspection
class DetectedPhyType(Enum):
	"""5 Members, P2Q ... P6Q"""
	P2Q = 0
	P3Q = 1
	P4Q = 2
	P5Q = 3
	P6Q = 4


# noinspection SpellCheckingInspection
class DisplayMeasurement(Enum):
	"""1 Members, MEV ... MEV"""
	MEV = 0


# noinspection SpellCheckingInspection
class DisplayView(Enum):
	"""15 Members, DEVM ... SOBW"""
	DEVM = 0
	FDEViation = 1
	FRANge = 2
	IQABs = 3
	IQDiff = 4
	IQERr = 5
	MODulation = 6
	OVERview = 7
	PDIFference = 8
	PENCoding = 9
	POWer = 10
	PVTime = 11
	SACP = 12
	SGACp = 13
	SOBW = 14


# noinspection SpellCheckingInspection
class EdrPacketType(Enum):
	"""6 Members, E21P ... E35P"""
	E21P = 0
	E23P = 1
	E25P = 2
	E31P = 3
	E33P = 4
	E35P = 5


# noinspection SpellCheckingInspection
class FilterWidth(Enum):
	"""2 Members, NARRow ... WIDE"""
	NARRow = 0
	WIDE = 1


# noinspection SpellCheckingInspection
class HwInterface(Enum):
	"""3 Members, NONE ... USB"""
	NONE = 0
	RS232 = 1
	USB = 2


# noinspection SpellCheckingInspection
class LeChannelsRange(Enum):
	"""2 Members, CH10 ... CH40"""
	CH10 = 0
	CH40 = 1


# noinspection SpellCheckingInspection
class LePacketType(Enum):
	"""3 Members, ADVertiser ... RFPHytest"""
	ADVertiser = 0
	RFCTe = 1
	RFPHytest = 2


# noinspection SpellCheckingInspection
class LePatternType(Enum):
	"""3 Members, OTHer ... P44"""
	OTHer = 0
	P11 = 1
	P44 = 2


# noinspection SpellCheckingInspection
class LePhysicalType(Enum):
	"""3 Members, LE1M ... LELR"""
	LE1M = 0
	LE2M = 1
	LELR = 2


# noinspection SpellCheckingInspection
class LePhyType(Enum):
	"""8 Members, LE1M ... P6Q"""
	LE1M = 0
	LE2M = 1
	LELR = 2
	P2Q = 3
	P3Q = 4
	P4Q = 5
	P5Q = 6
	P6Q = 7


# noinspection SpellCheckingInspection
class LeRangePaternType(Enum):
	"""6 Members, ALL0 ... PRBS9"""
	ALL0 = 0
	ALL1 = 1
	OTHer = 2
	P11 = 3
	P44 = 4
	PRBS9 = 5


# noinspection SpellCheckingInspection
class LeSymolTimeError(Enum):
	"""3 Members, NEG50 ... POS50"""
	NEG50 = 0
	OFF = 1
	POS50 = 2


# noinspection SpellCheckingInspection
class LogCategory(Enum):
	"""4 Members, CONTinue ... WARNing"""
	CONTinue = 0
	ERRor = 1
	INFO = 2
	WARNing = 3


# noinspection SpellCheckingInspection
class MeasureScope(Enum):
	"""2 Members, ALL ... SINGle"""
	ALL = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class MevPatternType(Enum):
	"""5 Members, ALL1 ... P44"""
	ALL1 = 0
	ALTernating = 1
	OTHer = 2
	P11 = 3
	P44 = 4


# noinspection SpellCheckingInspection
class PacketTypeA(Enum):
	"""9 Members, E21P ... E85P"""
	E21P = 0
	E23P = 1
	E25P = 2
	E41P = 3
	E43P = 4
	E45P = 5
	E81P = 6
	E83P = 7
	E85P = 8


# noinspection SpellCheckingInspection
class PacketTypeB(Enum):
	"""1 Members, DATA ... DATA"""
	DATA = 0


# noinspection SpellCheckingInspection
class PacketTypeC(Enum):
	"""6 Members, H41P ... H85P"""
	H41P = 0
	H43P = 1
	H45P = 2
	H81P = 3
	H83P = 4
	H85P = 5


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class Parity(Enum):
	"""3 Members, EVEN ... ODD"""
	EVEN = 0
	NONE = 1
	ODD = 2


# noinspection SpellCheckingInspection
class PatternIndependent(Enum):
	"""2 Members, PINDependent ... SPECconform"""
	PINDependent = 0
	SPECconform = 1


# noinspection SpellCheckingInspection
class PatternType(Enum):
	"""5 Members, ALL0 ... PRBS9"""
	ALL0 = 0
	ALL1 = 1
	P11 = 2
	P44 = 3
	PRBS9 = 4


# noinspection SpellCheckingInspection
class PatternTypeHdr(Enum):
	"""2 Members, OTHer ... PRBS9"""
	OTHer = 0
	PRBS9 = 1


# noinspection SpellCheckingInspection
class PayloadCoding(Enum):
	"""3 Members, L12D ... NONE"""
	L12D = 0
	L34D = 1
	NONE = 2


# noinspection SpellCheckingInspection
class PayloadLength(Enum):
	"""2 Members, _255 ... _37"""
	_255 = 0
	_37 = 1


# noinspection SpellCheckingInspection
class PduType(Enum):
	"""7 Members, ADVDirect ... SCRSp"""
	ADVDirect = 0
	ADVind = 1
	ADVNonconn = 2
	ADVScan = 3
	CONReq = 4
	SCReq = 5
	SCRSp = 6


# noinspection SpellCheckingInspection
class PhysicalLayer(Enum):
	"""2 Members, P4HP ... P8HP"""
	P4HP = 0
	P8HP = 1


# noinspection SpellCheckingInspection
class Protocol(Enum):
	"""3 Members, CTSRts ... XONXoff"""
	CTSRts = 0
	NONE = 1
	XONXoff = 2


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
class Result(Enum):
	"""2 Members, FAIL ... PASS"""
	FAIL = 0
	PASS = 1


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
class RxConverter(Enum):
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
class RxQualityMeasMode(Enum):
	"""3 Members, PER ... SPOT"""
	PER = 0
	SENS = 1
	SPOT = 2


# noinspection SpellCheckingInspection
class SegmentPacketType(Enum):
	"""13 Members, ADVertiser ... RFPHytest"""
	ADVertiser = 0
	DATA = 1
	DH1 = 2
	DH3 = 3
	DH5 = 4
	E21P = 5
	E23P = 6
	E25P = 7
	E31P = 8
	E33P = 9
	E35P = 10
	RFCTe = 11
	RFPHytest = 12


# noinspection SpellCheckingInspection
class StopBits(Enum):
	"""2 Members, S1 ... S2"""
	S1 = 0
	S2 = 1


# noinspection SpellCheckingInspection
class StopCondition(Enum):
	"""2 Members, NONE ... SLFail"""
	NONE = 0
	SLFail = 1


# noinspection SpellCheckingInspection
class SyncState(Enum):
	"""2 Members, ADJusted ... PENDing"""
	ADJusted = 0
	PENDing = 1


# noinspection SpellCheckingInspection
class TargetMainState(Enum):
	"""3 Members, OFF ... RUN"""
	OFF = 0
	RDY = 1
	RUN = 2


# noinspection SpellCheckingInspection
class TestScenario(Enum):
	"""3 Members, CSPath ... UNDefined"""
	CSPath = 0
	SALone = 1
	UNDefined = 2


# noinspection SpellCheckingInspection
class TransmitPatternType(Enum):
	"""2 Members, ALL1 ... OTHer"""
	ALL1 = 0
	OTHer = 1


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
class TxConnectorBench(Enum):
	"""15 Members, R118 ... RH18"""
	R118 = 0
	R214 = 1
	R218 = 2
	R258 = 3
	R318 = 4
	R418 = 5
	RA18 = 6
	RB14 = 7
	RB18 = 8
	RC18 = 9
	RD18 = 10
	RE18 = 11
	RF18 = 12
	RG18 = 13
	RH18 = 14


# noinspection SpellCheckingInspection
class TxConverter(Enum):
	"""40 Members, ITX1 ... TX44"""
	ITX1 = 0
	ITX11 = 1
	ITX12 = 2
	ITX13 = 3
	ITX14 = 4
	ITX2 = 5
	ITX21 = 6
	ITX22 = 7
	ITX23 = 8
	ITX24 = 9
	ITX3 = 10
	ITX31 = 11
	ITX32 = 12
	ITX33 = 13
	ITX34 = 14
	ITX4 = 15
	ITX41 = 16
	ITX42 = 17
	ITX43 = 18
	ITX44 = 19
	TX1 = 20
	TX11 = 21
	TX12 = 22
	TX13 = 23
	TX14 = 24
	TX2 = 25
	TX21 = 26
	TX22 = 27
	TX23 = 28
	TX24 = 29
	TX3 = 30
	TX31 = 31
	TX32 = 32
	TX33 = 33
	TX34 = 34
	TX4 = 35
	TX41 = 36
	TX42 = 37
	TX43 = 38
	TX44 = 39
