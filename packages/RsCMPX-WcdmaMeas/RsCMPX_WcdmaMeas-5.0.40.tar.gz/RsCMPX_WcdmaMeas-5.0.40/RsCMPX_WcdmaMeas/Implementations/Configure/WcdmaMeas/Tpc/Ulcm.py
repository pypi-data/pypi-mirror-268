from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UlcmCls:
	"""Ulcm commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ulcm", core, parent)

	def get_mlength(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ULCM:MLENgth \n
		Snippet: value: int = driver.configure.wcdmaMeas.tpc.ulcm.get_mlength() \n
		Query the number of slots measured in UL Compressed Mode mode. The value is fixed. It can only be determined while the UL
		Compressed Mode mode is active. \n
			:return: meas_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:ULCM:MLENgth?')
		return Conversions.str_to_int(response)

	def set_mlength(self, meas_length: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ULCM:MLENgth \n
		Snippet: driver.configure.wcdmaMeas.tpc.ulcm.set_mlength(meas_length = 1) \n
		Query the number of slots measured in UL Compressed Mode mode. The value is fixed. It can only be determined while the UL
		Compressed Mode mode is active. \n
			:param meas_length: No help available
		"""
		param = Conversions.decimal_value_to_str(meas_length)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ULCM:MLENgth {param}')

	def get_aexecution(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ULCM:AEXecution \n
		Snippet: value: bool = driver.configure.wcdmaMeas.tpc.ulcm.get_aexecution() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:ULCM:AEXecution?')
		return Conversions.str_to_bool(response)

	def set_aexecution(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ULCM:AEXecution \n
		Snippet: driver.configure.wcdmaMeas.tpc.ulcm.set_aexecution(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ULCM:AEXecution {param}')
