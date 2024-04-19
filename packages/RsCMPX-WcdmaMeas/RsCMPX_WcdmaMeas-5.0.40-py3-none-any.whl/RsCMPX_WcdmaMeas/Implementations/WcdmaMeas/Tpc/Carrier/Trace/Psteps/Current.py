from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self, carrier=repcap.Carrier.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:TRACe:PSTeps:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.tpc.carrier.trace.psteps.current.fetch(carrier = repcap.Carrier.Default) \n
		Return the values of the power steps trace per carrier. Each power step is calculated as the difference between the UE
		power of a slot and the UE power of the preceding slot. For the first measured slot, a 0 is returned. You can query the
		number of measured slots using the CONFigure:WCDMa:MEAS:TPC:...:MLENgth? command of the used measurement mode. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: power_steps: N power step results, one per measured slot Power step result number m indicates the difference between the UE power results number m and number m-1. The first power step result equals NCAP."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:TRACe:PSTeps:CURRent?', suppressed)
		return response

	def read(self, carrier=repcap.Carrier.Default) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:TRACe:PSTeps:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.tpc.carrier.trace.psteps.current.read(carrier = repcap.Carrier.Default) \n
		Return the values of the power steps trace per carrier. Each power step is calculated as the difference between the UE
		power of a slot and the UE power of the preceding slot. For the first measured slot, a 0 is returned. You can query the
		number of measured slots using the CONFigure:WCDMa:MEAS:TPC:...:MLENgth? command of the used measurement mode. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: power_steps: N power step results, one per measured slot Power step result number m indicates the difference between the UE power results number m and number m-1. The first power step result equals NCAP."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:TRACe:PSTeps:CURRent?', suppressed)
		return response

	def calculate(self, carrier=repcap.Carrier.Default) -> List[float or bool]:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:TRACe:PSTeps:CURRent \n
		Snippet: value: List[float or bool] = driver.wcdmaMeas.tpc.carrier.trace.psteps.current.calculate(carrier = repcap.Carrier.Default) \n
		Return the values of the power steps trace per carrier. Each power step is calculated as the difference between the UE
		power of a slot and the UE power of the preceding slot. For the first measured slot, a 0 is returned. You can query the
		number of measured slots using the CONFigure:WCDMa:MEAS:TPC:...:MLENgth? command of the used measurement mode. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: power_steps: (float or boolean items) N power step results, one per measured slot Power step result number m indicates the difference between the UE power results number m and number m-1. The first power step result equals NCAP."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:TRACe:PSTeps:CURRent?', suppressed)
		return Conversions.str_to_float_or_bool_list(response)
