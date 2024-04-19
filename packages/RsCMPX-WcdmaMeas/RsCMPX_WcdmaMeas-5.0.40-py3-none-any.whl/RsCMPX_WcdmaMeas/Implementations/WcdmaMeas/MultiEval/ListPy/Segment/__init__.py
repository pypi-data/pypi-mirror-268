from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SegmentCls:
	"""Segment commands group definition. 20 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: Segment, default value after init: Segment.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segment", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_segment_get', 'repcap_segment_set', repcap.Segment.Nr1)

	def repcap_segment_set(self, segment: repcap.Segment) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Segment.Default
		Default value after init: Segment.Nr1"""
		self._cmd_group.set_repcap_enum_value(segment)

	def repcap_segment_get(self) -> repcap.Segment:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def uePower(self):
		"""uePower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uePower'):
			from .UePower import UePowerCls
			self._uePower = UePowerCls(self._core, self._cmd_group)
		return self._uePower

	@property
	def phd(self):
		"""phd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phd'):
			from .Phd import PhdCls
			self._phd = PhdCls(self._core, self._cmd_group)
		return self._phd

	@property
	def pcde(self):
		"""pcde commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcde'):
			from .Pcde import PcdeCls
			self._pcde = PcdeCls(self._core, self._cmd_group)
		return self._pcde

	@property
	def cdPower(self):
		"""cdPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdPower'):
			from .CdPower import CdPowerCls
			self._cdPower = CdPowerCls(self._core, self._cmd_group)
		return self._cdPower

	@property
	def spectrum(self):
		"""spectrum commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def modulation(self):
		"""modulation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def cdError(self):
		"""cdError commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdError'):
			from .CdError import CdErrorCls
			self._cdError = CdErrorCls(self._core, self._cmd_group)
		return self._cdError

	def clone(self) -> 'SegmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SegmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
