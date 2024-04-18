from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvMagnitudeCls:
	"""EvMagnitude commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evMagnitude", core, parent)

	# noinspection PyTypeChecker
	class OffsetStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Rms: float: No parameter help available
			- Peak: float: No parameter help available
			- P_99: float: No parameter help available
			- Rms_Enabled: List[bool]: No parameter help available
			- Peak_Enabled: List[bool]: No parameter help available
			- P_99_Enabled: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Rms'),
			ArgStruct.scalar_float('Peak'),
			ArgStruct.scalar_float('P_99'),
			ArgStruct('Rms_Enabled', DataType.BooleanList, None, False, False, 3),
			ArgStruct('Peak_Enabled', DataType.BooleanList, None, False, False, 3),
			ArgStruct.scalar_bool('P_99_Enabled')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float = None
			self.Peak: float = None
			self.P_99: float = None
			self.Rms_Enabled: List[bool] = None
			self.Peak_Enabled: List[bool] = None
			self.P_99_Enabled: bool = None

	def get_offset(self) -> OffsetStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:P8HP:EVMagnitude:OFFSet \n
		Snippet: value: OffsetStruct = driver.configure.bluetooth.measurement.hdrp.limit.p8Hp.evMagnitude.get_offset() \n
		No command help available \n
			:return: structure: for return value, see the help for OffsetStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:P8HP:EVMagnitude:OFFSet?', self.__class__.OffsetStruct())

	def set_offset(self, value: OffsetStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:P8HP:EVMagnitude:OFFSet \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.hdrp.limit.p8Hp.evMagnitude.OffsetStruct() \n
		structure.Rms: float = 1.0 \n
		structure.Peak: float = 1.0 \n
		structure.P_99: float = 1.0 \n
		structure.Rms_Enabled: List[bool] = [True, False, True] \n
		structure.Peak_Enabled: List[bool] = [True, False, True] \n
		structure.P_99_Enabled: bool = False \n
		driver.configure.bluetooth.measurement.hdrp.limit.p8Hp.evMagnitude.set_offset(value = structure) \n
		No command help available \n
			:param value: see the help for OffsetStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:LIMit:P8HP:EVMagnitude:OFFSet', value)
