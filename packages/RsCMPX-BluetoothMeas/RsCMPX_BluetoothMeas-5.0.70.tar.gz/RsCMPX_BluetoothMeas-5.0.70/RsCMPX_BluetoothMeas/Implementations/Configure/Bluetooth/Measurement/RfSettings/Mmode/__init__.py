from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MmodeCls:
	"""Mmode commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mmode", core, parent)

	@property
	def nmode(self):
		"""nmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nmode'):
			from .Nmode import NmodeCls
			self._nmode = NmodeCls(self._core, self._cmd_group)
		return self._nmode

	# noinspection PyTypeChecker
	def get_value(self) -> enums.MeasureScope:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MMODe \n
		Snippet: value: enums.MeasureScope = driver.configure.bluetooth.measurement.rfSettings.mmode.get_value() \n
		No command help available \n
			:return: measure_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.MeasureScope)

	def set_value(self, measure_mode: enums.MeasureScope) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MMODe \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.mmode.set_value(measure_mode = enums.MeasureScope.ALL) \n
		No command help available \n
			:param measure_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(measure_mode, enums.MeasureScope)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MMODe {param}')

	def clone(self) -> 'MmodeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MmodeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
