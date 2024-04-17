from enum import Enum


# noinspection SpellCheckingInspection
class Bandwidth(Enum):
	"""8 Members, BW05mhz ... BW88mhz"""
	BW05mhz = 0
	BW10mhz = 1
	BW16mhz = 2
	BW20mhz = 3
	BW32mhz = 4
	BW40mhz = 5
	BW80mhz = 6
	BW88mhz = 7


# noinspection SpellCheckingInspection
class BurstEvalLength(Enum):
	"""2 Members, REDucedburst ... WHOLeburst"""
	REDucedburst = 0
	WHOLeburst = 1


# noinspection SpellCheckingInspection
class BurstType(Enum):
	"""4 Members, AUTO ... MIXed"""
	AUTO = 0
	DLIN = 1
	GREenfield = 2
	MIXed = 3


# noinspection SpellCheckingInspection
class BurstTypeB(Enum):
	"""2 Members, GREenfield ... MIXed"""
	GREenfield = 0
	MIXed = 1


# noinspection SpellCheckingInspection
class CfoEstimation(Enum):
	"""2 Members, FULLpacket ... PREamble"""
	FULLpacket = 0
	PREamble = 1


# noinspection SpellCheckingInspection
class ChannelEstimation(Enum):
	"""2 Members, PAYLoad ... PREamble"""
	PAYLoad = 0
	PREamble = 1


# noinspection SpellCheckingInspection
class Coderate(Enum):
	"""7 Members, AUTO ... CR56"""
	AUTO = 0
	CR12 = 1
	CR14dcm = 2
	CR23 = 3
	CR34 = 4
	CR38dcm = 5
	CR56 = 6


# noinspection SpellCheckingInspection
class CodingType(Enum):
	"""2 Members, BCC ... LDPC"""
	BCC = 0
	LDPC = 1


# noinspection SpellCheckingInspection
class ConnectorSwitch(Enum):
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
class ConnectorSwitchExt(Enum):
	"""98 Members, OFF ... RH8"""
	OFF = 0
	ON = 1
	R11 = 2
	R12 = 3
	R13 = 4
	R14 = 5
	R15 = 6
	R16 = 7
	R17 = 8
	R18 = 9
	R21 = 10
	R22 = 11
	R23 = 12
	R24 = 13
	R25 = 14
	R26 = 15
	R27 = 16
	R28 = 17
	R31 = 18
	R32 = 19
	R33 = 20
	R34 = 21
	R35 = 22
	R36 = 23
	R37 = 24
	R38 = 25
	R41 = 26
	R42 = 27
	R43 = 28
	R44 = 29
	R45 = 30
	R46 = 31
	R47 = 32
	R48 = 33
	RA1 = 34
	RA2 = 35
	RA3 = 36
	RA4 = 37
	RA5 = 38
	RA6 = 39
	RA7 = 40
	RA8 = 41
	RB1 = 42
	RB2 = 43
	RB3 = 44
	RB4 = 45
	RB5 = 46
	RB6 = 47
	RB7 = 48
	RB8 = 49
	RC1 = 50
	RC2 = 51
	RC3 = 52
	RC4 = 53
	RC5 = 54
	RC6 = 55
	RC7 = 56
	RC8 = 57
	RD1 = 58
	RD2 = 59
	RD3 = 60
	RD4 = 61
	RD5 = 62
	RD6 = 63
	RD7 = 64
	RD8 = 65
	RE1 = 66
	RE2 = 67
	RE3 = 68
	RE4 = 69
	RE5 = 70
	RE6 = 71
	RE7 = 72
	RE8 = 73
	RF1 = 74
	RF2 = 75
	RF3 = 76
	RF4 = 77
	RF5 = 78
	RF6 = 79
	RF7 = 80
	RF8 = 81
	RG1 = 82
	RG2 = 83
	RG3 = 84
	RG4 = 85
	RG5 = 86
	RG6 = 87
	RG7 = 88
	RG8 = 89
	RH1 = 90
	RH2 = 91
	RH3 = 92
	RH4 = 93
	RH5 = 94
	RH6 = 95
	RH7 = 96
	RH8 = 97


# noinspection SpellCheckingInspection
class ConnectorTuple(Enum):
	"""7 Members, CT12 ... CT78"""
	CT12 = 0
	CT14 = 1
	CT18 = 2
	CT34 = 3
	CT56 = 4
	CT58 = 5
	CT78 = 6


