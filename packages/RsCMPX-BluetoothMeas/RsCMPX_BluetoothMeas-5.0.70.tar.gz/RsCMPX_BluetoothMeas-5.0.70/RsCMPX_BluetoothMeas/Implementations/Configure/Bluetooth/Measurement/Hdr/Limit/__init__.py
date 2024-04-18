from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 7 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def pencoding(self):
		"""pencoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pencoding'):
			from .Pencoding import PencodingCls
			self._pencoding = PencodingCls(self._core, self._cmd_group)
		return self._pencoding

	@property
	def p4H(self):
		"""p4H commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_p4H'):
			from .P4H import P4HCls
			self._p4H = P4HCls(self._core, self._cmd_group)
		return self._p4H

	@property
	def p8H(self):
		"""p8H commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_p8H'):
			from .P8H import P8HCls
			self._p8H = P8HCls(self._core, self._cmd_group)
		return self._p8H

	# noinspection PyTypeChecker
	class PowerVsTimeStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Dpsk_Minus_Gfsk_Low: float: No parameter help available
			- Dpsk_Minus_Gfsk_Upp: float: No parameter help available
			- Guard_Period_Low: float: No parameter help available
			- Guard_Period_Upp: float: No parameter help available
			- Dpsk_Minus_Gfsk_Enable: List[bool]: No parameter help available
			- Guard_Period_Enable: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Dpsk_Minus_Gfsk_Low'),
			ArgStruct.scalar_float('Dpsk_Minus_Gfsk_Upp'),
			ArgStruct.scalar_float('Guard_Period_Low'),
			ArgStruct.scalar_float('Guard_Period_Upp'),
			ArgStruct('Dpsk_Minus_Gfsk_Enable', DataType.BooleanList, None, False, False, 4),
			ArgStruct('Guard_Period_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dpsk_Minus_Gfsk_Low: float = None
			self.Dpsk_Minus_Gfsk_Upp: float = None
			self.Guard_Period_Low: float = None
			self.Guard_Period_Upp: float = None
			self.Dpsk_Minus_Gfsk_Enable: List[bool] = None
			self.Guard_Period_Enable: List[bool] = None

	def get_power_vs_time(self) -> PowerVsTimeStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:PVTime \n
		Snippet: value: PowerVsTimeStruct = driver.configure.bluetooth.measurement.hdr.limit.get_power_vs_time() \n
		No command help available \n
			:return: structure: for return value, see the help for PowerVsTimeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:PVTime?', self.__class__.PowerVsTimeStruct())

	def set_power_vs_time(self, value: PowerVsTimeStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:PVTime \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.hdr.limit.PowerVsTimeStruct() \n
		structure.Dpsk_Minus_Gfsk_Low: float = 1.0 \n
		structure.Dpsk_Minus_Gfsk_Upp: float = 1.0 \n
		structure.Guard_Period_Low: float = 1.0 \n
		structure.Guard_Period_Upp: float = 1.0 \n
		structure.Dpsk_Minus_Gfsk_Enable: List[bool] = [True, False, True] \n
		structure.Guard_Period_Enable: List[bool] = [True, False, True] \n
		driver.configure.bluetooth.measurement.hdr.limit.set_power_vs_time(value = structure) \n
		No command help available \n
			:param value: see the help for PowerVsTimeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:PVTime', value)

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
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:FSTability \n
		Snippet: value: FstabilityStruct = driver.configure.bluetooth.measurement.hdr.limit.get_fstability() \n
		No command help available \n
			:return: structure: for return value, see the help for FstabilityStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:FSTability?', self.__class__.FstabilityStruct())

	def set_fstability(self, value: FstabilityStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:FSTability \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.hdr.limit.FstabilityStruct() \n
		structure.Wi: float = 1.0 \n
		structure.Wi_W_0: float = 1.0 \n
		structure.W_0_Max: float = 1.0 \n
		structure.Wi_Enabled: List[bool] = [True, False, True] \n
		structure.Wi_Wo_Enabled: List[bool] = [True, False, True] \n
		structure.W_0_Max_Enabled: List[bool] = [True, False, True] \n
		driver.configure.bluetooth.measurement.hdr.limit.set_fstability(value = structure) \n
		No command help available \n
			:param value: see the help for FstabilityStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:FSTability', value)

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
