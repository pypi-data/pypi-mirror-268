from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NiotMeasCls:
	"""NiotMeas commands group definition. 10 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("niotMeas", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def prach(self):
		"""prach commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	def clone(self) -> 'NiotMeasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NiotMeasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
