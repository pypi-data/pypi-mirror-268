from enum import Enum


# noinspection SpellCheckingInspection
class AcceptAttachCause(Enum):
	"""3 Members, C18 ... ON"""
	C18 = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class AccStratRelease(Enum):
	"""9 Members, REL10 ... REL9"""
	REL10 = 0
	REL11 = 1
	REL12 = 2
	REL13 = 3
	REL14 = 4
	REL15 = 5
	REL16 = 6
	REL8 = 7
	REL9 = 8


# noinspection SpellCheckingInspection
class AddSpectrumEmission(Enum):
	"""288 Members, NS01 ... NS99"""
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
	NS101 = 11
	NS102 = 12
	NS103 = 13
	NS104 = 14
	NS105 = 15
	NS106 = 16
	NS107 = 17
	NS108 = 18
	NS109 = 19
	NS11 = 20
	NS110 = 21
	NS111 = 22
	NS112 = 23
	NS113 = 24
	NS114 = 25
	NS115 = 26
	NS116 = 27
	NS117 = 28
	NS118 = 29
	NS119 = 30
	NS12 = 31
	NS120 = 32
	NS121 = 33
	NS122 = 34
	NS123 = 35
	NS124 = 36
	NS125 = 37
	NS126 = 38
	NS127 = 39
	NS128 = 40
	NS129 = 41
	NS13 = 42
	NS130 = 43
	NS131 = 44
	NS132 = 45
	NS133 = 46
	NS134 = 47
	NS135 = 48
	NS136 = 49
	NS137 = 50
	NS138 = 51
	NS139 = 52
	NS14 = 53
	NS140 = 54
	NS141 = 55
	NS142 = 56
	NS143 = 57
	NS144 = 58
	NS145 = 59
	NS146 = 60
	NS147 = 61
	NS148 = 62
	NS149 = 63
	NS15 = 64
	NS150 = 65
	NS151 = 66
	NS152 = 67
	NS153 = 68
	NS154 = 69
	NS155 = 70
	NS156 = 71
	NS157 = 72
	NS158 = 73
	NS159 = 74
	NS16 = 75
	NS160 = 76
	NS161 = 77
	NS162 = 78
	NS163 = 79
	NS164 = 80
	NS165 = 81
	NS166 = 82
	NS167 = 83
	NS168 = 84
	NS169 = 85
	NS17 = 86
	NS170 = 87
	NS171 = 88
	NS172 = 89
	NS173 = 90
	NS174 = 91
	NS175 = 92
	NS176 = 93
	NS177 = 94
	NS178 = 95
	NS179 = 96
	NS18 = 97
	NS180 = 98
	NS181 = 99
	NS182 = 100
	NS183 = 101
	NS184 = 102
	NS185 = 103
	NS186 = 104
	NS187 = 105
	NS188 = 106
	NS189 = 107
	NS19 = 108
	NS190 = 109
	NS191 = 110
	NS192 = 111
	NS193 = 112
	NS194 = 113
	NS195 = 114
	NS196 = 115
	NS197 = 116
	NS198 = 117
	NS199 = 118
	NS20 = 119
	NS200 = 120
	NS201 = 121
	NS202 = 122
	NS203 = 123
	NS204 = 124
	NS205 = 125
	NS206 = 126
	NS207 = 127
	NS208 = 128
	NS209 = 129
	NS21 = 130
	NS210 = 131
	NS211 = 132
	NS212 = 133
	NS213 = 134
	NS214 = 135
	NS215 = 136
	NS216 = 137
	NS217 = 138
	NS218 = 139
	NS219 = 140
	NS22 = 141
	NS220 = 142
	NS221 = 143
	NS222 = 144
	NS223 = 145
	NS224 = 146
	NS225 = 147
	NS226 = 148
	NS227 = 149
	NS228 = 150
	NS229 = 151
	NS23 = 152
	NS230 = 153
	NS231 = 154
	NS232 = 155
	NS233 = 156
	NS234 = 157
	NS235 = 158
	NS236 = 159
	NS237 = 160
	NS238 = 161
	NS239 = 162
	NS24 = 163
	NS240 = 164
	NS241 = 165
	NS242 = 166
	NS243 = 167
	NS244 = 168
	NS245 = 169
	NS246 = 170
	NS247 = 171
	NS248 = 172
	NS249 = 173
	NS25 = 174
	NS250 = 175
	NS251 = 176
	NS252 = 177
	NS253 = 178
	NS254 = 179
	NS255 = 180
	NS256 = 181
	NS257 = 182
	NS258 = 183
	NS259 = 184
	NS26 = 185
	NS260 = 186
	NS261 = 187
	NS262 = 188
	NS263 = 189
	NS264 = 190
	NS265 = 191
	NS266 = 192
	NS267 = 193
	NS268 = 194
	NS269 = 195
	NS27 = 196
	NS270 = 197
	NS271 = 198
	NS272 = 199
	NS273 = 200
	NS274 = 201
	NS275 = 202
	NS276 = 203
	NS277 = 204
	NS278 = 205
	NS279 = 206
	NS28 = 207
	NS280 = 208
	NS281 = 209
	NS282 = 210
	NS283 = 211
	NS284 = 212
	NS285 = 213
	NS286 = 214
	NS287 = 215
	NS288 = 216
	NS29 = 217
	NS30 = 218
	NS31 = 219
	NS32 = 220
	NS33 = 221
	NS34 = 222
	NS35 = 223
	NS36 = 224
	NS37 = 225
	NS38 = 226
	NS39 = 227
	NS40 = 228
	NS41 = 229
	NS42 = 230
	NS43 = 231
	NS44 = 232
	NS45 = 233
	NS46 = 234
	NS47 = 235
	NS48 = 236
	NS49 = 237
	NS50 = 238
	NS51 = 239
	NS52 = 240
	NS53 = 241
	NS54 = 242
	NS55 = 243
	NS56 = 244
	NS57 = 245
	NS58 = 246
	NS59 = 247
	NS60 = 248
	NS61 = 249
	NS62 = 250
	NS63 = 251
	NS64 = 252
	NS65 = 253
	NS66 = 254
	NS67 = 255
	NS68 = 256
	NS69 = 257
	NS70 = 258
	NS71 = 259
	NS72 = 260
	NS73 = 261
	NS74 = 262
	NS75 = 263
	NS76 = 264
	NS77 = 265
	NS78 = 266
	NS79 = 267
	NS80 = 268
	NS81 = 269
	NS82 = 270
	NS83 = 271
	NS84 = 272
	NS85 = 273
	NS86 = 274
	NS87 = 275
	NS88 = 276
	NS89 = 277
	NS90 = 278
	NS91 = 279
	NS92 = 280
	NS93 = 281
	NS94 = 282
	NS95 = 283
	NS96 = 284
	NS97 = 285
	NS98 = 286
	NS99 = 287


# noinspection SpellCheckingInspection
class Aggregationlevel(Enum):
	"""6 Members, AUTO ... D8U8"""
	AUTO = 0
	D1U1 = 1
	D4U2 = 2
	D4U4 = 3
	D8U4 = 4
	D8U8 = 5


# noinspection SpellCheckingInspection
class AntennaPorts(Enum):
	"""5 Members, NONE ... P1522"""
	NONE = 0
	P15 = 1
	P1516 = 2
	P1518 = 3
	P1522 = 4


# noinspection SpellCheckingInspection
class AntennasTxA(Enum):
	"""3 Members, FOUR ... TWO"""
	FOUR = 0
	ONE = 1
	TWO = 2


# noinspection SpellCheckingInspection
class AntennasTxB(Enum):
	"""3 Members, EIGHt ... TWO"""
	EIGHt = 0
	FOUR = 1
	TWO = 2


# noinspection SpellCheckingInspection
class AutoManualModeExt(Enum):
	"""3 Members, AUTO ... SEMiauto"""
	AUTO = 0
	MANual = 1
	SEMiauto = 2


