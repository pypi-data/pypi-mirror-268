from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BdAddressCls:
	"""BdAddress commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bdAddress", core, parent)

	def get_qhsl(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BDADdress:QHSL \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.bdAddress.get_qhsl() \n
		No command help available \n
			:return: bd_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BDADdress:QHSL?')
		return trim_str_response(response)

	def set_qhsl(self, bd_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BDADdress:QHSL \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.bdAddress.set_qhsl(bd_address = rawAbc) \n
		No command help available \n
			:param bd_address: No help available
		"""
		param = Conversions.value_to_str(bd_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BDADdress:QHSL {param}')

	def get_value(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BDADdress \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.bdAddress.get_value() \n
		Specifies the Bluetooth device address that the CMP180 expects the DUT to use to generate its access code. \n
			:return: bd_address: 12-digit hex number
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BDADdress?')
		return trim_str_response(response)

	def set_value(self, bd_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BDADdress \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.bdAddress.set_value(bd_address = rawAbc) \n
		Specifies the Bluetooth device address that the CMP180 expects the DUT to use to generate its access code. \n
			:param bd_address: 12-digit hex number
		"""
		param = Conversions.value_to_str(bd_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BDADdress {param}')
