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

	def set(self, evm: bool, tx_scalars: bool, iq_constellation: bool, power_vs_time: bool, spectrum_acp: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult[:ALL] \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.result.all.set(evm = False, tx_scalars = False, iq_constellation = False, power_vs_time = False, spectrum_acp = False) \n
		No command help available \n
			:param evm: No help available
			:param tx_scalars: No help available
			:param iq_constellation: No help available
			:param power_vs_time: No help available
			:param spectrum_acp: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('evm', evm, DataType.Boolean), ArgSingle('tx_scalars', tx_scalars, DataType.Boolean), ArgSingle('iq_constellation', iq_constellation, DataType.Boolean), ArgSingle('power_vs_time', power_vs_time, DataType.Boolean), ArgSingle('spectrum_acp', spectrum_acp, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Evm: bool: No parameter help available
			- Tx_Scalars: bool: No parameter help available
			- Iq_Constellation: bool: No parameter help available
			- Power_Vs_Time: bool: No parameter help available
			- Spectrum_Acp: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Evm'),
			ArgStruct.scalar_bool('Tx_Scalars'),
			ArgStruct.scalar_bool('Iq_Constellation'),
			ArgStruct.scalar_bool('Power_Vs_Time'),
			ArgStruct.scalar_bool('Spectrum_Acp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm: bool = None
			self.Tx_Scalars: bool = None
			self.Iq_Constellation: bool = None
			self.Power_Vs_Time: bool = None
			self.Spectrum_Acp: bool = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.bluetooth.measurement.hdrp.result.all.get() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:ALL?', self.__class__.AllStruct())
