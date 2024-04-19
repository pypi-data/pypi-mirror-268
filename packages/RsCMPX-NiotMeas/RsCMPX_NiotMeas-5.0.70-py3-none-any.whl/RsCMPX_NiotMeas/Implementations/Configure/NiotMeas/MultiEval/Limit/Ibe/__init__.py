from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IbeCls:
	"""Ibe commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ibe", core, parent)

	@property
	def iqOffset(self):
		"""iqOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	def set(self, enable: bool, minimum: float, sc_power: float, iq_image: float) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:IBE \n
		Snippet: driver.configure.niotMeas.multiEval.limit.ibe.set(enable = False, minimum = 1.0, sc_power = 1.0, iq_image = 1.0) \n
		Defines parameters used for calculation of an upper limit for the inband emissions, see 'Modulation limits: inband
		emissions'. \n
			:param enable: OFF: disables the limit check ON: enables the limit check
			:param minimum: No help available
			:param sc_power: No help available
			:param iq_image: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('minimum', minimum, DataType.Float), ArgSingle('sc_power', sc_power, DataType.Float), ArgSingle('iq_image', iq_image, DataType.Float))
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:IBE {param}'.rstrip())

	# noinspection PyTypeChecker
	class IbeStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Minimum: float: No parameter help available
			- Sc_Power: float: No parameter help available
			- Iq_Image: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Minimum'),
			ArgStruct.scalar_float('Sc_Power'),
			ArgStruct.scalar_float('Iq_Image')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Minimum: float = None
			self.Sc_Power: float = None
			self.Iq_Image: float = None

	def get(self) -> IbeStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:IBE \n
		Snippet: value: IbeStruct = driver.configure.niotMeas.multiEval.limit.ibe.get() \n
		Defines parameters used for calculation of an upper limit for the inband emissions, see 'Modulation limits: inband
		emissions'. \n
			:return: structure: for return value, see the help for IbeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:IBE?', self.__class__.IbeStruct())

	def clone(self) -> 'IbeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IbeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
