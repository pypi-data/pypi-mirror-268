from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LrangeCls:
	"""Lrange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrange", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.LePacketType:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PTYPe:LENergy:LRANge \n
		Snippet: value: enums.LePacketType = driver.bluetooth.measurement.inputSignal.adetected.ptype.lowEnergy.lrange.fetch() \n
		Returns the detected packet type for LE coded PHY. A result is available after the CMP180 has auto-detected a packet
		(method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.InputSignal.dmode AUTO) . \n
		Suppressed linked return values: reliability \n
			:return: packet_type: RFPHytest: LE test packet (direct test mode) ADVertiser: air interface packet with advertising channel PDU"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PTYPe:LENergy:LRANge?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.LePacketType)
