from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ComSettingsCls:
	"""ComSettings commands group definition. 7 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comSettings", core, parent)

	@property
	def ports(self):
		"""ports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ports'):
			from .Ports import PortsCls
			self._ports = PortsCls(self._core, self._cmd_group)
		return self._ports

	def get_com_port(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:COMPort \n
		Snippet: value: int = driver.configure.bluetooth.measurement.comSettings.get_com_port() \n
		No command help available \n
			:return: no: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:COMPort?')
		return Conversions.str_to_int(response)

	def set_com_port(self, no: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:COMPort \n
		Snippet: driver.configure.bluetooth.measurement.comSettings.set_com_port(no = 1) \n
		No command help available \n
			:param no: No help available
		"""
		param = Conversions.decimal_value_to_str(no)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:COMPort {param}')

	# noinspection PyTypeChecker
	def get_baud_rate(self) -> enums.BaudRate:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:BAUDrate \n
		Snippet: value: enums.BaudRate = driver.configure.bluetooth.measurement.comSettings.get_baud_rate() \n
		No command help available \n
			:return: baud_rate: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:BAUDrate?')
		return Conversions.str_to_scalar_enum(response, enums.BaudRate)

	def set_baud_rate(self, baud_rate: enums.BaudRate) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:BAUDrate \n
		Snippet: driver.configure.bluetooth.measurement.comSettings.set_baud_rate(baud_rate = enums.BaudRate.B110) \n
		No command help available \n
			:param baud_rate: No help available
		"""
		param = Conversions.enum_scalar_to_str(baud_rate, enums.BaudRate)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:BAUDrate {param}')

	# noinspection PyTypeChecker
	def get_stop_bits(self) -> enums.StopBits:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:STOPbits \n
		Snippet: value: enums.StopBits = driver.configure.bluetooth.measurement.comSettings.get_stop_bits() \n
		No command help available \n
			:return: stop_bits: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:STOPbits?')
		return Conversions.str_to_scalar_enum(response, enums.StopBits)

	def set_stop_bits(self, stop_bits: enums.StopBits) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:STOPbits \n
		Snippet: driver.configure.bluetooth.measurement.comSettings.set_stop_bits(stop_bits = enums.StopBits.S1) \n
		No command help available \n
			:param stop_bits: No help available
		"""
		param = Conversions.enum_scalar_to_str(stop_bits, enums.StopBits)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:STOPbits {param}')

	# noinspection PyTypeChecker
	def get_parity(self) -> enums.Parity:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PARity \n
		Snippet: value: enums.Parity = driver.configure.bluetooth.measurement.comSettings.get_parity() \n
		No command help available \n
			:return: parity: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PARity?')
		return Conversions.str_to_scalar_enum(response, enums.Parity)

	def set_parity(self, parity: enums.Parity) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PARity \n
		Snippet: driver.configure.bluetooth.measurement.comSettings.set_parity(parity = enums.Parity.EVEN) \n
		No command help available \n
			:param parity: No help available
		"""
		param = Conversions.enum_scalar_to_str(parity, enums.Parity)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PARity {param}')

	# noinspection PyTypeChecker
	def get_protocol(self) -> enums.Protocol:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PROTocol \n
		Snippet: value: enums.Protocol = driver.configure.bluetooth.measurement.comSettings.get_protocol() \n
		No command help available \n
			:return: protocol: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.Protocol)

	def set_protocol(self, protocol: enums.Protocol) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PROTocol \n
		Snippet: driver.configure.bluetooth.measurement.comSettings.set_protocol(protocol = enums.Protocol.CTSRts) \n
		No command help available \n
			:param protocol: No help available
		"""
		param = Conversions.enum_scalar_to_str(protocol, enums.Protocol)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:PROTocol {param}')

	# noinspection PyTypeChecker
	def get_dbits(self) -> enums.DataBits:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:DBITs \n
		Snippet: value: enums.DataBits = driver.configure.bluetooth.measurement.comSettings.get_dbits() \n
		No command help available \n
			:return: data_bits: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:DBITs?')
		return Conversions.str_to_scalar_enum(response, enums.DataBits)

	def set_dbits(self, data_bits: enums.DataBits) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:DBITs \n
		Snippet: driver.configure.bluetooth.measurement.comSettings.set_dbits(data_bits = enums.DataBits.D7) \n
		No command help available \n
			:param data_bits: No help available
		"""
		param = Conversions.enum_scalar_to_str(data_bits, enums.DataBits)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:COMSettings:DBITs {param}')

	def clone(self) -> 'ComSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ComSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
