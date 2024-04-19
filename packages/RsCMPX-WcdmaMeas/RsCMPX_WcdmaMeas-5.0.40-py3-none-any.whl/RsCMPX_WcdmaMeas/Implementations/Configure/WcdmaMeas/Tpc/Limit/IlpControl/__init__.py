from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IlpControlCls:
	"""IlpControl commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ilpControl", core, parent)

	@property
	def maxPower(self):
		"""maxPower commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_maxPower'):
			from .MaxPower import MaxPowerCls
			self._maxPower = MaxPowerCls(self._core, self._cmd_group)
		return self._maxPower

	@property
	def minPower(self):
		"""minPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minPower'):
			from .MinPower import MinPowerCls
			self._minPower = MinPowerCls(self._core, self._cmd_group)
		return self._minPower

	@property
	def pstep(self):
		"""pstep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pstep'):
			from .Pstep import PstepCls
			self._pstep = PstepCls(self._core, self._cmd_group)
		return self._pstep

	@property
	def epStep(self):
		"""epStep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_epStep'):
			from .EpStep import EpStepCls
			self._epStep = EpStepCls(self._core, self._cmd_group)
		return self._epStep

	@property
	def psGroup(self):
		"""psGroup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psGroup'):
			from .PsGroup import PsGroupCls
			self._psGroup = PsGroupCls(self._core, self._cmd_group)
		return self._psGroup

	def clone(self) -> 'IlpControlCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IlpControlCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
