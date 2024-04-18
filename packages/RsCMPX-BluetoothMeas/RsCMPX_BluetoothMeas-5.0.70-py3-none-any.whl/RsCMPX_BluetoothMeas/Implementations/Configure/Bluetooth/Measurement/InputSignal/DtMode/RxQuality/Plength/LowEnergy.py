from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	# noinspection PyTypeChecker
	def get_le_1_m(self) -> enums.PayloadLength:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LE1M \n
		Snippet: value: enums.PayloadLength = driver.configure.bluetooth.measurement.inputSignal.dtMode.rxQuality.plength.lowEnergy.get_le_1_m() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LE1M?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadLength)

	def set_le_1_m(self, payload_length: enums.PayloadLength) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LE1M \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.dtMode.rxQuality.plength.lowEnergy.set_le_1_m(payload_length = enums.PayloadLength._255) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.enum_scalar_to_str(payload_length, enums.PayloadLength)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LE1M {param}')

	# noinspection PyTypeChecker
	def get_le_2_m(self) -> enums.PayloadLength:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LE2M \n
		Snippet: value: enums.PayloadLength = driver.configure.bluetooth.measurement.inputSignal.dtMode.rxQuality.plength.lowEnergy.get_le_2_m() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LE2M?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadLength)

	def set_le_2_m(self, payload_length: enums.PayloadLength) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LE2M \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.dtMode.rxQuality.plength.lowEnergy.set_le_2_m(payload_length = enums.PayloadLength._255) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.enum_scalar_to_str(payload_length, enums.PayloadLength)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LE2M {param}')

	# noinspection PyTypeChecker
	def get_lrange(self) -> enums.PayloadLength:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LRANge \n
		Snippet: value: enums.PayloadLength = driver.configure.bluetooth.measurement.inputSignal.dtMode.rxQuality.plength.lowEnergy.get_lrange() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LRANge?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadLength)

	def set_lrange(self, payload_length: enums.PayloadLength) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LRANge \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.dtMode.rxQuality.plength.lowEnergy.set_lrange(payload_length = enums.PayloadLength._255) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.enum_scalar_to_str(payload_length, enums.PayloadLength)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DTMode:RXQuality:PLENgth:LENergy:LRANge {param}')
