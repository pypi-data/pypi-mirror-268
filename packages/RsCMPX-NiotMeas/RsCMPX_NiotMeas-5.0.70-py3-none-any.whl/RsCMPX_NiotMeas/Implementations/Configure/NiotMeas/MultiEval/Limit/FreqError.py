from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqErrorCls:
	"""FreqError commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("freqError", core, parent)

	def set(self, freq_err_enable: bool, freq_err_low: float or bool, freq_err_high: float or bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:FERRor \n
		Snippet: driver.configure.niotMeas.multiEval.limit.freqError.set(freq_err_enable = False, freq_err_low = 1.0, freq_err_high = 1.0) \n
		Defines upper limits for the carrier frequency error. \n
			:param freq_err_enable: OFF: disables the limit check ON: enables the limit check
			:param freq_err_low: (float or boolean) Upper limit for frequencies up to 1 GHz
			:param freq_err_high: (float or boolean) Upper limit for frequencies above 1 GHz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('freq_err_enable', freq_err_enable, DataType.Boolean), ArgSingle('freq_err_low', freq_err_low, DataType.FloatExt), ArgSingle('freq_err_high', freq_err_high, DataType.FloatExt))
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:FERRor {param}'.rstrip())

	# noinspection PyTypeChecker
	class FreqErrorStruct(StructBase):
		"""Response structure. Fields: \n
			- Freq_Err_Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Freq_Err_Low: float or bool: Upper limit for frequencies up to 1 GHz
			- Freq_Err_High: float or bool: Upper limit for frequencies above 1 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Freq_Err_Enable'),
			ArgStruct.scalar_float_ext('Freq_Err_Low'),
			ArgStruct.scalar_float_ext('Freq_Err_High')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Err_Enable: bool = None
			self.Freq_Err_Low: float or bool = None
			self.Freq_Err_High: float or bool = None

	def get(self) -> FreqErrorStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:FERRor \n
		Snippet: value: FreqErrorStruct = driver.configure.niotMeas.multiEval.limit.freqError.get() \n
		Defines upper limits for the carrier frequency error. \n
			:return: structure: for return value, see the help for FreqErrorStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:FERRor?', self.__class__.FreqErrorStruct())
