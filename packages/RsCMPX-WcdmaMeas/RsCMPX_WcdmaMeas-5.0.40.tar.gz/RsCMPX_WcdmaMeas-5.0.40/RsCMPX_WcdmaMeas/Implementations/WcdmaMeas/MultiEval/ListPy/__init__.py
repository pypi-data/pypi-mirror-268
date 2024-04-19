from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 181 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def sreliability(self):
		"""sreliability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sreliability'):
			from .Sreliability import SreliabilityCls
			self._sreliability = SreliabilityCls(self._core, self._cmd_group)
		return self._sreliability

	@property
	def uePower(self):
		"""uePower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uePower'):
			from .UePower import UePowerCls
			self._uePower = UePowerCls(self._core, self._cmd_group)
		return self._uePower

	@property
	def segment(self):
		"""segment commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import SegmentCls
			self._segment = SegmentCls(self._core, self._cmd_group)
		return self._segment

	@property
	def phd(self):
		"""phd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phd'):
			from .Phd import PhdCls
			self._phd = PhdCls(self._core, self._cmd_group)
		return self._phd

	@property
	def pcde(self):
		"""pcde commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcde'):
			from .Pcde import PcdeCls
			self._pcde = PcdeCls(self._core, self._cmd_group)
		return self._pcde

	@property
	def cdPower(self):
		"""cdPower commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdPower'):
			from .CdPower import CdPowerCls
			self._cdPower = CdPowerCls(self._core, self._cmd_group)
		return self._cdPower

	@property
	def spectrum(self):
		"""spectrum commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def modulation(self):
		"""modulation commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def cdError(self):
		"""cdError commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdError'):
			from .CdError import CdErrorCls
			self._cdError = CdErrorCls(self._core, self._cmd_group)
		return self._cdError

	def clone(self) -> 'ListPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
