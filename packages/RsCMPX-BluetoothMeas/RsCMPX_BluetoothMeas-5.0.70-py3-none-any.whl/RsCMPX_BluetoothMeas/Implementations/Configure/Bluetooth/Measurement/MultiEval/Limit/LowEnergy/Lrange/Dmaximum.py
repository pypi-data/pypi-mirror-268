from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmaximumCls:
	"""Dmaximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmaximum", core, parent)

	def set(self, freq_dev_f_1_lower: float, freq_dev_f_1_upper: float, freq_dev_f_1_enable: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LRANge:DMAXimum \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.lrange.dmaximum.set(freq_dev_f_1_lower = 1.0, freq_dev_f_1_upper = 1.0, freq_dev_f_1_enable = [True, False, True]) \n
		Defines the lower and upper Δf1 frequency deviation limits for LE coded PHY. The mnemonics DAVerage, DMINimum, DMAXimum
		distinguish average, minimum and maximum frequency deviations. \n
			:param freq_dev_f_1_lower: No help available
			:param freq_dev_f_1_upper: No help available
			:param freq_dev_f_1_enable: Disable or enable limits for current, average, maximum, and minimum results (4 values)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('freq_dev_f_1_lower', freq_dev_f_1_lower, DataType.Float), ArgSingle('freq_dev_f_1_upper', freq_dev_f_1_upper, DataType.Float), ArgSingle('freq_dev_f_1_enable', freq_dev_f_1_enable, DataType.BooleanList, None, False, False, 4))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LRANge:DMAXimum {param}'.rstrip())

	# noinspection PyTypeChecker
	class DmaximumStruct(StructBase):
		"""Response structure. Fields: \n
			- Freq_Dev_F_1_Lower: float: No parameter help available
			- Freq_Dev_F_1_Upper: float: No parameter help available
			- Freq_Dev_F_1_Enable: List[bool]: Disable or enable limits for current, average, maximum, and minimum results (4 values)"""
		__meta_args_list = [
			ArgStruct.scalar_float('Freq_Dev_F_1_Lower'),
			ArgStruct.scalar_float('Freq_Dev_F_1_Upper'),
			ArgStruct('Freq_Dev_F_1_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Dev_F_1_Lower: float = None
			self.Freq_Dev_F_1_Upper: float = None
			self.Freq_Dev_F_1_Enable: List[bool] = None

	def get(self) -> DmaximumStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LRANge:DMAXimum \n
		Snippet: value: DmaximumStruct = driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.lrange.dmaximum.get() \n
		Defines the lower and upper Δf1 frequency deviation limits for LE coded PHY. The mnemonics DAVerage, DMINimum, DMAXimum
		distinguish average, minimum and maximum frequency deviations. \n
			:return: structure: for return value, see the help for DmaximumStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LRANge:DMAXimum?', self.__class__.DmaximumStruct())
