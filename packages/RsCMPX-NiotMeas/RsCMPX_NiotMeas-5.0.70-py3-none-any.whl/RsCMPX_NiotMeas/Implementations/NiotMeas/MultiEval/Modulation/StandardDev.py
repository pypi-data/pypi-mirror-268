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
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Evm_Rms: float: Error vector magnitude RMS value
			- Evm_Peak: float: Error vector magnitude peak value
			- Mag_Error_Rms: float: Magnitude error RMS value
			- Mag_Err_Peak: float: Magnitude error peak value
			- Ph_Error_Rms: float: Phase error RMS value
			- Ph_Error_Peak: float: Phase error peak value
			- Iq_Offset: float: I/Q origin offset
			- Frequency_Error: float: Carrier frequency error
			- Timing_Error: float: Transmit time error.
			- Tx_Power: float: User equipment power
			- Peak_Power: float: User equipment peak power
			- Sc_Power: float: Power in allocated subcarriers
			- Evm_Dmrs: float: Error vector magnitude DMRS value
			- Mag_Err_Dmrs: float: Magnitude error DMRS value
			- Ph_Error_Dmrs: float: Phase error DMRS value
			- Iq_Gain_Imbalance: float: No parameter help available
			- Iq_Quadrature_Err: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
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
			ArgStruct.scalar_float('Tx_Power'),
			ArgStruct.scalar_float('Peak_Power'),
			ArgStruct.scalar_float('Sc_Power'),
			ArgStruct.scalar_float('Evm_Dmrs'),
			ArgStruct.scalar_float('Mag_Err_Dmrs'),
			ArgStruct.scalar_float('Ph_Error_Dmrs'),
			ArgStruct.scalar_float('Iq_Gain_Imbalance'),
			ArgStruct.scalar_float('Iq_Quadrature_Err')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
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
			self.Tx_Power: float = None
			self.Peak_Power: float = None
			self.Sc_Power: float = None
			self.Evm_Dmrs: float = None
			self.Mag_Err_Dmrs: float = None
			self.Ph_Error_Dmrs: float = None
			self.Iq_Gain_Imbalance: float = None
			self.Iq_Quadrature_Err: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NIOT:MEASurement<Instance>:MEValuation:MODulation:SDEViation \n
		Snippet: value: ResultData = driver.niotMeas.multiEval.modulation.standardDev.read() \n
		Return the current, average and standard deviation single value results. The values described below are returned by FETCh
		and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NIOT:MEASurement<Instance>:MEValuation:MODulation:SDEViation?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:MODulation:SDEViation \n
		Snippet: value: ResultData = driver.niotMeas.multiEval.modulation.standardDev.fetch() \n
		Return the current, average and standard deviation single value results. The values described below are returned by FETCh
		and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:MODulation:SDEViation?', self.__class__.ResultData())
