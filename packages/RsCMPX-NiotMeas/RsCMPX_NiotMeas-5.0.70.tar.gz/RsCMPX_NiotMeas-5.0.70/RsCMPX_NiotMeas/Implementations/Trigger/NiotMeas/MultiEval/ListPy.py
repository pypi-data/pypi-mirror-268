from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ListMode:
		"""SCPI: TRIGger:NIOT:MEASurement<Instance>:MEValuation:LIST:MODE \n
		Snippet: value: enums.ListMode = driver.trigger.niotMeas.multiEval.listPy.get_mode() \n
		Specifies the trigger mode for list mode measurements. For configuration of retrigger flags, see method RsCMPX_NiotMeas.
		Configure.NiotMeas.MultiEval.ListPy.Segment.Setup.set. \n
			:return: mode: ONCE: A trigger event is only required to start the measurement. As a result, the entire range of segments to be measured is captured without additional trigger event. The retrigger flag of the first segment is evaluated. The other retrigger flags are ignored. SEGMent: The retrigger flag of each segment is evaluated. It defines whether the measurement waits for a trigger event before capturing the segment, or not.
		"""
		response = self._core.io.query_str('TRIGger:NIOT:MEASurement<Instance>:MEValuation:LIST:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ListMode)

	def set_mode(self, mode: enums.ListMode) -> None:
		"""SCPI: TRIGger:NIOT:MEASurement<Instance>:MEValuation:LIST:MODE \n
		Snippet: driver.trigger.niotMeas.multiEval.listPy.set_mode(mode = enums.ListMode.ONCE) \n
		Specifies the trigger mode for list mode measurements. For configuration of retrigger flags, see method RsCMPX_NiotMeas.
		Configure.NiotMeas.MultiEval.ListPy.Segment.Setup.set. \n
			:param mode: ONCE: A trigger event is only required to start the measurement. As a result, the entire range of segments to be measured is captured without additional trigger event. The retrigger flag of the first segment is evaluated. The other retrigger flags are ignored. SEGMent: The retrigger flag of each segment is evaluated. It defines whether the measurement waits for a trigger event before capturing the segment, or not.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ListMode)
		self._core.io.write(f'TRIGger:NIOT:MEASurement<Instance>:MEValuation:LIST:MODE {param}')
