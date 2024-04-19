from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	class ModulationStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Mod_Statistics: int: Statistical length in slots
			- Modenable: bool: Enables or disables the measurement of modulation results
				- ON: Modulation results are measured according to the other enable flags in this command. Modulation results for which there is no explicit enable flag are also measured (e.g. I/Q offset, frequency error and timing error) .
				- OFF: No modulation results at all are measured. The other enable flags in this command are ignored.
			- Evm_Enable: bool: Enables or disables the measurement of EVM
			- Mag_Error_Enable: bool: Enables or disables the measurement of magnitude error
			- Phase_Err_Enable: bool: Enables or disables the measurement of phase error
			- Ib_Eenable: bool: Enables or disables the measurement of inband emissions
			- Mod_Scheme: enums.ModScheme: Modulation scheme used by the NB-IoT uplink signal: BPSK, QPSK, 16QAM For 16QAM,
			multiple subcarriers per RU must be in use (No. of SC 1) . See 'Resource unit allocation'"""
		__meta_args_list = [
			ArgStruct.scalar_int('Mod_Statistics'),
			ArgStruct.scalar_bool('Modenable'),
			ArgStruct.scalar_bool('Evm_Enable'),
			ArgStruct.scalar_bool('Mag_Error_Enable'),
			ArgStruct.scalar_bool('Phase_Err_Enable'),
			ArgStruct.scalar_bool('Ib_Eenable'),
			ArgStruct.scalar_enum('Mod_Scheme', enums.ModScheme)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Statistics: int = None
			self.Modenable: bool = None
			self.Evm_Enable: bool = None
			self.Mag_Error_Enable: bool = None
			self.Phase_Err_Enable: bool = None
			self.Ib_Eenable: bool = None
			self.Mod_Scheme: enums.ModScheme = None

	def set(self, structure: ModulationStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation \n
		Snippet with structure: \n
		structure = driver.configure.niotMeas.multiEval.listPy.segment.modulation.ModulationStruct() \n
		structure.Mod_Statistics: int = 1 \n
		structure.Modenable: bool = False \n
		structure.Evm_Enable: bool = False \n
		structure.Mag_Error_Enable: bool = False \n
		structure.Phase_Err_Enable: bool = False \n
		structure.Ib_Eenable: bool = False \n
		structure.Mod_Scheme: enums.ModScheme = enums.ModScheme.BPSK \n
		driver.configure.niotMeas.multiEval.listPy.segment.modulation.set(structure, segment = repcap.Segment.Default) \n
		Defines settings for modulation measurements in list mode for segment <no>. \n
			:param structure: for set value, see the help for ModulationStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct_with_opc(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation', structure)

	def get(self, segment=repcap.Segment.Default) -> ModulationStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation \n
		Snippet: value: ModulationStruct = driver.configure.niotMeas.multiEval.listPy.segment.modulation.get(segment = repcap.Segment.Default) \n
		Defines settings for modulation measurements in list mode for segment <no>. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ModulationStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct_with_opc(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation?', self.__class__.ModulationStruct())
