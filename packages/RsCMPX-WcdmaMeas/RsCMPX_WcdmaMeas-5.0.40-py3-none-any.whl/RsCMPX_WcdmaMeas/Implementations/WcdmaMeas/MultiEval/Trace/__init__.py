from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TraceCls:
	"""Trace commands group definition. 61 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	@property
	def phd(self):
		"""phd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phd'):
			from .Phd import PhdCls
			self._phd = PhdCls(self._core, self._cmd_group)
		return self._phd

	@property
	def cdeMonitor(self):
		"""cdeMonitor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdeMonitor'):
			from .CdeMonitor import CdeMonitorCls
			self._cdeMonitor = CdeMonitorCls(self._core, self._cmd_group)
		return self._cdeMonitor

	@property
	def cdpMonitor(self):
		"""cdpMonitor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdpMonitor'):
			from .CdpMonitor import CdpMonitorCls
			self._cdpMonitor = CdpMonitorCls(self._core, self._cmd_group)
		return self._cdpMonitor

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	@property
	def emask(self):
		"""emask commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_emask'):
			from .Emask import EmaskCls
			self._emask = EmaskCls(self._core, self._cmd_group)
		return self._emask

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .EvMagnitude import EvMagnitudeCls
			self._evMagnitude = EvMagnitudeCls(self._core, self._cmd_group)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import MerrorCls
			self._merror = MerrorCls(self._core, self._cmd_group)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import PerrorCls
			self._perror = PerrorCls(self._core, self._cmd_group)
		return self._perror

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import IqCls
			self._iq = IqCls(self._core, self._cmd_group)
		return self._iq

	def clone(self) -> 'TraceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TraceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
