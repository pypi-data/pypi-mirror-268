from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTimeCls:
	"""PowerVsTime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powerVsTime", core, parent)

	def set(self, pack_time_lower: float, pack_time_upper: float, pack_time_enable: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.powerVsTime.set(pack_time_lower = 1.0, pack_time_upper = 1.0, pack_time_enable = [True, False, True]) \n
		Sets and enables/disables a lower and upper timing error limit for PVT measurements. \n
			:param pack_time_lower: No help available
			:param pack_time_upper: No help available
			:param pack_time_enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('pack_time_lower', pack_time_lower, DataType.Float), ArgSingle('pack_time_upper', pack_time_upper, DataType.Float), ArgSingle('pack_time_enable', pack_time_enable, DataType.BooleanList, None, False, False, 4))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:PVTime {param}'.rstrip())

	# noinspection PyTypeChecker
	class PowerVsTimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Pack_Time_Lower: float: No parameter help available
			- Pack_Time_Upper: float: No parameter help available
			- Pack_Time_Enable: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Pack_Time_Lower'),
			ArgStruct.scalar_float('Pack_Time_Upper'),
			ArgStruct('Pack_Time_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pack_Time_Lower: float = None
			self.Pack_Time_Upper: float = None
			self.Pack_Time_Enable: List[bool] = None

	def get(self) -> PowerVsTimeStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:PVTime \n
		Snippet: value: PowerVsTimeStruct = driver.configure.bluetooth.measurement.multiEval.limit.powerVsTime.get() \n
		Sets and enables/disables a lower and upper timing error limit for PVT measurements. \n
			:return: structure: for return value, see the help for PowerVsTimeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:PVTime?', self.__class__.PowerVsTimeStruct())
