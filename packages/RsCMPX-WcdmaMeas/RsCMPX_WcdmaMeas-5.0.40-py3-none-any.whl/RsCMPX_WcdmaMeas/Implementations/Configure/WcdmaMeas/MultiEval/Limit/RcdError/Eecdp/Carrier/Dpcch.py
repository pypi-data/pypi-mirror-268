from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpcchCls:
	"""Dpcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpcch", core, parent)

	def set(self, enable: bool, beta_factor: int, spreading_factor: int, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier>:DPCCh \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.rcdError.eecdp.carrier.dpcch.set(enable = False, beta_factor = 1, spreading_factor = 1, carrier = repcap.Carrier.Default) \n
		Specifies the presence of a DPCCH in the uplink signal and the beta factor and spreading factor of the channel. A query
		also returns the nominal CDP and effective CDP resulting from these settings. \n
			:param enable: Channel disabled | enabled
			:param beta_factor: No help available
			:param spreading_factor: No help available
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('beta_factor', beta_factor, DataType.Integer), ArgSingle('spreading_factor', spreading_factor, DataType.Integer))
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}:DPCCh {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Channel disabled | enabled
			- Beta_Factor: int: No parameter help available
			- Spreading_Factor: int: No parameter help available
			- Nominal_Cdp: float: No parameter help available
			- Effective_Cdp: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Beta_Factor'),
			ArgStruct.scalar_int('Spreading_Factor'),
			ArgStruct.scalar_float('Nominal_Cdp'),
			ArgStruct.scalar_float('Effective_Cdp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Beta_Factor: int = None
			self.Spreading_Factor: int = None
			self.Nominal_Cdp: float = None
			self.Effective_Cdp: float = None

	def get(self, carrier=repcap.Carrier.Default) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier>:DPCCh \n
		Snippet: value: GetStruct = driver.configure.wcdmaMeas.multiEval.limit.rcdError.eecdp.carrier.dpcch.get(carrier = repcap.Carrier.Default) \n
		Specifies the presence of a DPCCH in the uplink signal and the beta factor and spreading factor of the channel. A query
		also returns the nominal CDP and effective CDP resulting from these settings. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}:DPCCh?', self.__class__.GetStruct())
