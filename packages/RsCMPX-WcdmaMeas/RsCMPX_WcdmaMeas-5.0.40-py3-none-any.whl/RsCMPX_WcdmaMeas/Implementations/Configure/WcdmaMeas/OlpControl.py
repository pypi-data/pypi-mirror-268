from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OlpControlCls:
	"""OlpControl commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("olpControl", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:TOUT \n
		Snippet: value: float = driver.configure.wcdmaMeas.olpControl.get_timeout() \n
		No command help available \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OLPControl:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:TOUT \n
		Snippet: driver.configure.wcdmaMeas.olpControl.set_timeout(timeout = 1.0) \n
		No command help available \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OLPControl:TOUT {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:MOEXception \n
		Snippet: value: bool = driver.configure.wcdmaMeas.olpControl.get_mo_exception() \n
		No command help available \n
			:return: meas_on_exception: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OLPControl:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:MOEXception \n
		Snippet: driver.configure.wcdmaMeas.olpControl.set_mo_exception(meas_on_exception = False) \n
		No command help available \n
			:param meas_on_exception: No help available
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OLPControl:MOEXception {param}')

	def get_limit(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:LIMit \n
		Snippet: value: float = driver.configure.wcdmaMeas.olpControl.get_limit() \n
		No command help available \n
			:return: olp_limit: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OLPControl:LIMit?')
		return Conversions.str_to_float(response)

	def set_limit(self, olp_limit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:LIMit \n
		Snippet: driver.configure.wcdmaMeas.olpControl.set_limit(olp_limit = 1.0) \n
		No command help available \n
			:param olp_limit: No help available
		"""
		param = Conversions.decimal_value_to_str(olp_limit)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OLPControl:LIMit {param}')