# noinspection SpellCheckingInspection
class DecodeStatus(Enum):
	"""3 Members, INV ... OK"""
	INV = 0
	NAV = 1
	OK = 2


# noinspection SpellCheckingInspection
class DisplayMode(Enum):
	"""2 Members, ABSolute ... RELative"""
	ABSolute = 0
	RELative = 1


# noinspection SpellCheckingInspection
class EvmMethod(Enum):
	"""3 Members, ST1999 ... ST2016"""
	ST1999 = 0
	ST2007 = 1
	ST2016 = 2


# noinspection SpellCheckingInspection
class FftOffset(Enum):
	"""3 Members, AUTO ... PEAK"""
	AUTO = 0
	CENT = 1
	PEAK = 2


# noinspection SpellCheckingInspection
class FrequencyBand(Enum):
	"""4 Members, B24Ghz ... B6GHz"""
	B24Ghz = 0
	B4GHz = 1
	B5GHz = 2
	B6GHz = 3


# noinspection SpellCheckingInspection
class GuardInterval(Enum):
	"""5 Members, GI08 ... SHORt"""
	GI08 = 0
	GI16 = 1
	GI32 = 2
	LONG = 3
	SHORt = 4


# noinspection SpellCheckingInspection
class GuiScenario(Enum):
	"""8 Members, CSPath ... UNDefined"""
	CSPath = 0
	MIMO2x2 = 1
	MIMO4x4 = 2
	MIMO8x8 = 3
	SALone = 4
	SMI4 = 5
	TMIMo = 6
	UNDefined = 7


# noinspection SpellCheckingInspection
class IeeeStandard(Enum):
	"""7 Members, DSSS ... VHTofdm"""
	DSSS = 0
	EHTofdm = 1
	HEOFdm = 2
	HTOFdm = 3
	LOFDm = 4
	POFDm = 5
	VHTofdm = 6


# noinspection SpellCheckingInspection
class LowHigh(Enum):
	"""2 Members, HIGH ... LOW"""
	HIGH = 0
	LOW = 1


# noinspection SpellCheckingInspection
class LtfSize(Enum):
	"""3 Members, LTF1 ... LTF4"""
	LTF1 = 0
	LTF2 = 1
	LTF4 = 2


# noinspection SpellCheckingInspection
class MimoScenario(Enum):
	"""10 Members, CSPath ... UNDefined"""
	CSPath = 0
	MIMO2x2 = 1
	MIMO4x4 = 2
	MIMO8x8 = 3
	SALone = 4
	SMI4 = 5
	TMIM2x2 = 6
	TMIM3x3 = 7
	TMIM4x4 = 8
	UNDefined = 9


# noinspection SpellCheckingInspection
class ModulationFilter(Enum):
	"""11 Members, ALL ... QPSK"""
	ALL = 0
	BPSK = 1
	CCK11 = 2
	CCK5_5 = 3
	DBPSk = 4
	DQPSk = 5
	QAM1024 = 6
	QAM16 = 7
	QAM256 = 8
	QAM64 = 9
	QPSK = 10


# noinspection SpellCheckingInspection
class ModulationTypeB(Enum):
	"""32 Members, BP1_5 ... QR34"""
	BP1_5 = 0
	BP2_25 = 1
	BP3 = 2
	BP4_5 = 3
	BPM6 = 4
	BPM9 = 5
	BR12 = 6
	Q1M12 = 7
	Q1M18 = 8
	Q1M24 = 9
	Q1M36 = 10
	Q1M6 = 11
	Q1M9 = 12
	Q1R12 = 13
	Q1R34 = 14
	Q6M12 = 15
	Q6M135 = 16
	Q6M24 = 17
	Q6M27 = 18
	Q6M48 = 19
	Q6M54 = 20
	Q6R23 = 21
	Q6R34 = 22
	Q6R56 = 23
	QM12 = 24
	QM18 = 25
	QM3 = 26
	QM4_5 = 27
	QM6 = 28
	QM9 = 29
	QR12 = 30
	QR34 = 31


# noinspection SpellCheckingInspection
class ModulationTypeC(Enum):
	"""4 Members, CCK11 ... DQPSk2"""
	CCK11 = 0
	CCK5 = 1
	DBPSk1 = 2
	DQPSk2 = 3


