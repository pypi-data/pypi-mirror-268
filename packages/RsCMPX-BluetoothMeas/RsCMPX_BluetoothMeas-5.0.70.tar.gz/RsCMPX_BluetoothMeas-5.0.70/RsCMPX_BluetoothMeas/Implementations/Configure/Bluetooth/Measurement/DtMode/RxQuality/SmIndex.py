from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmIndexCls:
	"""SmIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smIndex", core, parent)

	def get_low_energy(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SMINdex:LENergy \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.smIndex.get_low_energy() \n
		No command help available \n
			:return: mod_index_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SMINdex:LENergy?')
		return Conversions.str_to_bool(response)

	def set_low_energy(self, mod_index_type: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SMINdex:LENergy \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.smIndex.set_low_energy(mod_index_type = False) \n
		No command help available \n
			:param mod_index_type: No help available
		"""
		param = Conversions.bool_to_str(mod_index_type)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SMINdex:LENergy {param}')
