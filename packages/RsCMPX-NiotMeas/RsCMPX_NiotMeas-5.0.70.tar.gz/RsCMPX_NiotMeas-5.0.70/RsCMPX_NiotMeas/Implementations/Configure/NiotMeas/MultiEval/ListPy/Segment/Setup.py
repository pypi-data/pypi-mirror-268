from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetupCls:
	"""Setup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Segment_Length: int: Number of slots in the segment
			- Level: float: Expected nominal power in the segment. The range can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
			- Band: enums.Band: No parameter help available
			- Frequency: float: Carrier center frequency used in the segment
			- Npusch_Format: enums.NpuschFormat: Format of the NPUSCH.
			- Nof_Subcarrier: int: Number of subcarriers per resource unit The allowed values have dependencies, see 'Resource unit allocation'.
			- Start_Sc: int: Offset of the first allocated subcarrier from the edge of the transmission bandwidth For a subcarrier spacing of 3.75 kHz / 15 kHz, n equals 48 / 12.
			- Nof_Ru_S: enums.NofRsrcUnits: Number of resource units allocated for the NPUSCH
			- Nof_Repetitions: enums.NofRepetitionsList: Number of NPUSCH repetitions: 1, 2, 4, ..., 512, 1024, 2048
			- Retrigger_Flag: enums.RetriggerFlag: Specifies whether the measurement waits for a trigger event before measuring the segment, or not. For the first segment, the value OFF is always interpreted as ON. For subsequent segments, the retrigger flag is ignored for trigger mode ONCE and evaluated for trigger mode SEGMent, see [CMDLINKRESOLVED Trigger.NiotMeas.MultiEval.ListPy#Mode CMDLINKRESOLVED].
				- OFF: Measure the segment without retrigger.
				- ON: Wait for a trigger event from the trigger source configured via TRIGger:NIOT:MEASi:MEValuation:SOURce.
				- IFPower: Wait for a trigger event from the trigger source IF Power.
			- Evaluat_Offset: int: Number of slots at the beginning of the segment that are not evaluated"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Band', enums.Band),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Npusch_Format', enums.NpuschFormat),
			ArgStruct.scalar_int('Nof_Subcarrier'),
			ArgStruct.scalar_int('Start_Sc'),
			ArgStruct.scalar_enum('Nof_Ru_S', enums.NofRsrcUnits),
			ArgStruct.scalar_enum('Nof_Repetitions', enums.NofRepetitionsList),
			ArgStruct.scalar_enum('Retrigger_Flag', enums.RetriggerFlag),
			ArgStruct.scalar_int('Evaluat_Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Band: enums.Band = None
			self.Frequency: float = None
			self.Npusch_Format: enums.NpuschFormat = None
			self.Nof_Subcarrier: int = None
			self.Start_Sc: int = None
			self.Nof_Ru_S: enums.NofRsrcUnits = None
			self.Nof_Repetitions: enums.NofRepetitionsList = None
			self.Retrigger_Flag: enums.RetriggerFlag = None
			self.Evaluat_Offset: int = None

	def set(self, structure: SetupStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet with structure: \n
		structure = driver.configure.niotMeas.multiEval.listPy.segment.setup.SetupStruct() \n
		structure.Segment_Length: int = 1 \n
		structure.Level: float = 1.0 \n
		structure.Band: enums.Band = enums.Band.OB1 \n
		structure.Frequency: float = 1.0 \n
		structure.Npusch_Format: enums.NpuschFormat = enums.NpuschFormat.F1 \n
		structure.Nof_Subcarrier: int = 1 \n
		structure.Start_Sc: int = 1 \n
		structure.Nof_Ru_S: enums.NofRsrcUnits = enums.NofRsrcUnits.NRU01 \n
		structure.Nof_Repetitions: enums.NofRepetitionsList = enums.NofRepetitionsList.NR1 \n
		structure.Retrigger_Flag: enums.RetriggerFlag = enums.RetriggerFlag.IFPower \n
		structure.Evaluat_Offset: int = 1 \n
		driver.configure.niotMeas.multiEval.listPy.segment.setup.set(structure, segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of segment <no>. This command must be sent for all segments to be measured
		(method RsCMPX_NiotMeas.Configure.NiotMeas.MultiEval.ListPy.Lrange.set) . For the supported frequency range, see
		'Frequency ranges'. \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct_with_opc(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup', structure)

	def get(self, segment=repcap.Segment.Default) -> SetupStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: value: SetupStruct = driver.configure.niotMeas.multiEval.listPy.segment.setup.get(segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of segment <no>. This command must be sent for all segments to be measured
		(method RsCMPX_NiotMeas.Configure.NiotMeas.MultiEval.ListPy.Lrange.set) . For the supported frequency range, see
		'Frequency ranges'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct_with_opc(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup?', self.__class__.SetupStruct())
