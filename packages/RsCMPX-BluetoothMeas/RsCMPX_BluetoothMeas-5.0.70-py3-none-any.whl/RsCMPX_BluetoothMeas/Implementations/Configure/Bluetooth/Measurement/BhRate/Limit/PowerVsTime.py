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

	def set(self, psk_min_gfsk_low: float, psk_min_gfsk_upp: float, psk_min_gfsk_enable: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.limit.powerVsTime.set(psk_min_gfsk_low = 1.0, psk_min_gfsk_upp = 1.0, psk_min_gfsk_enable = [True, False, True]) \n
		No command help available \n
			:param psk_min_gfsk_low: No help available
			:param psk_min_gfsk_upp: No help available
			:param psk_min_gfsk_enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('psk_min_gfsk_low', psk_min_gfsk_low, DataType.Float), ArgSingle('psk_min_gfsk_upp', psk_min_gfsk_upp, DataType.Float), ArgSingle('psk_min_gfsk_enable', psk_min_gfsk_enable, DataType.BooleanList, None, False, False, 4))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:PVTime {param}'.rstrip())

	# noinspection PyTypeChecker
	class PowerVsTimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Psk_Min_Gfsk_Low: float: No parameter help available
			- Psk_Min_Gfsk_Upp: float: No parameter help available
			- Psk_Min_Gfsk_Enable: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Psk_Min_Gfsk_Low'),
			ArgStruct.scalar_float('Psk_Min_Gfsk_Upp'),
			ArgStruct('Psk_Min_Gfsk_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Psk_Min_Gfsk_Low: float = None
			self.Psk_Min_Gfsk_Upp: float = None
			self.Psk_Min_Gfsk_Enable: List[bool] = None

	def get(self) -> PowerVsTimeStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:PVTime \n
		Snippet: value: PowerVsTimeStruct = driver.configure.bluetooth.measurement.bhRate.limit.powerVsTime.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PowerVsTimeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:PVTime?', self.__class__.PowerVsTimeStruct())
