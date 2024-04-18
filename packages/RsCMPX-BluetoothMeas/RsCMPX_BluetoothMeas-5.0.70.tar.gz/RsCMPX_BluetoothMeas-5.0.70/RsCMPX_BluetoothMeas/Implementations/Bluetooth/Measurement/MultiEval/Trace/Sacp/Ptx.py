from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtxCls:
	"""Ptx commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptx", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SACP[:PTX] \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.sacp.ptx.fetch() \n
			INTRO_CMD_HELP: Returns the results of the Spectrum ACP table for BR and LE packets in line with the Bluetooth test specification. Note that the number of returned values depends on the current burst type. \n
			- For BR bursts, the trace returns 79 values.
			INTRO_CMD_HELP: The number of valid ACP results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sacp.Brate.Measurement.mode) : \n
			- In CH21 mode, the first 21 ACP values contain results for the relative channels –10, ..., 0, ..., +10; the remaining 58 values are not displayed.
			- In CH79 mode, valid ACP values are available for all 79 Bluetooth channels (2402 MHz, 2403 MHz, ..., 2480 MHz)
			- For LE bursts, the trace returns 81 values.
			INTRO_CMD_HELP: The number of valid ACP results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sacp.LowEnergy.Le2M.Measurement.mode) : \n
			- In CH10 (ACP +/- 5 Channels) mode, the first 21 ACP values contain results for the 1 MHz channels centered at fTX – 10 MHz, fTX – 9 MHz, ..., fTX + 10 MHz. The remaining 58 values are invalid (NAV) . This mode is applicable to all types of LE bursts.
			- In CH40 mode (LE All Channels) , ACP values 1 to 81 contain results for the 1 MHz channels centered at 2401 MHz, 2402 MHz, ..., 2481 MHz This mode is only applicable to test packets using LE 1M PHY or LE 2M PHY.  \n
		Suppressed linked return values: reliability \n
			:return: acp: As explained above, for BR bursts the trace returns 79, and for LE bursts it returns 81 values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SACP:PTX?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SACP[:PTX] \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.sacp.ptx.read() \n
			INTRO_CMD_HELP: Returns the results of the Spectrum ACP table for BR and LE packets in line with the Bluetooth test specification. Note that the number of returned values depends on the current burst type. \n
			- For BR bursts, the trace returns 79 values.
			INTRO_CMD_HELP: The number of valid ACP results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sacp.Brate.Measurement.mode) : \n
			- In CH21 mode, the first 21 ACP values contain results for the relative channels –10, ..., 0, ..., +10; the remaining 58 values are not displayed.
			- In CH79 mode, valid ACP values are available for all 79 Bluetooth channels (2402 MHz, 2403 MHz, ..., 2480 MHz)
			- For LE bursts, the trace returns 81 values.
			INTRO_CMD_HELP: The number of valid ACP results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sacp.LowEnergy.Le2M.Measurement.mode) : \n
			- In CH10 (ACP +/- 5 Channels) mode, the first 21 ACP values contain results for the 1 MHz channels centered at fTX – 10 MHz, fTX – 9 MHz, ..., fTX + 10 MHz. The remaining 58 values are invalid (NAV) . This mode is applicable to all types of LE bursts.
			- In CH40 mode (LE All Channels) , ACP values 1 to 81 contain results for the 1 MHz channels centered at 2401 MHz, 2402 MHz, ..., 2481 MHz This mode is only applicable to test packets using LE 1M PHY or LE 2M PHY.  \n
		Suppressed linked return values: reliability \n
			:return: acp: As explained above, for BR bursts the trace returns 79, and for LE bursts it returns 81 values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SACP:PTX?', suppressed)
		return response
