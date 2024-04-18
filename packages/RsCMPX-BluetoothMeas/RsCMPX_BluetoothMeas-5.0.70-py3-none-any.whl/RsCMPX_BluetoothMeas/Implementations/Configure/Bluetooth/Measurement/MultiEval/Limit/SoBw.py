from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SoBwCls:
	"""SoBw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("soBw", core, parent)

	def set(self, limit_threshold: float, eq_high_peak_upper: float, low_peak_upper: float, eq_high_peak_enable: bool, low_peak_enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SOBW \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.soBw.set(limit_threshold = 1.0, eq_high_peak_upper = 1.0, low_peak_upper = 1.0, eq_high_peak_enable = False, low_peak_enable = False) \n
		Defines and enables the limits for the 20 dB bandwidth measurement (BR only) . \n
			:param limit_threshold: Threshold value for 'high' vs 'low' peak emission bursts.
			:param eq_high_peak_upper: 20 dB bandwidth limit for 'high' peak emission bursts (≥LimitThreshold) .
			:param low_peak_upper: 20 dB bandwidth limit for 'low' peak emission bursts ( LimitThreshold) .
			:param eq_high_peak_enable: Disable or enable the 20 dB bandwidth limit for 'high' peak emission bursts.
			:param low_peak_enable: Disable or enable the 20 dB bandwidth limit for 'low' peak emission bursts.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('limit_threshold', limit_threshold, DataType.Float), ArgSingle('eq_high_peak_upper', eq_high_peak_upper, DataType.Float), ArgSingle('low_peak_upper', low_peak_upper, DataType.Float), ArgSingle('eq_high_peak_enable', eq_high_peak_enable, DataType.Boolean), ArgSingle('low_peak_enable', low_peak_enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SOBW {param}'.rstrip())

	# noinspection PyTypeChecker
	class SoBwStruct(StructBase):
		"""Response structure. Fields: \n
			- Limit_Threshold: float: Threshold value for 'high' vs 'low' peak emission bursts.
			- Eq_High_Peak_Upper: float: 20 dB bandwidth limit for 'high' peak emission bursts (≥LimitThreshold) .
			- Low_Peak_Upper: float: 20 dB bandwidth limit for 'low' peak emission bursts ( LimitThreshold) .
			- Eq_High_Peak_Enable: bool: Disable or enable the 20 dB bandwidth limit for 'high' peak emission bursts.
			- Low_Peak_Enable: bool: Disable or enable the 20 dB bandwidth limit for 'low' peak emission bursts."""
		__meta_args_list = [
			ArgStruct.scalar_float('Limit_Threshold'),
			ArgStruct.scalar_float('Eq_High_Peak_Upper'),
			ArgStruct.scalar_float('Low_Peak_Upper'),
			ArgStruct.scalar_bool('Eq_High_Peak_Enable'),
			ArgStruct.scalar_bool('Low_Peak_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Limit_Threshold: float = None
			self.Eq_High_Peak_Upper: float = None
			self.Low_Peak_Upper: float = None
			self.Eq_High_Peak_Enable: bool = None
			self.Low_Peak_Enable: bool = None

	def get(self) -> SoBwStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SOBW \n
		Snippet: value: SoBwStruct = driver.configure.bluetooth.measurement.multiEval.limit.soBw.get() \n
		Defines and enables the limits for the 20 dB bandwidth measurement (BR only) . \n
			:return: structure: for return value, see the help for SoBwStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SOBW?', self.__class__.SoBwStruct())
