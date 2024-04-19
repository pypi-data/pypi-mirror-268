from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for spectrum emission measurements exceeding the specified spectrum emission mask limits.
			- Obw: float: Occupied bandwidth
			- Tx_Power: float: Total TX power within 400 kHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Tx_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Obw: float = None
			self.Tx_Power: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NIOT:MEASurement<Instance>:MEValuation:SEMask:SDEViation \n
		Snippet: value: ResultData = driver.niotMeas.multiEval.seMask.standardDev.read() \n
		Return the current, average and standard deviation single value results of the spectrum emission measurement. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NIOT:MEASurement<Instance>:MEValuation:SEMask:SDEViation?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:SEMask:SDEViation \n
		Snippet: value: ResultData = driver.niotMeas.multiEval.seMask.standardDev.fetch() \n
		Return the current, average and standard deviation single value results of the spectrum emission measurement. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:SEMask:SDEViation?', self.__class__.ResultData())
