from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BhRateCls:
	"""BhRate commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bhRate", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_source(self) -> str:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:BHRate:SOURce \n
		Snippet: value: str = driver.trigger.bluetooth.measurement.bhRate.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('TRIGger:BLUetooth:MEASurement<Instance>:BHRate:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:BHRate:SOURce \n
		Snippet: driver.trigger.bluetooth.measurement.bhRate.set_source(source = 'abc') \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:BLUetooth:MEASurement<Instance>:BHRate:SOURce {param}')

	def get_threshold(self) -> float or bool:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:BHRate:THReshold \n
		Snippet: value: float or bool = driver.trigger.bluetooth.measurement.bhRate.get_threshold() \n
		No command help available \n
			:return: power: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:BLUetooth:MEASurement<Instance>:BHRate:THReshold?')
		return Conversions.str_to_float_or_bool(response)

	def set_threshold(self, power: float or bool) -> None:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:BHRate:THReshold \n
		Snippet: driver.trigger.bluetooth.measurement.bhRate.set_threshold(power = 1.0) \n
		No command help available \n
			:param power: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(power)
		self._core.io.write(f'TRIGger:BLUetooth:MEASurement<Instance>:BHRate:THReshold {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:BHRate:TOUT \n
		Snippet: value: float or bool = driver.trigger.bluetooth.measurement.bhRate.get_timeout() \n
		No command help available \n
			:return: timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:BLUetooth:MEASurement<Instance>:BHRate:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:BHRate:TOUT \n
		Snippet: driver.trigger.bluetooth.measurement.bhRate.set_timeout(timeout = 1.0) \n
		No command help available \n
			:param timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:BLUetooth:MEASurement<Instance>:BHRate:TOUT {param}')

	def clone(self) -> 'BhRateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BhRateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
