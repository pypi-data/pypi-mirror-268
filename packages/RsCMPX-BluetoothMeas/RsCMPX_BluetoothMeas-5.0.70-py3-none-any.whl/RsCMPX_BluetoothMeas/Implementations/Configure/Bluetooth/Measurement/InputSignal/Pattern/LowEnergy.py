from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	# noinspection PyTypeChecker
	def get_le_1_m(self) -> enums.LePatternType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy[:LE1M] \n
		Snippet: value: enums.LePatternType = driver.configure.bluetooth.measurement.inputSignal.pattern.lowEnergy.get_le_1_m() \n
		It specifies the data pattern type that the EUT transmits as user payload data in its LE packets. Commands for LE 1M PHY
		(...:LE1M...) and LE 2M PHY (...:LE2M...) are available. \n
			:return: pattern_type: P11: '10101010' in transmission order (LSB first) P44: '11110000' in transmission order (LSB first) OTHer: any pattern except P11, P44
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LE1M?')
		return Conversions.str_to_scalar_enum(response, enums.LePatternType)

	def set_le_1_m(self, pattern_type: enums.LePatternType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy[:LE1M] \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.pattern.lowEnergy.set_le_1_m(pattern_type = enums.LePatternType.OTHer) \n
		It specifies the data pattern type that the EUT transmits as user payload data in its LE packets. Commands for LE 1M PHY
		(...:LE1M...) and LE 2M PHY (...:LE2M...) are available. \n
			:param pattern_type: P11: '10101010' in transmission order (LSB first) P44: '11110000' in transmission order (LSB first) OTHer: any pattern except P11, P44
		"""
		param = Conversions.enum_scalar_to_str(pattern_type, enums.LePatternType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LE1M {param}')

	# noinspection PyTypeChecker
	def get_lrange(self) -> enums.TransmitPatternType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LRANge \n
		Snippet: value: enums.TransmitPatternType = driver.configure.bluetooth.measurement.inputSignal.pattern.lowEnergy.get_lrange() \n
		Specifies the data pattern type for LE coded PHY, that the EUT transmits as user payload data. \n
			:return: pattern_type: ALL1: '11111111' OTHer: any pattern except ALL1
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LRANge?')
		return Conversions.str_to_scalar_enum(response, enums.TransmitPatternType)

	def set_lrange(self, pattern_type: enums.TransmitPatternType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LRANge \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.pattern.lowEnergy.set_lrange(pattern_type = enums.TransmitPatternType.ALL1) \n
		Specifies the data pattern type for LE coded PHY, that the EUT transmits as user payload data. \n
			:param pattern_type: ALL1: '11111111' OTHer: any pattern except ALL1
		"""
		param = Conversions.enum_scalar_to_str(pattern_type, enums.TransmitPatternType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LRANge {param}')

	# noinspection PyTypeChecker
	def get_le_2_m(self) -> enums.LePatternType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LE2M \n
		Snippet: value: enums.LePatternType = driver.configure.bluetooth.measurement.inputSignal.pattern.lowEnergy.get_le_2_m() \n
		It specifies the data pattern type that the EUT transmits as user payload data in its LE packets. Commands for LE 1M PHY
		(...:LE1M...) and LE 2M PHY (...:LE2M...) are available. \n
			:return: pattern_type: P11: '10101010' in transmission order (LSB first) P44: '11110000' in transmission order (LSB first) OTHer: any pattern except P11, P44
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LE2M?')
		return Conversions.str_to_scalar_enum(response, enums.LePatternType)

	def set_le_2_m(self, pattern_type: enums.LePatternType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LE2M \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.pattern.lowEnergy.set_le_2_m(pattern_type = enums.LePatternType.OTHer) \n
		It specifies the data pattern type that the EUT transmits as user payload data in its LE packets. Commands for LE 1M PHY
		(...:LE1M...) and LE 2M PHY (...:LE2M...) are available. \n
			:param pattern_type: P11: '10101010' in transmission order (LSB first) P44: '11110000' in transmission order (LSB first) OTHer: any pattern except P11, P44
		"""
		param = Conversions.enum_scalar_to_str(pattern_type, enums.LePatternType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern:LENergy:LE2M {param}')
