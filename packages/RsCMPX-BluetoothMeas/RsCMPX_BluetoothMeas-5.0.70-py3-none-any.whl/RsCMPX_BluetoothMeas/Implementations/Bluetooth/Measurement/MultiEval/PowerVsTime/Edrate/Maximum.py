from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


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
			- Out_Of_Tol: float or bool: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#PowerVsTime CMDLINKRESOLVED]) exceeding the specified limits.
			- Nominal_Power: float or bool: Average power during the carrier-on state
			- Gfsk_Power: float or bool: Average power in the GFSK portion of the burst
			- Dpsk_Power: float or bool: Average power in the DPSK portion of the burst
			- Dpsk_Minus_Gfsk: float or bool: Difference between DPSK and GFSK power
			- Guard_Period: float or bool: Length of the guard band between the packet header and the synchronization sequence
			- Packet_Timing: enums.ResultStatus2: Time between the expected and actual start of the first symbol of the Bluetooth burst
			- Peak_Power: float or bool: Maximum power within the whole burst. The result is only available via remote command."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_float_ext('Gfsk_Power'),
			ArgStruct.scalar_float_ext('Dpsk_Power'),
			ArgStruct.scalar_float_ext('Dpsk_Minus_Gfsk'),
			ArgStruct.scalar_float_ext('Guard_Period'),
			ArgStruct.scalar_enum('Packet_Timing', enums.ResultStatus2),
			ArgStruct.scalar_float_ext('Peak_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Nominal_Power: float or bool = None
			self.Gfsk_Power: float or bool = None
			self.Dpsk_Power: float or bool = None
			self.Dpsk_Minus_Gfsk: float or bool = None
			self.Guard_Period: float or bool = None
			self.Packet_Timing: enums.ResultStatus2 = None
			self.Peak_Power: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:EDRate:MAXimum \n
		Snippet: value: CalculateStruct = driver.bluetooth.measurement.multiEval.powerVsTime.edrate.maximum.calculate() \n
		Returns the power results for EDR packets. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:EDRate:MAXimum?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float or bool: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#PowerVsTime CMDLINKRESOLVED]) exceeding the specified limits.
			- Nominal_Power: float: Average power during the carrier-on state
			- Gfsk_Power: float: Average power in the GFSK portion of the burst
			- Dpsk_Power: float: Average power in the DPSK portion of the burst
			- Dpsk_Minus_Gfsk: float: Difference between DPSK and GFSK power
			- Guard_Period: float: Length of the guard band between the packet header and the synchronization sequence
			- Packet_Timing: float: Time between the expected and actual start of the first symbol of the Bluetooth burst
			- Peak_Power: float: Maximum power within the whole burst. The result is only available via remote command."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Gfsk_Power'),
			ArgStruct.scalar_float('Dpsk_Power'),
			ArgStruct.scalar_float('Dpsk_Minus_Gfsk'),
			ArgStruct.scalar_float('Guard_Period'),
			ArgStruct.scalar_float('Packet_Timing'),
			ArgStruct.scalar_float('Peak_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Nominal_Power: float = None
			self.Gfsk_Power: float = None
			self.Dpsk_Power: float = None
			self.Dpsk_Minus_Gfsk: float = None
			self.Guard_Period: float = None
			self.Packet_Timing: float = None
			self.Peak_Power: float = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:EDRate:MAXimum \n
		Snippet: value: ReadStruct = driver.bluetooth.measurement.multiEval.powerVsTime.edrate.maximum.read() \n
		Returns the power results for EDR packets. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:EDRate:MAXimum?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#PowerVsTime CMDLINKRESOLVED]) exceeding the specified limits.
			- Nominal_Power: float: Average power during the carrier-on state
			- Gfsk_Power: float: Average power in the GFSK portion of the burst
			- Dpsk_Power: float: Average power in the DPSK portion of the burst
			- Dpsk_Minus_Gfsk: float: Difference between DPSK and GFSK power
			- Guard_Period: float: Length of the guard band between the packet header and the synchronization sequence
			- Packet_Timing: float: Time between the expected and actual start of the first symbol of the Bluetooth burst
			- Peak_Power: float: Maximum power within the whole burst. The result is only available via remote command."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Gfsk_Power'),
			ArgStruct.scalar_float('Dpsk_Power'),
			ArgStruct.scalar_float('Dpsk_Minus_Gfsk'),
			ArgStruct.scalar_float('Guard_Period'),
			ArgStruct.scalar_float('Packet_Timing'),
			ArgStruct.scalar_float('Peak_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Gfsk_Power: float = None
			self.Dpsk_Power: float = None
			self.Dpsk_Minus_Gfsk: float = None
			self.Guard_Period: float = None
			self.Packet_Timing: float = None
			self.Peak_Power: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:EDRate:MAXimum \n
		Snippet: value: FetchStruct = driver.bluetooth.measurement.multiEval.powerVsTime.edrate.maximum.fetch() \n
		Returns the power results for EDR packets. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:EDRate:MAXimum?', self.__class__.FetchStruct())
