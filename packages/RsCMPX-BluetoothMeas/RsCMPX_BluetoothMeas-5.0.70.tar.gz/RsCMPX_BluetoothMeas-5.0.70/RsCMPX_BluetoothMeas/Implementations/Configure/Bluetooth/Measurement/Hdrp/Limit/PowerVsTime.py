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

	def set(self, average_power_low: float, average_power_upp: float, average_pow_enable: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.limit.powerVsTime.set(average_power_low = 1.0, average_power_upp = 1.0, average_pow_enable = [True, False, True]) \n
		No command help available \n
			:param average_power_low: No help available
			:param average_power_upp: No help available
			:param average_pow_enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('average_power_low', average_power_low, DataType.Float), ArgSingle('average_power_upp', average_power_upp, DataType.Float), ArgSingle('average_pow_enable', average_pow_enable, DataType.BooleanList, None, False, False, 4))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:PVTime {param}'.rstrip())

	# noinspection PyTypeChecker
	class PowerVsTimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Average_Power_Low: float: No parameter help available
			- Average_Power_Upp: float: No parameter help available
			- Average_Pow_Enable: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Average_Power_Low'),
			ArgStruct.scalar_float('Average_Power_Upp'),
			ArgStruct('Average_Pow_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Average_Power_Low: float = None
			self.Average_Power_Upp: float = None
			self.Average_Pow_Enable: List[bool] = None

	def get(self) -> PowerVsTimeStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:PVTime \n
		Snippet: value: PowerVsTimeStruct = driver.configure.bluetooth.measurement.hdrp.limit.powerVsTime.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PowerVsTimeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:PVTime?', self.__class__.PowerVsTimeStruct())
