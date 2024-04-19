from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IemissionsCls:
	"""Iemissions commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iemissions", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NIOT:MEASurement<Instance>:MEValuation:TRACe:IEMissions \n
		Snippet: value: List[float] = driver.niotMeas.multiEval.trace.iemissions.read() \n
		Returns the values of the inband emissions trace. See also 'Square Inband Emissions'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of power values, one value per subcarrier For 15 kHz SC spacing, 12 power values are returned. For 3.75 kHz SC spacing, 48 power values are returned."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NIOT:MEASurement<Instance>:MEValuation:TRACe:IEMissions?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:TRACe:IEMissions \n
		Snippet: value: List[float] = driver.niotMeas.multiEval.trace.iemissions.fetch() \n
		Returns the values of the inband emissions trace. See also 'Square Inband Emissions'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of power values, one value per subcarrier For 15 kHz SC spacing, 12 power values are returned. For 3.75 kHz SC spacing, 48 power values are returned."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:TRACe:IEMissions?', suppressed)
		return response
