from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdeviationCls:
	"""Pdeviation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdeviation", core, parent)

	def set(self, ref_dev: float, tx_dev: float, ref_dev_enable: bool, tx_dev_enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:CTE:LENergy:LE2M:PDEViation \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.cte.lowEnergy.le2M.pdeviation.set(ref_dev = 1.0, tx_dev = 1.0, ref_dev_enable = False, tx_dev_enable = False) \n
		Defines the upper CTE power limits and enables/disables the limit check. Commands for uncoded LE 1M PHY (..:LE1M..) and
		LE 2M PHY (..:LE2M..) are available. \n
			:param ref_dev: Upper CTE power limit for reference antenna.
			:param tx_dev: Upper limit for power deviation in a slot.
			:param ref_dev_enable: Enables/disables the CTE power limit check for reference antenna.
			:param tx_dev_enable: Enables/disables the limit check for power deviation in a slot.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ref_dev', ref_dev, DataType.Float), ArgSingle('tx_dev', tx_dev, DataType.Float), ArgSingle('ref_dev_enable', ref_dev_enable, DataType.Boolean), ArgSingle('tx_dev_enable', tx_dev_enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:CTE:LENergy:LE2M:PDEViation {param}'.rstrip())

	# noinspection PyTypeChecker
	class PdeviationStruct(StructBase):
		"""Response structure. Fields: \n
			- Ref_Dev: float: Upper CTE power limit for reference antenna.
			- Tx_Dev: float: Upper limit for power deviation in a slot.
			- Ref_Dev_Enable: bool: Enables/disables the CTE power limit check for reference antenna.
			- Tx_Dev_Enable: bool: Enables/disables the limit check for power deviation in a slot."""
		__meta_args_list = [
			ArgStruct.scalar_float('Ref_Dev'),
			ArgStruct.scalar_float('Tx_Dev'),
			ArgStruct.scalar_bool('Ref_Dev_Enable'),
			ArgStruct.scalar_bool('Tx_Dev_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ref_Dev: float = None
			self.Tx_Dev: float = None
			self.Ref_Dev_Enable: bool = None
			self.Tx_Dev_Enable: bool = None

	def get(self) -> PdeviationStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:CTE:LENergy:LE2M:PDEViation \n
		Snippet: value: PdeviationStruct = driver.configure.bluetooth.measurement.multiEval.limit.cte.lowEnergy.le2M.pdeviation.get() \n
		Defines the upper CTE power limits and enables/disables the limit check. Commands for uncoded LE 1M PHY (..:LE1M..) and
		LE 2M PHY (..:LE2M..) are available. \n
			:return: structure: for return value, see the help for PdeviationStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:CTE:LENergy:LE2M:PDEViation?', self.__class__.PdeviationStruct())
