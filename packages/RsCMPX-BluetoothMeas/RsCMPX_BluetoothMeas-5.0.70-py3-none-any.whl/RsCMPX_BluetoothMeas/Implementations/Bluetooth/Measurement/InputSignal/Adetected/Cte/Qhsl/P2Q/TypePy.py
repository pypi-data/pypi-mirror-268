from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .........Internal.Types import DataType
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.CtePacketType:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:CTE:QHSL:P2Q:TYPE \n
		Snippet: value: enums.CtePacketType = driver.bluetooth.measurement.inputSignal.adetected.cte.qhsl.p2Q.typePy.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: packet_type: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:CTE:QHSL:P2Q:TYPE?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.CtePacketType)
