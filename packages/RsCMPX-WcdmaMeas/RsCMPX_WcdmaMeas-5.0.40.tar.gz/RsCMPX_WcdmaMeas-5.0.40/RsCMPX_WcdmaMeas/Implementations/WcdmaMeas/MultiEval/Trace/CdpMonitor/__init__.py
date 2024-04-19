from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdpMonitorCls:
	"""CdpMonitor commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdpMonitor", core, parent)

	@property
	def qsignal(self):
		"""qsignal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qsignal'):
			from .Qsignal import QsignalCls
			self._qsignal = QsignalCls(self._core, self._cmd_group)
		return self._qsignal

	@property
	def isignal(self):
		"""isignal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_isignal'):
			from .Isignal import IsignalCls
			self._isignal = IsignalCls(self._core, self._cmd_group)
		return self._isignal

	def clone(self) -> 'CdpMonitorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CdpMonitorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
