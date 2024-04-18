from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 10 total commands, 0 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Devm: bool: No parameter help available
			- Phase_Diff: bool: No parameter help available
			- Tx_Scalars: bool: No parameter help available
			- Iq_Absolute: bool: No parameter help available
			- Iq_Differential: bool: No parameter help available
			- Iq_Error: bool: No parameter help available
			- Phase_Encoding: bool: No parameter help available
			- Power_Vs_Time: bool: No parameter help available
			- Spectrum_Gat_Acp: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Devm'),
			ArgStruct.scalar_bool('Phase_Diff'),
			ArgStruct.scalar_bool('Tx_Scalars'),
			ArgStruct.scalar_bool('Iq_Absolute'),
			ArgStruct.scalar_bool('Iq_Differential'),
			ArgStruct.scalar_bool('Iq_Error'),
			ArgStruct.scalar_bool('Phase_Encoding'),
			ArgStruct.scalar_bool('Power_Vs_Time'),
			ArgStruct.scalar_bool('Spectrum_Gat_Acp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Devm: bool = None
			self.Phase_Diff: bool = None
			self.Tx_Scalars: bool = None
			self.Iq_Absolute: bool = None
			self.Iq_Differential: bool = None
			self.Iq_Error: bool = None
			self.Phase_Encoding: bool = None
			self.Power_Vs_Time: bool = None
			self.Spectrum_Gat_Acp: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.bluetooth.measurement.bhRate.result.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult[:ALL] \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.bhRate.result.AllStruct() \n
		structure.Devm: bool = False \n
		structure.Phase_Diff: bool = False \n
		structure.Tx_Scalars: bool = False \n
		structure.Iq_Absolute: bool = False \n
		structure.Iq_Differential: bool = False \n
		structure.Iq_Error: bool = False \n
		structure.Phase_Encoding: bool = False \n
		structure.Power_Vs_Time: bool = False \n
		structure.Spectrum_Gat_Acp: bool = False \n
		driver.configure.bluetooth.measurement.bhRate.result.set_all(value = structure) \n
		No command help available \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:ALL', value)

	def get_power_vs_time(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PVTime \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_power_vs_time() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PVTime?')
		return Conversions.str_to_bool(response)

	def set_power_vs_time(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_power_vs_time(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PVTime {param}')

	def get_sgacp(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:SGACp \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_sgacp() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:SGACp?')
		return Conversions.str_to_bool(response)

	def set_sgacp(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:SGACp \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_sgacp(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:SGACp {param}')

	def get_pencoding(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PENCoding \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_pencoding() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PENCoding?')
		return Conversions.str_to_bool(response)

	def set_pencoding(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PENCoding \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_pencoding(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PENCoding {param}')

	def get_iq_error(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQERr \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_iq_error() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQERr?')
		return Conversions.str_to_bool(response)

	def set_iq_error(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQERr \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_iq_error(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQERr {param}')

	def get_iq_difference(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQDiff \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_iq_difference() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQDiff?')
		return Conversions.str_to_bool(response)

	def set_iq_difference(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQDiff \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_iq_difference(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQDiff {param}')

	def get_iq_absolute(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQABsolute \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_iq_absolute() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQABsolute?')
		return Conversions.str_to_bool(response)

	def set_iq_absolute(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQABsolute \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_iq_absolute(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:IQABsolute {param}')

	def get_pdifference(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PDIFference \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_pdifference() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PDIFference?')
		return Conversions.str_to_bool(response)

	def set_pdifference(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PDIFference \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_pdifference(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:PDIFference {param}')

	def get_dev_magnitude(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:DEVMagnitude \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_dev_magnitude() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:DEVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_dev_magnitude(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:DEVMagnitude \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_dev_magnitude(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:DEVMagnitude {param}')

	def get_tx_scalar(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:TXSCalar \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.bhRate.result.get_tx_scalar() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:TXSCalar?')
		return Conversions.str_to_bool(response)

	def set_tx_scalar(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:TXSCalar \n
		Snippet: driver.configure.bluetooth.measurement.bhRate.result.set_tx_scalar(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:BHRate:RESult:TXSCalar {param}')
