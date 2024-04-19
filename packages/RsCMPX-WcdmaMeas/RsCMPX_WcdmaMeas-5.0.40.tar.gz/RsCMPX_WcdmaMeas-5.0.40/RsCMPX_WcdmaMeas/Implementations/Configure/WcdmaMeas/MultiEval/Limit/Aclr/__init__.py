from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AclrCls:
	"""Aclr commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aclr", core, parent)

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import RelativeCls
			self._relative = RelativeCls(self._core, self._cmd_group)
		return self._relative

	def get_absolute(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:ACLR:ABSolute \n
		Snippet: value: float or bool = driver.configure.wcdmaMeas.multiEval.limit.aclr.get_absolute() \n
		It defines an absolute upper limit for the ACLR. If the absolute upper limit is exceeded, relative limits are evaluated
		(method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.Aclr.Relative.set) . \n
			:return: limit_3_m_84: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:ACLR:ABSolute?')
		return Conversions.str_to_float_or_bool(response)

	def set_absolute(self, limit_3_m_84: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:ACLR:ABSolute \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.aclr.set_absolute(limit_3_m_84 = 1.0) \n
		It defines an absolute upper limit for the ACLR. If the absolute upper limit is exceeded, relative limits are evaluated
		(method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.Aclr.Relative.set) . \n
			:param limit_3_m_84: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit_3_m_84)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:ACLR:ABSolute {param}')

	def clone(self) -> 'AclrCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AclrCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
