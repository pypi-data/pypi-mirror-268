from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	@property
	def scIndex(self):
		"""scIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scIndex'):
			from .ScIndex import ScIndexCls
			self._scIndex = ScIndexCls(self._core, self._cmd_group)
		return self._scIndex

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified inband emission limits.
			- Margin: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Margin')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Margin: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:IEMission:MARGin:CURRent \n
		Snippet: value: FetchStruct = driver.niotMeas.multiEval.inbandEmission.margin.current.fetch() \n
		Return the limit line margin results for the inband emissions. The CURRent margin indicates the minimum (vertical)
		distance between the inband emissions limit line and the current trace. A negative result indicates that the limit is
		exceeded. The AVERage, EXTReme and SDEViation values are calculated from the current margins. The margin results cannot
		be displayed at the GUI. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:IEMission:MARGin:CURRent?', self.__class__.FetchStruct())

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
