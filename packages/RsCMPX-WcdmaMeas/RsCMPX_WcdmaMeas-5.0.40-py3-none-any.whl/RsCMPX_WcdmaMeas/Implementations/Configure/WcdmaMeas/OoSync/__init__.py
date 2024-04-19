from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OoSyncCls:
	"""OoSync commands group definition. 5 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ooSync", core, parent)

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	def get_aa_dpch_level(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:AADPchlevel \n
		Snippet: value: bool = driver.configure.wcdmaMeas.ooSync.get_aa_dpch_level() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:AADPchlevel?')
		return Conversions.str_to_bool(response)

	def set_aa_dpch_level(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:AADPchlevel \n
		Snippet: driver.configure.wcdmaMeas.ooSync.set_aa_dpch_level(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:AADPchlevel {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:TOUT \n
		Snippet: value: float = driver.configure.wcdmaMeas.ooSync.get_timeout() \n
		No command help available \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:TOUT \n
		Snippet: driver.configure.wcdmaMeas.ooSync.set_timeout(timeout = 1.0) \n
		No command help available \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:TOUT {param}')

	def clone(self) -> 'OoSyncCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OoSyncCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
