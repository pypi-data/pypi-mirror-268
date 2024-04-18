from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class P8HpCls:
	"""P8Hp commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("p8Hp", core, parent)

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .EvMagnitude import EvMagnitudeCls
			self._evMagnitude = EvMagnitudeCls(self._core, self._cmd_group)
		return self._evMagnitude

	# noinspection PyTypeChecker
	class SacpStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Ptx_Rel_Limit: float: No parameter help available
			- Ptx_Abs_Limit_1: float: No parameter help available
			- Ptx_Abs_Limit_2: float: No parameter help available
			- Ptx_Abs_Limit_3: float: No parameter help available
			- Ptx_Rel_Enabled: bool: No parameter help available
			- Ptx_Abs_1_Enable: bool: No parameter help available
			- Ptx_Abs_2_Enable: bool: No parameter help available
			- Ptx_Abs_3_Enable: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ptx_Rel_Limit'),
			ArgStruct.scalar_float('Ptx_Abs_Limit_1'),
			ArgStruct.scalar_float('Ptx_Abs_Limit_2'),
			ArgStruct.scalar_float('Ptx_Abs_Limit_3'),
			ArgStruct.scalar_bool('Ptx_Rel_Enabled'),
			ArgStruct.scalar_bool('Ptx_Abs_1_Enable'),
			ArgStruct.scalar_bool('Ptx_Abs_2_Enable'),
			ArgStruct.scalar_bool('Ptx_Abs_3_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ptx_Rel_Limit: float = None
			self.Ptx_Abs_Limit_1: float = None
			self.Ptx_Abs_Limit_2: float = None
			self.Ptx_Abs_Limit_3: float = None
			self.Ptx_Rel_Enabled: bool = None
			self.Ptx_Abs_1_Enable: bool = None
			self.Ptx_Abs_2_Enable: bool = None
			self.Ptx_Abs_3_Enable: bool = None

	def get_sacp(self) -> SacpStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:P8HP:SACP \n
		Snippet: value: SacpStruct = driver.configure.bluetooth.measurement.hdrp.limit.p8Hp.get_sacp() \n
		No command help available \n
			:return: structure: for return value, see the help for SacpStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:P8HP:SACP?', self.__class__.SacpStruct())

	def set_sacp(self, value: SacpStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:P8HP:SACP \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.hdrp.limit.p8Hp.SacpStruct() \n
		structure.Ptx_Rel_Limit: float = 1.0 \n
		structure.Ptx_Abs_Limit_1: float = 1.0 \n
		structure.Ptx_Abs_Limit_2: float = 1.0 \n
		structure.Ptx_Abs_Limit_3: float = 1.0 \n
		structure.Ptx_Rel_Enabled: bool = False \n
		structure.Ptx_Abs_1_Enable: bool = False \n
		structure.Ptx_Abs_2_Enable: bool = False \n
		structure.Ptx_Abs_3_Enable: bool = False \n
		driver.configure.bluetooth.measurement.hdrp.limit.p8Hp.set_sacp(value = structure) \n
		No command help available \n
			:param value: see the help for SacpStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:P8HP:SACP', value)

	def clone(self) -> 'P8HpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = P8HpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
