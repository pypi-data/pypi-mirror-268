from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for power dynamics measurements exceeding the specified power dynamics limits.
			- Off_Power_Before: float: OFF power before the preamble
			- On_Power_Rms: float: ON power mean value
			- On_Power_Peak: float: ON power peak value
			- Off_Power_After: float: OFF power after the preamble"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Off_Power_Before'),
			ArgStruct.scalar_float('On_Power_Rms'),
			ArgStruct.scalar_float('On_Power_Peak'),
			ArgStruct.scalar_float('Off_Power_After')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Off_Power_Before: float = None
			self.On_Power_Rms: float = None
			self.On_Power_Peak: float = None
			self.Off_Power_After: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NIOT:MEASurement<Instance>:PRACh:PDYNamics:MINimum \n
		Snippet: value: ResultData = driver.niotMeas.prach.pdynamics.minimum.read() \n
		Return the current, average, minimum, maximum and standard deviation single value results of the power dynamics
		measurement. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NIOT:MEASurement<Instance>:PRACh:PDYNamics:MINimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:PRACh:PDYNamics:MINimum \n
		Snippet: value: ResultData = driver.niotMeas.prach.pdynamics.minimum.fetch() \n
		Return the current, average, minimum, maximum and standard deviation single value results of the power dynamics
		measurement. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:PRACh:PDYNamics:MINimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for power dynamics measurements exceeding the specified power dynamics limits.
			- Off_Power_Before: float or bool: OFF power before the preamble
			- On_Power_Rms: float or bool: ON power mean value
			- On_Power_Peak: float or bool: ON power peak value
			- Off_Power_After: float or bool: OFF power after the preamble"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float_ext('Off_Power_Before'),
			ArgStruct.scalar_float_ext('On_Power_Rms'),
			ArgStruct.scalar_float_ext('On_Power_Peak'),
			ArgStruct.scalar_float_ext('Off_Power_After')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Off_Power_Before: float or bool = None
			self.On_Power_Rms: float or bool = None
			self.On_Power_Peak: float or bool = None
			self.Off_Power_After: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:NIOT:MEASurement<Instance>:PRACh:PDYNamics:MINimum \n
		Snippet: value: CalculateStruct = driver.niotMeas.prach.pdynamics.minimum.calculate() \n
		Return the current, average, minimum, maximum and standard deviation single value results of the power dynamics
		measurement. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:NIOT:MEASurement<Instance>:PRACh:PDYNamics:MINimum?', self.__class__.CalculateStruct())
