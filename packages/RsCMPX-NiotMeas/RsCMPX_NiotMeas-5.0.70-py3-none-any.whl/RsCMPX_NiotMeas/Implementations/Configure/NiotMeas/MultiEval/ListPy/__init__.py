from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 12 total commands, 3 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def lrange(self):
		"""lrange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lrange'):
			from .Lrange import LrangeCls
			self._lrange = LrangeCls(self._core, self._cmd_group)
		return self._lrange

	@property
	def segment(self):
		"""segment commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import SegmentCls
			self._segment = SegmentCls(self._core, self._cmd_group)
		return self._segment

	@property
	def singleCmw(self):
		"""singleCmw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmwCls
			self._singleCmw = SingleCmwCls(self._core, self._cmd_group)
		return self._singleCmw

	def get_os_index(self) -> int or bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:OSINdex \n
		Snippet: value: int or bool = driver.configure.niotMeas.multiEval.listPy.get_os_index() \n
		Selects the segment to be displayed in offline mode. The index refers to the range of measured segments, see method
		RsCMPX_NiotMeas.Configure.NiotMeas.MultiEval.ListPy.Lrange.set. Setting a value also enables the offline mode. \n
			:return: offline_seg_index: (integer or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:OSINdex?')
		return Conversions.str_to_int_or_bool(response)

	def set_os_index(self, offline_seg_index: int or bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:OSINdex \n
		Snippet: driver.configure.niotMeas.multiEval.listPy.set_os_index(offline_seg_index = 1) \n
		Selects the segment to be displayed in offline mode. The index refers to the range of measured segments, see method
		RsCMPX_NiotMeas.Configure.NiotMeas.MultiEval.ListPy.Lrange.set. Setting a value also enables the offline mode. \n
			:param offline_seg_index: (integer or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(offline_seg_index)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:OSINdex {param}')

	# noinspection PyTypeChecker
	def get_cmode(self) -> enums.ParameterSetMode:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:CMODe \n
		Snippet: value: enums.ParameterSetMode = driver.configure.niotMeas.multiEval.listPy.get_cmode() \n
		Sets the connector mode, selecting whether all list mode segments use the same RF connection. \n
			:return: connector_mode:
				- GLOBal: Use the same RF connection for all segments, see ROUTe:NIOT:MEASi:SPATh.
				- LIST: Assign a connection to each segment, see CONFigure:NIOT:MEASi:MEValuation:LIST:SEGMentno:CIDX."""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:CMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_cmode(self, connector_mode: enums.ParameterSetMode) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:CMODe \n
		Snippet: driver.configure.niotMeas.multiEval.listPy.set_cmode(connector_mode = enums.ParameterSetMode.GLOBal) \n
		Sets the connector mode, selecting whether all list mode segments use the same RF connection. \n
			:param connector_mode:
				- GLOBal: Use the same RF connection for all segments, see ROUTe:NIOT:MEASi:SPATh.
				- LIST: Assign a connection to each segment, see CONFigure:NIOT:MEASi:MEValuation:LIST:SEGMentno:CIDX."""
		param = Conversions.enum_scalar_to_str(connector_mode, enums.ParameterSetMode)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:CMODe {param}')

	def get_nconnections(self) -> int:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:NCONnections \n
		Snippet: value: int = driver.configure.niotMeas.multiEval.listPy.get_nconnections() \n
		Sets the number of connections to be defined for the list mode, for connector mode LIST. Define the connections via
		ROUTe:NIOT:MEAS<i>:SPATh. \n
			:return: no_of_connections: The maximum number of connections is limited by the number of connectors per smart channel.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:NCONnections?')
		return Conversions.str_to_int(response)

	def set_nconnections(self, no_of_connections: int) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:NCONnections \n
		Snippet: driver.configure.niotMeas.multiEval.listPy.set_nconnections(no_of_connections = 1) \n
		Sets the number of connections to be defined for the list mode, for connector mode LIST. Define the connections via
		ROUTe:NIOT:MEAS<i>:SPATh. \n
			:param no_of_connections: The maximum number of connections is limited by the number of connectors per smart channel.
		"""
		param = Conversions.decimal_value_to_str(no_of_connections)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST:NCONnections {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.listPy.get_value() \n
		Enables or disables the list mode. \n
			:return: enable: OFF: Disable list mode ON: Enable list mode
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST \n
		Snippet: driver.configure.niotMeas.multiEval.listPy.set_value(enable = False) \n
		Enables or disables the list mode. \n
			:param enable: OFF: Disable list mode ON: Enable list mode
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:LIST {param}')

	def clone(self) -> 'ListPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
