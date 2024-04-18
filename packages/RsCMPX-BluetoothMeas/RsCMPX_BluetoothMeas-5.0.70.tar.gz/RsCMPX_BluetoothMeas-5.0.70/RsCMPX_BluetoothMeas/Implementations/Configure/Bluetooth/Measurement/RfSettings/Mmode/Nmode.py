from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NmodeCls:
	"""Nmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nmode", core, parent)

	# noinspection PyTypeChecker
	def get_low_energy(self) -> enums.MeasureScope:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MMODe:NMODe:LENergy \n
		Snippet: value: enums.MeasureScope = driver.configure.bluetooth.measurement.rfSettings.mmode.nmode.get_low_energy() \n
		No command help available \n
			:return: measure_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MMODe:NMODe:LENergy?')
		return Conversions.str_to_scalar_enum(response, enums.MeasureScope)

	def set_low_energy(self, measure_mode: enums.MeasureScope) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MMODe:NMODe:LENergy \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.mmode.nmode.set_low_energy(measure_mode = enums.MeasureScope.ALL) \n
		No command help available \n
			:param measure_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(measure_mode, enums.MeasureScope)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MMODe:NMODe:LENergy {param}')
