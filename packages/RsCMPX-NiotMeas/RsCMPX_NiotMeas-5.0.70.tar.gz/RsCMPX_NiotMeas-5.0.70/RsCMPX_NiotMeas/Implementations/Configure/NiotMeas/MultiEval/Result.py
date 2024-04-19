from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 11 total commands, 0 Subgroups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Evm: bool: Error vector magnitude OFF: Do not evaluate results. ON: Evaluate results.
			- Magnitude_Error: bool: No parameter help available
			- Phase_Error: bool: No parameter help available
			- Inband_Emissions: bool: No parameter help available
			- Iq: bool: I/Q constellation diagram
			- Tx_Measurement: bool: TX measurement statistical overview
			- Spec_Em_Mask: bool: Spectrum emission mask
			- Aclr: bool: Adjacent channel leakage power ratio
			- Power_Monitor: bool: No parameter help available
			- Power_Dynamics: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Evm'),
			ArgStruct.scalar_bool('Magnitude_Error'),
			ArgStruct.scalar_bool('Phase_Error'),
			ArgStruct.scalar_bool('Inband_Emissions'),
			ArgStruct.scalar_bool('Iq'),
			ArgStruct.scalar_bool('Tx_Measurement'),
			ArgStruct.scalar_bool('Spec_Em_Mask'),
			ArgStruct.scalar_bool('Aclr'),
			ArgStruct.scalar_bool_optional('Power_Monitor'),
			ArgStruct.scalar_bool_optional('Power_Dynamics')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm: bool = None
			self.Magnitude_Error: bool = None
			self.Phase_Error: bool = None
			self.Inband_Emissions: bool = None
			self.Iq: bool = None
			self.Tx_Measurement: bool = None
			self.Spec_Em_Mask: bool = None
			self.Aclr: bool = None
			self.Power_Monitor: bool = None
			self.Power_Dynamics: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.niotMeas.multiEval.result.get_all() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. This command combines most other
		CONFigure:NIOT:MEAS<i>:MEValuation:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult[:ALL] \n
		Snippet with structure: \n
		structure = driver.configure.niotMeas.multiEval.result.AllStruct() \n
		structure.Evm: bool = False \n
		structure.Magnitude_Error: bool = False \n
		structure.Phase_Error: bool = False \n
		structure.Inband_Emissions: bool = False \n
		structure.Iq: bool = False \n
		structure.Tx_Measurement: bool = False \n
		structure.Spec_Em_Mask: bool = False \n
		structure.Aclr: bool = False \n
		structure.Power_Monitor: bool = False \n
		structure.Power_Dynamics: bool = False \n
		driver.configure.niotMeas.multiEval.result.set_all(value = structure) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. This command combines most other
		CONFigure:NIOT:MEAS<i>:MEValuation:RESult... commands. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:ALL', value)

	def get_ev_magnitude(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_ev_magnitude() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:EVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_ev_magnitude(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_ev_magnitude(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:EVMagnitude {param}')

	def get_merror(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:MERRor \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_merror() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:MERRor?')
		return Conversions.str_to_bool(response)

	def set_merror(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:MERRor \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_merror(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:MERRor {param}')

	def get_perror(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PERRor \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_perror() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PERRor?')
		return Conversions.str_to_bool(response)

	def set_perror(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PERRor \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_perror(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PERRor {param}')

	def get_iemissions(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:IEMissions \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_iemissions() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:IEMissions?')
		return Conversions.str_to_bool(response)

	def set_iemissions(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:IEMissions \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_iemissions(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:IEMissions {param}')

	def get_txm(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:TXM \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_txm() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:TXM?')
		return Conversions.str_to_bool(response)

	def set_txm(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:TXM \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_txm(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:TXM {param}')

	def get_iq(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:IQ \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_iq() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:IQ?')
		return Conversions.str_to_bool(response)

	def set_iq(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:IQ \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_iq(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:IQ {param}')

	def get_se_mask(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:SEMask \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_se_mask() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:SEMask?')
		return Conversions.str_to_bool(response)

	def set_se_mask(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:SEMask \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_se_mask(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:SEMask {param}')

	def get_aclr(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:ACLR \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_aclr() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:ACLR?')
		return Conversions.str_to_bool(response)

	def set_aclr(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:ACLR \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_aclr(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:ACLR {param}')

	def get_pmonitor(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PMONitor \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_pmonitor() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PMONitor?')
		return Conversions.str_to_bool(response)

	def set_pmonitor(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PMONitor \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_pmonitor(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PMONitor {param}')

	def get_pdynamics(self) -> bool:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PDYNamics \n
		Snippet: value: bool = driver.configure.niotMeas.multiEval.result.get_pdynamics() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:return: enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PDYNamics?')
		return Conversions.str_to_bool(response)

	def set_pdynamics(self, enable: bool) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PDYNamics \n
		Snippet: driver.configure.niotMeas.multiEval.result.set_pdynamics(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement.
			Table Header: Mnemonic / Square type / / Mnemonic / Square type \n
			- EVMagnitude / Error vector magnitude / TXM / TX meas. statistical overview
			- MERRor / Magnitude error / SEMask / Spectrum emission mask
			- PERRor / Phase error / ACLR / Adj. channel leakage power ratio
			- IEMissions / Inband emissions / PMONitor / Power monitor
			- IQ / I/Q constellation diagram / PDYNamics / Power dynamics \n
			:param enable: OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:RESult:PDYNamics {param}')
