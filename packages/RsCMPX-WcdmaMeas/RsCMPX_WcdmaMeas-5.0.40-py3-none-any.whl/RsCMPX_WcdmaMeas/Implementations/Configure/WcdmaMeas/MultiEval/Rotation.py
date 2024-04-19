from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RotationCls:
	"""Rotation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rotation", core, parent)

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:ROTation:MODulation \n
		Snippet: value: int = driver.configure.wcdmaMeas.multiEval.rotation.get_modulation() \n
		Defines the initial phase reference (φ=0) for I/Q constellation diagrams of QPSK signals. \n
			:return: rotation: The entered value is rounded to 0 deg or 45 deg. 0 deg: constellation points on the I- and Q-axes 45 deg: constellation points on angle bisectors between the I- and Q-axes
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:ROTation:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, rotation: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:ROTation:MODulation \n
		Snippet: driver.configure.wcdmaMeas.multiEval.rotation.set_modulation(rotation = 1) \n
		Defines the initial phase reference (φ=0) for I/Q constellation diagrams of QPSK signals. \n
			:param rotation: The entered value is rounded to 0 deg or 45 deg. 0 deg: constellation points on the I- and Q-axes 45 deg: constellation points on angle bisectors between the I- and Q-axes
		"""
		param = Conversions.decimal_value_to_str(rotation)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:ROTation:MODulation {param}')
