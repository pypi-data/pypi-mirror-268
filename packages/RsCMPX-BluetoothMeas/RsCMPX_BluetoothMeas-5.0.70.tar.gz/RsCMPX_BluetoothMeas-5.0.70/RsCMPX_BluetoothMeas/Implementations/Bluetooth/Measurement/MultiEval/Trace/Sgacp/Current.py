from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SGACp:CURRent \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.sgacp.current.fetch() \n
		Returns the results of the Spectrum Gated ACP traces for EDR packets. The CMP180 measures the current, average and
		maximum adjacent channel power values.
			INTRO_CMD_HELP: The number of valid results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sgacp.Edrate.Measurement.modeCH21 | CH79) : \n
			- If CH21 mode (ACP +/- 10 Channels) is selected, the first 21 values contain the results for the relative channels –10, ..., 0, ..., +10; the remaining 58 values are not displayed.
			- If CH79 mode (ACP 79 Channels) is selected, valid ACP values are available for all channels in the Bluetooth regulatory range.  \n
		Suppressed linked return values: reliability \n
			:return: acp: 79 ACP results"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SGACp:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SGACp:CURRent \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.sgacp.current.read() \n
		Returns the results of the Spectrum Gated ACP traces for EDR packets. The CMP180 measures the current, average and
		maximum adjacent channel power values.
			INTRO_CMD_HELP: The number of valid results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sgacp.Edrate.Measurement.modeCH21 | CH79) : \n
			- If CH21 mode (ACP +/- 10 Channels) is selected, the first 21 values contain the results for the relative channels –10, ..., 0, ..., +10; the remaining 58 values are not displayed.
			- If CH79 mode (ACP 79 Channels) is selected, valid ACP values are available for all channels in the Bluetooth regulatory range.  \n
		Suppressed linked return values: reliability \n
			:return: acp: 79 ACP results"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SGACp:CURRent?', suppressed)
		return response
