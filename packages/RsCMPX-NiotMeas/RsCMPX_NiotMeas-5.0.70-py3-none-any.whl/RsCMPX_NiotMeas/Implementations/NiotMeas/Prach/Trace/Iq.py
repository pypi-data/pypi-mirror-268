from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqCls:
	"""Iq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Iphase: List[float]: Normalized I amplitude
			- Qphase: List[float]: Normalized Q amplitude"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Iphase', DataType.FloatList, None, False, True, 1),
			ArgStruct('Qphase', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Iphase: List[float] = None
			self.Qphase: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NIOT:MEASurement<Instance>:PRACh:TRACe:IQ \n
		Snippet: value: FetchStruct = driver.niotMeas.prach.trace.iq.fetch() \n
		Returns the results in the I/Q constellation diagram. The return order is: <Reliability>, <IPhase>1, <QPhase>1, <IPhase>2,
		<QPhase>2, ... See also 'Square IQ'. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NIOT:MEASurement<Instance>:PRACh:TRACe:IQ?', self.__class__.FetchStruct())
