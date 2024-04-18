from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PencodingCls:
	"""Pencoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pencoding", core, parent)

	def set(self, phase_limit: float, phase_enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:PENCoding \n
		Snippet: driver.configure.bluetooth.measurement.hdr.limit.pencoding.set(phase_limit = 1.0, phase_enable = False) \n
		No command help available \n
			:param phase_limit: No help available
			:param phase_enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('phase_limit', phase_limit, DataType.Float), ArgSingle('phase_enable', phase_enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:PENCoding {param}'.rstrip())

	# noinspection PyTypeChecker
	class PencodingStruct(StructBase):
		"""Response structure. Fields: \n
			- Phase_Limit: float: No parameter help available
			- Phase_Enable: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Phase_Limit'),
			ArgStruct.scalar_bool('Phase_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Phase_Limit: float = None
			self.Phase_Enable: bool = None

	def get(self) -> PencodingStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:PENCoding \n
		Snippet: value: PencodingStruct = driver.configure.bluetooth.measurement.hdr.limit.pencoding.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PencodingStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:LIMit:PENCoding?', self.__class__.PencodingStruct())
