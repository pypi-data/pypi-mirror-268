from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTimeCls:
	"""PowerVsTime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powerVsTime", core, parent)

	def set(self, avg_pow_upper: float, peak_pow_upper: float, avg_pow_enabled: List[bool], peak_pow_enabled: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:QHSL:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.qhsl.powerVsTime.set(avg_pow_upper = 1.0, peak_pow_upper = 1.0, avg_pow_enabled = [True, False, True], peak_pow_enabled = [True, False, True]) \n
		No command help available \n
			:param avg_pow_upper: No help available
			:param peak_pow_upper: No help available
			:param avg_pow_enabled: No help available
			:param peak_pow_enabled: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('avg_pow_upper', avg_pow_upper, DataType.Float), ArgSingle('peak_pow_upper', peak_pow_upper, DataType.Float), ArgSingle('avg_pow_enabled', avg_pow_enabled, DataType.BooleanList, None, False, False, 4), ArgSingle('peak_pow_enabled', peak_pow_enabled, DataType.BooleanList, None, False, False, 4))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:QHSL:PVTime {param}'.rstrip())

	# noinspection PyTypeChecker
	class PowerVsTimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Avg_Pow_Upper: float: No parameter help available
			- Peak_Pow_Upper: float: No parameter help available
			- Avg_Pow_Enabled: List[bool]: No parameter help available
			- Peak_Pow_Enabled: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Avg_Pow_Upper'),
			ArgStruct.scalar_float('Peak_Pow_Upper'),
			ArgStruct('Avg_Pow_Enabled', DataType.BooleanList, None, False, False, 4),
			ArgStruct('Peak_Pow_Enabled', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Avg_Pow_Upper: float = None
			self.Peak_Pow_Upper: float = None
			self.Avg_Pow_Enabled: List[bool] = None
			self.Peak_Pow_Enabled: List[bool] = None

	def get(self) -> PowerVsTimeStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:QHSL:PVTime \n
		Snippet: value: PowerVsTimeStruct = driver.configure.bluetooth.measurement.multiEval.limit.qhsl.powerVsTime.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PowerVsTimeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:QHSL:PVTime?', self.__class__.PowerVsTimeStruct())
