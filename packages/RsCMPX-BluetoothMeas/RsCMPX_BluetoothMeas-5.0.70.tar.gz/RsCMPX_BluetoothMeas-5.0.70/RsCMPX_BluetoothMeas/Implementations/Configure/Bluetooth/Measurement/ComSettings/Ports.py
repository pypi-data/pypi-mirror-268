from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PortsCls:
	"""Ports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ports", core, parent)

	# noinspection PyTypeChecker
	class CatalogStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- No_Devices: int: No parameter help available
			- Item_Number: List[int]: No parameter help available
			- Discovered_Port: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('No_Devices'),
			ArgStruct('Item_Number', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Discovered_Port', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.No_Devices: int = None
			self.Item_Number: List[int] = None
			self.Discovered_Port: List[str] = None

	def get_catalog(self) -> CatalogStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PORTs:CATalog \n
		Snippet: value: CatalogStruct = driver.configure.bluetooth.measurement.comSettings.ports.get_catalog() \n
		No command help available \n
			:return: structure: for return value, see the help for CatalogStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PORTs:CATalog?', self.__class__.CatalogStruct())
