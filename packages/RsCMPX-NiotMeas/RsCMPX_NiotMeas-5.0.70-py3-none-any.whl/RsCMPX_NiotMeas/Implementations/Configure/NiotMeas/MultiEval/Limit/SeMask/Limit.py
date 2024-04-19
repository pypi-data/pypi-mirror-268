from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	def set(self, enable: bool, frequency_start: float, frequency_stop: float, power_level_start: float, power_level_stop: float, limit=repcap.Limit.Default) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit<nr> \n
		Snippet: driver.configure.niotMeas.multiEval.limit.seMask.limit.set(enable = False, frequency_start = 1.0, frequency_stop = 1.0, power_level_start = 1.0, power_level_stop = 1.0, limit = repcap.Limit.Default) \n
		Defines the emission mask area <no>. \n
			:param enable: OFF: disables the check of these requirements ON: enables the check of these requirements
			:param frequency_start: Start frequency of the area, relative to the edges of the channel bandwidth.
			:param frequency_stop: Stop frequency of the area, relative to the edges of the channel bandwidth.
			:param power_level_start: Upper limit at the FrequencyStart
			:param power_level_stop: Upper limit at the FrequencyEnd
			:param limit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('frequency_start', frequency_start, DataType.Float), ArgSingle('frequency_stop', frequency_stop, DataType.Float), ArgSingle('power_level_start', power_level_start, DataType.Float), ArgSingle('power_level_stop', power_level_stop, DataType.Float))
		limit_cmd_val = self._cmd_group.get_repcap_cmd_value(limit, repcap.Limit)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit{limit_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class LimitStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF: disables the check of these requirements ON: enables the check of these requirements
			- Frequency_Start: float: Start frequency of the area, relative to the edges of the channel bandwidth.
			- Frequency_Stop: float: Stop frequency of the area, relative to the edges of the channel bandwidth.
			- Power_Level_Start: float: Upper limit at the FrequencyStart
			- Power_Level_Stop: float: Upper limit at the FrequencyEnd"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Frequency_Start'),
			ArgStruct.scalar_float('Frequency_Stop'),
			ArgStruct.scalar_float('Power_Level_Start'),
			ArgStruct.scalar_float('Power_Level_Stop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Frequency_Start: float = None
			self.Frequency_Stop: float = None
			self.Power_Level_Start: float = None
			self.Power_Level_Stop: float = None

	def get(self, limit=repcap.Limit.Default) -> LimitStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit<nr> \n
		Snippet: value: LimitStruct = driver.configure.niotMeas.multiEval.limit.seMask.limit.get(limit = repcap.Limit.Default) \n
		Defines the emission mask area <no>. \n
			:param limit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: structure: for return value, see the help for LimitStruct structure arguments."""
		limit_cmd_val = self._cmd_group.get_repcap_cmd_value(limit, repcap.Limit)
		return self._core.io.query_struct(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit{limit_cmd_val}?', self.__class__.LimitStruct())
