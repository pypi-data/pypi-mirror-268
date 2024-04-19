from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NIOT:MEASurement<Instance>:MEValuation:TRACe:SEMask:CURRent \n
		Snippet: value: List[float] = driver.niotMeas.multiEval.trace.seMask.current.read() \n
		Returns the values of the spectrum emission traces. The results of the current, average and maximum traces can be
		retrieved. See also 'Square Spectrum Emission Mask'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of 1067 power results The value in the middle of the result array corresponds to the center frequency. The test point separation between two results equals 3.75 kHz."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NIOT:MEASurement<Instance>:MEValuation:TRACe:SEMask:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:TRACe:SEMask:CURRent \n
		Snippet: value: List[float] = driver.niotMeas.multiEval.trace.seMask.current.fetch() \n
		Returns the values of the spectrum emission traces. The results of the current, average and maximum traces can be
		retrieved. See also 'Square Spectrum Emission Mask'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of 1067 power results The value in the middle of the result array corresponds to the center frequency. The test point separation between two results equals 3.75 kHz."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:TRACe:SEMask:CURRent?', suppressed)
		return response
