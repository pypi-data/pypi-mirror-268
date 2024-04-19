from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScIndexCls:
	"""ScIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scIndex", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified inband emission limits.
			- Sc_Index: int: Subcarrier index"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_int('Sc_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Sc_Index: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:MEValuation:IEMission:MARGin:EXTReme:SCINdex \n
		Snippet: value: FetchStruct = driver.niotMeas.multiEval.inbandEmission.margin.extreme.scIndex.fetch() \n
		Return subcarrier indices for inband emission margins. At these SC indices, the CURRent and EXTReme margins have been
		detected (see method RsCMPX_NiotMeas.NiotMeas.MultiEval.InbandEmission.Margin.Current.fetch and ...:EXTReme) . \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:MEValuation:IEMission:MARGin:EXTReme:SCINdex?', self.__class__.FetchStruct())
