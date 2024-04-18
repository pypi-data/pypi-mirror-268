from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bursts_Out_Of_Tol: float: No parameter help available
			- Nominal_Power: float: No parameter help available
			- Gfsk_Power: float: No parameter help available
			- Psk_Power: float: No parameter help available
			- Psk_Gfsk_Power: float: No parameter help available
			- Guard_Period: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Bursts_Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Gfsk_Power'),
			ArgStruct.scalar_float('Psk_Power'),
			ArgStruct.scalar_float('Psk_Gfsk_Power'),
			ArgStruct.scalar_float('Guard_Period')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Gfsk_Power: float = None
			self.Psk_Power: float = None
			self.Psk_Gfsk_Power: float = None
			self.Guard_Period: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:BHRate:PVTime:AVERage \n
		Snippet: value: ResultData = driver.bluetooth.measurement.bhRate.powerVsTime.average.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:BHRate:PVTime:AVERage?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:BHRate:PVTime:AVERage \n
		Snippet: value: ResultData = driver.bluetooth.measurement.bhRate.powerVsTime.average.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:BHRate:PVTime:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bursts_Out_Of_Tol: float or bool: No parameter help available
			- Nominal_Power: float or bool: No parameter help available
			- Gfsk_Power: float or bool: No parameter help available
			- Psk_Power: float or bool: No parameter help available
			- Psk_Gfsk_Power: float or bool: No parameter help available
			- Guard_Period: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Bursts_Out_Of_Tol'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_float_ext('Gfsk_Power'),
			ArgStruct.scalar_float_ext('Psk_Power'),
			ArgStruct.scalar_float_ext('Psk_Gfsk_Power'),
			ArgStruct.scalar_float_ext('Guard_Period')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Of_Tol: float or bool = None
			self.Nominal_Power: float or bool = None
			self.Gfsk_Power: float or bool = None
			self.Psk_Power: float or bool = None
			self.Psk_Gfsk_Power: float or bool = None
			self.Guard_Period: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:BHRate:PVTime:AVERage \n
		Snippet: value: CalculateStruct = driver.bluetooth.measurement.bhRate.powerVsTime.average.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:BHRate:PVTime:AVERage?', self.__class__.CalculateStruct())
