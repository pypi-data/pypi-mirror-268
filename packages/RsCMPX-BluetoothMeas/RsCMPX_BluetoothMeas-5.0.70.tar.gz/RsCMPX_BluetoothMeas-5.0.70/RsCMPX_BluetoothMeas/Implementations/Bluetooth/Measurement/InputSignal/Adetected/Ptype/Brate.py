from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BrateCls:
	"""Brate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("brate", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.BrPacketType:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PTYPe:BRATe \n
		Snippet: value: enums.BrPacketType = driver.bluetooth.measurement.inputSignal.adetected.ptype.brate.fetch() \n
		Returns the detected BR packet type. A result is available after the CMP180 has auto-detected a packet (method
		RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.InputSignal.dmode AUTO) . \n
		Suppressed linked return values: reliability \n
			:return: packet_type: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PTYPe:BRATe?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.BrPacketType)
