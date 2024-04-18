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
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:CTE:LENergy:LE2M:TYPE \n
		Snippet: value: enums.CtePacketType = driver.bluetooth.measurement.inputSignal.adetected.cte.lowEnergy.le2M.typePy.fetch() \n
		Returns the detected CTE type. A result is available after the CMP180 has auto-detected a packet (method
		RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.InputSignal.dmodeAUTO) . Commands for uncoded LE 1M PHY (..:LE1M..
		) and LE 2M PHY (..:LE2M..) are available. \n
		Suppressed linked return values: reliability \n
			:return: packet_type: AOD1us, AOD2us: CTE type angle of departure, 1 µs or 2 µs slot AOAus, AOA2us: CTE type angle of arrival, 2 µs slot AOA1us: CTE type angle of arrival, 1 µs slot"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:CTE:LENergy:LE2M:TYPE?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.CtePacketType)
