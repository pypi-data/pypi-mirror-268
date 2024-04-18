from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	def get_le_1_m(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LE1M \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.rintegrity.lowEnergy.get_le_1_m() \n
		No command help available \n
			:return: report_integrity: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LE1M?')
		return Conversions.str_to_bool(response)

	def set_le_1_m(self, report_integrity: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LE1M \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.rintegrity.lowEnergy.set_le_1_m(report_integrity = False) \n
		No command help available \n
			:param report_integrity: No help available
		"""
		param = Conversions.bool_to_str(report_integrity)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LE1M {param}')

	def get_le_2_m(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LE2M \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.rintegrity.lowEnergy.get_le_2_m() \n
		No command help available \n
			:return: report_integrity: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LE2M?')
		return Conversions.str_to_bool(response)

	def set_le_2_m(self, report_integrity: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LE2M \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.rintegrity.lowEnergy.set_le_2_m(report_integrity = False) \n
		No command help available \n
			:param report_integrity: No help available
		"""
		param = Conversions.bool_to_str(report_integrity)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LE2M {param}')

	def get_lrange(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LRANge \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.rintegrity.lowEnergy.get_lrange() \n
		No command help available \n
			:return: report_integrity: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LRANge?')
		return Conversions.str_to_bool(response)

	def set_lrange(self, report_integrity: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LRANge \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.rintegrity.lowEnergy.set_lrange(report_integrity = False) \n
		No command help available \n
			:param report_integrity: No help available
		"""
		param = Conversions.bool_to_str(report_integrity)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:RINTegrity:LENergy:LRANge {param}')
