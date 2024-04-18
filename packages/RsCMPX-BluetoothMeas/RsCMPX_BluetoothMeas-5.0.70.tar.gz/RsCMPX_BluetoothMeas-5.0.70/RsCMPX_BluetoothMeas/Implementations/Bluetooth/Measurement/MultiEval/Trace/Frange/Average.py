from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:FRANge:AVERage \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.frange.average.read() \n
		Returns the average values of the Frequency Range trace. The values are available for BR packets. \n
		Suppressed linked return values: reliability \n
			:return: frequency_range: RX signal level measured at the frequencies between 501 pixels (502 values)"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:FRANge:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:FRANge:AVERage \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.frange.average.fetch() \n
		Returns the average values of the Frequency Range trace. The values are available for BR packets. \n
		Suppressed linked return values: reliability \n
			:return: frequency_range: RX signal level measured at the frequencies between 501 pixels (502 values)"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:FRANge:AVERage?', suppressed)
		return response
