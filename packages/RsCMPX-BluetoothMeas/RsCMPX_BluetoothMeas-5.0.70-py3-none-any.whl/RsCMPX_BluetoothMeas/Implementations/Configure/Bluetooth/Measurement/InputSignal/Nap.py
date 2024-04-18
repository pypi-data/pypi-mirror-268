from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NapCls:
	"""Nap commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nap", core, parent)

	def get_qhsl(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:NAP:QHSL \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.nap.get_qhsl() \n
		No command help available \n
			:return: bd_address_nap: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:NAP:QHSL?')
		return trim_str_response(response)

	def set_qhsl(self, bd_address_nap: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:NAP:QHSL \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.nap.set_qhsl(bd_address_nap = rawAbc) \n
		No command help available \n
			:param bd_address_nap: No help available
		"""
		param = Conversions.value_to_str(bd_address_nap)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:NAP:QHSL {param}')

	def get_value(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:NAP \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.nap.get_value() \n
		Specifies the non-specific address part of the DUT's Bluetooth device address. \n
			:return: bd_address_nap: Four-digit hex number
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:NAP?')
		return trim_str_response(response)

	def set_value(self, bd_address_nap: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:NAP \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.nap.set_value(bd_address_nap = rawAbc) \n
		Specifies the non-specific address part of the DUT's Bluetooth device address. \n
			:param bd_address_nap: Four-digit hex number
		"""
		param = Conversions.value_to_str(bd_address_nap)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:NAP {param}')
