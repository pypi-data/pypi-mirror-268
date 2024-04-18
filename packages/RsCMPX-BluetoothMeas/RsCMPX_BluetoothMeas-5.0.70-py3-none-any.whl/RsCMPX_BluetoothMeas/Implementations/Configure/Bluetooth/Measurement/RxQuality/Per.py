from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PerCls:
	"""Per commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("per", core, parent)

	def get_level(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:PER:LEVel \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rxQuality.per.get_level() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:PER:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:PER:LEVel \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.per.set_level(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:PER:LEVel {param}')

	def get_tx_packets(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:PER:TXPackets \n
		Snippet: value: int = driver.configure.bluetooth.measurement.rxQuality.per.get_tx_packets() \n
		No command help available \n
			:return: packets_to_send: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:PER:TXPackets?')
		return Conversions.str_to_int(response)

	def set_tx_packets(self, packets_to_send: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:PER:TXPackets \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.per.set_tx_packets(packets_to_send = 1) \n
		No command help available \n
			:param packets_to_send: No help available
		"""
		param = Conversions.decimal_value_to_str(packets_to_send)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:PER:TXPackets {param}')
