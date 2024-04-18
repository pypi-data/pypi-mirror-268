from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTimeCls:
	"""PowerVsTime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powerVsTime", core, parent)

	def set(self, avg_pow_lower: float, avg_pow_upper: float, pkm_avg_pow_upper: float, avg_pow_enabled: List[bool], pkm_avg_pow_enable: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.le2M.powerVsTime.set(avg_pow_lower = 1.0, avg_pow_upper = 1.0, pkm_avg_pow_upper = 1.0, avg_pow_enabled = [True, False, True], pkm_avg_pow_enable = [True, False, True]) \n
		Defines the power limits: lower and upper average power limits, upper limit for 'peak minus average power', limit check
		enabling. Commands for uncoded LE 1M PHY (..:LE1M..) , LE 2M PHY (..:LE2M..) , and LE coded PHY (..:LRANge..
		) are available. \n
			:param avg_pow_lower: No help available
			:param avg_pow_upper: No help available
			:param pkm_avg_pow_upper: No help available
			:param avg_pow_enabled: Disables or enables the limit check for the average power, 4 values, corresponding to the current, average, maximum and minimum results.
			:param pkm_avg_pow_enable: Disables or enables the limit check for the 'peak minus average power', 4 values, corresponding to the current, average, maximum and minimum results.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('avg_pow_lower', avg_pow_lower, DataType.Float), ArgSingle('avg_pow_upper', avg_pow_upper, DataType.Float), ArgSingle('pkm_avg_pow_upper', pkm_avg_pow_upper, DataType.Float), ArgSingle('avg_pow_enabled', avg_pow_enabled, DataType.BooleanList, None, False, False, 4), ArgSingle('pkm_avg_pow_enable', pkm_avg_pow_enable, DataType.BooleanList, None, False, False, 4))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:PVTime {param}'.rstrip())

	# noinspection PyTypeChecker
	class PowerVsTimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Avg_Pow_Lower: float: No parameter help available
			- Avg_Pow_Upper: float: No parameter help available
			- Pkm_Avg_Pow_Upper: float: No parameter help available
			- Avg_Pow_Enabled: List[bool]: Disables or enables the limit check for the average power, 4 values, corresponding to the current, average, maximum and minimum results.
			- Pkm_Avg_Pow_Enable: List[bool]: Disables or enables the limit check for the 'peak minus average power', 4 values, corresponding to the current, average, maximum and minimum results."""
		__meta_args_list = [
			ArgStruct.scalar_float('Avg_Pow_Lower'),
			ArgStruct.scalar_float('Avg_Pow_Upper'),
			ArgStruct.scalar_float('Pkm_Avg_Pow_Upper'),
			ArgStruct('Avg_Pow_Enabled', DataType.BooleanList, None, False, False, 4),
			ArgStruct('Pkm_Avg_Pow_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Avg_Pow_Lower: float = None
			self.Avg_Pow_Upper: float = None
			self.Pkm_Avg_Pow_Upper: float = None
			self.Avg_Pow_Enabled: List[bool] = None
			self.Pkm_Avg_Pow_Enable: List[bool] = None

	def get(self) -> PowerVsTimeStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:PVTime \n
		Snippet: value: PowerVsTimeStruct = driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.le2M.powerVsTime.get() \n
		Defines the power limits: lower and upper average power limits, upper limit for 'peak minus average power', limit check
		enabling. Commands for uncoded LE 1M PHY (..:LE1M..) , LE 2M PHY (..:LE2M..) , and LE coded PHY (..:LRANge..
		) are available. \n
			:return: structure: for return value, see the help for PowerVsTimeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:PVTime?', self.__class__.PowerVsTimeStruct())
