from enum import Enum


# noinspection SpellCheckingInspection
class Connector(Enum):
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
class MaxSpecPowLen(Enum):
	"""2 Members, MS1 ... PPDU"""
	MS1 = 0
	PPDU = 1


# noinspection SpellCheckingInspection
class PhrDataRate(Enum):
	"""8 Members, DRHP ... SYNC"""
	DRHP = 0
	DRLP = 1
	DRMD = 2
	IGN = 3
	RHMH = 4
	RHML = 5
	RSF = 6
	SYNC = 7


# noinspection SpellCheckingInspection
class PpduMode(Enum):
	"""2 Members, MPPDu ... SPPDu"""
	MPPDu = 0
	SPPDu = 1


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
class StsSegmentLen(Enum):
	"""4 Members, L128 ... L64"""
	L128 = 0
	L256 = 1
	L32 = 2
	L64 = 3


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
