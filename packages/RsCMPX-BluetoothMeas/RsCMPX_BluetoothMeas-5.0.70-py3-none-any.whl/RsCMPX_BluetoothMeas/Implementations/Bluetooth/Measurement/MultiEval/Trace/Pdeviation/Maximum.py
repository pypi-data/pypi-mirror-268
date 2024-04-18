from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:PDEViation:MAXimum \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.pdeviation.maximum.fetch() \n
		Returns the results of power deviation per slot for LE CTE traces. Deviation value is calculated as the peak-to-average
		power ratio. The results of the minimum and maximum traces can be retrieved. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: power_vs_slot: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:PDEViation:MAXimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:PDEViation:MAXimum \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.pdeviation.maximum.read() \n
		Returns the results of power deviation per slot for LE CTE traces. Deviation value is calculated as the peak-to-average
		power ratio. The results of the minimum and maximum traces can be retrieved. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: power_vs_slot: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:PDEViation:MAXimum?', suppressed)
		return response

	def calculate(self) -> List[float or bool]:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:PDEViation:MAXimum \n
		Snippet: value: List[float or bool] = driver.bluetooth.measurement.multiEval.trace.pdeviation.maximum.calculate() \n
		Returns the results of power deviation per slot for LE CTE traces. Deviation value is calculated as the peak-to-average
		power ratio. The results of the minimum and maximum traces can be retrieved. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: power_vs_slot: (float or boolean items) No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:PDEViation:MAXimum?', suppressed)
		return Conversions.str_to_float_or_bool_list(response)
