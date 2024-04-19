from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	def get_pon_upper(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:PONupper \n
		Snippet: value: float = driver.configure.wcdmaMeas.ooSync.limit.get_pon_upper() \n
		No command help available \n
			:return: pon_lower: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:PONupper?')
		return Conversions.str_to_float(response)

	def set_pon_upper(self, pon_lower: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:PONupper \n
		Snippet: driver.configure.wcdmaMeas.ooSync.limit.set_pon_upper(pon_lower = 1.0) \n
		No command help available \n
			:param pon_lower: No help available
		"""
		param = Conversions.decimal_value_to_str(pon_lower)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:PONupper {param}')

	def get_poff_upper(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:POFFupper \n
		Snippet: value: float = driver.configure.wcdmaMeas.ooSync.limit.get_poff_upper() \n
		No command help available \n
			:return: po_ulimit: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:POFFupper?')
		return Conversions.str_to_float(response)

	def set_poff_upper(self, po_ulimit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:POFFupper \n
		Snippet: driver.configure.wcdmaMeas.ooSync.limit.set_poff_upper(po_ulimit = 1.0) \n
		No command help available \n
			:param po_ulimit: No help available
		"""
		param = Conversions.decimal_value_to_str(po_ulimit)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:POFFupper {param}')

	def get_threshold(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:THReshold \n
		Snippet: value: float = driver.configure.wcdmaMeas.ooSync.limit.get_threshold() \n
		No command help available \n
			:return: threshold_level: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold_level: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:THReshold \n
		Snippet: driver.configure.wcdmaMeas.ooSync.limit.set_threshold(threshold_level = 1.0) \n
		No command help available \n
			:param threshold_level: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold_level)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:THReshold {param}')
