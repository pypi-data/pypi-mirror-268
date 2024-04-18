from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpotCheckCls:
	"""SpotCheck commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spotCheck", core, parent)

	def get_level(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SPOTcheck:LEVel \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rxQuality.spotCheck.get_level() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SPOTcheck:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SPOTcheck:LEVel \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.spotCheck.set_level(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SPOTcheck:LEVel {param}')
