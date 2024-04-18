from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, spot_check: bool, power: bool, modulation: bool, spectrum_acp: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:TRX:RESult[:ALL] \n
		Snippet: driver.configure.bluetooth.measurement.trx.result.all.set(spot_check = False, power = False, modulation = False, spectrum_acp = False) \n
		No command help available \n
			:param spot_check: No help available
			:param power: No help available
			:param modulation: No help available
			:param spectrum_acp: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('spot_check', spot_check, DataType.Boolean), ArgSingle('power', power, DataType.Boolean), ArgSingle('modulation', modulation, DataType.Boolean), ArgSingle('spectrum_acp', spectrum_acp, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:TRX:RESult:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Spot_Check: bool: No parameter help available
			- Power: bool: No parameter help available
			- Modulation: bool: No parameter help available
			- Spectrum_Acp: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Spot_Check'),
			ArgStruct.scalar_bool('Power'),
			ArgStruct.scalar_bool('Modulation'),
			ArgStruct.scalar_bool('Spectrum_Acp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spot_Check: bool = None
			self.Power: bool = None
			self.Modulation: bool = None
			self.Spectrum_Acp: bool = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:TRX:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.bluetooth.measurement.trx.result.all.get() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:TRX:RESult:ALL?', self.__class__.AllStruct())
