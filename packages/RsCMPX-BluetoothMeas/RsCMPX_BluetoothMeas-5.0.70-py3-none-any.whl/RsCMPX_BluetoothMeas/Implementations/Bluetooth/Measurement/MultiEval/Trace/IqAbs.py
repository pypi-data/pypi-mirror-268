from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqAbsCls:
	"""IqAbs commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqAbs", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Iphase: List[float]: N in-phase amplitudes (IPhase) and N quadrature-phase (QPhase) amplitudes, where N is equal to the number of processed 50-symbol blocks; see 'I/Q constellation trace points (EDR) '.
			- Qphase: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Iphase', DataType.FloatList, None, False, True, 1),
			ArgStruct('Qphase', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Iphase: List[float] = None
			self.Qphase: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:IQABs \n
		Snippet: value: ResultData = driver.bluetooth.measurement.multiEval.trace.iqAbs.read() \n
		Returns the values of the traces in the I/Q constellation diagrams. The mnemonics IQABs, IQDiff, and IQERr denote the
		absolute, differential and I/Q constellation error results. The I/Q traces are available for EDR packets (method
		RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.InputSignal.btype EDR) . \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:IQABs?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:IQABs \n
		Snippet: value: ResultData = driver.bluetooth.measurement.multiEval.trace.iqAbs.fetch() \n
		Returns the values of the traces in the I/Q constellation diagrams. The mnemonics IQABs, IQDiff, and IQERr denote the
		absolute, differential and I/Q constellation error results. The I/Q traces are available for EDR packets (method
		RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.InputSignal.btype EDR) . \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:IQABs?', self.__class__.ResultData())
