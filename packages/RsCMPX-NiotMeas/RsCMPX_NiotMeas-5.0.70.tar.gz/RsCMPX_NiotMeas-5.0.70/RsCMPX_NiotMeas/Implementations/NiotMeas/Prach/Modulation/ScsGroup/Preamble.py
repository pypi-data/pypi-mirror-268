from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PreambleCls:
	"""Preamble commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Preamble, default value after init: Preamble.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preamble", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_preamble_get', 'repcap_preamble_set', repcap.Preamble.Nr1)

	def repcap_preamble_set(self, preamble: repcap.Preamble) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Preamble.Default
		Default value after init: Preamble.Nr1"""
		self._cmd_group.set_repcap_enum_value(preamble)

	def repcap_preamble_get(self) -> repcap.Preamble:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

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

	def fetch(self, preamble=repcap.Preamble.Default) -> FetchStruct:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:PRACh:MODulation:SCSGroup:PREamble<Number> \n
		Snippet: value: FetchStruct = driver.niotMeas.prach.modulation.scsGroup.preamble.fetch(preamble = repcap.Preamble.Default) \n
		Returns the numbers of the subcarriers used by the symbol groups of a selected preamble, for multi-preamble measurements.
		See also 'NB-IoT preamble structure'. \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		preamble_cmd_val = self._cmd_group.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:PRACh:MODulation:SCSGroup:PREamble{preamble_cmd_val}?', self.__class__.FetchStruct())

	def clone(self) -> 'PreambleCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PreambleCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
