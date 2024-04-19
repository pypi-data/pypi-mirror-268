from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Evm_Rms: float: Error vector magnitude RMS value
			- Evm_Peak: float: Error vector magnitude peak value
			- Mag_Error_Rms: float: Magnitude error RMS value
			- Mag_Err_Peak: float: Magnitude error peak value
			- Ph_Error_Rms: float: Phase error RMS value
			- Ph_Error_Peak: float: Phase error peak value
			- Iq_Offset: float: I/Q origin offset
			- Frequency_Error: float: Carrier frequency error
			- Timing_Error: float: Transmit time error
			- Tx_Power_Minimum: float: Minimum user equipment power
			- Tx_Power_Maximum: float: Maximum user equipment power
			- Peak_Power_Min: float: Minimum user equipment peak power
			- Peak_Power_Max: float: Maximum user equipment peak power
			- Sc_Pow_Min: float: No parameter help available
			- Sc_Pow_Max: float: No parameter help available
			- Evm_Dmrs: float: Error vector magnitude DMRS value
			- Mag_Err_Dmrs: float: Magnitude error DMRS value
			- Ph_Error_Dmrs: float: Phase error DMRS value
			- Iq_Gain_Imbalance: float: No parameter help available
			- Iq_Quadrature_Err: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Mag_Error_Rms'),
			ArgStruct.scalar_float('Mag_Err_Peak'),
			ArgStruct.scalar_float('Ph_Error_Rms'),
			ArgStruct.scalar_float('Ph_Error_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Tx_Power_Minimum'),
			ArgStruct.scalar_float('Tx_Power_Maximum'),
			ArgStruct.scalar_float('Peak_Power_Min'),
			ArgStruct.scalar_float('Peak_Power_Max'),
			ArgStruct.scalar_float('Sc_Pow_Min'),
			ArgStruct.scalar_float('Sc_Pow_Max'),
			ArgStruct.scalar_float('Evm_Dmrs'),
			ArgStruct.scalar_float('Mag_Err_Dmrs'),
			ArgStruct.scalar_float('Ph_Error_Dmrs'),
			ArgStruct.scalar_float('Iq_Gain_Imbalance'),
			ArgStruct.scalar_float('Iq_Quadrature_Err')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Out_Of_Tolerance: int = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Mag_Error_Rms: float = None
			self.Mag_Err_Peak: float = None
			self.Ph_Error_Rms: float = None
			self.Ph_Error_Peak: float = None
			self.Iq_Offset: float = None
			self.Frequency_Error: float = None
			self.Timing_Error: float = None
			self.Tx_Power_Minimum: float = None
			self.Tx_Power_Maximum: float = None
			self.Peak_Power_Min: float = None
			self.Peak_Power_Max: float = None
			self.Sc_Pow_Min: float = None
			self.Sc_Pow_Max: float = None
			self.Evm_Dmrs: float = None
			self.Mag_Err_Dmrs: float = None
			self.Ph_Error_Dmrs: float = None
			self.Iq_Gain_Imbalance: float = None
			self.Iq_Quadrature_Err: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NIOT:MEASurement<Instance>:MEValuation:MODulation:EXTReme \n
		Snippet: value: ResultData = driver.niotMeas.multiEval.modulation.extreme.read() \n
		Returns the extreme single value results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NIOT:MEASurement<Instance>:MEValuation:MODulation:EXTReme?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:MODulation:EXTReme \n
		Snippet: value: ResultData = driver.niotMeas.multiEval.modulation.extreme.fetch() \n
		Returns the extreme single value results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:MODulation:EXTReme?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Evm_Rms: float or bool: Error vector magnitude RMS value
			- Evm_Peak: float or bool: Error vector magnitude peak value
			- Mag_Error_Rms: float or bool: Magnitude error RMS value
			- Mag_Err_Peak: float or bool: Magnitude error peak value
			- Ph_Error_Rms: float or bool: Phase error RMS value
			- Ph_Error_Peak: float or bool: Phase error peak value
			- Iq_Offset: float or bool: I/Q origin offset
			- Frequency_Error: float or bool: Carrier frequency error
			- Timing_Error: float or bool: Transmit time error
			- Tx_Power_Minimum: float or bool: Minimum user equipment power
			- Tx_Power_Maximum: float or bool: Maximum user equipment power
			- Peak_Power_Min: float or bool: Minimum user equipment peak power
			- Peak_Power_Max: float or bool: Maximum user equipment peak power
			- Sc_Pow_Min: float or bool: No parameter help available
			- Sc_Pow_Max: float or bool: No parameter help available
			- Evm_Dmrs: float or bool: Error vector magnitude DMRS value
			- Mag_Err_Dmrs: float or bool: Magnitude error DMRS value
			- Ph_Error_Dmrs: float or bool: Phase error DMRS value
			- Iq_Gain_Imbalance: float or bool: No parameter help available
			- Iq_Quadrature_Err: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float_ext('Evm_Rms'),
			ArgStruct.scalar_float_ext('Evm_Peak'),
			ArgStruct.scalar_float_ext('Mag_Error_Rms'),
			ArgStruct.scalar_float_ext('Mag_Err_Peak'),
			ArgStruct.scalar_float_ext('Ph_Error_Rms'),
			ArgStruct.scalar_float_ext('Ph_Error_Peak'),
			ArgStruct.scalar_float_ext('Iq_Offset'),
			ArgStruct.scalar_float_ext('Frequency_Error'),
			ArgStruct.scalar_float_ext('Timing_Error'),
			ArgStruct.scalar_float_ext('Tx_Power_Minimum'),
			ArgStruct.scalar_float_ext('Tx_Power_Maximum'),
			ArgStruct.scalar_float_ext('Peak_Power_Min'),
			ArgStruct.scalar_float_ext('Peak_Power_Max'),
			ArgStruct.scalar_float_ext('Sc_Pow_Min'),
			ArgStruct.scalar_float_ext('Sc_Pow_Max'),
			ArgStruct.scalar_float_ext('Evm_Dmrs'),
			ArgStruct.scalar_float_ext('Mag_Err_Dmrs'),
			ArgStruct.scalar_float_ext('Ph_Error_Dmrs'),
			ArgStruct.scalar_float_ext('Iq_Gain_Imbalance'),
			ArgStruct.scalar_float_ext('Iq_Quadrature_Err')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Out_Of_Tolerance: int = None
			self.Evm_Rms: float or bool = None
			self.Evm_Peak: float or bool = None
			self.Mag_Error_Rms: float or bool = None
			self.Mag_Err_Peak: float or bool = None
			self.Ph_Error_Rms: float or bool = None
			self.Ph_Error_Peak: float or bool = None
			self.Iq_Offset: float or bool = None
			self.Frequency_Error: float or bool = None
			self.Timing_Error: float or bool = None
			self.Tx_Power_Minimum: float or bool = None
			self.Tx_Power_Maximum: float or bool = None
			self.Peak_Power_Min: float or bool = None
			self.Peak_Power_Max: float or bool = None
			self.Sc_Pow_Min: float or bool = None
			self.Sc_Pow_Max: float or bool = None
			self.Evm_Dmrs: float or bool = None
			self.Mag_Err_Dmrs: float or bool = None
			self.Ph_Error_Dmrs: float or bool = None
			self.Iq_Gain_Imbalance: float or bool = None
			self.Iq_Quadrature_Err: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:NIOT:MEASurement<Instance>:MEValuation:MODulation:EXTReme \n
		Snippet: value: CalculateStruct = driver.niotMeas.multiEval.modulation.extreme.calculate() \n
		Returns the extreme single value results. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:NIOT:MEASurement<Instance>:MEValuation:MODulation:EXTReme?', self.__class__.CalculateStruct())
