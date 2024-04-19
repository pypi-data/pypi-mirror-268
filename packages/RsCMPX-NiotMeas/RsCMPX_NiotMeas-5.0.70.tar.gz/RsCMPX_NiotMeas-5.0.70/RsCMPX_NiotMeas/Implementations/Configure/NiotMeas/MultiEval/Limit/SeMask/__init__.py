from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMaskCls:
	"""SeMask commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seMask", core, parent)

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	def get_obw_limit(self) -> float or bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit \n
		Snippet: value: float or bool = driver.configure.niotMeas.multiEval.limit.seMask.get_obw_limit() \n
		Defines an upper limit for the occupied bandwidth. \n
			:return: obw_limit: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit?')
		return Conversions.str_to_float_or_bool(response)

	def set_obw_limit(self, obw_limit: float or bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit \n
		Snippet: driver.configure.niotMeas.multiEval.limit.seMask.set_obw_limit(obw_limit = 1.0) \n
		Defines an upper limit for the occupied bandwidth. \n
			:param obw_limit: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(obw_limit)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit {param}')

	def clone(self) -> 'SeMaskCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SeMaskCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
