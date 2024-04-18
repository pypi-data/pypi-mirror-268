from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	def get_le_1_m(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LE1M \n
		Snippet: value: int = driver.configure.bluetooth.measurement.dtMode.rxQuality.per.packets.lowEnergy.get_le_1_m() \n
		No command help available \n
			:return: number_of_packets: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LE1M?')
		return Conversions.str_to_int(response)

	def set_le_1_m(self, number_of_packets: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LE1M \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.per.packets.lowEnergy.set_le_1_m(number_of_packets = 1) \n
		No command help available \n
			:param number_of_packets: No help available
		"""
		param = Conversions.decimal_value_to_str(number_of_packets)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LE1M {param}')

	def get_le_2_m(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LE2M \n
		Snippet: value: int = driver.configure.bluetooth.measurement.dtMode.rxQuality.per.packets.lowEnergy.get_le_2_m() \n
		No command help available \n
			:return: number_of_packets: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LE2M?')
		return Conversions.str_to_int(response)

	def set_le_2_m(self, number_of_packets: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LE2M \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.per.packets.lowEnergy.set_le_2_m(number_of_packets = 1) \n
		No command help available \n
			:param number_of_packets: No help available
		"""
		param = Conversions.decimal_value_to_str(number_of_packets)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LE2M {param}')

	def get_lrange(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LRANge \n
		Snippet: value: int = driver.configure.bluetooth.measurement.dtMode.rxQuality.per.packets.lowEnergy.get_lrange() \n
		No command help available \n
			:return: number_of_packets: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LRANge?')
		return Conversions.str_to_int(response)

	def set_lrange(self, number_of_packets: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LRANge \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.per.packets.lowEnergy.set_lrange(number_of_packets = 1) \n
		No command help available \n
			:param number_of_packets: No help available
		"""
		param = Conversions.decimal_value_to_str(number_of_packets)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:PER:PACKets:LENergy:LRANge {param}')
