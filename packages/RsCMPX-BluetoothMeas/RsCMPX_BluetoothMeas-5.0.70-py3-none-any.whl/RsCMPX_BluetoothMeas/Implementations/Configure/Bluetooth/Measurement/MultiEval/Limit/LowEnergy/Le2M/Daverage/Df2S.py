from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Df2SCls:
	"""Df2S commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("df2S", core, parent)

	def set(self, freq_dev_f_2_lower: float, freq_dev_f_2_upper: float, freq_dev_f_2_enable: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:DAVerage:DF2S \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.le2M.daverage.df2S.set(freq_dev_f_2_lower = 1.0, freq_dev_f_2_upper = 1.0, freq_dev_f_2_enable = [True, False, True]) \n
		Defines the lower and upper Δf2 frequency deviation limits for LE 2M PHY. The mnemonics DAVerage, DMINimum, DMAXimum
		distinguish average, minimum and maximum frequency deviations. \n
			:param freq_dev_f_2_lower: No help available
			:param freq_dev_f_2_upper: No help available
			:param freq_dev_f_2_enable: Disable or enable limits for current, average, maximum, and minimum results (4 values)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('freq_dev_f_2_lower', freq_dev_f_2_lower, DataType.Float), ArgSingle('freq_dev_f_2_upper', freq_dev_f_2_upper, DataType.Float), ArgSingle('freq_dev_f_2_enable', freq_dev_f_2_enable, DataType.BooleanList, None, False, False, 4))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:DAVerage:DF2S {param}'.rstrip())

	# noinspection PyTypeChecker
	class Df2SStruct(StructBase):
		"""Response structure. Fields: \n
			- Freq_Dev_F_2_Lower: float: No parameter help available
			- Freq_Dev_F_2_Upper: float: No parameter help available
			- Freq_Dev_F_2_Enable: List[bool]: Disable or enable limits for current, average, maximum, and minimum results (4 values)"""
		__meta_args_list = [
			ArgStruct.scalar_float('Freq_Dev_F_2_Lower'),
			ArgStruct.scalar_float('Freq_Dev_F_2_Upper'),
			ArgStruct('Freq_Dev_F_2_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Dev_F_2_Lower: float = None
			self.Freq_Dev_F_2_Upper: float = None
			self.Freq_Dev_F_2_Enable: List[bool] = None

	def get(self) -> Df2SStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:DAVerage:DF2S \n
		Snippet: value: Df2SStruct = driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.le2M.daverage.df2S.get() \n
		Defines the lower and upper Δf2 frequency deviation limits for LE 2M PHY. The mnemonics DAVerage, DMINimum, DMAXimum
		distinguish average, minimum and maximum frequency deviations. \n
			:return: structure: for return value, see the help for Df2SStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:DAVerage:DF2S?', self.__class__.Df2SStruct())
