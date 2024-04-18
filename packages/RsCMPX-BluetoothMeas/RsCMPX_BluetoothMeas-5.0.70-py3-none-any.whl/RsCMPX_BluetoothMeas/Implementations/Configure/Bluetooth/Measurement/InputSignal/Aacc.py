from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AaccCls:
	"""Aacc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aacc", core, parent)

	def get_qhsl(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:AACC:QHSL \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.aacc.get_qhsl() \n
		No command help available \n
			:return: access_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:AACC:QHSL?')
		return trim_str_response(response)

	def set_qhsl(self, access_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:AACC:QHSL \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.aacc.set_qhsl(access_address = rawAbc) \n
		No command help available \n
			:param access_address: No help available
		"""
		param = Conversions.value_to_str(access_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:AACC:QHSL {param}')