# noinspection SpellCheckingInspection
class AwgnMeasurement(Enum):
	"""3 Members, NOISe ... SIGNal"""
	NOISe = 0
	OFF = 1
	SIGNal = 2


# noinspection SpellCheckingInspection
class BandClass(Enum):
	"""21 Members, AWS ... USPC"""
	AWS = 0
	B18M = 1
	IEXT = 2
	IM2K = 3
	JTAC = 4
	KCEL = 5
	KPCS = 6
	LO7C = 7
	N45T = 8
	NA7C = 9
	NA8S = 10
	NA9C = 11
	NAPC = 12
	PA4M = 13
	PA8M = 14
	PS7C = 15
	TACS = 16
	U25B = 17
	U25F = 18
	USC = 19
	USPC = 20


# noinspection SpellCheckingInspection
class BandIndicator(Enum):
	"""2 Members, G18 ... G19"""
	G18 = 0
	G19 = 1


# noinspection SpellCheckingInspection
class Bandwidth(Enum):
	"""6 Members, B014 ... B200"""
	B014 = 0
	B030 = 1
	B050 = 2
	B100 = 3
	B150 = 4
	B200 = 5


# noinspection SpellCheckingInspection
class BasebandBoard(Enum):
	"""140 Members, BBR1 ... SUW44"""
	BBR1 = 0
	BBR11 = 1
	BBR12 = 2
	BBR13 = 3
	BBR14 = 4
	BBR2 = 5
	BBR21 = 6
	BBR22 = 7
	BBR23 = 8
	BBR24 = 9
	BBR3 = 10
	BBR31 = 11
	BBR32 = 12
	BBR33 = 13
	BBR34 = 14
	BBR4 = 15
	BBR41 = 16
	BBR42 = 17
	BBR43 = 18
	BBR44 = 19
	BBT1 = 20
	BBT11 = 21
	BBT12 = 22
	BBT13 = 23
	BBT14 = 24
	BBT2 = 25
	BBT21 = 26
	BBT22 = 27
	BBT23 = 28
	BBT24 = 29
	BBT3 = 30
	BBT31 = 31
	BBT32 = 32
	BBT33 = 33
	BBT34 = 34
	BBT4 = 35
	BBT41 = 36
	BBT42 = 37
	BBT43 = 38
	BBT44 = 39
	SUA012 = 40
	SUA034 = 41
	SUA056 = 42
	SUA078 = 43
	SUA1 = 44
	SUA11 = 45
	SUA112 = 46
	SUA12 = 47
	SUA13 = 48
	SUA134 = 49
	SUA14 = 50
	SUA15 = 51
	SUA156 = 52
	SUA16 = 53
	SUA17 = 54
	SUA178 = 55
	SUA18 = 56
	SUA2 = 57
	SUA21 = 58
	SUA212 = 59
	SUA22 = 60
	SUA23 = 61
	SUA234 = 62
	SUA24 = 63
	SUA25 = 64
	SUA256 = 65
	SUA26 = 66
	SUA27 = 67
	SUA278 = 68
	SUA28 = 69
	SUA3 = 70
	SUA31 = 71
	SUA312 = 72
	SUA32 = 73
	SUA33 = 74
	SUA334 = 75
	SUA34 = 76
	SUA35 = 77
	SUA356 = 78
	SUA36 = 79
	SUA37 = 80
	SUA378 = 81
	SUA38 = 82
	SUA4 = 83
	SUA41 = 84
	SUA412 = 85
	SUA42 = 86
	SUA43 = 87
	SUA434 = 88
	SUA44 = 89
	SUA45 = 90
	SUA456 = 91
	SUA46 = 92
	SUA47 = 93
	SUA478 = 94
	SUA48 = 95
	SUA5 = 96
	SUA6 = 97
	SUA7 = 98
	SUA8 = 99
	SUU1 = 100
	SUU11 = 101
	SUU12 = 102
	SUU13 = 103
	SUU14 = 104
	SUU2 = 105
	SUU21 = 106
	SUU22 = 107
	SUU23 = 108
	SUU24 = 109
	SUU3 = 110
	SUU31 = 111
	SUU32 = 112
	SUU33 = 113
	SUU34 = 114
	SUU4 = 115
	SUU41 = 116
	SUU42 = 117
	SUU43 = 118
	SUU44 = 119
	SUW1 = 120
	SUW11 = 121
	SUW12 = 122
	SUW13 = 123
	SUW14 = 124
	SUW2 = 125
	SUW21 = 126
	SUW22 = 127
	SUW23 = 128
	SUW24 = 129
	SUW3 = 130
	SUW31 = 131
	SUW32 = 132
	SUW33 = 133
	SUW34 = 134
	SUW4 = 135
	SUW41 = 136
	SUW42 = 137
	SUW43 = 138
	SUW44 = 139


# noinspection SpellCheckingInspection
class BeamformingMode(Enum):
	"""4 Members, OFF ... TSBF"""
	OFF = 0
	ON = 1
	PMAT = 2
	TSBF = 3


# noinspection SpellCheckingInspection
class BeamformingNoOfLayers(Enum):
	"""3 Members, L1 ... L2"""
	L1 = 0
	L1I = 1
	L2 = 2


# noinspection SpellCheckingInspection
class BlerAlgorithm(Enum):
	"""4 Members, ERC1 ... ERC4"""
	ERC1 = 0
	ERC2 = 1
	ERC3 = 2
	ERC4 = 3


# noinspection SpellCheckingInspection
class BlerStopCondition(Enum):
	"""5 Members, AC1St ... SCC2"""
	AC1St = 0
	ACWait = 1
	PCC = 2
	SCC1 = 3
	SCC2 = 4


# noinspection SpellCheckingInspection
class Bursts(Enum):
	"""2 Members, FBURst ... RBURst"""
	FBURst = 0
	RBURst = 1


# noinspection SpellCheckingInspection
class CarrAggregationMode(Enum):
	"""2 Members, INTRaband ... OFF"""
	INTRaband = 0
	OFF = 1


# noinspection SpellCheckingInspection
class Cdma2kBand(Enum):
	"""18 Members, BC0 ... BC9"""
	BC0 = 0
	BC1 = 1
	BC10 = 2
	BC11 = 3
	BC12 = 4
	BC13 = 5
	BC14 = 6
	BC15 = 7
	BC16 = 8
	BC17 = 9
	BC2 = 10
	BC3 = 11
	BC4 = 12
	BC5 = 13
	BC6 = 14
	BC7 = 15
	BC8 = 16
	BC9 = 17


# noinspection SpellCheckingInspection
class CePucchRepsA(Enum):
	"""4 Members, R1 ... R8"""
	R1 = 0
	R2 = 1
	R4 = 2
	R8 = 3


# noinspection SpellCheckingInspection
class CePucchRepsB(Enum):
	"""6 Members, R128 ... R8"""
	R128 = 0
	R16 = 1
	R32 = 2
	R4 = 3
	R64 = 4
	R8 = 5


# noinspection SpellCheckingInspection
class CeRepetitionsA(Enum):
	"""6 Members, R1 ... R8"""
	R1 = 0
	R16 = 1
	R2 = 2
	R32 = 3
	R4 = 4
	R8 = 5


# noinspection SpellCheckingInspection
class CeRepetitionsB(Enum):
	"""15 Members, R1 ... R8"""
	R1 = 0
	R1024 = 1
	R128 = 2
	R1536 = 3
	R16 = 4
	R192 = 5
	R2048 = 6
	R256 = 7
	R32 = 8
	R384 = 9
	R4 = 10
	R512 = 11
	R64 = 12
	R768 = 13
	R8 = 14


# noinspection SpellCheckingInspection
class Confidence(Enum):
	"""6 Members, EFAil ... UNDecided"""
	EFAil = 0
	EPASs = 1
	FAIL = 2
	PASS = 3
	RUNNing = 4
	UNDecided = 5


