from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdThresholdCls:
	"""CdThreshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdThreshold", core, parent)

	def get_modulation(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:CDTHreshold:MODulation \n
		Snippet: value: float = driver.configure.wcdmaMeas.multiEval.cdThreshold.get_modulation() \n
		Defines the minimum relative signal strength of the (E-) DPDCH in the WCDMA signal (if present) to be detected and
		evaluated. \n
			:return: threshold: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:CDTHreshold:MODulation?')
		return Conversions.str_to_float(response)

	def set_modulation(self, threshold: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:CDTHreshold:MODulation \n
		Snippet: driver.configure.wcdmaMeas.multiEval.cdThreshold.set_modulation(threshold = 1.0) \n
		Defines the minimum relative signal strength of the (E-) DPDCH in the WCDMA signal (if present) to be detected and
		evaluated. \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:CDTHreshold:MODulation {param}')
