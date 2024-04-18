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
			- Out_Of_Tol: float or bool: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#SoBw CMDLINKRESOLVED]) exceeding the specified limit.
			- Nominal_Power: float or bool: Average power during the carrier-on state.
			- Peak_Emission: float or bool: Peak power in the measured spectral range.
			- Fl: float or bool: Lower frequency where the transmit power drops 20 dB below the peak emission.
			- Fh: float or bool: Higher frequency where the transmit power drops 20 dB below the peak emission.
			- Fh_Min_Fl: float or bool: 20 dB bandwidth; difference between fH – fL."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_float_ext('Peak_Emission'),
			ArgStruct.scalar_float_ext('Fl'),
			ArgStruct.scalar_float_ext('Fh'),
			ArgStruct.scalar_float_ext('Fh_Min_Fl')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Nominal_Power: float or bool = None
			self.Peak_Emission: float or bool = None
			self.Fl: float or bool = None
			self.Fh: float or bool = None
			self.Fh_Min_Fl: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:SOBW:BRATe:MAXimum \n
		Snippet: value: CalculateStruct = driver.bluetooth.measurement.multiEval.soBw.brate.maximum.calculate() \n
		Returns the Spectrum 20 dB Bandwidth results. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:SOBW:BRATe:MAXimum?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float or bool: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#SoBw CMDLINKRESOLVED]) exceeding the specified limit.
			- Nominal_Power: float: Average power during the carrier-on state.
			- Peak_Emission: float: Peak power in the measured spectral range.
			- Fl: float: Lower frequency where the transmit power drops 20 dB below the peak emission.
			- Fh: float: Higher frequency where the transmit power drops 20 dB below the peak emission.
			- Fh_Min_Fl: float: 20 dB bandwidth; difference between fH – fL."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Peak_Emission'),
			ArgStruct.scalar_float('Fl'),
			ArgStruct.scalar_float('Fh'),
			ArgStruct.scalar_float('Fh_Min_Fl')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Nominal_Power: float = None
			self.Peak_Emission: float = None
			self.Fl: float = None
			self.Fh: float = None
			self.Fh_Min_Fl: float = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:SOBW:BRATe:MAXimum \n
		Snippet: value: ReadStruct = driver.bluetooth.measurement.multiEval.soBw.brate.maximum.read() \n
		Returns the Spectrum 20 dB Bandwidth results. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:SOBW:BRATe:MAXimum?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.Bluetooth.Measurement.MultiEval.Scount#SoBw CMDLINKRESOLVED]) exceeding the specified limit.
			- Nominal_Power: float: Average power during the carrier-on state.
			- Peak_Emission: float: Peak power in the measured spectral range.
			- Fl: float: Lower frequency where the transmit power drops 20 dB below the peak emission.
			- Fh: float: Higher frequency where the transmit power drops 20 dB below the peak emission.
			- Fh_Min_Fl: float: 20 dB bandwidth; difference between fH – fL."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Peak_Emission'),
			ArgStruct.scalar_float('Fl'),
			ArgStruct.scalar_float('Fh'),
			ArgStruct.scalar_float('Fh_Min_Fl')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Peak_Emission: float = None
			self.Fl: float = None
			self.Fh: float = None
			self.Fh_Min_Fl: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:SOBW:BRATe:MAXimum \n
		Snippet: value: FetchStruct = driver.bluetooth.measurement.multiEval.soBw.brate.maximum.fetch() \n
		Returns the Spectrum 20 dB Bandwidth results. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:SOBW:BRATe:MAXimum?', self.__class__.FetchStruct())
