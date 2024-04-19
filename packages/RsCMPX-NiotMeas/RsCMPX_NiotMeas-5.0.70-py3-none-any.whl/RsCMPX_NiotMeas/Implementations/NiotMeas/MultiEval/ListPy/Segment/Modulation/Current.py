from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment
			- Statist_Expired: int: Reached statistical length in slots
			- Out_Of_Tolerance: int: Percentage of measured slots with failed limit check
			- Evm_Rms: float: Error vector magnitude RMS value
			- Evm_Peak: float: Error vector magnitude peak value
			- Mag_Error_Rms: float: Magnitude error RMS value
			- Mag_Err_Peak: float: Magnitude error peak value
			- Ph_Error_Rms: float: Phase error RMS value
			- Ph_Error_Peak: float: Phase error peak value
			- Iq_Offset: float: I/Q origin offset
			- Frequency_Error: float: Carrier frequency error
			- Timing_Error: float: Transmit time error
			- Tx_Power: float: User equipment power
			- Peak_Power: float: User equipment peak power
			- Sc_Power: float: Power in allocated subcarriers
			- Evm_Dmrs: float: Error vector magnitude DMRS value
			- Mag_Err_Dmrs: float: Magnitude error DMRS value
			- Ph_Error_Dmrs: float: Phase error DMRS value"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
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
			ArgStruct.scalar_float('Ph_Error_Dmrs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
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

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation:CURRent \n
		Snippet: value: FetchStruct = driver.niotMeas.multiEval.listPy.segment.modulation.current.fetch(segment = repcap.Segment.Default) \n
		Returns current, average and standard deviation modulation single value results for segment <no> in list mode. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation:CURRent?', self.__class__.FetchStruct())
