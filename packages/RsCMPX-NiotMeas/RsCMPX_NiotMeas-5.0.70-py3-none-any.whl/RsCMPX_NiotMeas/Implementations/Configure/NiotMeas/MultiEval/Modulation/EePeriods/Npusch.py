from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NpuschCls:
	"""Npusch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npusch", core, parent)

	# noinspection PyTypeChecker
	def get_leading(self) -> enums.LeadLag:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:NPUSch:LEADing \n
		Snippet: value: enums.LeadLag = driver.configure.niotMeas.multiEval.modulation.eePeriods.npusch.get_leading() \n
		Defines an exclusion period at the beginning of each NPUSCH transmission. The excluded symbols are ignored for modulation
		results. \n
			:return: leading: OFF: no exclusion S1: exclude first symbol
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:NPUSch:LEADing?')
		return Conversions.str_to_scalar_enum(response, enums.LeadLag)

	def set_leading(self, leading: enums.LeadLag) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:NPUSch:LEADing \n
		Snippet: driver.configure.niotMeas.multiEval.modulation.eePeriods.npusch.set_leading(leading = enums.LeadLag.OFF) \n
		Defines an exclusion period at the beginning of each NPUSCH transmission. The excluded symbols are ignored for modulation
		results. \n
			:param leading: OFF: no exclusion S1: exclude first symbol
		"""
		param = Conversions.enum_scalar_to_str(leading, enums.LeadLag)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:NPUSch:LEADing {param}')

	# noinspection PyTypeChecker
	def get_lagging(self) -> enums.LeadLag:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:NPUSch:LAGGing \n
		Snippet: value: enums.LeadLag = driver.configure.niotMeas.multiEval.modulation.eePeriods.npusch.get_lagging() \n
		Defines an exclusion period at the end of each NPUSCH transmission. The excluded symbols are ignored for modulation
		results. \n
			:return: lagging: OFF: no exclusion S1: exclude first symbol
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:NPUSch:LAGGing?')
		return Conversions.str_to_scalar_enum(response, enums.LeadLag)

	def set_lagging(self, lagging: enums.LeadLag) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:NPUSch:LAGGing \n
		Snippet: driver.configure.niotMeas.multiEval.modulation.eePeriods.npusch.set_lagging(lagging = enums.LeadLag.OFF) \n
		Defines an exclusion period at the end of each NPUSCH transmission. The excluded symbols are ignored for modulation
		results. \n
			:param lagging: OFF: no exclusion S1: exclude first symbol
		"""
		param = Conversions.enum_scalar_to_str(lagging, enums.LeadLag)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:NPUSch:LAGGing {param}')
