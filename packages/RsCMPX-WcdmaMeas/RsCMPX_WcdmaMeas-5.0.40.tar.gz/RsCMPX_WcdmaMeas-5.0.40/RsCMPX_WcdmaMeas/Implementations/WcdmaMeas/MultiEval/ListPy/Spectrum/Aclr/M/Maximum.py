from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def fetch(self, aclr_mode: enums.AclrMode = None, minus=repcap.Minus.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SPECtrum:ACLR:M<nr>:MAXimum \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.listPy.spectrum.aclr.m.maximum.fetch(aclr_mode = enums.AclrMode.ABSolute, minus = repcap.Minus.Default) \n
		Return the power of the adjacent channels for all measured list mode segments.
			INTRO_CMD_HELP: The adjacent channel selected via M<no>/P<no> is at the following frequency relative to the carrier frequency: \n
			- M1 = -5 MHz, M2 = -10 MHz
			- P1 = +5 MHz, P2 = +10 MHz  \n
		Suppressed linked return values: reliability \n
			:param aclr_mode: ABSolute: ACLR power is displayed in dBm as an absolute value. RELative: ACLR power is displayed in dB relative to carrier power.
			:param minus: optional repeated capability selector. Default value: Ch1 (settable in the interface 'M')
			:return: aclr: Comma-separated list of values, one per measured segment"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aclr_mode', aclr_mode, DataType.Enum, enums.AclrMode, is_optional=True))
		minus_cmd_val = self._cmd_group.get_repcap_cmd_value(minus, repcap.Minus)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SPECtrum:ACLR:M{minus_cmd_val}:MAXimum? {param}'.rstrip(), suppressed)
		return response
