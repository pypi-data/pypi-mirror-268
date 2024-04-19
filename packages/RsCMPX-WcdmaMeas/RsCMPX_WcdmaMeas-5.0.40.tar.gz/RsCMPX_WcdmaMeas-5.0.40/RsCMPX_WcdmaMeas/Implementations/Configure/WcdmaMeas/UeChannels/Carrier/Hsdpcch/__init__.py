from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HsdpcchCls:
	"""Hsdpcch commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hsdpcch", core, parent)

	@property
	def config(self):
		"""config commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_config'):
			from .Config import ConfigCls
			self._config = ConfigCls(self._core, self._cmd_group)
		return self._config

	def set(self, enable: bool, beta_factor: int, spreading_factor: int, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:HSDPcch \n
		Snippet: driver.configure.wcdmaMeas.ueChannels.carrier.hsdpcch.set(enable = False, beta_factor = 1, spreading_factor = 1, carrier = repcap.Carrier.Default) \n
		Specifies the presence of an HS-DPCCH in the uplink signal and the beta factor and spreading factor of the channel. For
		the HS-DPCCH three sets of beta factor and spreading factor can be configured, depending on whether it transports an ACK,
		NACK or CQI. This command configures/returns the values related to the currently active set. For selection of the active
		set, see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.UeChannels.Carrier.Hsdpcch.Config.set. \n
			:param enable: Channel disabled | enabled
			:param beta_factor: No help available
			:param spreading_factor: No help available
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('beta_factor', beta_factor, DataType.Integer), ArgSingle('spreading_factor', spreading_factor, DataType.Integer))
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:HSDPcch {param}'.rstrip())

	# noinspection PyTypeChecker
	class HsdpcchStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Channel disabled | enabled
			- Beta_Factor: int: No parameter help available
			- Spreading_Factor: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Beta_Factor'),
			ArgStruct.scalar_int('Spreading_Factor')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Beta_Factor: int = None
			self.Spreading_Factor: int = None

	def get(self, carrier=repcap.Carrier.Default) -> HsdpcchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:HSDPcch \n
		Snippet: value: HsdpcchStruct = driver.configure.wcdmaMeas.ueChannels.carrier.hsdpcch.get(carrier = repcap.Carrier.Default) \n
		Specifies the presence of an HS-DPCCH in the uplink signal and the beta factor and spreading factor of the channel. For
		the HS-DPCCH three sets of beta factor and spreading factor can be configured, depending on whether it transports an ACK,
		NACK or CQI. This command configures/returns the values related to the currently active set. For selection of the active
		set, see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.UeChannels.Carrier.Hsdpcch.Config.set. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for HsdpcchStruct structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:HSDPcch?', self.__class__.HsdpcchStruct())

	def clone(self) -> 'HsdpcchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HsdpcchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
