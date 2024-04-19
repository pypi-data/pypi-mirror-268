from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IlpControlCls:
	"""IlpControl commands group definition. 5 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ilpControl", core, parent)

	@property
	def tsef(self):
		"""tsef commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsef'):
			from .Tsef import TsefCls
			self._tsef = TsefCls(self._core, self._cmd_group)
		return self._tsef

	@property
	def tsgh(self):
		"""tsgh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsgh'):
			from .Tsgh import TsghCls
			self._tsgh = TsghCls(self._core, self._cmd_group)
		return self._tsgh

	def get_mlength(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:MLENgth \n
		Snippet: value: int = driver.configure.wcdmaMeas.tpc.ilpControl.get_mlength() \n
		Query the number of slots measured in Inner Loop Power Control mode. The value depends on the selected TPC setup and the
		test step settings. It can only be determined while the Inner Loop Power Control mode is active. In other modes INV is
		returned. \n
			:return: meas_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:MLENgth?')
		return Conversions.str_to_int(response)

	def get_ts_segment(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSSegment \n
		Snippet: value: bool = driver.configure.wcdmaMeas.tpc.ilpControl.get_ts_segment() \n
		Enables or disables segmentation for test steps E, F, G and H. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSSegment?')
		return Conversions.str_to_bool(response)

	def set_ts_segment(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSSegment \n
		Snippet: driver.configure.wcdmaMeas.tpc.ilpControl.set_ts_segment(enable = False) \n
		Enables or disables segmentation for test steps E, F, G and H. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSSegment {param}')

	def get_aexecution(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:AEXecution \n
		Snippet: value: bool = driver.configure.wcdmaMeas.tpc.ilpControl.get_aexecution() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:AEXecution?')
		return Conversions.str_to_bool(response)

	def set_aexecution(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:AEXecution \n
		Snippet: driver.configure.wcdmaMeas.tpc.ilpControl.set_aexecution(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:AEXecution {param}')

	def clone(self) -> 'IlpControlCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IlpControlCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
