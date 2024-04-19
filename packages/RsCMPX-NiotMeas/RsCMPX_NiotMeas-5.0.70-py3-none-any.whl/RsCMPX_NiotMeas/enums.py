from enum import Enum


# noinspection SpellCheckingInspection
class Band(Enum):
	"""39 Members, OB1 ... UDEF"""
	OB1 = 0
	OB10 = 1
	OB11 = 2
	OB12 = 3
	OB13 = 4
	OB14 = 5
	OB17 = 6
	OB18 = 7
	OB19 = 8
	OB2 = 9
	OB20 = 10
	OB21 = 11
	OB22 = 12
	OB23 = 13
	OB24 = 14
	OB25 = 15
	OB255 = 16
	OB256 = 17
	OB26 = 18
	OB27 = 19
	OB28 = 20
	OB3 = 21
	OB30 = 22
	OB31 = 23
	OB4 = 24
	OB5 = 25
	OB65 = 26
	OB66 = 27
	OB68 = 28
	OB7 = 29
	OB70 = 30
	OB71 = 31
	OB72 = 32
	OB73 = 33
	OB74 = 34
	OB8 = 35
	OB85 = 36
	OB9 = 37
	UDEF = 38


# noinspection SpellCheckingInspection
class ChannelBw(Enum):
	"""1 Members, B200 ... B200"""
	B200 = 0


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
class CyclicPrefix(Enum):
	"""2 Members, EXTended ... NORMal"""
	EXTended = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class LeadLag(Enum):
	"""2 Members, OFF ... S1"""
	OFF = 0
	S1 = 1


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
class MeasurementMode(Enum):
	"""2 Members, MELMode ... NORMal"""
	MELMode = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class Mode(Enum):
	"""2 Members, FDD ... TDD"""
	FDD = 0
	TDD = 1


# noinspection SpellCheckingInspection
class ModScheme(Enum):
	"""3 Members, BPSK ... QPSK"""
	BPSK = 0
	Q16 = 1
	QPSK = 2


# noinspection SpellCheckingInspection
class NofRepetitions(Enum):
	"""12 Members, NR1 ... NR8"""
	NR1 = 0
	NR128 = 1
	NR16 = 2
	NR1K = 3
	NR2 = 4
	NR256 = 5
	NR2K = 6
	NR32 = 7
	NR4 = 8
	NR512 = 9
	NR64 = 10
	NR8 = 11


# noinspection SpellCheckingInspection
class NofRepetitionsList(Enum):
	"""16 Members, NR1 ... NR8"""
	NR1 = 0
	NR128 = 1
	NR1536 = 2
	NR16 = 3
	NR192 = 4
	NR1K = 5
	NR2 = 6
	NR256 = 7
	NR2K = 8
	NR32 = 9
	NR384 = 10
	NR4 = 11
	NR512 = 12
	NR64 = 13
	NR768 = 14
	NR8 = 15


# noinspection SpellCheckingInspection
class NofRsrcUnits(Enum):
	"""8 Members, NRU01 ... NRU10"""
	NRU01 = 0
	NRU02 = 1
	NRU03 = 2
	NRU04 = 3
	NRU05 = 4
	NRU06 = 5
	NRU08 = 6
	NRU10 = 7


# noinspection SpellCheckingInspection
class NpuschFormat(Enum):
	"""2 Members, F1 ... F2"""
	F1 = 0
	F2 = 1


# noinspection SpellCheckingInspection
class ObwMode(Enum):
	"""2 Members, BW99 ... M26"""
	BW99 = 0
	M26 = 1


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class PeriodPreamble(Enum):
	"""5 Members, MS160 ... MS80"""
	MS160 = 0
	MS240 = 1
	MS320 = 2
	MS40 = 3
	MS80 = 4


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
class SubCarrSpacing(Enum):
	"""2 Members, S15K ... S3K75"""
	S15K = 0
	S3K75 = 1


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
