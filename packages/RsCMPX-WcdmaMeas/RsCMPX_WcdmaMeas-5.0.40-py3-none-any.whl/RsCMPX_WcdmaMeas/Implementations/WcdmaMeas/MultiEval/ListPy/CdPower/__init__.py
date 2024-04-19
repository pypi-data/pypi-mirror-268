from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdPowerCls:
	"""CdPower commands group definition. 30 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdPower", core, parent)

	@property
	def dpcch(self):
		"""dpcch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpcch'):
			from .Dpcch import DpcchCls
			self._dpcch = DpcchCls(self._core, self._cmd_group)
		return self._dpcch

	@property
	def dpdch(self):
		"""dpdch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpdch'):
			from .Dpdch import DpdchCls
			self._dpdch = DpdchCls(self._core, self._cmd_group)
		return self._dpdch

	@property
	def hsdpcch(self):
		"""hsdpcch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsdpcch'):
			from .Hsdpcch import HsdpcchCls
			self._hsdpcch = HsdpcchCls(self._core, self._cmd_group)
		return self._hsdpcch

	@property
	def edpcch(self):
		"""edpcch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_edpcch'):
			from .Edpcch import EdpcchCls
			self._edpcch = EdpcchCls(self._core, self._cmd_group)
		return self._edpcch

	@property
	def edpdch(self):
		"""edpdch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_edpdch'):
			from .Edpdch import EdpdchCls
			self._edpdch = EdpdchCls(self._core, self._cmd_group)
		return self._edpdch

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDevCls
			self._standardDev = StandardDevCls(self._core, self._cmd_group)
		return self._standardDev

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	def clone(self) -> 'CdPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CdPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
