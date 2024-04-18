from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LrangeCls:
	"""Lrange commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrange", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Nominal_Power: float: Average power during the carrier-on state
			- No_Of_Exceptions: int: Number of exceptions (channels ±3, ±4 ... with an ACP above the Exception PTx threshold)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_int('No_Of_Exceptions')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nominal_Power: float = None
			self.No_Of_Exceptions: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LRANge \n
		Snippet: value: ResultData = driver.bluetooth.measurement.multiEval.sacp.lowEnergy.lrange.read() \n
		Returns the Spectrum ACP results for LE 2M PHY (...:LE2M...) and LE coded PHY (...:LRANge...) . See 'Square Spectrum ACP'.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LRANge?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LRANge \n
		Snippet: value: ResultData = driver.bluetooth.measurement.multiEval.sacp.lowEnergy.lrange.fetch() \n
		Returns the Spectrum ACP results for LE 2M PHY (...:LE2M...) and LE coded PHY (...:LRANge...) . See 'Square Spectrum ACP'.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LRANge?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Nominal_Power: float or bool: Average power during the carrier-on state
			- No_Of_Exceptions: float or bool: Number of exceptions (channels ±3, ±4 ... with an ACP above the Exception PTx threshold)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_float_ext('No_Of_Exceptions')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nominal_Power: float or bool = None
			self.No_Of_Exceptions: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LRANge \n
		Snippet: value: CalculateStruct = driver.bluetooth.measurement.multiEval.sacp.lowEnergy.lrange.calculate() \n
		Returns the Spectrum ACP results for LE 2M PHY (...:LE2M...) and LE coded PHY (...:LRANge...) . See 'Square Spectrum ACP'.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:SACP:LENergy:LRANge?', self.__class__.CalculateStruct())
