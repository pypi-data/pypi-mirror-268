from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputSignalCls:
	"""InputSignal commands group definition. 9 total commands, 0 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputSignal", core, parent)

	# noinspection PyTypeChecker
	def get_pattern(self) -> enums.PatternTypeHdr:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PATTern \n
		Snippet: value: enums.PatternTypeHdr = driver.configure.bluetooth.measurement.hdr.inputSignal.get_pattern() \n
		No command help available \n
			:return: pattern_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.PatternTypeHdr)

	def set_pattern(self, pattern_type: enums.PatternTypeHdr) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PATTern \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_pattern(pattern_type = enums.PatternTypeHdr.OTHer) \n
		No command help available \n
			:param pattern_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(pattern_type, enums.PatternTypeHdr)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PATTern {param}')

	def get_plength(self) -> List[int]:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PLENgth \n
		Snippet: value: List[int] = driver.configure.bluetooth.measurement.hdr.inputSignal.get_plength() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PLENgth?')
		return response

	def set_plength(self, payload_length: List[int]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PLENgth \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_plength(payload_length = [1, 2, 3]) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.list_to_csv_str(payload_length)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PLENgth {param}')

	# noinspection PyTypeChecker
	def get_ptype(self) -> enums.PacketTypeC:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PTYPe \n
		Snippet: value: enums.PacketTypeC = driver.configure.bluetooth.measurement.hdr.inputSignal.get_ptype() \n
		No command help available \n
			:return: packet_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.PacketTypeC)

	def set_ptype(self, packet_type: enums.PacketTypeC) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PTYPe \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_ptype(packet_type = enums.PacketTypeC.H41P) \n
		No command help available \n
			:param packet_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.PacketTypeC)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:PTYPe {param}')

	def get_nap(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:NAP \n
		Snippet: value: str = driver.configure.bluetooth.measurement.hdr.inputSignal.get_nap() \n
		No command help available \n
			:return: nap_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:NAP?')
		return trim_str_response(response)

	def set_nap(self, nap_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:NAP \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_nap(nap_address = rawAbc) \n
		No command help available \n
			:param nap_address: No help available
		"""
		param = Conversions.value_to_str(nap_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:NAP {param}')

	def get_uap(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:UAP \n
		Snippet: value: str = driver.configure.bluetooth.measurement.hdr.inputSignal.get_uap() \n
		No command help available \n
			:return: uap_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:UAP?')
		return trim_str_response(response)

	def set_uap(self, uap_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:UAP \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_uap(uap_address = rawAbc) \n
		No command help available \n
			:param uap_address: No help available
		"""
		param = Conversions.value_to_str(uap_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:UAP {param}')

	def get_lap(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:LAP \n
		Snippet: value: str = driver.configure.bluetooth.measurement.hdr.inputSignal.get_lap() \n
		No command help available \n
			:return: lap_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:LAP?')
		return trim_str_response(response)

	def set_lap(self, lap_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:LAP \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_lap(lap_address = rawAbc) \n
		No command help available \n
			:param lap_address: No help available
		"""
		param = Conversions.value_to_str(lap_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:LAP {param}')

	def get_bd_address(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:BDADdress \n
		Snippet: value: str = driver.configure.bluetooth.measurement.hdr.inputSignal.get_bd_address() \n
		No command help available \n
			:return: bd_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:BDADdress?')
		return trim_str_response(response)

	def set_bd_address(self, bd_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:BDADdress \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_bd_address(bd_address = rawAbc) \n
		No command help available \n
			:param bd_address: No help available
		"""
		param = Conversions.value_to_str(bd_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:BDADdress {param}')

	def get_asynchronize(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:ASYNchronize \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.hdr.inputSignal.get_asynchronize() \n
		No command help available \n
			:return: auto_sync: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:ASYNchronize?')
		return Conversions.str_to_bool(response)

	def set_asynchronize(self, auto_sync: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:ASYNchronize \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_asynchronize(auto_sync = False) \n
		No command help available \n
			:param auto_sync: No help available
		"""
		param = Conversions.bool_to_str(auto_sync)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:ASYNchronize {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.AutoManualMode:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:DMODe \n
		Snippet: value: enums.AutoManualMode = driver.configure.bluetooth.measurement.hdr.inputSignal.get_dmode() \n
		No command help available \n
			:return: detection_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_dmode(self, detection_mode: enums.AutoManualMode) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:DMODe \n
		Snippet: driver.configure.bluetooth.measurement.hdr.inputSignal.set_dmode(detection_mode = enums.AutoManualMode.AUTO) \n
		No command help available \n
			:param detection_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(detection_mode, enums.AutoManualMode)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDR:ISIGnal:DMODe {param}')
