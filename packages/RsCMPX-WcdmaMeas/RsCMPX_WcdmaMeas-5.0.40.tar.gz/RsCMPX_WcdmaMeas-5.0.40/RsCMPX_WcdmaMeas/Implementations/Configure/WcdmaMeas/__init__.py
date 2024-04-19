from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WcdmaMeasCls:
	"""WcdmaMeas commands group definition. 164 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wcdmaMeas", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	@property
	def cell(self):
		"""cell commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import CellCls
			self._cell = CellCls(self._core, self._cmd_group)
		return self._cell

	@property
	def ueSignal(self):
		"""ueSignal commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_ueSignal'):
			from .UeSignal import UeSignalCls
			self._ueSignal = UeSignalCls(self._core, self._cmd_group)
		return self._ueSignal

	@property
	def ueChannels(self):
		"""ueChannels commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueChannels'):
			from .UeChannels import UeChannelsCls
			self._ueChannels = UeChannelsCls(self._core, self._cmd_group)
		return self._ueChannels

	@property
	def rfSettings(self):
		"""rfSettings commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def multiEval(self):
		"""multiEval commands group. 11 Sub-classes, 7 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def tpc(self):
		"""tpc commands group. 7 Sub-classes, 5 commands."""
		if not hasattr(self, '_tpc'):
			from .Tpc import TpcCls
			self._tpc = TpcCls(self._core, self._cmd_group)
		return self._tpc

	@property
	def prach(self):
		"""prach commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	@property
	def ooSync(self):
		"""ooSync commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ooSync'):
			from .OoSync import OoSyncCls
			self._ooSync = OoSyncCls(self._core, self._cmd_group)
		return self._ooSync

	@property
	def olpControl(self):
		"""olpControl commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_olpControl'):
			from .OlpControl import OlpControlCls
			self._olpControl = OlpControlCls(self._core, self._cmd_group)
		return self._olpControl

	def clone(self) -> 'WcdmaMeasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = WcdmaMeasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
