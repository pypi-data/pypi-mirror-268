from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YieldPyCls:
	"""YieldPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("yieldPy", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:BRATe:YIELd \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.modulation.brate.yieldPy.fetch() \n
		Returns the percentage of auto-detected BR packets with a particular pattern type. A result is available after the CMP180
		has auto-detected a packet (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.InputSignal.dmode AUTO) . \n
		Suppressed linked return values: reliability \n
			:return: pattern_yield: Pattern yield for 11110000 patterns, 10101010 patterns, and any other patterns (3 values)"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:BRATe:YIELd?', suppressed)
		return response
