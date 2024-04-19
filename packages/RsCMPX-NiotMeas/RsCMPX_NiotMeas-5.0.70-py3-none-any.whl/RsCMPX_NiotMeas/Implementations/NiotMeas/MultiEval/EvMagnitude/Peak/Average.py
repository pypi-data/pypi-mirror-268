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
		"""SCPI: READ:NIOT:MEASurement<Instance>:MEValuation:EVMagnitude:PEAK:AVERage \n
		Snippet: value: List[float] = driver.niotMeas.multiEval.evMagnitude.peak.average.read() \n
		Returns the values of the EVM peak bar graphs for the SC-FDMA symbols in the measured slot. The results of the current,
		average and maximum bar graphs can be retrieved. See also 'Square EVM'. \n
		Suppressed linked return values: reliability \n
			:return: results: Comma-separated list of 7 results, for SC-FDMA symbol 0 to 6"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NIOT:MEASurement<Instance>:MEValuation:EVMagnitude:PEAK:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:EVMagnitude:PEAK:AVERage \n
		Snippet: value: List[float] = driver.niotMeas.multiEval.evMagnitude.peak.average.fetch() \n
		Returns the values of the EVM peak bar graphs for the SC-FDMA symbols in the measured slot. The results of the current,
		average and maximum bar graphs can be retrieved. See also 'Square EVM'. \n
		Suppressed linked return values: reliability \n
			:return: results: Comma-separated list of 7 results, for SC-FDMA symbol 0 to 6"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:EVMagnitude:PEAK:AVERage?', suppressed)
		return response
