from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DcarrierCls:
	"""Dcarrier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcarrier", core, parent)

	def get_separation(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:DCARrier:SEParation \n
		Snippet: value: float = driver.configure.wcdmaMeas.rfSettings.dcarrier.get_separation() \n
		Sets the carrier 1 and carrier 2 frequency separation for measurements with dual uplink carrier. \n
			:return: dc_freq_sep: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:RFSettings:DCARrier:SEParation?')
		return Conversions.str_to_float(response)

	def set_separation(self, dc_freq_sep: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:DCARrier:SEParation \n
		Snippet: driver.configure.wcdmaMeas.rfSettings.dcarrier.set_separation(dc_freq_sep = 1.0) \n
		Sets the carrier 1 and carrier 2 frequency separation for measurements with dual uplink carrier. \n
			:param dc_freq_sep: No help available
		"""
		param = Conversions.decimal_value_to_str(dc_freq_sep)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:DCARrier:SEParation {param}')
