from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Utra_Neg: float: Power in the adjacent UTRA channel with lower frequency
			- Gsm_Neg: float: Power in the adjacent GSM channel with lower frequency
			- Nb_Iot: float: Power in the allocated NB-IoT channel
			- Gsm_Pos: float: Power in the adjacent GSM channel with higher frequency
			- Utra_Pos: float: Power in the adjacent UTRA channel with higher frequency"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Utra_Neg'),
			ArgStruct.scalar_float('Gsm_Neg'),
			ArgStruct.scalar_float('Nb_Iot'),
			ArgStruct.scalar_float('Gsm_Pos'),
			ArgStruct.scalar_float('Utra_Pos')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Utra_Neg: float = None
			self.Gsm_Neg: float = None
			self.Nb_Iot: float = None
			self.Gsm_Pos: float = None
			self.Utra_Pos: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NIOT:MEASurement<Instance>:MEValuation:TRACe:ACLR:CURRent \n
		Snippet: value: ResultData = driver.niotMeas.multiEval.trace.aclr.current.read() \n
		Returns the absolute powers as displayed in the ACLR diagram. The current and average values can be retrieved. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NIOT:MEASurement<Instance>:MEValuation:TRACe:ACLR:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:TRACe:ACLR:CURRent \n
		Snippet: value: ResultData = driver.niotMeas.multiEval.trace.aclr.current.fetch() \n
		Returns the absolute powers as displayed in the ACLR diagram. The current and average values can be retrieved. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:TRACe:ACLR:CURRent?', self.__class__.ResultData())
