from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 6 total commands, 0 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.niotMeas.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:return: rf_input_ext_att: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, rf_input_ext_att: float) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.niotMeas.rfSettings.set_eattenuation(rf_input_ext_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:param rf_input_ext_att: No help available
		"""
		param = Conversions.decimal_value_to_str(rf_input_ext_att)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.niotMeas.rfSettings.get_umargin() \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. \n
			:return: user_margin: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.niotMeas.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. \n
			:param user_margin: No help available
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.niotMeas.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal. \n
			:return: exp_nom_pow: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nom_pow: float) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: driver.configure.niotMeas.rfSettings.set_envelope_power(exp_nom_pow = 1.0) \n
		Sets the expected nominal power of the measured RF signal. \n
			:param exp_nom_pow: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		param = Conversions.decimal_value_to_str(exp_nom_pow)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:RFSettings:ENPower {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.niotMeas.rfSettings.get_frequency() \n
		Selects the center frequency of the RF analyzer. Using the unit CH, the frequency can be set via the channel number. The
		allowed channel number range depends on the operating band, see 'Frequency bands'. For the supported frequency range, see
		'Frequency ranges'. \n
			:return: analyzer_freq: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, analyzer_freq: float) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.niotMeas.rfSettings.set_frequency(analyzer_freq = 1.0) \n
		Selects the center frequency of the RF analyzer. Using the unit CH, the frequency can be set via the channel number. The
		allowed channel number range depends on the operating band, see 'Frequency bands'. For the supported frequency range, see
		'Frequency ranges'. \n
			:param analyzer_freq: No help available
		"""
		param = Conversions.decimal_value_to_str(analyzer_freq)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:RFSettings:FREQuency {param}')

	def get_foffset(self) -> int:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: value: int = driver.configure.niotMeas.rfSettings.get_foffset() \n
		No command help available \n
			:return: offset: No help available
		"""
		response = self._core.io.query_str_with_opc('CONFigure:NIOT:MEASurement<Instance>:RFSettings:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, offset: int) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: driver.configure.niotMeas.rfSettings.set_foffset(offset = 1) \n
		No command help available \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write_with_opc(f'CONFigure:NIOT:MEASurement<Instance>:RFSettings:FOFFset {param}')

	def get_ml_offset(self) -> float:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: value: float = driver.configure.niotMeas.rfSettings.get_ml_offset() \n
		No command help available \n
			:return: mix_lev_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:RFSettings:MLOFfset?')
		return Conversions.str_to_float(response)

	def set_ml_offset(self, mix_lev_offset: float) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: driver.configure.niotMeas.rfSettings.set_ml_offset(mix_lev_offset = 1.0) \n
		No command help available \n
			:param mix_lev_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(mix_lev_offset)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:RFSettings:MLOFfset {param}')
