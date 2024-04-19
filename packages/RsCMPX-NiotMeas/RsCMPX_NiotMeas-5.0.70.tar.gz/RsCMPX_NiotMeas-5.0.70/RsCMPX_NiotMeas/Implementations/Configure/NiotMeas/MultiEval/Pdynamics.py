from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdynamicsCls:
	"""Pdynamics commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdynamics", core, parent)

	# noinspection PyTypeChecker
	def get_tmask(self) -> enums.TimeMask:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:PDYNamics:TMASk \n
		Snippet: value: enums.TimeMask = driver.configure.niotMeas.multiEval.pdynamics.get_tmask() \n
		No command help available \n
			:return: time_mask: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:PDYNamics:TMASk?')
		return Conversions.str_to_scalar_enum(response, enums.TimeMask)

	def set_tmask(self, time_mask: enums.TimeMask) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:PDYNamics:TMASk \n
		Snippet: driver.configure.niotMeas.multiEval.pdynamics.set_tmask(time_mask = enums.TimeMask.GOO) \n
		No command help available \n
			:param time_mask: No help available
		"""
		param = Conversions.enum_scalar_to_str(time_mask, enums.TimeMask)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:PDYNamics:TMASk {param}')
