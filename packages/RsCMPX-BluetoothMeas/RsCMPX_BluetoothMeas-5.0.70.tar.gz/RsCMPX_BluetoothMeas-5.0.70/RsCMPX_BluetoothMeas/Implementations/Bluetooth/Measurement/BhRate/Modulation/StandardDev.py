from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bursts_Out_Of_Tol: float: No parameter help available
			- Wi: float: No parameter help available
			- W_0_Wi: float: No parameter help available
			- W_0_Max: float: No parameter help available
			- Rms_Devm: float: No parameter help available
			- Peak_Devm: float: No parameter help available
			- Nominal_Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Bursts_Out_Of_Tol'),
			ArgStruct.scalar_float('Wi'),
			ArgStruct.scalar_float('W_0_Wi'),
			ArgStruct.scalar_float('W_0_Max'),
			ArgStruct.scalar_float('Rms_Devm'),
			ArgStruct.scalar_float('Peak_Devm'),
			ArgStruct.scalar_float('Nominal_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Of_Tol: float = None
			self.Wi: float = None
			self.W_0_Wi: float = None
			self.W_0_Max: float = None
			self.Rms_Devm: float = None
			self.Peak_Devm: float = None
			self.Nominal_Power: float = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:BHRate:MODulation:SDEViation \n
		Snippet: value: ReadStruct = driver.bluetooth.measurement.bhRate.modulation.standardDev.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:BHRate:MODulation:SDEViation?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bursts_Out_Of_Tol: float: No parameter help available
			- Nominal_Power: float: No parameter help available
			- Wi: float: No parameter help available
			- W_0_Wi: float: No parameter help available
			- W_0_Max: float: No parameter help available
			- Rms_Devm: float: No parameter help available
			- Peak_Devm: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Bursts_Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Wi'),
			ArgStruct.scalar_float('W_0_Wi'),
			ArgStruct.scalar_float('W_0_Max'),
			ArgStruct.scalar_float('Rms_Devm'),
			ArgStruct.scalar_float('Peak_Devm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Wi: float = None
			self.W_0_Wi: float = None
			self.W_0_Max: float = None
			self.Rms_Devm: float = None
			self.Peak_Devm: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:BHRate:MODulation:SDEViation \n
		Snippet: value: FetchStruct = driver.bluetooth.measurement.bhRate.modulation.standardDev.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:BHRate:MODulation:SDEViation?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bursts_Out_Of_Tol: float or bool: No parameter help available
			- Nominal_Power: float: No parameter help available
			- Wi: float or bool: No parameter help available
			- W_0_Wi: float or bool: No parameter help available
			- W_0_Max: float or bool: No parameter help available
			- Rms_Devm: float or bool: No parameter help available
			- Peak_Devm: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Bursts_Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float_ext('Wi'),
			ArgStruct.scalar_float_ext('W_0_Wi'),
			ArgStruct.scalar_float_ext('W_0_Max'),
			ArgStruct.scalar_float_ext('Rms_Devm'),
			ArgStruct.scalar_float_ext('Peak_Devm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Of_Tol: float or bool = None
			self.Nominal_Power: float = None
			self.Wi: float or bool = None
			self.W_0_Wi: float or bool = None
			self.W_0_Max: float or bool = None
			self.Rms_Devm: float or bool = None
			self.Peak_Devm: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:BHRate:MODulation:SDEViation \n
		Snippet: value: CalculateStruct = driver.bluetooth.measurement.bhRate.modulation.standardDev.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:BHRate:MODulation:SDEViation?', self.__class__.CalculateStruct())
