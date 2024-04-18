from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float or bool: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#Modulation CMDLINKRESOLVED]) exceeding the specified limits.
			- Omega_I: float or bool: Initial center frequency error
			- Omega_Iplus_Omega_0_Max: float or bool: Maximum compensated frequency error
			- Omega_0_Max: float or bool: Maximum compensated frequency error
			- Rms_Devm: float or bool: Differential EVM results
			- Peak_Devm: float or bool: No parameter help available
			- P_99_Devm: float or bool: No parameter help available
			- Nominal_Power: float or bool: Average power during the carrier-on state"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float_ext('Omega_I'),
			ArgStruct.scalar_float_ext('Omega_Iplus_Omega_0_Max'),
			ArgStruct.scalar_float_ext('Omega_0_Max'),
			ArgStruct.scalar_float_ext('Rms_Devm'),
			ArgStruct.scalar_float_ext('Peak_Devm'),
			ArgStruct.scalar_float_ext('P_99_Devm'),
			ArgStruct.scalar_float_ext('Nominal_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Omega_I: float or bool = None
			self.Omega_Iplus_Omega_0_Max: float or bool = None
			self.Omega_0_Max: float or bool = None
			self.Rms_Devm: float or bool = None
			self.Peak_Devm: float or bool = None
			self.P_99_Devm: float or bool = None
			self.Nominal_Power: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:EDRate:MAXimum \n
		Snippet: value: CalculateStruct = driver.bluetooth.measurement.multiEval.modulation.edrate.maximum.calculate() \n
		Returns the modulation results for EDR packets. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:EDRate:MAXimum?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#Modulation CMDLINKRESOLVED]) exceeding the specified limits.
			- Omega_I: float: Initial center frequency error
			- Omega_Iplus_Omega_0_Max: float: Maximum compensated frequency error
			- Omega_0_Max: float: Maximum compensated frequency error
			- Rms_Devm: float: Differential EVM results
			- Peak_Devm: float: No parameter help available
			- P_99_Devm: float: No parameter help available
			- Nominal_Power: float: Average power during the carrier-on state"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Omega_I'),
			ArgStruct.scalar_float('Omega_Iplus_Omega_0_Max'),
			ArgStruct.scalar_float('Omega_0_Max'),
			ArgStruct.scalar_float('Rms_Devm'),
			ArgStruct.scalar_float('Peak_Devm'),
			ArgStruct.scalar_float('P_99_Devm'),
			ArgStruct.scalar_float('Nominal_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Omega_I: float = None
			self.Omega_Iplus_Omega_0_Max: float = None
			self.Omega_0_Max: float = None
			self.Rms_Devm: float = None
			self.Peak_Devm: float = None
			self.P_99_Devm: float = None
			self.Nominal_Power: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:EDRate:MAXimum \n
		Snippet: value: ResultData = driver.bluetooth.measurement.multiEval.modulation.edrate.maximum.fetch() \n
		Returns the modulation results for EDR packets. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:EDRate:MAXimum?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:EDRate:MAXimum \n
		Snippet: value: ResultData = driver.bluetooth.measurement.multiEval.modulation.edrate.maximum.read() \n
		Returns the modulation results for EDR packets. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:EDRate:MAXimum?', self.__class__.ResultData())
