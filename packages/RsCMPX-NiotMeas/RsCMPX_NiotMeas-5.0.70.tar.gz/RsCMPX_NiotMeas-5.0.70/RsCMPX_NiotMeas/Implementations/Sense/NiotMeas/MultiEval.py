from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	def get_nsr_units(self) -> int:
		"""SCPI: SENSe:NIOT:MEASurement<Instance>:MEValuation:NSRunits \n
		Snippet: value: int = driver.sense.niotMeas.multiEval.get_nsr_units() \n
		Queries the number of slots per resource unit. \n
			:return: nof_slots: No help available
		"""
		response = self._core.io.query_str('SENSe:NIOT:MEASurement<Instance>:MEValuation:NSRunits?')
		return Conversions.str_to_int(response)
