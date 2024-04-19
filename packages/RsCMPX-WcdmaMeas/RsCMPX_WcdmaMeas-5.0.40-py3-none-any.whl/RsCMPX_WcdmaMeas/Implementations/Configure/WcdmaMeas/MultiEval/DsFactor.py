from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DsFactorCls:
	"""DsFactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsFactor", core, parent)

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.SpreadingFactorA:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:DSFactor:MODulation \n
		Snippet: value: enums.SpreadingFactorA = driver.configure.wcdmaMeas.multiEval.dsFactor.get_modulation() \n
		Selects the spreading factor for the displayed code domain monitor results. \n
			:return: spreading_factor: Spreading factor 4 to 256
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:DSFactor:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.SpreadingFactorA)

	def set_modulation(self, spreading_factor: enums.SpreadingFactorA) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:DSFactor:MODulation \n
		Snippet: driver.configure.wcdmaMeas.multiEval.dsFactor.set_modulation(spreading_factor = enums.SpreadingFactorA.SF128) \n
		Selects the spreading factor for the displayed code domain monitor results. \n
			:param spreading_factor: Spreading factor 4 to 256
		"""
		param = Conversions.enum_scalar_to_str(spreading_factor, enums.SpreadingFactorA)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:DSFactor:MODulation {param}')
