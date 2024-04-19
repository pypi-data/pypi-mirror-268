from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, utra: bool, gsm: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle \n
		Snippet: driver.configure.niotMeas.multiEval.spectrum.aclr.enable.set(utra = False, gsm = False) \n
		Enables or disables the evaluation of the adjacent UTRA channels and the adjacent GSM channels. \n
			:param utra: No help available
			:param gsm: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('utra', utra, DataType.Boolean), ArgSingle('gsm', gsm, DataType.Boolean))
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle {param}'.rstrip())

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Response structure. Fields: \n
			- Utra: bool: No parameter help available
			- Gsm: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Utra'),
			ArgStruct.scalar_bool('Gsm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Utra: bool = None
			self.Gsm: bool = None

	def get(self) -> EnableStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle \n
		Snippet: value: EnableStruct = driver.configure.niotMeas.multiEval.spectrum.aclr.enable.get() \n
		Enables or disables the evaluation of the adjacent UTRA channels and the adjacent GSM channels. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle?', self.__class__.EnableStruct())
