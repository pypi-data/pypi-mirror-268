from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SearchCls:
	"""Search commands group definition. 11 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("search", core, parent)

	@property
	def rintegrity(self):
		"""rintegrity commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rintegrity'):
			from .Rintegrity import RintegrityCls
			self._rintegrity = RintegrityCls(self._core, self._cmd_group)
		return self._rintegrity

	@property
	def packets(self):
		"""packets commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_packets'):
			from .Packets import PacketsCls
			self._packets = PacketsCls(self._core, self._cmd_group)
		return self._packets

	@property
	def limit(self):
		"""limit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	def get_start_level(self) -> float or bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:STARtlevel \n
		Snippet: value: float or bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.search.get_start_level() \n
		No command help available \n
			:return: start_level: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:STARtlevel?')
		return Conversions.str_to_float_or_bool(response)

	def set_start_level(self, start_level: float or bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:STARtlevel \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.search.set_start_level(start_level = 1.0) \n
		No command help available \n
			:param start_level: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(start_level)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:STARtlevel {param}')

	def get_step(self) -> float or bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:STEP \n
		Snippet: value: float or bool = driver.configure.bluetooth.measurement.dtMode.rxQuality.search.get_step() \n
		No command help available \n
			:return: level_step: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:STEP?')
		return Conversions.str_to_float_or_bool(response)

	def set_step(self, level_step: float or bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:STEP \n
		Snippet: driver.configure.bluetooth.measurement.dtMode.rxQuality.search.set_step(level_step = 1.0) \n
		No command help available \n
			:param level_step: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(level_step)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:STEP {param}')

	def clone(self) -> 'SearchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SearchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