# noinspection SpellCheckingInspection
class ConnectionType(Enum):
	"""2 Members, DAPPlication ... TESTmode"""
	DAPPlication = 0
	TESTmode = 1


# noinspection SpellCheckingInspection
class CoverageEnhMode(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class CqiMode(Enum):
	"""6 Members, FCPRi ... TTIBased"""
	FCPRi = 0
	FCRI = 1
	FPMI = 2
	FPRI = 3
	FWB = 4
	TTIBased = 5


# noinspection SpellCheckingInspection
class CsbfDestination(Enum):
	"""5 Members, CDMA ... WCDMa"""
	CDMA = 0
	GSM = 1
	NONE = 2
	TDSCdma = 3
	WCDMa = 4


# noinspection SpellCheckingInspection
class CsiReportingMode(Enum):
	"""2 Members, S1 ... S2"""
	S1 = 0
	S2 = 1


# noinspection SpellCheckingInspection
class CsirsMode(Enum):
	"""2 Members, ACSirs ... MANual"""
	ACSirs = 0
	MANual = 1


# noinspection SpellCheckingInspection
class CyclicPrefix(Enum):
	"""2 Members, EXTended ... NORMal"""
	EXTended = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class DciFormat(Enum):
	"""8 Members, D1 ... D61"""
	D1 = 0
	D1A = 1
	D1B = 2
	D2 = 3
	D2A = 4
	D2B = 5
	D2C = 6
	D61 = 7


# noinspection SpellCheckingInspection
class DedBearerProfile(Enum):
	"""4 Members, DRAM ... VOICe"""
	DRAM = 0
	DRUM = 1
	VIDeo = 2
	VOICe = 3


# noinspection SpellCheckingInspection
class DeviceType(Enum):
	"""1 Members, NBFBcopt ... NBFBcopt"""
	NBFBcopt = 0


# noinspection SpellCheckingInspection
class DownlinkNarrowBandPosition(Enum):
	"""4 Members, GPP3 ... MID"""
	GPP3 = 0
	HIGH = 1
	LOW = 2
	MID = 3


# noinspection SpellCheckingInspection
class DownlinkRsrcBlockPosition(Enum):
	"""7 Members, HIGH ... P5"""
	HIGH = 0
	LOW = 1
	P10 = 2
	P23 = 3
	P35 = 4
	P48 = 5
	P5 = 6


# noinspection SpellCheckingInspection
class DpCycle(Enum):
	"""4 Members, P032 ... P256"""
	P032 = 0
	P064 = 1
	P128 = 2
	P256 = 3


# noinspection SpellCheckingInspection
class DsTime(Enum):
	"""4 Members, OFF ... P2H"""
	OFF = 0
	ON = 1
	P1H = 2
	P2H = 3


# noinspection SpellCheckingInspection
class DuplexMode(Enum):
	"""3 Members, FDD ... TDD"""
	FDD = 0
	FTDD = 1
	TDD = 2


# noinspection SpellCheckingInspection
class EblerStopCondition(Enum):
	"""2 Members, CLEVel ... NONE"""
	CLEVel = 0
	NONE = 1


# noinspection SpellCheckingInspection
class EmtcRmcPattern(Enum):
	"""5 Members, P1 ... P5"""
	P1 = 0
	P2 = 1
	P3 = 2
	P4 = 3
	P5 = 4


# noinspection SpellCheckingInspection
class EnableCqiReport(Enum):
	"""2 Members, OFF ... PERiodic"""
	OFF = 0
	PERiodic = 1


# noinspection SpellCheckingInspection
class EnableDrx(Enum):
	"""5 Members, DRXL ... UDEFined"""
	DRXL = 0
	DRXS = 1
	OFF = 2
	ON = 3
	UDEFined = 4


# noinspection SpellCheckingInspection
class EnablePreambles(Enum):
	"""3 Members, NIPReambles ... ON"""
	NIPReambles = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class FadingBoard(Enum):
	"""60 Members, FAD012 ... FAD8"""
	FAD012 = 0
	FAD034 = 1
	FAD056 = 2
	FAD078 = 3
	FAD1 = 4
	FAD11 = 5
	FAD112 = 6
	FAD12 = 7
	FAD13 = 8
	FAD134 = 9
	FAD14 = 10
	FAD15 = 11
	FAD156 = 12
	FAD16 = 13
	FAD17 = 14
	FAD178 = 15
	FAD18 = 16
	FAD2 = 17
	FAD21 = 18
	FAD212 = 19
	FAD22 = 20
	FAD23 = 21
	FAD234 = 22
	FAD24 = 23
	FAD25 = 24
	FAD256 = 25
	FAD26 = 26
	FAD27 = 27
	FAD278 = 28
	FAD28 = 29
	FAD3 = 30
	FAD31 = 31
	FAD312 = 32
	FAD32 = 33
	FAD33 = 34
	FAD334 = 35
	FAD34 = 36
	FAD35 = 37
	FAD356 = 38
	FAD36 = 39
	FAD37 = 40
	FAD378 = 41
	FAD38 = 42
	FAD4 = 43
	FAD41 = 44
	FAD412 = 45
	FAD42 = 46
	FAD43 = 47
	FAD434 = 48
	FAD44 = 49
	FAD45 = 50
	FAD456 = 51
	FAD46 = 52
	FAD47 = 53
	FAD478 = 54
	FAD48 = 55
	FAD5 = 56
	FAD6 = 57
	FAD7 = 58
	FAD8 = 59


# noinspection SpellCheckingInspection
class FadingMatrixMode(Enum):
	"""3 Members, KRONecker ... SCWI"""
	KRONecker = 0
	NORMal = 1
	SCWI = 2


# noinspection SpellCheckingInspection
class FadingMode(Enum):
	"""2 Members, NORMal ... USER"""
	NORMal = 0
	USER = 1


# noinspection SpellCheckingInspection
class FadingProfile(Enum):
	"""41 Members, CTESt ... USER"""
	CTESt = 0
	EP5High = 1
	EP5Low = 2
	EP5Medium = 3
	ET3High = 4
	ET3Low = 5
	ET3Medium = 6
	ET7High = 7
	ET7Low = 8
	ET7Medium = 9
	ETH30 = 10
	ETL30 = 11
	ETM30 = 12
	EV5High = 13
	EV5Low = 14
	EV5Medium = 15
	EV7High = 16
	EV7Low = 17
	EV7Medium = 18
	EVH200 = 19
	EVL200 = 20
	EVM200 = 21
	HST = 22
	HST2 = 23
	HSTRain = 24
	IILS = 25
	IINL = 26
	IRALos = 27
	IRANlos = 28
	ISALos = 29
	ISANlos = 30
	IUALos = 31
	IUANlos = 32
	IULS = 33
	IUNLos1 = 34
	IUNLos2 = 35
	UMA3 = 36
	UMA30 = 37
	UMI3 = 38
	UMI30 = 39
	USER = 40


# noinspection SpellCheckingInspection
class FilterCoefficient(Enum):
	"""2 Members, FC4 ... FC8"""
	FC4 = 0
	FC8 = 1


# noinspection SpellCheckingInspection
class FilterRsrpqCoefficient(Enum):
	"""2 Members, FC0 ... FC4"""
	FC0 = 0
	FC4 = 1


# noinspection SpellCheckingInspection
class FrameStructure(Enum):
	"""3 Members, T1 ... T3"""
	T1 = 0
	T2 = 1
	T3 = 2


# noinspection SpellCheckingInspection
class GeoScope(Enum):
	"""4 Members, CIMMediate ... PLMN"""
	CIMMediate = 0
	CNORmal = 1
	LOCation = 2
	PLMN = 3


# noinspection SpellCheckingInspection
class GeranBband(Enum):
	"""11 Members, G045 ... G19"""
	G045 = 0
	G048 = 1
	G071 = 2
	G075 = 3
	G081 = 4
	G085 = 5
	G09E = 6
	G09P = 7
	G09R = 8
	G18 = 9
	G19 = 10


# noinspection SpellCheckingInspection
class GsmBand(Enum):
	"""6 Members, G04 ... GT081"""
	G04 = 0
	G085 = 1
	G09 = 2
	G18 = 3
	G19 = 4
	GT081 = 5


# noinspection SpellCheckingInspection
class HandoverDestination(Enum):
	"""6 Members, CDMA ... WCDMa"""
	CDMA = 0
	EVDO = 1
	GSM = 2
	LTE = 3
	TDSCdma = 4
	WCDMa = 5


# noinspection SpellCheckingInspection
class HandoverMode(Enum):
	"""3 Members, HANDover ... REDirection"""
	HANDover = 0
	MTCSfallback = 1
	REDirection = 2


# noinspection SpellCheckingInspection
class HeaderCompression(Enum):
	"""2 Members, ADB ... VVB"""
	ADB = 0
	VVB = 1


# noinspection SpellCheckingInspection
class IdleDrxLength(Enum):
	"""14 Members, L1024 ... L8192"""
	L1024 = 0
	L10240 = 1
	L12288 = 2
	L131072 = 3
	L14336 = 4
	L16384 = 5
	L2048 = 6
	L262144 = 7
	L32768 = 8
	L4096 = 9
	L512 = 10
	L6144 = 11
	L65536 = 12
	L8192 = 13


# noinspection SpellCheckingInspection
class IdleLevel(Enum):
	"""5 Members, LEV0 ... UE"""
	LEV0 = 0
	LEV1 = 1
	LEV2 = 2
	LEV3 = 3
	UE = 4


# noinspection SpellCheckingInspection
class InactivityTimer(Enum):
	"""22 Members, PSF1 ... PSF80"""
	PSF1 = 0
	PSF10 = 1
	PSF100 = 2
	PSF1280 = 3
	PSF1920 = 4
	PSF2 = 5
	PSF20 = 6
	PSF200 = 7
	PSF2560 = 8
	PSF3 = 9
	PSF30 = 10
	PSF300 = 11
	PSF4 = 12
	PSF40 = 13
	PSF5 = 14
	PSF50 = 15
	PSF500 = 16
	PSF6 = 17
	PSF60 = 18
	PSF750 = 19
	PSF8 = 20
	PSF80 = 21


# noinspection SpellCheckingInspection
class InsertLossMode(Enum):
	"""3 Members, LACP ... USER"""
	LACP = 0
	NORMal = 1
	USER = 2


# noinspection SpellCheckingInspection
class InterBandHandoverMode(Enum):
	"""2 Members, BHANdover ... REDirection"""
	BHANdover = 0
	REDirection = 1


# noinspection SpellCheckingInspection
class IntervalA(Enum):
	"""4 Members, I1 ... I8"""
	I1 = 0
	I2 = 1
	I4 = 2
	I8 = 3


# noinspection SpellCheckingInspection
class IntervalB(Enum):
	"""4 Members, I16 ... I8"""
	I16 = 0
	I2 = 1
	I4 = 2
	I8 = 3


# noinspection SpellCheckingInspection
class IntervalC(Enum):
	"""10 Members, S10 ... S80"""
	S10 = 0
	S128 = 1
	S160 = 2
	S20 = 3
	S32 = 4
	S320 = 5
	S40 = 6
	S64 = 7
	S640 = 8
	S80 = 9


# noinspection SpellCheckingInspection
class IpAddress(Enum):
	"""3 Members, IP1 ... IP3"""
	IP1 = 0
	IP2 = 1
	IP3 = 2


# noinspection SpellCheckingInspection
class IpVersion(Enum):
	"""3 Members, IPV4 ... IPV6"""
	IPV4 = 0
	IPV46 = 1
	IPV6 = 2


# noinspection SpellCheckingInspection
class IqOutSampleRate(Enum):
	"""8 Members, M1 ... M9"""
	M1 = 0
	M100 = 1
	M15 = 2
	M19 = 3
	M3 = 4
	M30 = 5
	M7 = 6
	M9 = 7


# noinspection SpellCheckingInspection
class KeepConstant(Enum):
	"""2 Members, DSHift ... SPEed"""
	DSHift = 0
	SPEed = 1


# noinspection SpellCheckingInspection
class LaaPeriod(Enum):
	"""3 Members, MS160 ... MS80"""
	MS160 = 0
	MS40 = 1
	MS80 = 2


# noinspection SpellCheckingInspection
class LaaUePeriod(Enum):
	"""5 Members, MS160 ... MS80"""
	MS160 = 0
	MS320 = 1
	MS40 = 2
	MS640 = 3
	MS80 = 4


# noinspection SpellCheckingInspection
class LastMessageSent(Enum):
	"""4 Members, FAILed ... SUCCessful"""
	FAILed = 0
	OFF = 1
	ON = 2
	SUCCessful = 3


# noinspection SpellCheckingInspection
class LdCycle(Enum):
	"""20 Members, SF10 ... SF80"""
	SF10 = 0
	SF1024 = 1
	SF10240 = 2
	SF128 = 3
	SF1280 = 4
	SF160 = 5
	SF20 = 6
	SF2048 = 7
	SF256 = 8
	SF2560 = 9
	SF32 = 10
	SF320 = 11
	SF40 = 12
	SF512 = 13
	SF5120 = 14
	SF60 = 15
	SF64 = 16
	SF640 = 17
	SF70 = 18
	SF80 = 19


# noinspection SpellCheckingInspection
class LdsPeriod(Enum):
	"""3 Members, M160 ... M80"""
	M160 = 0
	M40 = 1
	M80 = 2


# noinspection SpellCheckingInspection
class LimitErrRation(Enum):
	"""3 Members, P001 ... P050"""
	P001 = 0
	P010 = 1
	P050 = 2


# noinspection SpellCheckingInspection
class LogCategory(Enum):
	"""4 Members, CONTinue ... WARNing"""
	CONTinue = 0
	ERRor = 1
	INFO = 2
	WARNing = 3


# noinspection SpellCheckingInspection
class LogCategory2(Enum):
	"""5 Members, CONTinue ... WARNing"""
	CONTinue = 0
	ERRor = 1
	HIDDen = 2
	INFO = 3
	WARNing = 4


# noinspection SpellCheckingInspection
class LongSmsHandling(Enum):
	"""2 Members, MSMS ... TRUNcate"""
	MSMS = 0
	TRUNcate = 1


# noinspection SpellCheckingInspection
class MainState(Enum):
	"""3 Members, OFF ... RFHandover"""
	OFF = 0
	ON = 1
	RFHandover = 2


# noinspection SpellCheckingInspection
class MaxNuRohcConSes(Enum):
	"""14 Members, CS1024 ... CS8"""
	CS1024 = 0
	CS12 = 1
	CS128 = 2
	CS16 = 3
	CS16384 = 4
	CS2 = 5
	CS24 = 6
	CS256 = 7
	CS32 = 8
	CS4 = 9
	CS48 = 10
	CS512 = 11
	CS64 = 12
	CS8 = 13


# noinspection SpellCheckingInspection
class MeasCellCycle(Enum):
	"""8 Members, OFF ... SF640"""
	OFF = 0
	SF1024 = 1
	SF1280 = 2
	SF160 = 3
	SF256 = 4
	SF320 = 5
	SF512 = 6
	SF640 = 7


# noinspection SpellCheckingInspection
class MessageClass(Enum):
	"""5 Members, CL0 ... NONE"""
	CL0 = 0
	CL1 = 1
	CL2 = 2
	CL3 = 3
	NONE = 4


# noinspection SpellCheckingInspection
class MessageHandling(Enum):
	"""3 Members, FILE ... UCODed"""
	FILE = 0
	INTernal = 1
	UCODed = 2


# noinspection SpellCheckingInspection
class MessageHandlingB(Enum):
	"""2 Members, FILE ... INTernal"""
	FILE = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class MessageType(Enum):
	"""12 Members, AAMBer ... UDETws"""
	AAMBer = 0
	AEXTreme = 1
	APResidentia = 2
	ASEVere = 3
	EARThquake = 4
	ETWarning = 5
	ETWTest = 6
	GFENcing = 7
	TSUNami = 8
	UDCMas = 9
	UDEFined = 10
	UDETws = 11


# noinspection SpellCheckingInspection
class MimoMatrixSelection(Enum):
	"""4 Members, CM3Gpp ... UDEFined"""
	CM3Gpp = 0
	HADamard = 1
	IDENtity = 2
	UDEFined = 3


# noinspection SpellCheckingInspection
class Modulation(Enum):
	"""5 Members, Q1024 ... QPSK"""
	Q1024 = 0
	Q16 = 1
	Q256 = 2
	Q64 = 3
	QPSK = 4


# noinspection SpellCheckingInspection
class MpdcchRepetitions(Enum):
	"""9 Members, MR1 ... MR8"""
	MR1 = 0
	MR128 = 1
	MR16 = 2
	MR2 = 3
	MR256 = 4
	MR32 = 5
	MR4 = 6
	MR64 = 7
	MR8 = 8


# noinspection SpellCheckingInspection
class MprachRepetitions(Enum):
	"""9 Members, R1 ... R8"""
	R1 = 0
	R128 = 1
	R16 = 2
	R2 = 3
	R256 = 4
	R32 = 5
	R4 = 6
	R64 = 7
	R8 = 8


# noinspection SpellCheckingInspection
class MpschArepetitions(Enum):
	"""3 Members, MR16 ... NCON"""
	MR16 = 0
	MR32 = 1
	NCON = 2


# noinspection SpellCheckingInspection
class MpschBrepetitions(Enum):
	"""9 Members, MR1024 ... NCON"""
	MR1024 = 0
	MR1536 = 1
	MR192 = 2
	MR2048 = 3
	MR256 = 4
	MR384 = 5
	MR512 = 6
	MR768 = 7
	NCON = 8


# noinspection SpellCheckingInspection
class MultiClusterDlTable(Enum):
	"""2 Members, DETermined ... UDEFined"""
	DETermined = 0
	UDEFined = 1


# noinspection SpellCheckingInspection
class NbValue(Enum):
	"""11 Members, NB2T ... NBT8"""
	NB2T = 0
	NB4T = 1
	NBT = 2
	NBT128 = 3
	NBT16 = 4
	NBT2 = 5
	NBT256 = 6
	NBT32 = 7
	NBT4 = 8
	NBT64 = 9
	NBT8 = 10


# noinspection SpellCheckingInspection
class NetworkSegment(Enum):
	"""3 Members, A ... C"""
	A = 0
	B = 1
	C = 2


# noinspection SpellCheckingInspection
class NominalPowerMode(Enum):
	"""3 Members, AUToranging ... ULPC"""
	AUToranging = 0
	MANual = 1
	ULPC = 2


# noinspection SpellCheckingInspection
class NoOfDigits(Enum):
	"""2 Members, THRee ... TWO"""
	THRee = 0
	TWO = 1


# noinspection SpellCheckingInspection
class NoOfLayers(Enum):
	"""2 Members, L2 ... L4"""
	L2 = 0
	L4 = 1


# noinspection SpellCheckingInspection
class NumberRb(Enum):
	"""41 Members, N1 ... ZERO"""
	N1 = 0
	N10 = 1
	N100 = 2
	N12 = 3
	N15 = 4
	N16 = 5
	N17 = 6
	N18 = 7
	N2 = 8
	N20 = 9
	N21 = 10
	N24 = 11
	N25 = 12
	N27 = 13
	N3 = 14
	N30 = 15
	N32 = 16
	N36 = 17
	N4 = 18
	N40 = 19
	N42 = 20
	N45 = 21
	N48 = 22
	N5 = 23
	N50 = 24
	N54 = 25
	N6 = 26
	N60 = 27
	N64 = 28
	N7 = 29
	N72 = 30
	N75 = 31
	N8 = 32
	N80 = 33
	N81 = 34
	N83 = 35
	N9 = 36
	N90 = 37
	N92 = 38
	N96 = 39
	ZERO = 40


# noinspection SpellCheckingInspection
class NumberRb2(Enum):
	"""13 Members, N1 ... ZERO"""
	N1 = 0
	N12 = 1
	N15 = 2
	N18 = 3
	N2 = 4
	N21 = 5
	N24 = 6
	N3 = 7
	N4 = 8
	N5 = 9
	N6 = 10
	N9 = 11
	ZERO = 12


# noinspection SpellCheckingInspection
class OccOfdmSymbols(Enum):
	"""15 Members, SYM0 ... SYM9"""
	SYM0 = 0
	SYM1 = 1
	SYM10 = 2
	SYM11 = 3
	SYM12 = 4
	SYM13 = 5
	SYM14 = 6
	SYM2 = 7
	SYM3 = 8
	SYM4 = 9
	SYM5 = 10
	SYM6 = 11
	SYM7 = 12
	SYM8 = 13
	SYM9 = 14


# noinspection SpellCheckingInspection
class OnDurationTimer(Enum):
	"""24 Members, PSF1 ... PSF800"""
	PSF1 = 0
	PSF10 = 1
	PSF100 = 2
	PSF1000 = 3
	PSF1200 = 4
	PSF1600 = 5
	PSF2 = 6
	PSF20 = 7
	PSF200 = 8
	PSF3 = 9
	PSF30 = 10
	PSF300 = 11
	PSF4 = 12
	PSF40 = 13
	PSF400 = 14
	PSF5 = 15
	PSF50 = 16
	PSF500 = 17
	PSF6 = 18
	PSF60 = 19
	PSF600 = 20
	PSF8 = 21
	PSF80 = 22
	PSF800 = 23


# noinspection SpellCheckingInspection
class OperatingBandA(Enum):
	"""3 Members, OB1 ... OB3"""
	OB1 = 0
	OB2 = 1
	OB3 = 2


# noinspection SpellCheckingInspection
class OperatingBandB(Enum):
	"""24 Members, OB1 ... OBS3"""
	OB1 = 0
	OB10 = 1
	OB11 = 2
	OB12 = 3
	OB13 = 4
	OB14 = 5
	OB19 = 6
	OB2 = 7
	OB20 = 8
	OB21 = 9
	OB22 = 10
	OB25 = 11
	OB26 = 12
	OB3 = 13
	OB4 = 14
	OB5 = 15
	OB6 = 16
	OB7 = 17
	OB8 = 18
	OB9 = 19
	OBL1 = 20
	OBS1 = 21
	OBS2 = 22
	OBS3 = 23


# noinspection SpellCheckingInspection
class OperatingBandC(Enum):
	"""71 Members, OB1 ... UDEFined"""
	OB1 = 0
	OB10 = 1
	OB11 = 2
	OB12 = 3
	OB13 = 4
	OB14 = 5
	OB15 = 6
	OB16 = 7
	OB17 = 8
	OB18 = 9
	OB19 = 10
	OB2 = 11
	OB20 = 12
	OB21 = 13
	OB22 = 14
	OB23 = 15
	OB24 = 16
	OB25 = 17
	OB250 = 18
	OB252 = 19
	OB255 = 20
	OB26 = 21
	OB27 = 22
	OB28 = 23
	OB29 = 24
	OB3 = 25
	OB30 = 26
	OB31 = 27
	OB32 = 28
	OB33 = 29
	OB34 = 30
	OB35 = 31
	OB36 = 32
	OB37 = 33
	OB38 = 34
	OB39 = 35
	OB4 = 36
	OB40 = 37
	OB41 = 38
	OB42 = 39
	OB43 = 40
	OB44 = 41
	OB45 = 42
	OB46 = 43
	OB48 = 44
	OB49 = 45
	OB5 = 46
	OB50 = 47
	OB51 = 48
	OB52 = 49
	OB53 = 50
	OB6 = 51
	OB65 = 52
	OB66 = 53
	OB67 = 54
	OB68 = 55
	OB69 = 56
	OB7 = 57
	OB70 = 58
	OB71 = 59
	OB72 = 60
	OB73 = 61
	OB74 = 62
	OB75 = 63
	OB76 = 64
	OB8 = 65
	OB85 = 66
	OB87 = 67
	OB88 = 68
	OB9 = 69
	UDEFined = 70


# noinspection SpellCheckingInspection
class OperatingBandD(Enum):
	"""32 Members, OB1 ... OB9"""
	OB1 = 0
	OB10 = 1
	OB11 = 2
	OB12 = 3
	OB13 = 4
	OB14 = 5
	OB15 = 6
	OB16 = 7
	OB17 = 8
	OB18 = 9
	OB19 = 10
	OB2 = 11
	OB20 = 12
	OB21 = 13
	OB22 = 14
	OB23 = 15
	OB24 = 16
	OB25 = 17
	OB26 = 18
	OB27 = 19
	OB28 = 20
	OB29 = 21
	OB3 = 22
	OB30 = 23
	OB31 = 24
	OB32 = 25
	OB4 = 26
	OB5 = 27
	OB6 = 28
	OB7 = 29
	OB8 = 30
	OB9 = 31


# noinspection SpellCheckingInspection
class PallocConfig(Enum):
	"""4 Members, BOTH ... NO"""
	BOTH = 0
	END = 1
	INIT = 2
	NO = 3


# noinspection SpellCheckingInspection
class PathCompAlpha(Enum):
	"""8 Members, DOT4 ... ZERO"""
	DOT4 = 0
	DOT5 = 1
	DOT6 = 2
	DOT7 = 3
	DOT8 = 4
	DOT9 = 5
	ONE = 6
	ZERO = 7


# noinspection SpellCheckingInspection
class PdcchSymbolsCount(Enum):
	"""5 Members, AUTO ... P4"""
	AUTO = 0
	P1 = 1
	P2 = 2
	P3 = 3
	P4 = 4


# noinspection SpellCheckingInspection
class PortsMapping(Enum):
	"""2 Members, R1 ... R1R2"""
	R1 = 0
	R1R2 = 1


# noinspection SpellCheckingInspection
class PowerOffset(Enum):
	"""3 Members, N3DB ... ZERO"""
	N3DB = 0
	N6DB = 1
	ZERO = 2


# noinspection SpellCheckingInspection
class PreambleTransmReps(Enum):
	"""8 Members, R1 ... R8"""
	R1 = 0
	R128 = 1
	R16 = 2
	R2 = 3
	R32 = 4
	R4 = 5
	R64 = 6
	R8 = 7


# noinspection SpellCheckingInspection
class PrecodingMatrixMode(Enum):
	"""17 Members, PMI0 ... RANDom_pmi"""
	PMI0 = 0
	PMI1 = 1
	PMI10 = 2
	PMI11 = 3
	PMI12 = 4
	PMI13 = 5
	PMI14 = 6
	PMI15 = 7
	PMI2 = 8
	PMI3 = 9
	PMI4 = 10
	PMI5 = 11
	PMI6 = 12
	PMI7 = 13
	PMI8 = 14
	PMI9 = 15
	RANDom_pmi = 16


# noinspection SpellCheckingInspection
class Priority(Enum):
	"""3 Members, BACKground ... NORMal"""
	BACKground = 0
	HIGH = 1
	NORMal = 2


# noinspection SpellCheckingInspection
class PrStep(Enum):
	"""4 Members, P2DB ... ZERO"""
	P2DB = 0
	P4DB = 1
	P6DB = 2
	ZERO = 3


# noinspection SpellCheckingInspection
class PswAction(Enum):
	"""7 Members, CONNect ... SMS"""
	CONNect = 0
	DETach = 1
	DISConnect = 2
	HANDover = 3
	OFF = 4
	ON = 5
	SMS = 6


# noinspection SpellCheckingInspection
class PswState(Enum):
	"""12 Members, ATTached ... SMESsage"""
	ATTached = 0
	CESTablished = 1
	CONNecting = 2
	DISConnect = 3
	IHANdover = 4
	OFF = 5
	OHANdover = 6
	ON = 7
	PAGing = 8
	RMESsage = 9
	SIGNaling = 10
	SMESsage = 11


# noinspection SpellCheckingInspection
class PucchFormat(Enum):
	"""4 Members, F1BCs ... F5"""
	F1BCs = 0
	F3 = 1
	F4 = 2
	F5 = 3


# noinspection SpellCheckingInspection
class Qoffset(Enum):
	"""31 Members, N1 ... ZERO"""
	N1 = 0
	N10 = 1
	N12 = 2
	N14 = 3
	N16 = 4
	N18 = 5
	N2 = 6
	N20 = 7
	N22 = 8
	N24 = 9
	N3 = 10
	N4 = 11
	N5 = 12
	N6 = 13
	N8 = 14
	P1 = 15
	P10 = 16
	P12 = 17
	P14 = 18
	P16 = 19
	P18 = 20
	P2 = 21
	P20 = 22
	P22 = 23
	P24 = 24
	P3 = 25
	P4 = 26
	P5 = 27
	P6 = 28
	P8 = 29
	ZERO = 30


# noinspection SpellCheckingInspection
class RandomValueMode(Enum):
	"""2 Members, EVEN ... ODD"""
	EVEN = 0
	ODD = 1


# noinspection SpellCheckingInspection
class RbPosition(Enum):
	"""56 Members, FULL ... P99"""
	FULL = 0
	HIGH = 1
	LOW = 2
	MID = 3
	P0 = 4
	P1 = 5
	P10 = 6
	P11 = 7
	P12 = 8
	P13 = 9
	P14 = 10
	P15 = 11
	P16 = 12
	P19 = 13
	P2 = 14
	P20 = 15
	P21 = 16
	P22 = 17
	P24 = 18
	P25 = 19
	P28 = 20
	P3 = 21
	P30 = 22
	P31 = 23
	P33 = 24
	P36 = 25
	P37 = 26
	P39 = 27
	P4 = 28
	P40 = 29
	P43 = 30
	P44 = 31
	P45 = 32
	P48 = 33
	P49 = 34
	P50 = 35
	P51 = 36
	P52 = 37
	P54 = 38
	P56 = 39
	P57 = 40
	P58 = 41
	P6 = 42
	P62 = 43
	P63 = 44
	P66 = 45
	P68 = 46
	P7 = 47
	P70 = 48
	P74 = 49
	P75 = 50
	P8 = 51
	P83 = 52
	P9 = 53
	P96 = 54
	P99 = 55


# noinspection SpellCheckingInspection
class RedundancyVerSequence(Enum):
	"""3 Members, TS1 ... UDEFined"""
	TS1 = 0
	TS4 = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class RejectAttachCause(Enum):
	"""38 Members, C10 ... TANA12"""
	C10 = 0
	C100 = 1
	C101 = 2
	C111 = 3
	C13 = 4
	C14 = 5
	C15 = 6
	C16 = 7
	C17 = 8
	C18 = 9
	C19 = 10
	C2 = 11
	C20 = 12
	C21 = 13
	C23 = 14
	C24 = 15
	C25 = 16
	C26 = 17
	C35 = 18
	C39 = 19
	C40 = 20
	C42 = 21
	C5 = 22
	C6 = 23
	C8 = 24
	C9 = 25
	C95 = 26
	C96 = 27
	C97 = 28
	C98 = 29
	C99 = 30
	CONG22 = 31
	EPS7 = 32
	IUE3 = 33
	OFF = 34
	ON = 35
	PLMN11 = 36
	TANA12 = 37


# noinspection SpellCheckingInspection
class Repeat(Enum):
	"""2 Members, CONTinuous ... SINGleshot"""
	CONTinuous = 0
	SINGleshot = 1


# noinspection SpellCheckingInspection
class RepetitionLevel(Enum):
	"""4 Members, RL1 ... RL4"""
	RL1 = 0
	RL2 = 1
	RL3 = 2
	RL4 = 3


# noinspection SpellCheckingInspection
class ReportInterval(Enum):
	"""8 Members, I1024 ... I640"""
	I1024 = 0
	I10240 = 1
	I120 = 2
	I2048 = 3
	I240 = 4
	I480 = 5
	I5120 = 6
	I640 = 7


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
class RestartMode(Enum):
	"""3 Members, AUTO ... TRIGger"""
	AUTO = 0
	MANual = 1
	TRIGger = 2


# noinspection SpellCheckingInspection
class RetransmissionTimer(Enum):
	"""17 Members, PSF0 ... PSF96"""
	PSF0 = 0
	PSF1 = 1
	PSF112 = 2
	PSF128 = 3
	PSF16 = 4
	PSF160 = 5
	PSF2 = 6
	PSF24 = 7
	PSF320 = 8
	PSF33 = 9
	PSF4 = 10
	PSF40 = 11
	PSF6 = 12
	PSF64 = 13
	PSF8 = 14
	PSF80 = 15
	PSF96 = 16


# noinspection SpellCheckingInspection
class RlcMode(Enum):
	"""2 Members, AM ... UM"""
	AM = 0
	UM = 1


# noinspection SpellCheckingInspection
class RpControlPattern(Enum):
	"""6 Members, RDA ... RUC"""
	RDA = 0
	RDB = 1
	RDC = 2
	RUA = 3
	RUB = 4
	RUC = 5


# noinspection SpellCheckingInspection
class RrcState(Enum):
	"""2 Members, CONNected ... IDLE"""
	CONNected = 0
	IDLE = 1


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
class SccAction(Enum):
	"""6 Members, MACactivate ... RRCDelete"""
	MACactivate = 0
	MACDeactivat = 1
	OFF = 2
	ON = 3
	RRCadd = 4
	RRCDelete = 5


# noinspection SpellCheckingInspection
class Scenario(Enum):
	"""106 Members, AD ... TROF"""
	AD = 0
	ADF = 1
	BF = 2
	BFF = 3
	BFSM4 = 4
	BH = 5
	BHF = 6
	CAFF = 7
	CAFR = 8
	CATF = 9
	CATR = 10
	CC = 11
	CCMP = 12
	CCMS1 = 13
	CF = 14
	CFF = 15
	CH = 16
	CHF = 17
	CHSM4 = 18
	CJ = 19
	CJF = 20
	CJFS4 = 21
	CJSM4 = 22
	CL = 23
	DD = 24
	DH = 25
	DHF = 26
	DJ = 27
	DJSM4 = 28
	DL = 29
	DLSM4 = 30
	DN = 31
	DNSM4 = 32
	DP = 33
	DPF = 34
	EE = 35
	EJ = 36
	EJF = 37
	EL = 38
	ELSM4 = 39
	EN = 40
	ENSM4 = 41
	EP = 42
	EPF = 43
	EPFS4 = 44
	EPSM4 = 45
	ER = 46
	ERSM4 = 47
	ET = 48
	FF = 49
	FL = 50
	FLF = 51
	FN = 52
	FNSM4 = 53
	FP = 54
	FPF = 55
	FPFS4 = 56
	FPSM4 = 57
	FR = 58
	FRSM4 = 59
	FT = 60
	FTSM4 = 61
	FV = 62
	FVSM4 = 63
	FX = 64
	GG = 65
	GN = 66
	GNF = 67
	GP = 68
	GPF = 69
	GPFS4 = 70
	GPSM4 = 71
	GR = 72
	GRSM4 = 73
	GT = 74
	GTSM4 = 75
	GV = 76
	GVSM4 = 77
	GX = 78
	GXSM4 = 79
	GYA = 80
	GYAS4 = 81
	GYC = 82
	HH = 83
	HP = 84
	HPF = 85
	HR = 86
	HRSM4 = 87
	HT = 88
	HTSM4 = 89
	HV = 90
	HVSM4 = 91
	HX = 92
	HXSM4 = 93
	HYA = 94
	HYAS4 = 95
	HYC = 96
	HYCS4 = 97
	HYE = 98
	HYES4 = 99
	HYG = 100
	NAV = 101
	SCEL = 102
	SCF = 103
	TRO = 104
	TROF = 105


# noinspection SpellCheckingInspection
class SchedulingType(Enum):
	"""7 Members, CQI ... UDTTibased"""
	CQI = 0
	EMAMode = 1
	EMCSched = 2
	RMC = 3
	SPS = 4
	UDCHannels = 5
	UDTTibased = 6


# noinspection SpellCheckingInspection
class SdCycle(Enum):
	"""17 Members, SF10 ... SF80"""
	SF10 = 0
	SF128 = 1
	SF16 = 2
	SF160 = 3
	SF2 = 4
	SF20 = 5
	SF256 = 6
	SF32 = 7
	SF320 = 8
	SF4 = 9
	SF40 = 10
	SF5 = 11
	SF512 = 12
	SF64 = 13
	SF640 = 14
	SF8 = 15
	SF80 = 16


# noinspection SpellCheckingInspection
class SearchSpace(Enum):
	"""2 Members, COMM ... UESP"""
	COMM = 0
	UESP = 1


# noinspection SpellCheckingInspection
class SecurityAlgorithm(Enum):
	"""2 Members, NULL ... S3G"""
	NULL = 0
	S3G = 1


# noinspection SpellCheckingInspection
class SemissionValue(Enum):
	"""32 Members, NS01 ... NS32"""
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
	NS11 = 10
	NS12 = 11
	NS13 = 12
	NS14 = 13
	NS15 = 14
	NS16 = 15
	NS17 = 16
	NS18 = 17
	NS19 = 18
	NS20 = 19
	NS21 = 20
	NS22 = 21
	NS23 = 22
	NS24 = 23
	NS25 = 24
	NS26 = 25
	NS27 = 26
	NS28 = 27
	NS29 = 28
	NS30 = 29
	NS31 = 30
	NS32 = 31


# noinspection SpellCheckingInspection
class SetPosition(Enum):
	"""9 Members, INV ... SCC7"""
	INV = 0
	PCC = 1
	SCC1 = 2
	SCC2 = 3
	SCC3 = 4
	SCC4 = 5
	SCC5 = 6
	SCC6 = 7
	SCC7 = 8


# noinspection SpellCheckingInspection
class SetType(Enum):
	"""10 Members, ALT0 ... UDSingle"""
	ALT0 = 0
	CLOop = 1
	CONStant = 2
	FULPower = 3
	MAXPower = 4
	MINPower = 5
	RPControl = 6
	SINGle = 7
	UDContinuous = 8
	UDSingle = 9


# noinspection SpellCheckingInspection
class SignalingGeneratorState(Enum):
	"""7 Members, ADINtermed ... RFHandover"""
	ADINtermed = 0
	ADJusted = 1
	INValid = 2
	OFF = 3
	ON = 4
	PENDing = 5
	RFHandover = 6


# noinspection SpellCheckingInspection
class SmsCodingGroup(Enum):
	"""2 Members, DCMClass ... GDCoding"""
	DCMClass = 0
	GDCoding = 1


# noinspection SpellCheckingInspection
class SmsDataCoding(Enum):
	"""2 Members, BIT7 ... BIT8"""
	BIT7 = 0
	BIT8 = 1


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class SourceTime(Enum):
	"""2 Members, CMWTime ... DATE"""
	CMWTime = 0
	DATE = 1


# noinspection SpellCheckingInspection
class SpsInteval(Enum):
	"""16 Members, S1 ... SADL"""
	S1 = 0
	S10 = 1
	S128 = 2
	S160 = 3
	S2 = 4
	S20 = 5
	S3 = 6
	S32 = 7
	S320 = 8
	S4 = 9
	S40 = 10
	S5 = 11
	S64 = 12
	S640 = 13
	S80 = 14
	SADL = 15


# noinspection SpellCheckingInspection
class StartingPosition(Enum):
	"""2 Members, OFDM0 ... OFDM7"""
	OFDM0 = 0
	OFDM7 = 1


# noinspection SpellCheckingInspection
class SubFramePattern(Enum):
	"""3 Members, HAB10 ... STANdard"""
	HAB10 = 0
	HAB8 = 1
	STANdard = 2


# noinspection SpellCheckingInspection
class SupportedExt(Enum):
	"""3 Members, NINFormation ... SUPPorted"""
	NINFormation = 0
	NSUPported = 1
	SUPPorted = 2


# noinspection SpellCheckingInspection
class SupportedLong(Enum):
	"""2 Members, NSUPported ... SUPPorted"""
	NSUPported = 0
	SUPPorted = 1


# noinspection SpellCheckingInspection
class Symbols(Enum):
	"""15 Members, S0 ... S9"""
	S0 = 0
	S1 = 1
	S10 = 2
	S11 = 3
	S12 = 4
	S13 = 5
	S14 = 6
	S2 = 7
	S3 = 8
	S4 = 9
	S5 = 10
	S6 = 11
	S7 = 12
	S8 = 13
	S9 = 14


# noinspection SpellCheckingInspection
class SymbolsDuration(Enum):
	"""5 Members, S1 ... S70"""
	S1 = 0
	S14 = 1
	S28 = 2
	S42 = 3
	S70 = 4


# noinspection SpellCheckingInspection
class SyncState(Enum):
	"""4 Members, MACactivated ... RRCadded"""
	MACactivated = 0
	OFF = 1
	ON = 2
	RRCadded = 3


# noinspection SpellCheckingInspection
class SyncZone(Enum):
	"""2 Members, NONE ... Z1"""
	NONE = 0
	Z1 = 1


# noinspection SpellCheckingInspection
class Table(Enum):
	"""7 Members, ANY ... TFLC2"""
	ANY = 0
	CW1 = 1
	CW2 = 2
	OTLC1 = 3
	OTLC2 = 4
	TFLC1 = 5
	TFLC2 = 6


# noinspection SpellCheckingInspection
class TimeResolution(Enum):
	"""1 Members, HRES ... HRES"""
	HRES = 0


# noinspection SpellCheckingInspection
class TransBlockSizeIdx(Enum):
	"""38 Members, T1 ... ZERO"""
	T1 = 0
	T10 = 1
	T11 = 2
	T12 = 3
	T13 = 4
	T14 = 5
	T15 = 6
	T16 = 7
	T17 = 8
	T18 = 9
	T19 = 10
	T2 = 11
	T20 = 12
	T21 = 13
	T22 = 14
	T23 = 15
	T24 = 16
	T25 = 17
	T26 = 18
	T27 = 19
	T28 = 20
	T29 = 21
	T3 = 22
	T30 = 23
	T31 = 24
	T32 = 25
	T33 = 26
	T34 = 27
	T35 = 28
	T36 = 29
	T37 = 30
	T4 = 31
	T5 = 32
	T6 = 33
	T7 = 34
	T8 = 35
	T9 = 36
	ZERO = 37


# noinspection SpellCheckingInspection
class TransGap(Enum):
	"""2 Members, G040 ... G080"""
	G040 = 0
	G080 = 1


# noinspection SpellCheckingInspection
class TransmissionMode(Enum):
	"""8 Members, TM1 ... TM9"""
	TM1 = 0
	TM2 = 1
	TM3 = 2
	TM4 = 3
	TM6 = 4
	TM7 = 5
	TM8 = 6
	TM9 = 7


# noinspection SpellCheckingInspection
class TransmitAntenaSelection(Enum):
	"""2 Members, OFF ... OLOop"""
	OFF = 0
	OLOop = 1


# noinspection SpellCheckingInspection
class TransmitAttempts(Enum):
	"""7 Members, A10 ... A8"""
	A10 = 0
	A3 = 1
	A4 = 2
	A5 = 3
	A6 = 4
	A7 = 5
	A8 = 6


# noinspection SpellCheckingInspection
class TransmScheme(Enum):
	"""13 Members, CLSingle ... UNDefined"""
	CLSingle = 0
	CLSMultiplex = 1
	DBF78 = 2
	FBF710 = 3
	OLSMultiplex = 4
	S7I8 = 5
	SBF5 = 6
	SBF8 = 7
	SIMO = 8
	SISO = 9
	TBF79 = 10
	TXDiversity = 11
	UNDefined = 12


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


# noinspection SpellCheckingInspection
class TxRxConfiguration(Enum):
	"""2 Members, DUAL ... SINGle"""
	DUAL = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class UeCatManual(Enum):
	"""15 Members, _0 ... M2"""
	_0 = 0
	_1 = 1
	_10 = 2
	_11 = 3
	_12 = 4
	_2 = 5
	_3 = 6
	_4 = 7
	_5 = 8
	_6 = 9
	_7 = 10
	_8 = 11
	_9 = 12
	M1 = 13
	M2 = 14


# noinspection SpellCheckingInspection
class UeChangesType(Enum):
	"""2 Members, RRCReconfig ... SIBPaging"""
	RRCReconfig = 0
	SIBPaging = 1


# noinspection SpellCheckingInspection
class UeProcessesCount(Enum):
	"""3 Members, N1 ... N4"""
	N1 = 0
	N3 = 1
	N4 = 2


# noinspection SpellCheckingInspection
class UeSidelinkProcessesCount(Enum):
	"""2 Members, N400 ... N50"""
	N400 = 0
	N50 = 1


# noinspection SpellCheckingInspection
class UeUsage(Enum):
	"""2 Members, DCENtric ... VCENtric"""
	DCENtric = 0
	VCENtric = 1


# noinspection SpellCheckingInspection
class UlHarqMode(Enum):
	"""5 Members, D0ONly ... PND0"""
	D0ONly = 0
	D0PHich = 1
	PHIChonly = 2
	PNACk = 3
	PND0 = 4


# noinspection SpellCheckingInspection
class UlPwrMaster(Enum):
	"""8 Members, PCC ... SCC7"""
	PCC = 0
	SCC1 = 1
	SCC2 = 2
	SCC3 = 3
	SCC4 = 4
	SCC5 = 5
	SCC6 = 6
	SCC7 = 7


# noinspection SpellCheckingInspection
class UpDownDirection(Enum):
	"""2 Members, DOWN ... UP"""
	DOWN = 0
	UP = 1


# noinspection SpellCheckingInspection
class UplinkNarrowBandPosition(Enum):
	"""16 Members, HIGH ... NB9"""
	HIGH = 0
	LOW = 1
	NB1 = 2
	NB10 = 3
	NB11 = 4
	NB12 = 5
	NB13 = 6
	NB14 = 7
	NB2 = 8
	NB3 = 9
	NB4 = 10
	NB5 = 11
	NB6 = 12
	NB7 = 13
	NB8 = 14
	NB9 = 15


# noinspection SpellCheckingInspection
class VdPreference(Enum):
	"""4 Members, CVONly ... IPVPrefered"""
	CVONly = 0
	CVPRefered = 1
	IPVonly = 2
	IPVPrefered = 3


# noinspection SpellCheckingInspection
class VolteHandoverType(Enum):
	"""2 Members, PSData ... PSVolte"""
	PSData = 0
	PSVolte = 1


# noinspection SpellCheckingInspection
class Window(Enum):
	"""16 Members, W10240 ... W8960"""
	W10240 = 0
	W11520 = 1
	W1280 = 2
	W12800 = 3
	W14080 = 4
	W15360 = 5
	W16640 = 6
	W17920 = 7
	W19200 = 8
	W20480 = 9
	W2560 = 10
	W3840 = 11
	W5120 = 12
	W6400 = 13
	W7680 = 14
	W8960 = 15


# noinspection SpellCheckingInspection
class WmQuantity(Enum):
	"""2 Members, ECNO ... RSCP"""
	ECNO = 0
	RSCP = 1
