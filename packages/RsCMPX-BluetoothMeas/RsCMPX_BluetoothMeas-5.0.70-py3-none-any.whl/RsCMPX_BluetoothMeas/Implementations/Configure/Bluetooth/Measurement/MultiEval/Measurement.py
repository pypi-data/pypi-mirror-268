from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def get_me_count(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MEASurement:MECount \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.measurement.get_me_count() \n
		No command help available \n
			:return: max_error_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MEASurement:MECount?')
		return Conversions.str_to_int(response)

	def set_me_count(self, max_error_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MEASurement:MECount \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.measurement.set_me_count(max_error_count = 1) \n
		No command help available \n
			:param max_error_count: No help available
		"""
		param = Conversions.decimal_value_to_str(max_error_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MEASurement:MECount {param}')
