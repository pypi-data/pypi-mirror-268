from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MperiodCls:
	"""Mperiod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mperiod", core, parent)

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.MeasPeriod:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:MPERiod:MODulation \n
		Snippet: value: enums.MeasPeriod = driver.configure.wcdmaMeas.multiEval.mperiod.get_modulation() \n
		Selects the width of the basic measurement period within each measured slot. To define the number of measured slots, see
		method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.msCount. \n
			:return: meas_period: FULLslot: Full-slot measurement HALFslot: Half-slot measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:MPERiod:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.MeasPeriod)

	def set_modulation(self, meas_period: enums.MeasPeriod) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:MPERiod:MODulation \n
		Snippet: driver.configure.wcdmaMeas.multiEval.mperiod.set_modulation(meas_period = enums.MeasPeriod.FULLslot) \n
		Selects the width of the basic measurement period within each measured slot. To define the number of measured slots, see
		method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.msCount. \n
			:param meas_period: FULLslot: Full-slot measurement HALFslot: Half-slot measurement
		"""
		param = Conversions.enum_scalar_to_str(meas_period, enums.MeasPeriod)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:MPERiod:MODulation {param}')
