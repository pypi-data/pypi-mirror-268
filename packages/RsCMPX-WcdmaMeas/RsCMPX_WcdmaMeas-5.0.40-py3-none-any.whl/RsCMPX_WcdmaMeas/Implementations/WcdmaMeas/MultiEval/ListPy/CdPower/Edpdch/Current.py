from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self, edpdChannel=repcap.EdpdChannel.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:CDPower:EDPDch<nr>:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.listPy.cdPower.edpdch.current.fetch(edpdChannel = repcap.EdpdChannel.Default) \n
		Return RMS CDP and CDE vs. slot values for a selected E-DPDCH for all measured list mode segments. \n
		Suppressed linked return values: reliability \n
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: edpdch: Comma-separated list of values, one per measured segment"""
		edpdChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:CDPower:EDPDch{edpdChannel_cmd_val}:CURRent?', suppressed)
		return response
