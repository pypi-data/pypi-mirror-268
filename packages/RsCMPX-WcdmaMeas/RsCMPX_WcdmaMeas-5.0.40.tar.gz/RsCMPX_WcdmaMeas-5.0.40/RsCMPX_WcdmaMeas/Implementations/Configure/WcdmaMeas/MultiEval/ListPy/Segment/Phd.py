from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhdCls:
	"""Phd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phd", core, parent)

	def set(self, enable_phd: bool, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:PHD \n
		Snippet: driver.configure.wcdmaMeas.multiEval.listPy.segment.phd.set(enable_phd = False, segment = repcap.Segment.Default) \n
		Enables the calculation of the phase discontinuity vs slot results in segment no. <no>; see 'Multi-evaluation list mode'. \n
			:param enable_phd: OFF: Disable measurement ON: Enable measurement of phase discontinuity
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.bool_to_str(enable_phd)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:PHD {param}')

	def get(self, segment=repcap.Segment.Default) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:PHD \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.listPy.segment.phd.get(segment = repcap.Segment.Default) \n
		Enables the calculation of the phase discontinuity vs slot results in segment no. <no>; see 'Multi-evaluation list mode'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: enable_phd: OFF: Disable measurement ON: Enable measurement of phase discontinuity"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:PHD?')
		return Conversions.str_to_bool(response)
