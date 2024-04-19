from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScsGroupCls:
	"""ScsGroup commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scsGroup", core, parent)

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import PreambleCls
			self._preamble = PreambleCls(self._core, self._cmd_group)
		return self._preamble

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Sub_Carr_1: int: Subcarrier number for the first symbol group
			- Sub_Carr_2: int: Subcarrier number for the second symbol group
			- Sub_Carr_3: int: Subcarrier number for the third symbol group
			- Sub_Carr_4: int: Subcarrier number for the fourth symbol group"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Sub_Carr_1'),
			ArgStruct.scalar_int('Sub_Carr_2'),
			ArgStruct.scalar_int('Sub_Carr_3'),
			ArgStruct.scalar_int('Sub_Carr_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Sub_Carr_1: int = None
			self.Sub_Carr_2: int = None
			self.Sub_Carr_3: int = None
			self.Sub_Carr_4: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:PRACh:MODulation:SCSGroup \n
		Snippet: value: FetchStruct = driver.niotMeas.prach.modulation.scsGroup.fetch() \n
		Returns the numbers of the subcarriers used by the symbol groups of the preamble, for single-preamble measurements. See
		also 'NB-IoT preamble structure'. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:PRACh:MODulation:SCSGroup?', self.__class__.FetchStruct())

	def clone(self) -> 'ScsGroupCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScsGroupCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
