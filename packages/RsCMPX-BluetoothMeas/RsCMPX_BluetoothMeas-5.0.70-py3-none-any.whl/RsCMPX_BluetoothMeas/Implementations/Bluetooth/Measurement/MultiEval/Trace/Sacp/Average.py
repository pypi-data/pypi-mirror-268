from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SACP:AVERage \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.sacp.average.read() \n
		Returns 81 values of the Spectrum ACP results in line with the Bluetooth test specification.
			INTRO_CMD_HELP: The number of valid ACP results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sacp.LowEnergy.Le2M.Measurement.mode) : \n
			- For LE bursts, the trace returns 81 values.
			INTRO_CMD_HELP: The number of valid ACP results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sacp.LowEnergy.Le2M.Measurement.mode) : \n
			- In CH10 mode (ACP +/- 5 Channels) , the first 21 ACP values contain results for the 1 MHz channels centered at fTX – 10 MHz, fTX – 9 MHz, ..., fTX + 10 MHz. The remaining 58 values are invalid (NAV) . This mode is applicable to all types of LE bursts.
			- In CH40 mode (LE All Channels) , ACP values 1 to 81 contain results for the 1 MHz channels centered at 2401 MHz, 2402 MHz, ..., 2481 MHz This mode is only applicable to test packets using LE 1M PHY or LE 2M PHY.  \n
		Suppressed linked return values: reliability \n
			:return: acp: 81 spectrum ACP results"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SACP:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SACP:AVERage \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.sacp.average.fetch() \n
		Returns 81 values of the Spectrum ACP results in line with the Bluetooth test specification.
			INTRO_CMD_HELP: The number of valid ACP results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sacp.LowEnergy.Le2M.Measurement.mode) : \n
			- For LE bursts, the trace returns 81 values.
			INTRO_CMD_HELP: The number of valid ACP results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sacp.LowEnergy.Le2M.Measurement.mode) : \n
			- In CH10 mode (ACP +/- 5 Channels) , the first 21 ACP values contain results for the 1 MHz channels centered at fTX – 10 MHz, fTX – 9 MHz, ..., fTX + 10 MHz. The remaining 58 values are invalid (NAV) . This mode is applicable to all types of LE bursts.
			- In CH40 mode (LE All Channels) , ACP values 1 to 81 contain results for the 1 MHz channels centered at 2401 MHz, 2402 MHz, ..., 2481 MHz This mode is only applicable to test packets using LE 1M PHY or LE 2M PHY.  \n
		Suppressed linked return values: reliability \n
			:return: acp: 81 spectrum ACP results"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SACP:AVERage?', suppressed)
		return response
