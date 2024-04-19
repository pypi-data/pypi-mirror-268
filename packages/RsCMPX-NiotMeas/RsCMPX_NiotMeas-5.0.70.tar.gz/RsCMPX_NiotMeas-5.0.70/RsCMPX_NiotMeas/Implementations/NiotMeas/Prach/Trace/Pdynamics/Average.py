from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NIOT:MEASurement<Instance>:PRACh:TRACe:PDYNamics:AVERage \n
		Snippet: value: List[float] = driver.niotMeas.prach.trace.pdynamics.average.read() \n
		Return the values of the power dynamics traces. Each value is sampled with 96 Ts, corresponding to 3.125 µs. The results
		of the current, average and maximum traces can be retrieved. See also 'Square Power Dynamics'. \n
		Suppressed linked return values: reliability \n
			:return: power: 2816 power values, from -1200 µs to +7596.875 µs relative to the start of the preamble. The values have a spacing of 3.125 µs. The 385th value is at the start of the preamble (0 µs) ."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NIOT:MEASurement<Instance>:PRACh:TRACe:PDYNamics:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:PRACh:TRACe:PDYNamics:AVERage \n
		Snippet: value: List[float] = driver.niotMeas.prach.trace.pdynamics.average.fetch() \n
		Return the values of the power dynamics traces. Each value is sampled with 96 Ts, corresponding to 3.125 µs. The results
		of the current, average and maximum traces can be retrieved. See also 'Square Power Dynamics'. \n
		Suppressed linked return values: reliability \n
			:return: power: 2816 power values, from -1200 µs to +7596.875 µs relative to the start of the preamble. The values have a spacing of 3.125 µs. The 385th value is at the start of the preamble (0 µs) ."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NIOT:MEASurement<Instance>:PRACh:TRACe:PDYNamics:AVERage?', suppressed)
		return response
