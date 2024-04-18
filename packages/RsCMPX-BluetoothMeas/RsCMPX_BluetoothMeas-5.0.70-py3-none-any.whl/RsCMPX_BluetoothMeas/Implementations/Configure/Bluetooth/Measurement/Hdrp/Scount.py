from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScountCls:
	"""Scount commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	def get_power_vs_time(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:PVTime \n
		Snippet: value: int = driver.configure.bluetooth.measurement.hdrp.scount.get_power_vs_time() \n
		No command help available \n
			:return: stat_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:PVTime?')
		return Conversions.str_to_int(response)

	def set_power_vs_time(self, stat_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.scount.set_power_vs_time(stat_count = 1) \n
		No command help available \n
			:param stat_count: No help available
		"""
		param = Conversions.decimal_value_to_str(stat_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:PVTime {param}')

	def get_sacp(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:SACP \n
		Snippet: value: int = driver.configure.bluetooth.measurement.hdrp.scount.get_sacp() \n
		No command help available \n
			:return: stat_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:SACP?')
		return Conversions.str_to_int(response)

	def set_sacp(self, stat_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:SACP \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.scount.set_sacp(stat_count = 1) \n
		No command help available \n
			:param stat_count: No help available
		"""
		param = Conversions.decimal_value_to_str(stat_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:SACP {param}')

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:MODulation \n
		Snippet: value: int = driver.configure.bluetooth.measurement.hdrp.scount.get_modulation() \n
		No command help available \n
			:return: stat_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, stat_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:MODulation \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.scount.set_modulation(stat_count = 1) \n
		No command help available \n
			:param stat_count: No help available
		"""
		param = Conversions.decimal_value_to_str(stat_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCOunt:MODulation {param}')
