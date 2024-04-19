from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 23 total commands, 9 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def rcdError(self):
		"""rcdError commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcdError'):
			from .RcdError import RcdErrorCls
			self._rcdError = RcdErrorCls(self._core, self._cmd_group)
		return self._rcdError

	@property
	def pcontrol(self):
		"""pcontrol commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcontrol'):
			from .Pcontrol import PcontrolCls
			self._pcontrol = PcontrolCls(self._core, self._cmd_group)
		return self._pcontrol

	@property
	def phsDpcch(self):
		"""phsDpcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phsDpcch'):
			from .PhsDpcch import PhsDpcchCls
			self._phsDpcch = PhsDpcchCls(self._core, self._cmd_group)
		return self._phsDpcch

	@property
	def phd(self):
		"""phd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phd'):
			from .Phd import PhdCls
			self._phd = PhdCls(self._core, self._cmd_group)
		return self._phd

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .EvMagnitude import EvMagnitudeCls
			self._evMagnitude = EvMagnitudeCls(self._core, self._cmd_group)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import MerrorCls
			self._merror = MerrorCls(self._core, self._cmd_group)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import PerrorCls
			self._perror = PerrorCls(self._core, self._cmd_group)
		return self._perror

	@property
	def emask(self):
		"""emask commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_emask'):
			from .Emask import EmaskCls
			self._emask = EmaskCls(self._core, self._cmd_group)
		return self._emask

	@property
	def aclr(self):
		"""aclr commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_aclr'):
			from .Aclr import AclrCls
			self._aclr = AclrCls(self._core, self._cmd_group)
		return self._aclr

	def get_iq_offset(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:IQOFfset \n
		Snippet: value: float or bool = driver.configure.wcdmaMeas.multiEval.limit.get_iq_offset() \n
		Defines an upper limit for the I/Q origin offset. \n
			:return: iq_offset: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:IQOFfset?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_offset(self, iq_offset: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:IQOFfset \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.set_iq_offset(iq_offset = 1.0) \n
		Defines an upper limit for the I/Q origin offset. \n
			:param iq_offset: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_offset)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:IQOFfset {param}')

	def get_iq_imbalance(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:IQIMbalance \n
		Snippet: value: float or bool = driver.configure.wcdmaMeas.multiEval.limit.get_iq_imbalance() \n
		Defines an upper limit for the I/Q imbalance. \n
			:return: iq_imbalance: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_imbalance(self, iq_imbalance: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:IQIMbalance \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.set_iq_imbalance(iq_imbalance = 1.0) \n
		Defines an upper limit for the I/Q imbalance. \n
			:param iq_imbalance: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_imbalance)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:CFERror \n
		Snippet: value: float or bool = driver.configure.wcdmaMeas.multiEval.limit.get_cf_error() \n
		Defines an upper limit for the carrier frequency error. \n
			:return: frequency_error: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, frequency_error: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:CFERror \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.set_cf_error(frequency_error = 1.0) \n
		Defines an upper limit for the carrier frequency error. \n
			:param frequency_error: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(frequency_error)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:CFERror {param}')

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
