from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FoffsetCls:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, freq_offset: float, freq_offset_enable: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:CTE:LENergy:LE2M:FOFFset \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.cte.lowEnergy.le2M.foffset.set(freq_offset = 1.0, freq_offset_enable = [True, False, True]) \n
		Sets/gets the frequency offset limit for the CTE portion. Commands for uncoded LE 1M PHY (..:LE1M..) and LE 2M PHY (..
		:LE2M..) are available. \n
			:param freq_offset: No help available
			:param freq_offset_enable: Disable or enable limit checking for current, average, and maximum results (3 values)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('freq_offset', freq_offset, DataType.Float), ArgSingle('freq_offset_enable', freq_offset_enable, DataType.BooleanList, None, False, False, 3))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:CTE:LENergy:LE2M:FOFFset {param}'.rstrip())

	# noinspection PyTypeChecker
	class FoffsetStruct(StructBase):
		"""Response structure. Fields: \n
			- Freq_Offset: float: No parameter help available
			- Freq_Offset_Enable: List[bool]: Disable or enable limit checking for current, average, and maximum results (3 values)"""
		__meta_args_list = [
			ArgStruct.scalar_float('Freq_Offset'),
			ArgStruct('Freq_Offset_Enable', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Offset: float = None
			self.Freq_Offset_Enable: List[bool] = None

	def get(self) -> FoffsetStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:CTE:LENergy:LE2M:FOFFset \n
		Snippet: value: FoffsetStruct = driver.configure.bluetooth.measurement.multiEval.limit.cte.lowEnergy.le2M.foffset.get() \n
		Sets/gets the frequency offset limit for the CTE portion. Commands for uncoded LE 1M PHY (..:LE1M..) and LE 2M PHY (..
		:LE2M..) are available. \n
			:return: structure: for return value, see the help for FoffsetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:CTE:LENergy:LE2M:FOFFset?', self.__class__.FoffsetStruct())
