from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 141 total commands, 11 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .EvMagnitude import EvMagnitudeCls
			self._evMagnitude = EvMagnitudeCls(self._core, self._cmd_group)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import MerrorCls
			self._merror = MerrorCls(self._core, self._cmd_group)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import PerrorCls
			self._perror = PerrorCls(self._core, self._cmd_group)
		return self._perror

	@property
	def inbandEmission(self):
		"""inbandEmission commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_inbandEmission'):
			from .InbandEmission import InbandEmissionCls
			self._inbandEmission = InbandEmissionCls(self._core, self._cmd_group)
		return self._inbandEmission

	@property
	def modulation(self):
		"""modulation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def seMask(self):
		"""seMask commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_seMask'):
			from .SeMask import SeMaskCls
			self._seMask = SeMaskCls(self._core, self._cmd_group)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .Aclr import AclrCls
			self._aclr = AclrCls(self._core, self._cmd_group)
		return self._aclr

	@property
	def pdynamics(self):
		"""pdynamics commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Pdynamics import PdynamicsCls
			self._pdynamics = PdynamicsCls(self._core, self._cmd_group)
		return self._pdynamics

	@property
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:NIOT:MEASurement<Instance>:MEValuation \n
		Snippet: driver.niotMeas.multiEval.initiate() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:NIOT:MEASurement<Instance>:MEValuation', opc_timeout_ms)

	def stop(self) -> None:
		"""SCPI: STOP:NIOT:MEASurement<Instance>:MEValuation \n
		Snippet: driver.niotMeas.multiEval.stop() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:NIOT:MEASurement<Instance>:MEValuation')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:NIOT:MEASurement<Instance>:MEValuation \n
		Snippet: driver.niotMeas.multiEval.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_NiotMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:NIOT:MEASurement<Instance>:MEValuation', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:NIOT:MEASurement<Instance>:MEValuation \n
		Snippet: driver.niotMeas.multiEval.abort() \n
			INTRO_CMD_HELP: Starts, stops or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the RUN state.
			- STOP... halts the measurement immediately. The measurement enters the RDY state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the OFF state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:NIOT:MEASurement<Instance>:MEValuation', opc_timeout_ms)

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
