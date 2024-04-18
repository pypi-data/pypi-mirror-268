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
	def fetch(self) -> enums.LeRangePaternType:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PATTern:LENergy:LRANge \n
		Snippet: value: enums.LeRangePaternType = driver.bluetooth.measurement.inputSignal.adetected.pattern.lowEnergy.lrange.fetch() \n
		Returns the detected payload pattern type for LE coded PHY. A result is available after the CMP180 has auto-detected a
		packet (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.InputSignal.dmode AUTO) . \n
		Suppressed linked return values: reliability \n
			:return: pattern_type: ALL0: '00000000' ALL1: '11111111' P11: '10101010' P44: '11110000' OTHer: any pattern except ALL0, ALL1, P11, P44, PRBS9 PRBS9: Pseudo random binary sequence of nine bits"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PATTern:LENergy:LRANge?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.LeRangePaternType)
