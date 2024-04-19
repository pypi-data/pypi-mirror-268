from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScountCls:
	"""Scount commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	def get_ber(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SCOunt:BER \n
		Snippet: value: int = driver.configure.wcdmaMeas.multiEval.scount.get_ber() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: Number of transport blocks
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SCOunt:BER?')
		return Conversions.str_to_int(response)

	def set_ber(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SCOunt:BER \n
		Snippet: driver.configure.wcdmaMeas.multiEval.scount.set_ber(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: Number of transport blocks
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SCOunt:BER {param}')

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SCOunt:MODulation \n
		Snippet: value: int = driver.configure.wcdmaMeas.multiEval.scount.get_modulation() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: Number of measurement intervals
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SCOunt:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SCOunt:MODulation \n
		Snippet: driver.configure.wcdmaMeas.multiEval.scount.set_modulation(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: Number of measurement intervals
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SCOunt:MODulation {param}')

	def get_spectrum(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SCOunt:SPECtrum \n
		Snippet: value: int = driver.configure.wcdmaMeas.multiEval.scount.get_spectrum() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: Number of measurement intervals
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SCOunt:SPECtrum?')
		return Conversions.str_to_int(response)

	def set_spectrum(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SCOunt:SPECtrum \n
		Snippet: driver.configure.wcdmaMeas.multiEval.scount.set_spectrum(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: Number of measurement intervals
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SCOunt:SPECtrum {param}')
