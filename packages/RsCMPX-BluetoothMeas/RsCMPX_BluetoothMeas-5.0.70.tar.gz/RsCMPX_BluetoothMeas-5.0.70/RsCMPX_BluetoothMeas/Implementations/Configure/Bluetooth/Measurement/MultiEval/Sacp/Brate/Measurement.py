from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BrEdrChannelsRange:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:BRATe:MEASurement:MODE \n
		Snippet: value: enums.BrEdrChannelsRange = driver.configure.bluetooth.measurement.multiEval.sacp.brate.measurement.get_mode() \n
		Selects the measured ACP channel range for BR or EDR packets. The ACP can be measured over the expected transmit channel
		+/- 10 channels (21 channels in total) or over the entire Bluetooth regulatory range (79 channels) . \n
			:return: meas_mode: Measure 79 or 21 channels
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:BRATe:MEASurement:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BrEdrChannelsRange)

	def set_mode(self, meas_mode: enums.BrEdrChannelsRange) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:BRATe:MEASurement:MODE \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.sacp.brate.measurement.set_mode(meas_mode = enums.BrEdrChannelsRange.CH21) \n
		Selects the measured ACP channel range for BR or EDR packets. The ACP can be measured over the expected transmit channel
		+/- 10 channels (21 channels in total) or over the entire Bluetooth regulatory range (79 channels) . \n
			:param meas_mode: Measure 79 or 21 channels
		"""
		param = Conversions.enum_scalar_to_str(meas_mode, enums.BrEdrChannelsRange)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:BRATe:MEASurement:MODE {param}')
