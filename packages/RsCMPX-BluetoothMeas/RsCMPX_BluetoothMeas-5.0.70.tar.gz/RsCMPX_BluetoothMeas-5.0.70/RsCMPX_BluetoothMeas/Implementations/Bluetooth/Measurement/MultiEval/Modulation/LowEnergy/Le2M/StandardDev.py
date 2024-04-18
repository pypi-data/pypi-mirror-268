from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#Modulation CMDLINKRESOLVED]) exceeding the specified limits, see 'Modulation limits (LE) '.
			- Delta_F_299_P_9: float: Frequency deviation value Δf2 above which 99.9% of all measured Δf2 values occur
			- Freq_Accuracy: float: No parameter help available
			- Freq_Drift: float: No parameter help available
			- Max_Drift: float: No parameter help available
			- Nominal_Power: float: Average power during the carrier-on state
			- Mod_Ratio: float: Modulation ratio Δf2 avg / Δf1 avg
			- Freq_Offset: float: No parameter help available
			- Init_Freq_Drift: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Delta_F_299_P_9'),
			ArgStruct.scalar_float('Freq_Accuracy'),
			ArgStruct.scalar_float('Freq_Drift'),
			ArgStruct.scalar_float('Max_Drift'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Mod_Ratio'),
			ArgStruct.scalar_float('Freq_Offset'),
			ArgStruct.scalar_float('Init_Freq_Drift')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Delta_F_299_P_9: float = None
			self.Freq_Accuracy: float = None
			self.Freq_Drift: float = None
			self.Max_Drift: float = None
			self.Nominal_Power: float = None
			self.Mod_Ratio: float = None
			self.Freq_Offset: float = None
			self.Init_Freq_Drift: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:LENergy:LE2M:SDEViation \n
		Snippet: value: ResultData = driver.bluetooth.measurement.multiEval.modulation.lowEnergy.le2M.standardDev.fetch() \n
		Returns the standard deviation of the modulation results for LE uncoded PHY (LE 1M PHY, LE 2M PHY) , see 'Square TX
		Measurement - modulation statistics'. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:LENergy:LE2M:SDEViation?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float or bool: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#Modulation CMDLINKRESOLVED]) exceeding the specified limits, see 'Modulation limits (LE) '.
			- Delta_F_299_P_9: float or bool: Frequency deviation value Δf2 above which 99.9% of all measured Δf2 values occur
			- Freq_Accuracy: float or bool: No parameter help available
			- Freq_Drift: float or bool: No parameter help available
			- Max_Drift: float or bool: No parameter help available
			- Nominal_Power: float or bool: Average power during the carrier-on state
			- Mod_Ratio: enums.ResultStatus2: Modulation ratio Δf2 avg / Δf1 avg
			- Freq_Offset: float or bool: No parameter help available
			- Init_Freq_Drift: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float_ext('Delta_F_299_P_9'),
			ArgStruct.scalar_float_ext('Freq_Accuracy'),
			ArgStruct.scalar_float_ext('Freq_Drift'),
			ArgStruct.scalar_float_ext('Max_Drift'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_enum('Mod_Ratio', enums.ResultStatus2),
			ArgStruct.scalar_float_ext('Freq_Offset'),
			ArgStruct.scalar_float_ext('Init_Freq_Drift')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Delta_F_299_P_9: float or bool = None
			self.Freq_Accuracy: float or bool = None
			self.Freq_Drift: float or bool = None
			self.Max_Drift: float or bool = None
			self.Nominal_Power: float or bool = None
			self.Mod_Ratio: enums.ResultStatus2 = None
			self.Freq_Offset: float or bool = None
			self.Init_Freq_Drift: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:LENergy:LE2M:SDEViation \n
		Snippet: value: CalculateStruct = driver.bluetooth.measurement.multiEval.modulation.lowEnergy.le2M.standardDev.calculate() \n
		Returns the standard deviation of the modulation results for LE uncoded PHY (LE 1M PHY, LE 2M PHY) , see 'Square TX
		Measurement - modulation statistics'. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:LENergy:LE2M:SDEViation?', self.__class__.CalculateStruct())

	def read(self) -> ResultData:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:LENergy:LE2M:SDEViation \n
		Snippet: value: ResultData = driver.bluetooth.measurement.multiEval.modulation.lowEnergy.le2M.standardDev.read() \n
		Returns the standard deviation of the modulation results for LE uncoded PHY (LE 1M PHY, LE 2M PHY) , see 'Square TX
		Measurement - modulation statistics'. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:LENergy:LE2M:SDEViation?', self.__class__.ResultData())
