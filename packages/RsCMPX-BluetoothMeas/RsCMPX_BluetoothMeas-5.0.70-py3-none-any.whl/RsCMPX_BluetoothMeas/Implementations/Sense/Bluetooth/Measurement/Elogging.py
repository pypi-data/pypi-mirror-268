from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EloggingCls:
	"""Elogging commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("elogging", core, parent)

	# noinspection PyTypeChecker
	class LastStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Timestamp: str: No parameter help available
			- Category: enums.LogCategory: No parameter help available
			- Event: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Timestamp'),
			ArgStruct.scalar_enum('Category', enums.LogCategory),
			ArgStruct.scalar_str('Event')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamp: str = None
			self.Category: enums.LogCategory = None
			self.Event: str = None

	def get_last(self) -> LastStruct:
		"""SCPI: SENSe:BLUetooth:MEASurement<Instance>:ELOGging:LAST \n
		Snippet: value: LastStruct = driver.sense.bluetooth.measurement.elogging.get_last() \n
		No command help available \n
			:return: structure: for return value, see the help for LastStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:BLUetooth:MEASurement<Instance>:ELOGging:LAST?', self.__class__.LastStruct())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Timestamp: List[str]: No parameter help available
			- Category: List[enums.LogCategory]: No parameter help available
			- Event: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Timestamp', DataType.StringList, None, False, True, 1),
			ArgStruct('Category', DataType.EnumList, enums.LogCategory, False, True, 1),
			ArgStruct('Event', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamp: List[str] = None
			self.Category: List[enums.LogCategory] = None
			self.Event: List[str] = None

	def get_all(self) -> AllStruct:
		"""SCPI: SENSe:BLUetooth:MEASurement<Instance>:ELOGging:ALL \n
		Snippet: value: AllStruct = driver.sense.bluetooth.measurement.elogging.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:BLUetooth:MEASurement<Instance>:ELOGging:ALL?', self.__class__.AllStruct())
