from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Le1MCls:
	"""Le1M commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("le1M", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.DetectedPatternType:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PATTern:LENergy[:LE1M] \n
		Snippet: value: enums.DetectedPatternType = driver.bluetooth.measurement.inputSignal.adetected.pattern.lowEnergy.le1M.fetch() \n
		Returns the detected payload pattern type. Commands for LE 1M PHY (...:LE1M...) and LE 2M PHY (...:LE2M...) are available.
		A result is available after the CMP180 has auto-detected a packet (method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.InputSignal.dmode AUTO) . \n
		Suppressed linked return values: reliability \n
			:return: pattern_type: P11: 10101010 P44: 11110000 OTHer: any pattern except P11, P44 ALTernating: the periodical change between the pattern P11 and P44"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PATTern:LENergy:LE1M?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.DetectedPatternType)
