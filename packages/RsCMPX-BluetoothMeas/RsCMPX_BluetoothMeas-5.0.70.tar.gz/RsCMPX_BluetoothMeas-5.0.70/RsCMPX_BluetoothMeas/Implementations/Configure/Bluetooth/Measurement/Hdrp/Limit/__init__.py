from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 6 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	@property
	def p4Hp(self):
		"""p4Hp commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_p4Hp'):
			from .P4Hp import P4HpCls
			self._p4Hp = P4HpCls(self._core, self._cmd_group)
		return self._p4Hp

	@property
	def p8Hp(self):
		"""p8Hp commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_p8Hp'):
			from .P8Hp import P8HpCls
			self._p8Hp = P8HpCls(self._core, self._cmd_group)
		return self._p8Hp

	# noinspection PyTypeChecker
	class FstabilityStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Wi: float: No parameter help available
			- Wi_W_0: float: No parameter help available
			- W_0_Max: float: No parameter help available
			- Wi_Enabled: List[bool]: No parameter help available
			- Wi_Wo_Enabled: List[bool]: No parameter help available
			- W_0_Max_Enabled: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Wi'),
			ArgStruct.scalar_float('Wi_W_0'),
			ArgStruct.scalar_float('W_0_Max'),
			ArgStruct('Wi_Enabled', DataType.BooleanList, None, False, False, 3),
			ArgStruct('Wi_Wo_Enabled', DataType.BooleanList, None, False, False, 3),
			ArgStruct('W_0_Max_Enabled', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Wi: float = None
			self.Wi_W_0: float = None
			self.W_0_Max: float = None
			self.Wi_Enabled: List[bool] = None
			self.Wi_Wo_Enabled: List[bool] = None
			self.W_0_Max_Enabled: List[bool] = None

	def get_fstability(self) -> FstabilityStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:FSTability \n
		Snippet: value: FstabilityStruct = driver.configure.bluetooth.measurement.hdrp.limit.get_fstability() \n
		No command help available \n
			:return: structure: for return value, see the help for FstabilityStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:FSTability?', self.__class__.FstabilityStruct())

	def set_fstability(self, value: FstabilityStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:FSTability \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.hdrp.limit.FstabilityStruct() \n
		structure.Wi: float = 1.0 \n
		structure.Wi_W_0: float = 1.0 \n
		structure.W_0_Max: float = 1.0 \n
		structure.Wi_Enabled: List[bool] = [True, False, True] \n
		structure.Wi_Wo_Enabled: List[bool] = [True, False, True] \n
		structure.W_0_Max_Enabled: List[bool] = [True, False, True] \n
		driver.configure.bluetooth.measurement.hdrp.limit.set_fstability(value = structure) \n
		No command help available \n
			:param value: see the help for FstabilityStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:FSTability', value)

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
