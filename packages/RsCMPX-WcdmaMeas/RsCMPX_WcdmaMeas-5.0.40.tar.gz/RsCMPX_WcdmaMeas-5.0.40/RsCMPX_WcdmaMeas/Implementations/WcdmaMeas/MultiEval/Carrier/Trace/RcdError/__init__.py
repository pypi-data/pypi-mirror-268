from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RcdErrorCls:
	"""RcdError commands group definition. 50 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcdError", core, parent)

	@property
	def sf(self):
		"""sf commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sf'):
			from .Sf import SfCls
			self._sf = SfCls(self._core, self._cmd_group)
		return self._sf

	@property
	def dpcch(self):
		"""dpcch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpcch'):
			from .Dpcch import DpcchCls
			self._dpcch = DpcchCls(self._core, self._cmd_group)
		return self._dpcch

	@property
	def dpdch(self):
		"""dpdch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpdch'):
			from .Dpdch import DpdchCls
			self._dpdch = DpdchCls(self._core, self._cmd_group)
		return self._dpdch

	@property
	def hsdpcch(self):
		"""hsdpcch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsdpcch'):
			from .Hsdpcch import HsdpcchCls
			self._hsdpcch = HsdpcchCls(self._core, self._cmd_group)
		return self._hsdpcch

	@property
	def edpcch(self):
		"""edpcch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_edpcch'):
			from .Edpcch import EdpcchCls
			self._edpcch = EdpcchCls(self._core, self._cmd_group)
		return self._edpcch

	@property
	def edpdch(self):
		"""edpdch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_edpdch'):
			from .Edpdch import EdpdchCls
			self._edpdch = EdpdchCls(self._core, self._cmd_group)
		return self._edpdch

	def clone(self) -> 'RcdErrorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RcdErrorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
