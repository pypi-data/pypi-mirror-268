from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CarrierCls:
	"""Carrier commands group definition. 7 total commands, 5 Subgroups, 1 group commands
	Repeated Capability: Carrier, default value after init: Carrier.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrier_get', 'repcap_carrier_set', repcap.Carrier.Nr1)

	def repcap_carrier_set(self, carrier: repcap.Carrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Carrier.Default
		Default value after init: Carrier.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrier)

	def repcap_carrier_get(self) -> repcap.Carrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def edpdch(self):
		"""edpdch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edpdch'):
			from .Edpdch import EdpdchCls
			self._edpdch = EdpdchCls(self._core, self._cmd_group)
		return self._edpdch

	@property
	def edpcch(self):
		"""edpcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edpcch'):
			from .Edpcch import EdpcchCls
			self._edpcch = EdpcchCls(self._core, self._cmd_group)
		return self._edpcch

	@property
	def hsdpcch(self):
		"""hsdpcch commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_hsdpcch'):
			from .Hsdpcch import HsdpcchCls
			self._hsdpcch = HsdpcchCls(self._core, self._cmd_group)
		return self._hsdpcch

	@property
	def dpdch(self):
		"""dpdch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpdch'):
			from .Dpdch import DpdchCls
			self._dpdch = DpdchCls(self._core, self._cmd_group)
		return self._dpdch

	@property
	def dpcch(self):
		"""dpcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpcch'):
			from .Dpcch import DpcchCls
			self._dpcch = DpcchCls(self._core, self._cmd_group)
		return self._dpcch

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Enable_Dpcch: bool: No parameter help available
			- Beta_Dpcch: int: No parameter help available
			- Sf_Dpcch: int: No parameter help available
			- Enable_Dpdch: bool: No parameter help available
			- Beta_Dpdch: int: No parameter help available
			- Sf_Dpdch: int: No parameter help available
			- Enable_Hs_Dpcch: bool: No parameter help available
			- Beta_Hsdpcch: int: No parameter help available
			- Sf_Hs_Dpcch: int: No parameter help available
			- Enable_Edpcch: bool: No parameter help available
			- Beta_Edpcch: int: No parameter help available
			- Sfe_Dpcch: int: No parameter help available
			- Enable_Edpdch_1: bool: No parameter help available
			- Beta_Edpdch_1: int: No parameter help available
			- Sfe_Dpd_Ch_1: int: No parameter help available
			- Enable_Edpdch_2: bool: No parameter help available
			- Beta_Edpdch_2: int: No parameter help available
			- Sfe_Dpd_Ch_2: int: No parameter help available
			- Enable_Edpdch_3: bool: No parameter help available
			- Beta_Edpdch_3: int: No parameter help available
			- Sfe_Dpd_Ch_3: int: No parameter help available
			- Enable_Edpdch_4: bool: No parameter help available
			- Beta_Edpdch_4: int: No parameter help available
			- Sfe_Dpd_Ch_4: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Dpcch'),
			ArgStruct.scalar_int('Beta_Dpcch'),
			ArgStruct.scalar_int('Sf_Dpcch'),
			ArgStruct.scalar_bool_optional('Enable_Dpdch'),
			ArgStruct.scalar_int_optional('Beta_Dpdch'),
			ArgStruct.scalar_int_optional('Sf_Dpdch'),
			ArgStruct.scalar_bool_optional('Enable_Hs_Dpcch'),
			ArgStruct.scalar_int_optional('Beta_Hsdpcch'),
			ArgStruct.scalar_int_optional('Sf_Hs_Dpcch'),
			ArgStruct.scalar_bool_optional('Enable_Edpcch'),
			ArgStruct.scalar_int_optional('Beta_Edpcch'),
			ArgStruct.scalar_int_optional('Sfe_Dpcch'),
			ArgStruct.scalar_bool_optional('Enable_Edpdch_1'),
			ArgStruct.scalar_int_optional('Beta_Edpdch_1'),
			ArgStruct.scalar_int_optional('Sfe_Dpd_Ch_1'),
			ArgStruct.scalar_bool_optional('Enable_Edpdch_2'),
			ArgStruct.scalar_int_optional('Beta_Edpdch_2'),
			ArgStruct.scalar_int_optional('Sfe_Dpd_Ch_2'),
			ArgStruct.scalar_bool_optional('Enable_Edpdch_3'),
			ArgStruct.scalar_int_optional('Beta_Edpdch_3'),
			ArgStruct.scalar_int_optional('Sfe_Dpd_Ch_3'),
			ArgStruct.scalar_bool_optional('Enable_Edpdch_4'),
			ArgStruct.scalar_int_optional('Beta_Edpdch_4'),
			ArgStruct.scalar_int_optional('Sfe_Dpd_Ch_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Dpcch: bool = None
			self.Beta_Dpcch: int = None
			self.Sf_Dpcch: int = None
			self.Enable_Dpdch: bool = None
			self.Beta_Dpdch: int = None
			self.Sf_Dpdch: int = None
			self.Enable_Hs_Dpcch: bool = None
			self.Beta_Hsdpcch: int = None
			self.Sf_Hs_Dpcch: int = None
			self.Enable_Edpcch: bool = None
			self.Beta_Edpcch: int = None
			self.Sfe_Dpcch: int = None
			self.Enable_Edpdch_1: bool = None
			self.Beta_Edpdch_1: int = None
			self.Sfe_Dpd_Ch_1: int = None
			self.Enable_Edpdch_2: bool = None
			self.Beta_Edpdch_2: int = None
			self.Sfe_Dpd_Ch_2: int = None
			self.Enable_Edpdch_3: bool = None
			self.Beta_Edpdch_3: int = None
			self.Sfe_Dpd_Ch_3: int = None
			self.Enable_Edpdch_4: bool = None
			self.Beta_Edpdch_4: int = None
			self.Sfe_Dpd_Ch_4: int = None

	def set(self, structure: SetStruct, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier> \n
		Snippet with structure: \n
		structure = driver.configure.wcdmaMeas.multiEval.limit.rcdError.eecdp.carrier.SetStruct() \n
		structure.Enable_Dpcch: bool = False \n
		structure.Beta_Dpcch: int = 1 \n
		structure.Sf_Dpcch: int = 1 \n
		structure.Enable_Dpdch: bool = False \n
		structure.Beta_Dpdch: int = 1 \n
		structure.Sf_Dpdch: int = 1 \n
		structure.Enable_Hs_Dpcch: bool = False \n
		structure.Beta_Hsdpcch: int = 1 \n
		structure.Sf_Hs_Dpcch: int = 1 \n
		structure.Enable_Edpcch: bool = False \n
		structure.Beta_Edpcch: int = 1 \n
		structure.Sfe_Dpcch: int = 1 \n
		structure.Enable_Edpdch_1: bool = False \n
		structure.Beta_Edpdch_1: int = 1 \n
		structure.Sfe_Dpd_Ch_1: int = 1 \n
		structure.Enable_Edpdch_2: bool = False \n
		structure.Beta_Edpdch_2: int = 1 \n
		structure.Sfe_Dpd_Ch_2: int = 1 \n
		structure.Enable_Edpdch_3: bool = False \n
		structure.Beta_Edpdch_3: int = 1 \n
		structure.Sfe_Dpd_Ch_3: int = 1 \n
		structure.Enable_Edpdch_4: bool = False \n
		structure.Beta_Edpdch_4: int = 1 \n
		structure.Sfe_Dpd_Ch_4: int = 1 \n
		driver.configure.wcdmaMeas.multiEval.limit.rcdError.eecdp.carrier.set(structure, carrier = repcap.Carrier.Default) \n
			INTRO_CMD_HELP: Specifies the channel configuration in the uplink signal. This command has the same effect as the sum of the following commands: \n
			- method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.RcdError.Eecdp.Carrier.Dpcch.set
			- method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.RcdError.Eecdp.Carrier.Dpdch.set
			- method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.RcdError.Eecdp.Carrier.Hsdpcch.set
			- method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.RcdError.Eecdp.Carrier.Edpcch.set
			- CONFigure:WCDMa:MEAS<i>:MEValuation:LIMit:RCDerror:EECDp:CARRier<c>:EDPDch<no>
		Please refer to these commands for additional information (ranges and *RST values) . The parameter array described below
		is repeated for each channel (eight times) in the following order: DPCCH, DPDCH, HS-DPCCH, E-DPCCH, E-DPDCH 1, ...
		, E-DPDCH 4. Thus a setting requires 3*8 values and a query returns 5*8 values. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable_Dpcch: bool: No parameter help available
			- Beta_Dpcch: int: No parameter help available
			- Sf_Dpcch: int: No parameter help available
			- Nom_Cdp_Dpcch: float: No parameter help available
			- Eff_Cdp_Dpcch: float: No parameter help available
			- Enable_Dpdch: bool: No parameter help available
			- Beta_Dpdch: int: No parameter help available
			- Sf_Dpdch: int: No parameter help available
			- Nom_Cdp_Dpdch: float: No parameter help available
			- Eff_Cdp_Dpdch: float: No parameter help available
			- Enable_Hs_Dpcch: bool: No parameter help available
			- Beta_Hsdpcch: int: No parameter help available
			- Sf_Hs_Dpcch: int: No parameter help available
			- Nom_Hs_Dpcch: float: No parameter help available
			- Eff_Hs_Dpcch: float: No parameter help available
			- Enable_Edpcch: bool: No parameter help available
			- Beta_Edpcch: int: No parameter help available
			- Sfe_Dpcch: int: No parameter help available
			- Nom_Edpcch: float: No parameter help available
			- Effe_Dpcch: float: No parameter help available
			- Enable_Edpdch_1: bool: No parameter help available
			- Beta_Edpdch_1: int: No parameter help available
			- Sfe_Dpd_Ch_1: int: No parameter help available
			- Nom_Edpdch_1: float: No parameter help available
			- Eff_Edpdch_1: float: No parameter help available
			- Enable_Edpdch_2: bool: No parameter help available
			- Beta_Edpdch_2: int: No parameter help available
			- Sfe_Dpd_Ch_2: int: No parameter help available
			- Nom_Edpdch_2: float: No parameter help available
			- Eff_Edpdch_2: float: No parameter help available
			- Enable_Edpdch_3: bool: No parameter help available
			- Beta_Edpdch_3: int: No parameter help available
			- Sfe_Dpd_Ch_3: int: No parameter help available
			- Nom_Edpdch_3: float: No parameter help available
			- Eff_Edpdch_3: float: No parameter help available
			- Enable_Edpdch_4: bool: No parameter help available
			- Beta_Edpdch_4: int: No parameter help available
			- Sfe_Dpd_Ch_4: int: No parameter help available
			- Nom_Edpdch_4: float: No parameter help available
			- Eff_Edpdch_4: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Dpcch'),
			ArgStruct.scalar_int('Beta_Dpcch'),
			ArgStruct.scalar_int('Sf_Dpcch'),
			ArgStruct.scalar_float('Nom_Cdp_Dpcch'),
			ArgStruct.scalar_float('Eff_Cdp_Dpcch'),
			ArgStruct.scalar_bool('Enable_Dpdch'),
			ArgStruct.scalar_int('Beta_Dpdch'),
			ArgStruct.scalar_int('Sf_Dpdch'),
			ArgStruct.scalar_float('Nom_Cdp_Dpdch'),
			ArgStruct.scalar_float('Eff_Cdp_Dpdch'),
			ArgStruct.scalar_bool('Enable_Hs_Dpcch'),
			ArgStruct.scalar_int('Beta_Hsdpcch'),
			ArgStruct.scalar_int('Sf_Hs_Dpcch'),
			ArgStruct.scalar_float('Nom_Hs_Dpcch'),
			ArgStruct.scalar_float('Eff_Hs_Dpcch'),
			ArgStruct.scalar_bool('Enable_Edpcch'),
			ArgStruct.scalar_int('Beta_Edpcch'),
			ArgStruct.scalar_int('Sfe_Dpcch'),
			ArgStruct.scalar_float('Nom_Edpcch'),
			ArgStruct.scalar_float('Effe_Dpcch'),
			ArgStruct.scalar_bool('Enable_Edpdch_1'),
			ArgStruct.scalar_int('Beta_Edpdch_1'),
			ArgStruct.scalar_int('Sfe_Dpd_Ch_1'),
			ArgStruct.scalar_float('Nom_Edpdch_1'),
			ArgStruct.scalar_float('Eff_Edpdch_1'),
			ArgStruct.scalar_bool('Enable_Edpdch_2'),
			ArgStruct.scalar_int('Beta_Edpdch_2'),
			ArgStruct.scalar_int('Sfe_Dpd_Ch_2'),
			ArgStruct.scalar_float('Nom_Edpdch_2'),
			ArgStruct.scalar_float('Eff_Edpdch_2'),
			ArgStruct.scalar_bool('Enable_Edpdch_3'),
			ArgStruct.scalar_int('Beta_Edpdch_3'),
			ArgStruct.scalar_int('Sfe_Dpd_Ch_3'),
			ArgStruct.scalar_float('Nom_Edpdch_3'),
			ArgStruct.scalar_float('Eff_Edpdch_3'),
			ArgStruct.scalar_bool('Enable_Edpdch_4'),
			ArgStruct.scalar_int('Beta_Edpdch_4'),
			ArgStruct.scalar_int('Sfe_Dpd_Ch_4'),
			ArgStruct.scalar_float('Nom_Edpdch_4'),
			ArgStruct.scalar_float('Eff_Edpdch_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Dpcch: bool = None
			self.Beta_Dpcch: int = None
			self.Sf_Dpcch: int = None
			self.Nom_Cdp_Dpcch: float = None
			self.Eff_Cdp_Dpcch: float = None
			self.Enable_Dpdch: bool = None
			self.Beta_Dpdch: int = None
			self.Sf_Dpdch: int = None
			self.Nom_Cdp_Dpdch: float = None
			self.Eff_Cdp_Dpdch: float = None
			self.Enable_Hs_Dpcch: bool = None
			self.Beta_Hsdpcch: int = None
			self.Sf_Hs_Dpcch: int = None
			self.Nom_Hs_Dpcch: float = None
			self.Eff_Hs_Dpcch: float = None
			self.Enable_Edpcch: bool = None
			self.Beta_Edpcch: int = None
			self.Sfe_Dpcch: int = None
			self.Nom_Edpcch: float = None
			self.Effe_Dpcch: float = None
			self.Enable_Edpdch_1: bool = None
			self.Beta_Edpdch_1: int = None
			self.Sfe_Dpd_Ch_1: int = None
			self.Nom_Edpdch_1: float = None
			self.Eff_Edpdch_1: float = None
			self.Enable_Edpdch_2: bool = None
			self.Beta_Edpdch_2: int = None
			self.Sfe_Dpd_Ch_2: int = None
			self.Nom_Edpdch_2: float = None
			self.Eff_Edpdch_2: float = None
			self.Enable_Edpdch_3: bool = None
			self.Beta_Edpdch_3: int = None
			self.Sfe_Dpd_Ch_3: int = None
			self.Nom_Edpdch_3: float = None
			self.Eff_Edpdch_3: float = None
			self.Enable_Edpdch_4: bool = None
			self.Beta_Edpdch_4: int = None
			self.Sfe_Dpd_Ch_4: int = None
			self.Nom_Edpdch_4: float = None
			self.Eff_Edpdch_4: float = None

	def get(self, carrier=repcap.Carrier.Default) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier> \n
		Snippet: value: GetStruct = driver.configure.wcdmaMeas.multiEval.limit.rcdError.eecdp.carrier.get(carrier = repcap.Carrier.Default) \n
			INTRO_CMD_HELP: Specifies the channel configuration in the uplink signal. This command has the same effect as the sum of the following commands: \n
			- method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.RcdError.Eecdp.Carrier.Dpcch.set
			- method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.RcdError.Eecdp.Carrier.Dpdch.set
			- method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.RcdError.Eecdp.Carrier.Hsdpcch.set
			- method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.RcdError.Eecdp.Carrier.Edpcch.set
			- CONFigure:WCDMa:MEAS<i>:MEValuation:LIMit:RCDerror:EECDp:CARRier<c>:EDPDch<no>
		Please refer to these commands for additional information (ranges and *RST values) . The parameter array described below
		is repeated for each channel (eight times) in the following order: DPCCH, DPDCH, HS-DPCCH, E-DPCCH, E-DPDCH 1, ...
		, E-DPDCH 4. Thus a setting requires 3*8 values and a query returns 5*8 values. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'CarrierCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CarrierCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
