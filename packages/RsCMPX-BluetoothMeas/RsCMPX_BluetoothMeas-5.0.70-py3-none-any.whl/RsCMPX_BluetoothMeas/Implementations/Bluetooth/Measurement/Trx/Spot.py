from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpotCls:
	"""Spot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spot", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.Result:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:TRX:SPOT \n
		Snippet: value: enums.Result = driver.bluetooth.measurement.trx.spot.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: spot_check_result: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:TRX:SPOT?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Result)
