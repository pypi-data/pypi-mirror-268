from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubcarrierCls:
	"""Subcarrier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subcarrier", core, parent)

	def set(self, nof_subcarrier: int, offset: int) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SUBCarrier \n
		Snippet: driver.configure.niotMeas.multiEval.subcarrier.set(nof_subcarrier = 1, offset = 1) \n
		Specifies the subcarrier configuration of the allocated resource units. \n
			:param nof_subcarrier: Number of subcarriers per resource unit The allowed values have dependencies, see 'Resource unit allocation'.
			:param offset: Offset of the first allocated subcarrier from the edge of the transmission bandwidth For a subcarrier spacing of 3.75 kHz / 15 kHz, n equals 48 / 12.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('nof_subcarrier', nof_subcarrier, DataType.Integer), ArgSingle('offset', offset, DataType.Integer))
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:SUBCarrier {param}'.rstrip())

	# noinspection PyTypeChecker
	class SubcarrierStruct(StructBase):
		"""Response structure. Fields: \n
			- Nof_Subcarrier: int: Number of subcarriers per resource unit The allowed values have dependencies, see 'Resource unit allocation'.
			- Offset: int: Offset of the first allocated subcarrier from the edge of the transmission bandwidth For a subcarrier spacing of 3.75 kHz / 15 kHz, n equals 48 / 12."""
		__meta_args_list = [
			ArgStruct.scalar_int('Nof_Subcarrier'),
			ArgStruct.scalar_int('Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nof_Subcarrier: int = None
			self.Offset: int = None

	def get(self) -> SubcarrierStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SUBCarrier \n
		Snippet: value: SubcarrierStruct = driver.configure.niotMeas.multiEval.subcarrier.get() \n
		Specifies the subcarrier configuration of the allocated resource units. \n
			:return: structure: for return value, see the help for SubcarrierStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:SUBCarrier?', self.__class__.SubcarrierStruct())
