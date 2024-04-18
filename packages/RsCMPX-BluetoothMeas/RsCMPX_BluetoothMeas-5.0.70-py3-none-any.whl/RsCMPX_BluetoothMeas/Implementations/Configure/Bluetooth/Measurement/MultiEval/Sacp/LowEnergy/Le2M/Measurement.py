from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.LeChannelsRange:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LE2M:MEASurement:MODE \n
		Snippet: value: enums.LeChannelsRange = driver.configure.bluetooth.measurement.multiEval.sacp.lowEnergy.le2M.measurement.get_mode() \n
		Specifies the channel range for ACP measurements. It can be selected to cover either the full LE frequency band (forty 2
		MHz channels) or only the adjacency of the current LE channel (ten 2 MHz channels) . The commands for LE 1M PHY (...:LE1M.
		..) and LE 2M PHY (...:LE2M...) are available. Note: Although LE channels are 2 MHz wide, the channel width in ACP
		measurements is always 1 MHz ('half-channel') . \n
			:return: meas_mode: CH10: ACP +/- 5 Channels - covers the current and its 10 adjacent 2 MHz LE channels (5 to the left, 5 to the right) . The CMP180 measures the 1 MHz channels centered at fTX – 10 MHz, ..., fTX + 10 MHz. CH40: LE All Channels - covers all 40 LE channels. The CMP180 measures the 81 half-channels centered at 2401 MHz, 2402 MHz, ..., 2481 MHz.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LE2M:MEASurement:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.LeChannelsRange)

	def set_mode(self, meas_mode: enums.LeChannelsRange) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LE2M:MEASurement:MODE \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.sacp.lowEnergy.le2M.measurement.set_mode(meas_mode = enums.LeChannelsRange.CH10) \n
		Specifies the channel range for ACP measurements. It can be selected to cover either the full LE frequency band (forty 2
		MHz channels) or only the adjacency of the current LE channel (ten 2 MHz channels) . The commands for LE 1M PHY (...:LE1M.
		..) and LE 2M PHY (...:LE2M...) are available. Note: Although LE channels are 2 MHz wide, the channel width in ACP
		measurements is always 1 MHz ('half-channel') . \n
			:param meas_mode: CH10: ACP +/- 5 Channels - covers the current and its 10 adjacent 2 MHz LE channels (5 to the left, 5 to the right) . The CMP180 measures the 1 MHz channels centered at fTX – 10 MHz, ..., fTX + 10 MHz. CH40: LE All Channels - covers all 40 LE channels. The CMP180 measures the 81 half-channels centered at 2401 MHz, 2402 MHz, ..., 2481 MHz.
		"""
		param = Conversions.enum_scalar_to_str(meas_mode, enums.LeChannelsRange)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LE2M:MEASurement:MODE {param}')
