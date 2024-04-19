from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdpdchCls:
	"""Edpdch commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: EdpdChannel, default value after init: EdpdChannel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edpdch", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_edpdChannel_get', 'repcap_edpdChannel_set', repcap.EdpdChannel.Nr1)

	def repcap_edpdChannel_set(self, edpdChannel: repcap.EdpdChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to EdpdChannel.Default
		Default value after init: EdpdChannel.Nr1"""
		self._cmd_group.set_repcap_enum_value(edpdChannel)

	def repcap_edpdChannel_get(self) -> repcap.EdpdChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, enable: bool, beta_factor: int, spreading_factor: int, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:EDPDch<nr> \n
		Snippet: driver.configure.wcdmaMeas.ueChannels.carrier.edpdch.set(enable = False, beta_factor = 1, spreading_factor = 1, carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Specifies the presence of a selected E-DPDCH (1 to 4) in the uplink signal and the beta factor and spreading factor of
		the channel. \n
			:param enable: Channel disabled | enabled
			:param beta_factor: No help available
			:param spreading_factor: No help available
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('beta_factor', beta_factor, DataType.Integer), ArgSingle('spreading_factor', spreading_factor, DataType.Integer))
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:EDPDch{edpdChannel_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class EdpdchStruct(StructBase):
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

	def get(self, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> EdpdchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:EDPDch<nr> \n
		Snippet: value: EdpdchStruct = driver.configure.wcdmaMeas.ueChannels.carrier.edpdch.get(carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Specifies the presence of a selected E-DPDCH (1 to 4) in the uplink signal and the beta factor and spreading factor of
		the channel. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: structure: for return value, see the help for EdpdchStruct structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:EDPDch{edpdChannel_cmd_val}?', self.__class__.EdpdchStruct())

	def clone(self) -> 'EdpdchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EdpdchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
