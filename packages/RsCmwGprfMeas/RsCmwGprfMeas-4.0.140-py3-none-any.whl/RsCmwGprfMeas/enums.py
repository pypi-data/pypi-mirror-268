from enum import Enum


# noinspection SpellCheckingInspection
class AveragingMode(Enum):
	"""2 Members, LINear ... LOGarithmic"""
	LINear = 0
	LOGarithmic = 1


# noinspection SpellCheckingInspection
class CcdfMode(Enum):
	"""2 Members, POWer ... STATistic"""
	POWer = 0
	STATistic = 1


# noinspection SpellCheckingInspection
class CmwsConnector(Enum):
	"""96 Members, R11 ... RH8"""
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
	RC1 = 48
	RC2 = 49
	RC3 = 50
	RC4 = 51
	RC5 = 52
	RC6 = 53
	RC7 = 54
	RC8 = 55
	RD1 = 56
	RD2 = 57
	RD3 = 58
	RD4 = 59
	RD5 = 60
	RD6 = 61
	RD7 = 62
	RD8 = 63
	RE1 = 64
	RE2 = 65
	RE3 = 66
	RE4 = 67
	RE5 = 68
	RE6 = 69
	RE7 = 70
	RE8 = 71
	RF1 = 72
	RF2 = 73
	RF3 = 74
	RF4 = 75
	RF5 = 76
	RF6 = 77
	RF7 = 78
	RF8 = 79
	RG1 = 80
	RG2 = 81
	RG3 = 82
	RG4 = 83
	RG5 = 84
	RG6 = 85
	RG7 = 86
	RG8 = 87
	RH1 = 88
	RH2 = 89
	RH3 = 90
	RH4 = 91
	RH5 = 92
	RH6 = 93
	RH7 = 94
	RH8 = 95


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
class DigitalFilterType(Enum):
	"""5 Members, BANDpass ... WCDMa"""
	BANDpass = 0
	CDMA = 1
	GAUSs = 2
	TDSCdma = 3
	WCDMa = 4


# noinspection SpellCheckingInspection
class FileSave(Enum):
	"""3 Members, OFF ... ONLY"""
	OFF = 0
	ON = 1
	ONLY = 2


# noinspection SpellCheckingInspection
class FilterType(Enum):
	"""5 Members, B10Mhz ... NYQuist"""
	B10Mhz = 0
	B1MHz = 1
	GAUSs = 2
	NY1Mhz = 3
	NYQuist = 4


# noinspection SpellCheckingInspection
class IqFormat(Enum):
	"""2 Members, IQ ... RPHI"""
	IQ = 0
	RPHI = 1


# noinspection SpellCheckingInspection
class MagnitudeUnit(Enum):
	"""2 Members, RAW ... VOLT"""
	RAW = 0
	VOLT = 1


# noinspection SpellCheckingInspection
class MeasTab(Enum):
	"""6 Members, EPSensor ... SPECtrum"""
	EPSensor = 0
	FFTSanalyzer = 1
	IQRecorder = 2
	IQVSlot = 3
	POWer = 4
	SPECtrum = 5


# noinspection SpellCheckingInspection
class MeasurementMode(Enum):
	"""2 Members, NORMal ... TALignment"""
	NORMal = 0
	TALignment = 1


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
class PathIndex(Enum):
	"""8 Members, P1 ... P8"""
	P1 = 0
	P2 = 1
	P3 = 2
	P4 = 3
	P5 = 4
	P6 = 5
	P7 = 6
	P8 = 7


# noinspection SpellCheckingInspection
class PathLossState(Enum):
	"""3 Members, NCAP ... RDY"""
	NCAP = 0
	PEND = 1
	RDY = 2


# noinspection SpellCheckingInspection
class PwrSensorResolution(Enum):
	"""4 Members, PD0 ... PD3"""
	PD0 = 0
	PD1 = 1
	PD2 = 2
	PD3 = 3


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
class Scenario(Enum):
	"""5 Members, CSPath ... UNDefined"""
	CSPath = 0
	MAIQ = 1
	MAPR = 2
	SALone = 3
	UNDefined = 4


# noinspection SpellCheckingInspection
class SignalSlopeExt(Enum):
	"""4 Members, FALLing ... RISing"""
	FALLing = 0
	FEDGe = 1
	REDGe = 2
	RISing = 3


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
class TargetMainState(Enum):
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
class Timing(Enum):
	"""2 Members, CENTered ... STEP"""
	CENTered = 0
	STEP = 1


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
class TriggerSource(Enum):
	"""4 Members, EXTernal ... IFPower"""
	EXTernal = 0
	FREerun = 1
	IF = 2
	IFPower = 3


# noinspection SpellCheckingInspection
class UserDebugMode(Enum):
	"""2 Members, DEBug ... USER"""
	DEBug = 0
	USER = 1


# noinspection SpellCheckingInspection
class ZeroingState(Enum):
	"""2 Members, FAILed ... PASSed"""
	FAILed = 0
	PASSed = 1
