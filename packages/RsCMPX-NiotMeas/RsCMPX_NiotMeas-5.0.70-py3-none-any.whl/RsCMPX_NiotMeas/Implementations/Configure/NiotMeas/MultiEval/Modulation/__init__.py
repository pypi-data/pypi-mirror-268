from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def eePeriods(self):
		"""eePeriods commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eePeriods'):
			from .EePeriods import EePeriodsCls
			self._eePeriods = EePeriodsCls(self._core, self._cmd_group)
		return self._eePeriods

	# noinspection PyTypeChecker
	def get_mscheme(self) -> enums.ModScheme:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:MSCHeme \n
		Snippet: value: enums.ModScheme = driver.configure.niotMeas.multiEval.modulation.get_mscheme() \n
		Selects the modulation scheme used by the measured signal. \n
			:return: mod_scheme: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:MSCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.ModScheme)

	def set_mscheme(self, mod_scheme: enums.ModScheme) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:MSCHeme \n
		Snippet: driver.configure.niotMeas.multiEval.modulation.set_mscheme(mod_scheme = enums.ModScheme.BPSK) \n
		Selects the modulation scheme used by the measured signal. \n
			:param mod_scheme: No help available
		"""
		param = Conversions.enum_scalar_to_str(mod_scheme, enums.ModScheme)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:MSCHeme {param}')

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
