from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMaskCls:
	"""SeMask commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seMask", core, parent)

	# noinspection PyTypeChecker
	def get_obw_mode(self) -> enums.ObwMode:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SPECtrum:SEMask:OBWMode \n
		Snippet: value: enums.ObwMode = driver.configure.niotMeas.multiEval.spectrum.seMask.get_obw_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:NIOT:MEASurement<Instance>:MEValuation:SPECtrum:SEMask:OBWMode?')
		return Conversions.str_to_scalar_enum(response, enums.ObwMode)

	def set_obw_mode(self, mode: enums.ObwMode) -> None:
		"""SCPI: CONFigure:NIOT:MEASurement<Instance>:MEValuation:SPECtrum:SEMask:OBWMode \n
		Snippet: driver.configure.niotMeas.multiEval.spectrum.seMask.set_obw_mode(mode = enums.ObwMode.BW99) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ObwMode)
		self._core.io.write(f'CONFigure:NIOT:MEASurement<Instance>:MEValuation:SPECtrum:SEMask:OBWMode {param}')
