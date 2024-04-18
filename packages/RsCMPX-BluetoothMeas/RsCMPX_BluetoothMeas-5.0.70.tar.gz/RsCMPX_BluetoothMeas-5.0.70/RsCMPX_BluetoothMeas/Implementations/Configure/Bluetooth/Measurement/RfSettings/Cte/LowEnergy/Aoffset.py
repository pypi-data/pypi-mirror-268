from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AoffsetCls:
	"""Aoffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aoffset", core, parent)

	def set(self, ant_ref_1: float, ant_ref_2: float, ant_ref_3: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:AOFFset \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.cte.lowEnergy.aoffset.set(ant_ref_1 = 1.0, ant_ref_2 = 1.0, ant_ref_3 = 1.0) \n
		No command help available \n
			:param ant_ref_1: No help available
			:param ant_ref_2: No help available
			:param ant_ref_3: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ant_ref_1', ant_ref_1, DataType.Float), ArgSingle('ant_ref_2', ant_ref_2, DataType.Float), ArgSingle('ant_ref_3', ant_ref_3, DataType.Float))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:AOFFset {param}'.rstrip())

	# noinspection PyTypeChecker
	class AoffsetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ant_Ref_1: float: No parameter help available
			- Ant_Ref_2: float: No parameter help available
			- Ant_Ref_3: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ant_Ref_1'),
			ArgStruct.scalar_float('Ant_Ref_2'),
			ArgStruct.scalar_float('Ant_Ref_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ant_Ref_1: float = None
			self.Ant_Ref_2: float = None
			self.Ant_Ref_3: float = None

	def get(self) -> AoffsetStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:AOFFset \n
		Snippet: value: AoffsetStruct = driver.configure.bluetooth.measurement.rfSettings.cte.lowEnergy.aoffset.get() \n
		No command help available \n
			:return: structure: for return value, see the help for AoffsetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:AOFFset?', self.__class__.AoffsetStruct())
