from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsequenceCls:
	"""Ssequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssequence", core, parent)

	def set(self, sync_bit_errors: int, trailer_bit_errs: int, sync_bit_enable: bool, trailer_bit_enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:EDRate:PENCoding:SSEQuence \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.edrate.pencoding.ssequence.set(sync_bit_errors = 1, trailer_bit_errs = 1, sync_bit_enable = False, trailer_bit_enable = False) \n
		No command help available \n
			:param sync_bit_errors: No help available
			:param trailer_bit_errs: No help available
			:param sync_bit_enable: No help available
			:param trailer_bit_enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sync_bit_errors', sync_bit_errors, DataType.Integer), ArgSingle('trailer_bit_errs', trailer_bit_errs, DataType.Integer), ArgSingle('sync_bit_enable', sync_bit_enable, DataType.Boolean), ArgSingle('trailer_bit_enable', trailer_bit_enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:EDRate:PENCoding:SSEQuence {param}'.rstrip())

	# noinspection PyTypeChecker
	class SsequenceStruct(StructBase):
		"""Response structure. Fields: \n
			- Sync_Bit_Errors: int: No parameter help available
			- Trailer_Bit_Errs: int: No parameter help available
			- Sync_Bit_Enable: bool: No parameter help available
			- Trailer_Bit_Enable: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Sync_Bit_Errors'),
			ArgStruct.scalar_int('Trailer_Bit_Errs'),
			ArgStruct.scalar_bool('Sync_Bit_Enable'),
			ArgStruct.scalar_bool('Trailer_Bit_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sync_Bit_Errors: int = None
			self.Trailer_Bit_Errs: int = None
			self.Sync_Bit_Enable: bool = None
			self.Trailer_Bit_Enable: bool = None

	def get(self) -> SsequenceStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:EDRate:PENCoding:SSEQuence \n
		Snippet: value: SsequenceStruct = driver.configure.bluetooth.measurement.multiEval.limit.edrate.pencoding.ssequence.get() \n
		No command help available \n
			:return: structure: for return value, see the help for SsequenceStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:EDRate:PENCoding:SSEQuence?', self.__class__.SsequenceStruct())
