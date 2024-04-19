from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmodeCls:
	"""Dmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmode", core, parent)

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.DetectionMode:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:DMODe:MODulation \n
		Snippet: value: enums.DetectionMode = driver.configure.wcdmaMeas.multiEval.dmode.get_modulation() \n
		Selects the detection mode for uplink WCDMA signals. \n
			:return: detection_mode: A3G: 3GPP Signal Auto
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:DMODe:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.DetectionMode)

	def set_modulation(self, detection_mode: enums.DetectionMode) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:DMODe:MODulation \n
		Snippet: driver.configure.wcdmaMeas.multiEval.dmode.set_modulation(detection_mode = enums.DetectionMode.A3G) \n
		Selects the detection mode for uplink WCDMA signals. \n
			:param detection_mode: A3G: 3GPP Signal Auto
		"""
		param = Conversions.enum_scalar_to_str(detection_mode, enums.DetectionMode)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:DMODe:MODulation {param}')
