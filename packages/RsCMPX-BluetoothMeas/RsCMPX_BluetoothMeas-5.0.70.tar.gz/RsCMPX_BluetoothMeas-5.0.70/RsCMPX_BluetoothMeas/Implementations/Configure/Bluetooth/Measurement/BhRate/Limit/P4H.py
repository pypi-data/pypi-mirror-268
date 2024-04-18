from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class P4HCls:
	"""P4H commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("p4H", core, parent)

	# noinspection PyTypeChecker
	class DevmStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
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

	def get_devm(self) -> DevmStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:P4H:DEVM \n
		Snippet: value: DevmStruct = driver.configure.bluetooth.measurement.bhRate.limit.p4H.get_devm() \n
		No command help available \n
			:return: structure: for return value, see the help for DevmStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:P4H:DEVM?', self.__class__.DevmStruct())

	def set_devm(self, value: DevmStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:P4H:DEVM \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.bhRate.limit.p4H.DevmStruct() \n
		structure.Rms: float = 1.0 \n
		structure.Peak: float = 1.0 \n
		structure.P_99: float = 1.0 \n
		structure.Rms_Enabled: List[bool] = [True, False, True] \n
		structure.Peak_Enabled: List[bool] = [True, False, True] \n
		structure.P_99_Enabled: bool = False \n
		driver.configure.bluetooth.measurement.bhRate.limit.p4H.set_devm(value = structure) \n
		No command help available \n
			:param value: see the help for DevmStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:P4H:DEVM', value)

	# noinspection PyTypeChecker
	class SgacpStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Ptx_Rel_Limit: float: No parameter help available
			- Ptx_Abs_Limit_1: float: No parameter help available
			- Ptx_Abs_Limit_2: float: No parameter help available
			- Ptx_Rel_Enable: bool: No parameter help available
			- Ptx_Abs_1_Enable: bool: No parameter help available
			- Ptx_Abs_2_Enable: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ptx_Rel_Limit'),
			ArgStruct.scalar_float('Ptx_Abs_Limit_1'),
			ArgStruct.scalar_float('Ptx_Abs_Limit_2'),
			ArgStruct.scalar_bool('Ptx_Rel_Enable'),
			ArgStruct.scalar_bool('Ptx_Abs_1_Enable'),
			ArgStruct.scalar_bool('Ptx_Abs_2_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ptx_Rel_Limit: float = None
			self.Ptx_Abs_Limit_1: float = None
			self.Ptx_Abs_Limit_2: float = None
			self.Ptx_Rel_Enable: bool = None
			self.Ptx_Abs_1_Enable: bool = None
			self.Ptx_Abs_2_Enable: bool = None

	def get_sgacp(self) -> SgacpStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:P4H:SGACp \n
		Snippet: value: SgacpStruct = driver.configure.bluetooth.measurement.bhRate.limit.p4H.get_sgacp() \n
		No command help available \n
			:return: structure: for return value, see the help for SgacpStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:P4H:SGACp?', self.__class__.SgacpStruct())

	def set_sgacp(self, value: SgacpStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:P4H:SGACp \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.bhRate.limit.p4H.SgacpStruct() \n
		structure.Ptx_Rel_Limit: float = 1.0 \n
		structure.Ptx_Abs_Limit_1: float = 1.0 \n
		structure.Ptx_Abs_Limit_2: float = 1.0 \n
		structure.Ptx_Rel_Enable: bool = False \n
		structure.Ptx_Abs_1_Enable: bool = False \n
		structure.Ptx_Abs_2_Enable: bool = False \n
		driver.configure.bluetooth.measurement.bhRate.limit.p4H.set_sgacp(value = structure) \n
		No command help available \n
			:param value: see the help for SgacpStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:LIMit:P4H:SGACp', value)
