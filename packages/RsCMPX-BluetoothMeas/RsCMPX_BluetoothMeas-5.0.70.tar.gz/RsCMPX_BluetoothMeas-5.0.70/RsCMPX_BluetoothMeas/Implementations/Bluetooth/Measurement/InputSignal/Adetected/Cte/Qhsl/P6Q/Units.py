from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .........Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UnitsCls:
	"""Units commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("units", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:CTE:QHSL:P6Q:UNITs \n
		Snippet: value: int = driver.bluetooth.measurement.inputSignal.adetected.cte.qhsl.p6Q.units.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: duration_units: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:CTE:QHSL:P6Q:UNITs?', suppressed)
		return Conversions.str_to_int(response)
