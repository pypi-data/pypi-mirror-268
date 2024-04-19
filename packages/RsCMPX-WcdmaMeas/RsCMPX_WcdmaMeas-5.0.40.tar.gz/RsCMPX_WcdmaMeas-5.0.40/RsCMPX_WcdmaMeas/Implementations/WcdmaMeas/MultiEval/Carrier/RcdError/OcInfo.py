from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OcInfoCls:
	"""OcInfo commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ocInfo", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- State: List[enums.State]: State of the channel OFF: Channel off since start of measurement VAR: The channel has been on and off. ON: Channel on since start of measurement
			- Spreading_Factor: List[enums.SpreadingFactorB]: Spreading factor of the channel 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256: constant spreading factor V2 | V4 | V8 | V16 | V32 | V64 | V128 | V256: varying spreading factor, indicates the smallest occurred value
			- Modulation: List[enums.Modulation]: Modulation format of the channel BPSK: Constantly BPSK modulated 4PAM: Constantly 4PAM modulated 4PVar: BPSK and 4PAM occurred"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('State', DataType.EnumList, enums.State, False, True, 1),
			ArgStruct('Spreading_Factor', DataType.EnumList, enums.SpreadingFactorB, False, True, 1),
			ArgStruct('Modulation', DataType.EnumList, enums.Modulation, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.State: List[enums.State] = None
			self.Spreading_Factor: List[enums.SpreadingFactorB] = None
			self.Modulation: List[enums.Modulation] = None

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:RCDerror:OCINfo \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.carrier.rcdError.ocInfo.read(carrier = repcap.Carrier.Default) \n
		Returns the overall channel information for the RCDE measurement. This information is determined from all measured slots.
			INTRO_CMD_HELP: The parameters <State>, <SpreadFactor> and <Modulation> are returned for the individual channels: \n
			- Values 2 to 4: DPCCH
			- Values 5 to 7: DPDCH
			- Values 8 to 10: HSDPCCH
			- Values 11 to 13: EDPCCH
			- Values 14 to 16: EDPDCH1
			- Values 17 to 19: EDPDCH2
			- Values 20 to 22: EDPDCH3
			- Values 23 to 25: EDPDCH4  \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:RCDerror:OCINfo?', self.__class__.ResultData())

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:RCDerror:OCINfo \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.carrier.rcdError.ocInfo.fetch(carrier = repcap.Carrier.Default) \n
		Returns the overall channel information for the RCDE measurement. This information is determined from all measured slots.
			INTRO_CMD_HELP: The parameters <State>, <SpreadFactor> and <Modulation> are returned for the individual channels: \n
			- Values 2 to 4: DPCCH
			- Values 5 to 7: DPDCH
			- Values 8 to 10: HSDPCCH
			- Values 11 to 13: EDPCCH
			- Values 14 to 16: EDPDCH1
			- Values 17 to 19: EDPDCH2
			- Values 20 to 22: EDPDCH3
			- Values 23 to 25: EDPDCH4  \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:RCDerror:OCINfo?', self.__class__.ResultData())
