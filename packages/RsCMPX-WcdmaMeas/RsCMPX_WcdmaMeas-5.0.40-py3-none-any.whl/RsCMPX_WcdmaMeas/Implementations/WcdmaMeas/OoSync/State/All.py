from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, timeout: float = None, target_main_state: enums.TargetMainState = None, target_sync_state: enums.TargetSyncState = None) -> List[enums.ResourceState]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:OOSYnc:STATe:ALL \n
		Snippet: value: List[enums.ResourceState] = driver.wcdmaMeas.ooSync.state.all.fetch(timeout = 1.0, target_main_state = enums.TargetMainState.OFF, target_sync_state = enums.TargetSyncState.ADJusted) \n
		No command help available \n
			:param timeout: No help available
			:param target_main_state: No help available
			:param target_sync_state: No help available
			:return: state: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('timeout', timeout, DataType.Float, None, is_optional=True), ArgSingle('target_main_state', target_main_state, DataType.Enum, enums.TargetMainState, is_optional=True), ArgSingle('target_sync_state', target_sync_state, DataType.Enum, enums.TargetSyncState, is_optional=True))
		response = self._core.io.query_str(f'FETCh:WCDMa:MEASurement<Instance>:OOSYnc:STATe:ALL? {param}'.rstrip())
		return Conversions.str_to_list_enum(response, enums.ResourceState)
