from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_source(self) -> List[str]:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:CATalog:SOURce \n
		Snippet: value: List[str] = driver.trigger.wcdmaMeas.prach.catalog.get_source() \n
		Lists all trigger source values that can be set using method RsCMPX_WcdmaMeas.Trigger.WcdmaMeas.Prach.source. \n
			:return: trigger_list: Comma-separated list of all supported values. Each value is represented as a string.
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:PRACh:CATalog:SOURce?')
		return Conversions.str_to_str_list(response)
