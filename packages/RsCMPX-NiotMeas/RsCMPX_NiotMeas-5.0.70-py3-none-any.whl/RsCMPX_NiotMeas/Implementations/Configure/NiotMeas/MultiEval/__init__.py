from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 62 total commands, 8 Subgroups, 16 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def subcarrier(self):
		"""subcarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subcarrier'):
			from .Subcarrier import SubcarrierCls
			self._subcarrier = SubcarrierCls(self._core, self._cmd_group)
		return self._subcarrier

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def spectrum(self):
		"""spectrum commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def pdynamics(self):
		"""pdynamics commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Pdynamics import PdynamicsCls
			self._pdynamics = PdynamicsCls(self._core, self._cmd_group)
		return self._pdynamics

	@property
	def scount(self):
		"""scount commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 11 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	# noinspection PyTypeChecker
	def get_fsy_range(self) -> enums.LowHigh:
		"""SCPI: CONFigure:NIOT:MEASurement<instance>:MEValuation:FSYRange \n
		Snippet: value: enums.LowHigh = driver.configure.niotMeas.multiEval.get_fsy_range() \n
		Specifies the frequency synchronization range. \n
			:return: fsr: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:FSYRange?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def set_fsy_range(self, fsr: enums.LowHigh) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<instance>:MEValuation:FSYRange \n
		Snippet: driver.configure.niotMeas.multiEval.set_fsy_range(fsr = enums.LowHigh.HIGH) \n
		Specifies the frequency synchronization range. \n
			:param fsr: No help available
		"""
		param = Conversions.enum_scalar_to_str(fsr, enums.LowHigh)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:FSYRange {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.niotMeas.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.configure.niotMeas.multiEval.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:TOUT {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.Mode:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:DMODe \n
		Snippet: value: enums.Mode = driver.configure.niotMeas.multiEval.get_dmode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str_with_opc('CONFigure:NIOT:MEASurement<Instance>:MEValuation:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.Mode)

	def set_dmode(self, mode: enums.Mode) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:DMODe \n
		Snippet: driver.configure.niotMeas.multiEval.set_dmode(mode = enums.Mode.FDD) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Mode)
		self._core.io.write_with_opc(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:DMODe {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.MeasurementMode:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MMODe \n
		Snippet: value: enums.MeasurementMode = driver.configure.niotMeas.multiEval.get_mmode() \n
		Selects the measurement mode. \n
			:return: measurement_mode: NORMal: normal mode MELMode: multi-evaluation list mode
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementMode)

	def set_mmode(self, measurement_mode: enums.MeasurementMode) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MMODe \n
		Snippet: driver.configure.niotMeas.multiEval.set_mmode(measurement_mode = enums.MeasurementMode.MELMode) \n
		Selects the measurement mode. \n
			:param measurement_mode: NORMal: normal mode MELMode: multi-evaluation list mode
		"""
		param = Conversions.enum_scalar_to_str(measurement_mode, enums.MeasurementMode)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:MMODe {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.niotMeas.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: driver.configure.niotMeas.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:REPetition {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.niotMeas.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.niotMeas.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:SCONdition {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.get_mo_exception() \n
		Specifies whether measurement results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF: Faulty results are rejected ON: Results are never rejected
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.niotMeas.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF: Faulty results are rejected ON: Results are never rejected
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_cprefix(self) -> enums.CyclicPrefix:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:CPRefix \n
		Snippet: value: enums.CyclicPrefix = driver.configure.niotMeas.multiEval.get_cprefix() \n
		No command help available \n
			:return: cyclic_prefix: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:CPRefix?')
		return Conversions.str_to_scalar_enum(response, enums.CyclicPrefix)

	def set_cprefix(self, cyclic_prefix: enums.CyclicPrefix) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:CPRefix \n
		Snippet: driver.configure.niotMeas.multiEval.set_cprefix(cyclic_prefix = enums.CyclicPrefix.EXTended) \n
		No command help available \n
			:param cyclic_prefix: No help available
		"""
		param = Conversions.enum_scalar_to_str(cyclic_prefix, enums.CyclicPrefix)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:CPRefix {param}')

	# noinspection PyTypeChecker
	def get_channel_bw(self) -> enums.ChannelBw:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:CBANdwidth \n
		Snippet: value: enums.ChannelBw = driver.configure.niotMeas.multiEval.get_channel_bw() \n
		No command help available \n
			:return: channel_bw: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:CBANdwidth?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBw)

	def set_channel_bw(self, channel_bw: enums.ChannelBw) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:CBANdwidth \n
		Snippet: driver.configure.niotMeas.multiEval.set_channel_bw(channel_bw = enums.ChannelBw.B200) \n
		No command help available \n
			:param channel_bw: No help available
		"""
		param = Conversions.enum_scalar_to_str(channel_bw, enums.ChannelBw)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:CBANdwidth {param}')

	def get_plc_id(self) -> int:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:PLCid \n
		Snippet: value: int = driver.configure.niotMeas.multiEval.get_plc_id() \n
		Specifies the physical layer cell ID. \n
			:return: phs_layer_cell_id: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:PLCid?')
		return Conversions.str_to_int(response)

	def set_plc_id(self, phs_layer_cell_id: int) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:PLCid \n
		Snippet: driver.configure.niotMeas.multiEval.set_plc_id(phs_layer_cell_id = 1) \n
		Specifies the physical layer cell ID. \n
			:param phs_layer_cell_id: No help available
		"""
		param = Conversions.decimal_value_to_str(phs_layer_cell_id)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:PLCid {param}')

	def get_dss(self) -> int:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:DSS \n
		Snippet: value: int = driver.configure.niotMeas.multiEval.get_dss() \n
		Specifies the delta sequence shift value (Δss) used to calculate the sequence shift pattern for the NPUSCH. \n
			:return: delta_seq_shift: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:DSS?')
		return Conversions.str_to_int(response)

	def set_dss(self, delta_seq_shift: int) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:DSS \n
		Snippet: driver.configure.niotMeas.multiEval.set_dss(delta_seq_shift = 1) \n
		Specifies the delta sequence shift value (Δss) used to calculate the sequence shift pattern for the NPUSCH. \n
			:param delta_seq_shift: No help available
		"""
		param = Conversions.decimal_value_to_str(delta_seq_shift)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:DSS {param}')

	# noinspection PyTypeChecker
	def get_sc_spacing(self) -> enums.SubCarrSpacing:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SCSPacing \n
		Snippet: value: enums.SubCarrSpacing = driver.configure.niotMeas.multiEval.get_sc_spacing() \n
		Selects the subcarrier spacing. \n
			:return: sub_carr_spacing: 3.75 kHz or 15 kHz
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.SubCarrSpacing)

	def set_sc_spacing(self, sub_carr_spacing: enums.SubCarrSpacing) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SCSPacing \n
		Snippet: driver.configure.niotMeas.multiEval.set_sc_spacing(sub_carr_spacing = enums.SubCarrSpacing.S15K) \n
		Selects the subcarrier spacing. \n
			:param sub_carr_spacing: 3.75 kHz or 15 kHz
		"""
		param = Conversions.enum_scalar_to_str(sub_carr_spacing, enums.SubCarrSpacing)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:SCSPacing {param}')

	# noinspection PyTypeChecker
	def get_np_format(self) -> enums.NpuschFormat:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:NPFormat \n
		Snippet: value: enums.NpuschFormat = driver.configure.niotMeas.multiEval.get_np_format() \n
		Specifies the format of the NPUSCH. \n
			:return: npusch_format: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:NPFormat?')
		return Conversions.str_to_scalar_enum(response, enums.NpuschFormat)

	def set_np_format(self, npusch_format: enums.NpuschFormat) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:NPFormat \n
		Snippet: driver.configure.niotMeas.multiEval.set_np_format(npusch_format = enums.NpuschFormat.F1) \n
		Specifies the format of the NPUSCH. \n
			:param npusch_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(npusch_format, enums.NpuschFormat)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:NPFormat {param}')

	# noinspection PyTypeChecker
	def get_nrepetitions(self) -> enums.NofRepetitions:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:NREPetitions \n
		Snippet: value: enums.NofRepetitions = driver.configure.niotMeas.multiEval.get_nrepetitions() \n
		Specifies the number of NPUSCH repetitions. \n
			:return: nof_repetitions: Number of NPUSCH repetitions: 1, 2, 4, ..., 512, 1024, 2048
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:NREPetitions?')
		return Conversions.str_to_scalar_enum(response, enums.NofRepetitions)

	def set_nrepetitions(self, nof_repetitions: enums.NofRepetitions) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:NREPetitions \n
		Snippet: driver.configure.niotMeas.multiEval.set_nrepetitions(nof_repetitions = enums.NofRepetitions.NR1) \n
		Specifies the number of NPUSCH repetitions. \n
			:param nof_repetitions: Number of NPUSCH repetitions: 1, 2, 4, ..., 512, 1024, 2048
		"""
		param = Conversions.enum_scalar_to_str(nof_repetitions, enums.NofRepetitions)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:NREPetitions {param}')

	# noinspection PyTypeChecker
	def get_nr_units(self) -> enums.NofRsrcUnits:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:NRUNits \n
		Snippet: value: enums.NofRsrcUnits = driver.configure.niotMeas.multiEval.get_nr_units() \n
		Specifies the number of resource units allocated for the NPUSCH. \n
			:return: nof_ru: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:NRUNits?')
		return Conversions.str_to_scalar_enum(response, enums.NofRsrcUnits)

	def set_nr_units(self, nof_ru: enums.NofRsrcUnits) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:NRUNits \n
		Snippet: driver.configure.niotMeas.multiEval.set_nr_units(nof_ru = enums.NofRsrcUnits.NRU01) \n
		Specifies the number of resource units allocated for the NPUSCH. \n
			:param nof_ru: No help available
		"""
		param = Conversions.enum_scalar_to_str(nof_ru, enums.NofRsrcUnits)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:NRUNits {param}')

	def get_nslots(self) -> int:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:NSLots \n
		Snippet: value: int = driver.configure.niotMeas.multiEval.get_nslots() \n
		Configures the length of the captured sequence of slots. \n
			:return: nof_slots: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:NSLots?')
		return Conversions.str_to_int(response)

	def set_nslots(self, nof_slots: int) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:NSLots \n
		Snippet: driver.configure.niotMeas.multiEval.set_nslots(nof_slots = 1) \n
		Configures the length of the captured sequence of slots. \n
			:param nof_slots: No help available
		"""
		param = Conversions.decimal_value_to_str(nof_slots)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:NSLots {param}')

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
