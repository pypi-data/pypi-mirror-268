from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PencodingCls:
	"""Pencoding commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pencoding", core, parent)

	@property
	def ssequence(self):
		"""ssequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssequence'):
			from .Ssequence import SsequenceCls
			self._ssequence = SsequenceCls(self._core, self._cmd_group)
		return self._ssequence

	def set(self, phase_encoding: float, phase_encod_enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:EDRate:PENCoding \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.edrate.pencoding.set(phase_encoding = 1.0, phase_encod_enable = False) \n
		No command help available \n
			:param phase_encoding: No help available
			:param phase_encod_enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('phase_encoding', phase_encoding, DataType.Float), ArgSingle('phase_encod_enable', phase_encod_enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:EDRate:PENCoding {param}'.rstrip())

	# noinspection PyTypeChecker
	class PencodingStruct(StructBase):
		"""Response structure. Fields: \n
			- Phase_Encoding: float: No parameter help available
			- Phase_Encod_Enable: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Phase_Encoding'),
			ArgStruct.scalar_bool('Phase_Encod_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Phase_Encoding: float = None
			self.Phase_Encod_Enable: bool = None

	def get(self) -> PencodingStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:EDRate:PENCoding \n
		Snippet: value: PencodingStruct = driver.configure.bluetooth.measurement.multiEval.limit.edrate.pencoding.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PencodingStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:EDRate:PENCoding?', self.__class__.PencodingStruct())

	def clone(self) -> 'PencodingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PencodingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
