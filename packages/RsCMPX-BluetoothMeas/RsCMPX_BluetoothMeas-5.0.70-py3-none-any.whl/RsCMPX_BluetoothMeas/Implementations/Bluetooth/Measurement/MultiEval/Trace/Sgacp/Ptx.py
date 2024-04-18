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
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SGACp[:PTX] \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.sgacp.ptx.fetch() \n
		Returns the values of the Spectrum Gated ACP tables for EDR packets. The CMP180 measures the adjacent channel power
		values PTX(f) in line with Bluetooth test specification.
			INTRO_CMD_HELP: The number of valid results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sgacp.Edrate.Measurement.mode CH21 | CH79) : \n
			- If ACP +/- 10 Channels is selected, the first 21 values contain the results for the relative channels –10, ..., 0, ..., +10; the remaining 58 values are not displayed.
			- If ACP 79 Channels is selected, valid ACP values are available for all channels in the Bluetooth regulatory range.  \n
		Suppressed linked return values: reliability \n
			:return: acp: 79 ACP results"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SGACp:PTX?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SGACp[:PTX] \n
		Snippet: value: List[float] = driver.bluetooth.measurement.multiEval.trace.sgacp.ptx.read() \n
		Returns the values of the Spectrum Gated ACP tables for EDR packets. The CMP180 measures the adjacent channel power
		values PTX(f) in line with Bluetooth test specification.
			INTRO_CMD_HELP: The number of valid results depends on the ACP measurement mode (method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Sgacp.Edrate.Measurement.mode CH21 | CH79) : \n
			- If ACP +/- 10 Channels is selected, the first 21 values contain the results for the relative channels –10, ..., 0, ..., +10; the remaining 58 values are not displayed.
			- If ACP 79 Channels is selected, valid ACP values are available for all channels in the Bluetooth regulatory range.  \n
		Suppressed linked return values: reliability \n
			:return: acp: 79 ACP results"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:SGACp:PTX?', suppressed)
		return response
