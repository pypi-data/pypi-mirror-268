from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmodeCls:
	"""Amode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amode", core, parent)

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.AnalysisMode:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:AMODe:MODulation \n
		Snippet: value: enums.AnalysisMode = driver.configure.wcdmaMeas.multiEval.amode.get_modulation() \n
		Defines whether a possible origin offset is included in the measurement results (WOOFfset) or subtracted out (NOOFfset) . \n
			:return: analysis_mode: WOOFfset: With origin offset NOOFfset: No origin offset
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:AMODe:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.AnalysisMode)

	def set_modulation(self, analysis_mode: enums.AnalysisMode) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:AMODe:MODulation \n
		Snippet: driver.configure.wcdmaMeas.multiEval.amode.set_modulation(analysis_mode = enums.AnalysisMode.NOOFfset) \n
		Defines whether a possible origin offset is included in the measurement results (WOOFfset) or subtracted out (NOOFfset) . \n
			:param analysis_mode: WOOFfset: With origin offset NOOFfset: No origin offset
		"""
		param = Conversions.enum_scalar_to_str(analysis_mode, enums.AnalysisMode)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:AMODe:MODulation {param}')
