from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LapCls:
	"""Lap commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lap", core, parent)

	def get_qhsl(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LAP:QHSL \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.lap.get_qhsl() \n
		No command help available \n
			:return: bd_address_lap: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LAP:QHSL?')
		return trim_str_response(response)

	def set_qhsl(self, bd_address_lap: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LAP:QHSL \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.lap.set_qhsl(bd_address_lap = rawAbc) \n
		No command help available \n
			:param bd_address_lap: No help available
		"""
		param = Conversions.value_to_str(bd_address_lap)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LAP:QHSL {param}')

	def get_value(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LAP \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.lap.get_value() \n
		Specifies the lower address part of the DUT's Bluetooth device address. \n
			:return: bd_address_lap: Six-digit hex number
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LAP?')
		return trim_str_response(response)

	def set_value(self, bd_address_lap: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LAP \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.lap.set_value(bd_address_lap = rawAbc) \n
		Specifies the lower address part of the DUT's Bluetooth device address. \n
			:param bd_address_lap: Six-digit hex number
		"""
		param = Conversions.value_to_str(bd_address_lap)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LAP {param}')
