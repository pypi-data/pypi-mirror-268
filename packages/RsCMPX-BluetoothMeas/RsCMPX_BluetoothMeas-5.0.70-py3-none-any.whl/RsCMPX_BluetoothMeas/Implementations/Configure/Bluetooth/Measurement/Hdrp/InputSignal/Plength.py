from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlengthCls:
	"""Plength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	def set(self, payload_len_four: List[int], payload_len_eight: List[int]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PLENgth \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.inputSignal.plength.set(payload_len_four = [1, 2, 3], payload_len_eight = [1, 2, 3]) \n
		No command help available \n
			:param payload_len_four: No help available
			:param payload_len_eight: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('payload_len_four', payload_len_four, DataType.IntegerList, None, False, False, 3), ArgSingle('payload_len_eight', payload_len_eight, DataType.IntegerList, None, False, False, 3))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PLENgth {param}'.rstrip())

	# noinspection PyTypeChecker
	class PlengthStruct(StructBase):
		"""Response structure. Fields: \n
			- Payload_Len_Four: List[int]: No parameter help available
			- Payload_Len_Eight: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Payload_Len_Four', DataType.IntegerList, None, False, False, 3),
			ArgStruct('Payload_Len_Eight', DataType.IntegerList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Payload_Len_Four: List[int] = None
			self.Payload_Len_Eight: List[int] = None

	def get(self) -> PlengthStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PLENgth \n
		Snippet: value: PlengthStruct = driver.configure.bluetooth.measurement.hdrp.inputSignal.plength.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PlengthStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PLENgth?', self.__class__.PlengthStruct())
