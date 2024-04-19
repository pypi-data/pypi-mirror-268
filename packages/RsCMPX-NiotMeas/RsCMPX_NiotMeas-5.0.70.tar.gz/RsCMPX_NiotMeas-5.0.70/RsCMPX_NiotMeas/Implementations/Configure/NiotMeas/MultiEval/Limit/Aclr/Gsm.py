from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GsmCls:
	"""Gsm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gsm", core, parent)

	def set(self, relative_level: float or bool, absolute_level: float or bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:ACLR:GSM \n
		Snippet: driver.configure.niotMeas.multiEval.limit.aclr.gsm.set(relative_level = 1.0, absolute_level = 1.0) \n
		Defines a relative and absolute limit for the ACLR measured in the adjacent GSM channel. \n
			:param relative_level: (float or boolean) No help available
			:param absolute_level: (float or boolean) No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('relative_level', relative_level, DataType.FloatExt), ArgSingle('absolute_level', absolute_level, DataType.FloatExt))
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:ACLR:GSM {param}'.rstrip())

	# noinspection PyTypeChecker
	class GsmStruct(StructBase):
		"""Response structure. Fields: \n
			- Relative_Level: float or bool: No parameter help available
			- Absolute_Level: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Relative_Level'),
			ArgStruct.scalar_float_ext('Absolute_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Relative_Level: float or bool = None
			self.Absolute_Level: float or bool = None

	def get(self) -> GsmStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:ACLR:GSM \n
		Snippet: value: GsmStruct = driver.configure.niotMeas.multiEval.limit.aclr.gsm.get() \n
		Defines a relative and absolute limit for the ACLR measured in the adjacent GSM channel. \n
			:return: structure: for return value, see the help for GsmStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIMit:ACLR:GSM?', self.__class__.GsmStruct())
