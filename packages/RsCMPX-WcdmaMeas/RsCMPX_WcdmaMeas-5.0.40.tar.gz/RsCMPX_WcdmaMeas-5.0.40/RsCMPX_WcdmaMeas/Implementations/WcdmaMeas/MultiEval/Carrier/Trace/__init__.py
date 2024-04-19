from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TraceCls:
	"""Trace commands group definition. 215 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	@property
	def uePower(self):
		"""uePower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_uePower'):
			from .UePower import UePowerCls
			self._uePower = UePowerCls(self._core, self._cmd_group)
		return self._uePower

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .EvMagnitude import EvMagnitudeCls
			self._evMagnitude = EvMagnitudeCls(self._core, self._cmd_group)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import MerrorCls
			self._merror = MerrorCls(self._core, self._cmd_group)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import PerrorCls
			self._perror = PerrorCls(self._core, self._cmd_group)
		return self._perror

	@property
	def cdPower(self):
		"""cdPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdPower'):
			from .CdPower import CdPowerCls
			self._cdPower = CdPowerCls(self._core, self._cmd_group)
		return self._cdPower

	@property
	def cdError(self):
		"""cdError commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdError'):
			from .CdError import CdErrorCls
			self._cdError = CdErrorCls(self._core, self._cmd_group)
		return self._cdError

	@property
	def freqError(self):
		"""freqError commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	@property
	def psteps(self):
		"""psteps commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_psteps'):
			from .Psteps import PstepsCls
			self._psteps = PstepsCls(self._core, self._cmd_group)
		return self._psteps

	@property
	def rcdError(self):
		"""rcdError commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_rcdError'):
			from .RcdError import RcdErrorCls
			self._rcdError = RcdErrorCls(self._core, self._cmd_group)
		return self._rcdError

	def clone(self) -> 'TraceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TraceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
