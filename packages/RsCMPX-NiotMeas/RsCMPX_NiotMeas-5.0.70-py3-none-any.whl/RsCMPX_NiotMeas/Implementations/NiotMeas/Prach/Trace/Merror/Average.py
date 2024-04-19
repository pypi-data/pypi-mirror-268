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
		"""SCPI: READ:NIOT:MEASurement<Instance>:PRACh:TRACe:MERRor:AVERage \n
		Snippet: value: List[float] = driver.niotMeas.prach.trace.merror.average.read() \n
		Return the values of the magnitude error traces. Each value is averaged over the samples in one preamble symbol.
		The results of the current, average and maximum traces can be retrieved. See also 'Squares EVM, Magnitude Error, Phase
		Error'. \n
		Suppressed linked return values: reliability \n
			:return: results: Comma-separated list of 20 results, one result per symbol"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NIOT:MEASurement<Instance>:PRACh:TRACe:MERRor:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:PRACh:TRACe:MERRor:AVERage \n
		Snippet: value: List[float] = driver.niotMeas.prach.trace.merror.average.fetch() \n
		Return the values of the magnitude error traces. Each value is averaged over the samples in one preamble symbol.
		The results of the current, average and maximum traces can be retrieved. See also 'Squares EVM, Magnitude Error, Phase
		Error'. \n
		Suppressed linked return values: reliability \n
			:return: results: Comma-separated list of 20 results, one result per symbol"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NIOT:MEASurement<Instance>:PRACh:TRACe:MERRor:AVERage?', suppressed)
		return response
