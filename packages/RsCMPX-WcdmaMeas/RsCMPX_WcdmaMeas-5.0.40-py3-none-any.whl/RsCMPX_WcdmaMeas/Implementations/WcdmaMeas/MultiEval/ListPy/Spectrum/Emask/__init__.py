from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EmaskCls:
	"""Emask commands group definition. 30 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emask", core, parent)

	@property
	def hda(self):
		"""hda commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_hda'):
			from .Hda import HdaCls
			self._hda = HdaCls(self._core, self._cmd_group)
		return self._hda

	@property
	def had(self):
		"""had commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_had'):
			from .Had import HadCls
			self._had = HadCls(self._core, self._cmd_group)
		return self._had

	@property
	def ab(self):
		"""ab commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ab'):
			from .Ab import AbCls
			self._ab = AbCls(self._core, self._cmd_group)
		return self._ab

	@property
	def bc(self):
		"""bc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bc'):
			from .Bc import BcCls
			self._bc = BcCls(self._core, self._cmd_group)
		return self._bc

	@property
	def cd(self):
		"""cd commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cd'):
			from .Cd import CdCls
			self._cd = CdCls(self._core, self._cmd_group)
		return self._cd

	@property
	def ef(self):
		"""ef commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ef'):
			from .Ef import EfCls
			self._ef = EfCls(self._core, self._cmd_group)
		return self._ef

	@property
	def fe(self):
		"""fe commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fe'):
			from .Fe import FeCls
			self._fe = FeCls(self._core, self._cmd_group)
		return self._fe

	@property
	def dc(self):
		"""dc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dc'):
			from .Dc import DcCls
			self._dc = DcCls(self._core, self._cmd_group)
		return self._dc

	@property
	def cb(self):
		"""cb commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cb'):
			from .Cb import CbCls
			self._cb = CbCls(self._core, self._cmd_group)
		return self._cb

	@property
	def ba(self):
		"""ba commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ba'):
			from .Ba import BaCls
			self._ba = BaCls(self._core, self._cmd_group)
		return self._ba

	def clone(self) -> 'EmaskCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EmaskCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
