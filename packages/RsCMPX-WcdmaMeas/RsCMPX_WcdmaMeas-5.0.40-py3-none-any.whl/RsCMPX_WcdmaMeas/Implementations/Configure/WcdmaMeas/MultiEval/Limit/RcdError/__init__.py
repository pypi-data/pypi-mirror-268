from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RcdErrorCls:
	"""RcdError commands group definition. 8 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcdError", core, parent)

	@property
	def eecdp(self):
		"""eecdp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eecdp'):
			from .Eecdp import EecdpCls
			self._eecdp = EecdpCls(self._core, self._cmd_group)
		return self._eecdp

	# noinspection PyTypeChecker
	class EcdpStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Threshold_Bpsk_1: float: Lower ECDP threshold for BPSK requirement 1
			- Threshold_Bpsk_2: float: Lower ECDP threshold for BPSK requirement 2
			- Limit_Bpsk_1: float: RCDE limit for BPSK requirement 1
			- Limit_Bpks_2: float: RCDE limit for BPSK requirement 2 (limit = this value minus ECDP)
			- Threshold_4_Pam_1: float: Lower ECDP threshold for 4PAM requirement 1
			- Threshold_4_Pam_2: float: Lower ECDP threshold for 4PAM requirement 2
			- Limit_4_Pam_1: float: RCDE limit for 4PAM requirement 1
			- Limit_4_Pam_2: float: RCDE limit for 4PAM requirement 2 (limit = this value minus ECDP)"""
		__meta_args_list = [
			ArgStruct.scalar_float('Threshold_Bpsk_1'),
			ArgStruct.scalar_float('Threshold_Bpsk_2'),
			ArgStruct.scalar_float('Limit_Bpsk_1'),
			ArgStruct.scalar_float('Limit_Bpks_2'),
			ArgStruct.scalar_float('Threshold_4_Pam_1'),
			ArgStruct.scalar_float('Threshold_4_Pam_2'),
			ArgStruct.scalar_float('Limit_4_Pam_1'),
			ArgStruct.scalar_float('Limit_4_Pam_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Threshold_Bpsk_1: float = None
			self.Threshold_Bpsk_2: float = None
			self.Limit_Bpsk_1: float = None
			self.Limit_Bpks_2: float = None
			self.Threshold_4_Pam_1: float = None
			self.Threshold_4_Pam_2: float = None
			self.Limit_4_Pam_1: float = None
			self.Limit_4_Pam_2: float = None

	def get_ecdp(self) -> EcdpStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:ECDP \n
		Snippet: value: EcdpStruct = driver.configure.wcdmaMeas.multiEval.limit.rcdError.get_ecdp() \n
		Defines upper limits for the relative CDE (RCDE) of BPSK and 4PAM modulated channels. For each modulation format, two
		requirements are defined. \n
			:return: structure: for return value, see the help for EcdpStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:ECDP?', self.__class__.EcdpStruct())

	def set_ecdp(self, value: EcdpStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:ECDP \n
		Snippet with structure: \n
		structure = driver.configure.wcdmaMeas.multiEval.limit.rcdError.EcdpStruct() \n
		structure.Threshold_Bpsk_1: float = 1.0 \n
		structure.Threshold_Bpsk_2: float = 1.0 \n
		structure.Limit_Bpsk_1: float = 1.0 \n
		structure.Limit_Bpks_2: float = 1.0 \n
		structure.Threshold_4_Pam_1: float = 1.0 \n
		structure.Threshold_4_Pam_2: float = 1.0 \n
		structure.Limit_4_Pam_1: float = 1.0 \n
		structure.Limit_4_Pam_2: float = 1.0 \n
		driver.configure.wcdmaMeas.multiEval.limit.rcdError.set_ecdp(value = structure) \n
		Defines upper limits for the relative CDE (RCDE) of BPSK and 4PAM modulated channels. For each modulation format, two
		requirements are defined. \n
			:param value: see the help for EcdpStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:ECDP', value)

	def clone(self) -> 'RcdErrorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RcdErrorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
