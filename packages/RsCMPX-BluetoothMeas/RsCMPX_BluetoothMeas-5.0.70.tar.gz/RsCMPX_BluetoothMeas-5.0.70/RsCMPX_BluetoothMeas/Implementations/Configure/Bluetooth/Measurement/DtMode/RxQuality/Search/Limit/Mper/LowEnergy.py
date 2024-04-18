from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	def get_le_1_m(self) -> float or bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LE1M \n
		Snippet: value: float or bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.search.limit.mper.lowEnergy.get_le_1_m() \n
		No command help available \n
			:return: limit: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LE1M?')
		return Conversions.str_to_float_or_bool(response)

	def set_le_1_m(self, limit: float or bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LE1M \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.search.limit.mper.lowEnergy.set_le_1_m(limit = 1.0) \n
		No command help available \n
			:param limit: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LE1M {param}')

	def get_le_2_m(self) -> float or bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LE2M \n
		Snippet: value: float or bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.search.limit.mper.lowEnergy.get_le_2_m() \n
		No command help available \n
			:return: limit: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LE2M?')
		return Conversions.str_to_float_or_bool(response)

	def set_le_2_m(self, limit: float or bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LE2M \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.search.limit.mper.lowEnergy.set_le_2_m(limit = 1.0) \n
		No command help available \n
			:param limit: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LE2M {param}')

	def get_lrange(self) -> float or bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LRANge \n
		Snippet: value: float or bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.search.limit.mper.lowEnergy.get_lrange() \n
		No command help available \n
			:return: limit: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LRANge?')
		return Conversions.str_to_float_or_bool(response)

	def set_lrange(self, limit: float or bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LRANge \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.search.limit.mper.lowEnergy.set_lrange(limit = 1.0) \n
		No command help available \n
			:param limit: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:LIMit:MPER:LENergy:LRANge {param}')
