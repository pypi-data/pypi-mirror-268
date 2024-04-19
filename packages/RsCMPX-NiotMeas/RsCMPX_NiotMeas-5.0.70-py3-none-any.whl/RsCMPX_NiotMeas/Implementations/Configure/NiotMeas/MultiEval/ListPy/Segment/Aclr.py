from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AclrCls:
	"""Aclr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aclr", core, parent)

	def set(self, aclr_statistics: int, aclr_enable: bool, utra_enable: bool, gsm_enable: bool, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:ACLR \n
		Snippet: driver.configure.niotMeas.multiEval.listPy.segment.aclr.set(aclr_statistics = 1, aclr_enable = False, utra_enable = False, gsm_enable = False, segment = repcap.Segment.Default) \n
		Defines settings for ACLR measurements in list mode for segment <no>. \n
			:param aclr_statistics: Statistical length in slots
			:param aclr_enable: Enables or disables the measurement of ACLR results
				- ON: ACLR results are measured according to the other enable flags in this command. ACLR results for which there is no explicit enable flag are also measured (e.g. power in the NB-IoT channel) .
				- OFF: No ACLR results at all are measured. The other enable flags in this command are ignored.
			:param utra_enable: Enables or disables the evaluation of adjacent UTRA channels
			:param gsm_enable: Enables or disables the evaluation of adjacent GSM channels
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aclr_statistics', aclr_statistics, DataType.Integer), ArgSingle('aclr_enable', aclr_enable, DataType.Boolean), ArgSingle('utra_enable', utra_enable, DataType.Boolean), ArgSingle('gsm_enable', gsm_enable, DataType.Boolean))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_with_opc(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:ACLR {param}'.rstrip())

	# noinspection PyTypeChecker
	class AclrStruct(StructBase):
		"""Response structure. Fields: \n
			- Aclr_Statistics: int: Statistical length in slots
			- Aclr_Enable: bool: Enables or disables the measurement of ACLR results
				- ON: ACLR results are measured according to the other enable flags in this command. ACLR results for which there is no explicit enable flag are also measured (e.g. power in the NB-IoT channel) .
				- OFF: No ACLR results at all are measured. The other enable flags in this command are ignored.
			- Utra_Enable: bool: Enables or disables the evaluation of adjacent UTRA channels
			- Gsm_Enable: bool: Enables or disables the evaluation of adjacent GSM channels"""
		__meta_args_list = [
			ArgStruct.scalar_int('Aclr_Statistics'),
			ArgStruct.scalar_bool('Aclr_Enable'),
			ArgStruct.scalar_bool('Utra_Enable'),
			ArgStruct.scalar_bool('Gsm_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aclr_Statistics: int = None
			self.Aclr_Enable: bool = None
			self.Utra_Enable: bool = None
			self.Gsm_Enable: bool = None

	def get(self, segment=repcap.Segment.Default) -> AclrStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:ACLR \n
		Snippet: value: AclrStruct = driver.configure.niotMeas.multiEval.listPy.segment.aclr.get(segment = repcap.Segment.Default) \n
		Defines settings for ACLR measurements in list mode for segment <no>. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for AclrStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct_with_opc(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:ACLR?', self.__class__.AclrStruct())