# noinspection SpellCheckingInspection
class ModulationTypeD(Enum):
	"""28 Members, _16Q ... UNSPecified"""
	_16Q = 0
	_16Q12 = 1
	_16Q14 = 2
	_16Q34 = 3
	_16Q38 = 4
	_1KQ = 5
	_1KQ34 = 6
	_1KQ56 = 7
	_256Q = 8
	_256Q34 = 9
	_256Q56 = 10
	_4KQ = 11
	_4KQ34 = 12
	_4KQ56 = 13
	_64Q = 14
	_64Q12 = 15
	_64Q23 = 16
	_64Q34 = 17
	_64Q56 = 18
	BPSK = 19
	BPSK12 = 20
	BPSK14 = 21
	BPSK34 = 22
	QPSK = 23
	QPSK12 = 24
	QPSK14 = 25
	QPSK34 = 26
	UNSPecified = 27


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class PlcpType(Enum):
	"""2 Members, LONGplcp ... SHORtplcp"""
	LONGplcp = 0
	SHORtplcp = 1


# noinspection SpellCheckingInspection
class PowerClass(Enum):
	"""4 Members, CLA ... USERdefined"""
	CLA = 0
	CLB = 1
	CLCD = 2
	USERdefined = 3


# noinspection SpellCheckingInspection
class ReceiveMode(Enum):
	"""4 Members, CMIMo ... TMIMo"""
	CMIMo = 0
	SISO = 1
	SMIMo = 2
	TMIMo = 3


