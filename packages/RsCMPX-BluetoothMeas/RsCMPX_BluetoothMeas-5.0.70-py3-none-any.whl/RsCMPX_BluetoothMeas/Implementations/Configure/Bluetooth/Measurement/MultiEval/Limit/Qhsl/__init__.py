from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QhslCls:
	"""Qhsl commands group definition. 8 total commands, 7 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qhsl", core, parent)

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	@property
	def p2Q(self):
		"""p2Q commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_p2Q'):
			from .P2Q import P2QCls
			self._p2Q = P2QCls(self._core, self._cmd_group)
		return self._p2Q

	@property
	def p3Q(self):
		"""p3Q commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_p3Q'):
			from .P3Q import P3QCls
			self._p3Q = P3QCls(self._core, self._cmd_group)
		return self._p3Q

	@property
	def p4Q(self):
		"""p4Q commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_p4Q'):
			from .P4Q import P4QCls
			self._p4Q = P4QCls(self._core, self._cmd_group)
		return self._p4Q

	@property
	def p5Q(self):
		"""p5Q commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_p5Q'):
			from .P5Q import P5QCls
			self._p5Q = P5QCls(self._core, self._cmd_group)
		return self._p5Q

	@property
	def p6Q(self):
		"""p6Q commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_p6Q'):
			from .P6Q import P6QCls
			self._p6Q = P6QCls(self._core, self._cmd_group)
		return self._p6Q

	@property
	def sacp(self):
		"""sacp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sacp'):
			from .Sacp import SacpCls
			self._sacp = SacpCls(self._core, self._cmd_group)
		return self._sacp

	# noinspection PyTypeChecker
	class FstabilityStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Wi: float: No parameter help available
			- Wiplus_W_0_Max: float: No parameter help available
			- W_0_Max: float: No parameter help available
			- Wi_Enabled: List[bool]: No parameter help available
			- Wi_W_0_Max_Enabled: List[bool]: No parameter help available
			- W_0_Max_Enabled: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Wi'),
			ArgStruct.scalar_float('Wiplus_W_0_Max'),
			ArgStruct.scalar_float('W_0_Max'),
			ArgStruct('Wi_Enabled', DataType.BooleanList, None, False, False, 3),
			ArgStruct('Wi_W_0_Max_Enabled', DataType.BooleanList, None, False, False, 3),
			ArgStruct('W_0_Max_Enabled', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Wi: float = None
			self.Wiplus_W_0_Max: float = None
			self.W_0_Max: float = None
			self.Wi_Enabled: List[bool] = None
			self.Wi_W_0_Max_Enabled: List[bool] = None
			self.W_0_Max_Enabled: List[bool] = None

	def get_fstability(self) -> FstabilityStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:QHSL:FSTability \n
		Snippet: value: FstabilityStruct = driver.configure.bluetooth.measurement.multiEval.limit.qhsl.get_fstability() \n
		No command help available \n
			:return: structure: for return value, see the help for FstabilityStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:QHSL:FSTability?', self.__class__.FstabilityStruct())

	def set_fstability(self, value: FstabilityStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:QHSL:FSTability \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.limit.qhsl.FstabilityStruct() \n
		structure.Wi: float = 1.0 \n
		structure.Wiplus_W_0_Max: float = 1.0 \n
		structure.W_0_Max: float = 1.0 \n
		structure.Wi_Enabled: List[bool] = [True, False, True] \n
		structure.Wi_W_0_Max_Enabled: List[bool] = [True, False, True] \n
		structure.W_0_Max_Enabled: List[bool] = [True, False, True] \n
		driver.configure.bluetooth.measurement.multiEval.limit.qhsl.set_fstability(value = structure) \n
		No command help available \n
			:param value: see the help for FstabilityStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:QHSL:FSTability', value)

	def clone(self) -> 'QhslCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = QhslCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
