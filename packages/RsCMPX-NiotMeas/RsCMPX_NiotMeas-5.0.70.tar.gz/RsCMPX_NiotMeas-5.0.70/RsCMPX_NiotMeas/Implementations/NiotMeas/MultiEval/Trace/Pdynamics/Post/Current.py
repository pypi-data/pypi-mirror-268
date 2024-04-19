from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NIOT:MEASurement<Instance>:MEValuation:TRACe:PDYNamics:POST:CURRent \n
		Snippet: value: List[float] = driver.niotMeas.multiEval.trace.pdynamics.post.current.read() \n
		Return the values of the right power dynamics trace (end of last allocated RU) . The results of the current, average and
		maximum traces can be retrieved. See also 'Square Power Dynamics'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of 1408 power values The 705th value refers to the time 0 µs, the end of the last allocated RU. The other details depend on the subcarrier spacing, see table."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NIOT:MEASurement<Instance>:MEValuation:TRACe:PDYNamics:POST:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:TRACe:PDYNamics:POST:CURRent \n
		Snippet: value: List[float] = driver.niotMeas.multiEval.trace.pdynamics.post.current.fetch() \n
		Return the values of the right power dynamics trace (end of last allocated RU) . The results of the current, average and
		maximum traces can be retrieved. See also 'Square Power Dynamics'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of 1408 power values The 705th value refers to the time 0 µs, the end of the last allocated RU. The other details depend on the subcarrier spacing, see table."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:TRACe:PDYNamics:POST:CURRent?', suppressed)
		return response
