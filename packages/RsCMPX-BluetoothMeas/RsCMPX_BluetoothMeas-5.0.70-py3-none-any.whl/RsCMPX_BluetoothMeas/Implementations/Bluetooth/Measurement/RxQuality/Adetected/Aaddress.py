from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AaddressCls:
	"""Aaddress commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aaddress", core, parent)

	def fetch(self) -> str:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:RXQuality:ADETected:AADDress \n
		Snippet: value: str = driver.bluetooth.measurement.rxQuality.adetected.aaddress.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: adv_address: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:RXQuality:ADETected:AADDress?', suppressed)
		return trim_str_response(response)