# noinspection SpellCheckingInspection
class RefPower(Enum):
	"""2 Members, MAXimum ... MEAN"""
	MAXimum = 0
	MEAN = 1


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
class RxConnectorExt(Enum):
	"""219 Members, I11I ... RH8"""
	I11I = 0
	I12O = 1
	I13I = 2
	I14O = 3
	I15I = 4
	I16O = 5
	I17I = 6
	I18O = 7
	I21I = 8
	I22O = 9
	I23I = 10
	I24O = 11
	I25I = 12
	I26O = 13
	I27I = 14
	I28O = 15
	I31I = 16
	I32O = 17
	I33I = 18
	I34O = 19
	I35I = 20
	I36O = 21
	I37I = 22
	I38O = 23
	I41I = 24
	I42O = 25
	I43I = 26
	I44O = 27
	I45I = 28
	I46O = 29
	I47I = 30
	I48O = 31
	IFI1 = 32
	IFI2 = 33
	IFI3 = 34
	IFI4 = 35
	IFI5 = 36
	IFI6 = 37
	IFO1 = 38
	IFO2 = 39
	IFO3 = 40
	IFO4 = 41
	IFO5 = 42
	IFO6 = 43
	IQ1I = 44
	IQ2O = 45
	IQ3I = 46
	IQ4O = 47
	IQ5I = 48
	IQ6O = 49
	IQ7I = 50
	IQ8O = 51
	R10D = 52
	R11 = 53
	R118 = 54
	R1183 = 55
	R1184 = 56
	R11C = 57
	R11D = 58
	R11O = 59
	R11O3 = 60
	R11O4 = 61
	R12 = 62
	R12C = 63
	R12D = 64
	R12I = 65
	R13 = 66
	R13C = 67
	R13O = 68
	R14 = 69
	R14C = 70
	R14I = 71
	R15 = 72
	R16 = 73
	R17 = 74
	R18 = 75
	R21 = 76
	R214 = 77
	R218 = 78
	R21C = 79
	R21O = 80
	R22 = 81
	R22C = 82
	R22I = 83
	R23 = 84
	R23C = 85
	R23O = 86
	R24 = 87
	R24C = 88
	R24I = 89
	R25 = 90
	R258 = 91
	R26 = 92
	R27 = 93
	R28 = 94
	R31 = 95
	R318 = 96
	R31C = 97
	R31O = 98
	R32 = 99
	R32C = 100
	R32I = 101
	R33 = 102
	R33C = 103
	R33O = 104
	R34 = 105
	R34C = 106
	R34I = 107
	R35 = 108
	R36 = 109
	R37 = 110
	R38 = 111
	R41 = 112
	R418 = 113
	R41C = 114
	R41O = 115
	R42 = 116
	R42C = 117
	R42I = 118
	R43 = 119
	R43C = 120
	R43O = 121
	R44 = 122
	R44C = 123
	R44I = 124
	R45 = 125
	R46 = 126
	R47 = 127
	R48 = 128
	RA1 = 129
	RA18 = 130
	RA2 = 131
	RA3 = 132
	RA4 = 133
	RA5 = 134
	RA6 = 135
	RA7 = 136
	RA8 = 137
	RB1 = 138
	RB14 = 139
	RB18 = 140
	RB2 = 141
	RB3 = 142
	RB4 = 143
	RB5 = 144
	RB6 = 145
	RB7 = 146
	RB8 = 147
	RC1 = 148
	RC18 = 149
	RC2 = 150
	RC3 = 151
	RC4 = 152
	RC5 = 153
	RC6 = 154
	RC7 = 155
	RC8 = 156
	RD1 = 157
	RD18 = 158
	RD2 = 159
	RD3 = 160
	RD4 = 161
	RD5 = 162
	RD6 = 163
	RD7 = 164
	RD8 = 165
	RE1 = 166
	RE18 = 167
	RE2 = 168
	RE3 = 169
	RE4 = 170
	RE5 = 171
	RE6 = 172
	RE7 = 173
	RE8 = 174
	RF1 = 175
	RF18 = 176
	RF1C = 177
	RF1O = 178
	RF2 = 179
	RF2C = 180
	RF2I = 181
	RF3 = 182
	RF3C = 183
	RF3O = 184
	RF4 = 185
	RF4C = 186
	RF4I = 187
	RF5 = 188
	RF5C = 189
	RF6 = 190
	RF6C = 191
	RF7 = 192
	RF7C = 193
	RF8 = 194
	RF8C = 195
	RF9C = 196
	RFAC = 197
	RFAO = 198
	RFBC = 199
	RFBI = 200
	RG1 = 201
	RG18 = 202
	RG2 = 203
	RG3 = 204
	RG4 = 205
	RG5 = 206
	RG6 = 207
	RG7 = 208
	RG8 = 209
	RH1 = 210
	RH18 = 211
	RH2 = 212
	RH3 = 213
	RH4 = 214
	RH5 = 215
	RH6 = 216
	RH7 = 217
	RH8 = 218


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
class RxTxConverter(Enum):
	"""80 Members, IRX1 ... TX44"""
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
	ITX1 = 20
	ITX11 = 21
	ITX12 = 22
	ITX13 = 23
	ITX14 = 24
	ITX2 = 25
	ITX21 = 26
	ITX22 = 27
	ITX23 = 28
	ITX24 = 29
	ITX3 = 30
	ITX31 = 31
	ITX32 = 32
	ITX33 = 33
	ITX34 = 34
	ITX4 = 35
	ITX41 = 36
	ITX42 = 37
	ITX43 = 38
	ITX44 = 39
	RX1 = 40
	RX11 = 41
	RX12 = 42
	RX13 = 43
	RX14 = 44
	RX2 = 45
	RX21 = 46
	RX22 = 47
	RX23 = 48
	RX24 = 49
	RX3 = 50
	RX31 = 51
	RX32 = 52
	RX33 = 53
	RX34 = 54
	RX4 = 55
	RX41 = 56
	RX42 = 57
	RX43 = 58
	RX44 = 59
	TX1 = 60
	TX11 = 61
	TX12 = 62
	TX13 = 63
	TX14 = 64
	TX2 = 65
	TX21 = 66
	TX22 = 67
	TX23 = 68
	TX24 = 69
	TX3 = 70
	TX31 = 71
	TX32 = 72
	TX33 = 73
	TX34 = 74
	TX4 = 75
	TX41 = 76
	TX42 = 77
	TX43 = 78
	TX44 = 79


# noinspection SpellCheckingInspection
class SlopeType(Enum):
	"""2 Members, NEGative ... POSitive"""
	NEGative = 0
	POSitive = 1


# noinspection SpellCheckingInspection
class StopCondition(Enum):
	"""2 Members, NONE ... SLFail"""
	NONE = 0
	SLFail = 1


# noinspection SpellCheckingInspection
class SynchroMode(Enum):
	"""2 Members, NORMal ... TOLerant"""
	NORMal = 0
	TOLerant = 1


# noinspection SpellCheckingInspection
class TrainingMode(Enum):
	"""2 Members, MMODe ... TMODe"""
	MMODe = 0
	TMODe = 1


# noinspection SpellCheckingInspection
class TriggerSlope(Enum):
	"""4 Members, FEDGe ... REDGe"""
	FEDGe = 0
	OFF = 1
	ON = 2
	REDGe = 3
