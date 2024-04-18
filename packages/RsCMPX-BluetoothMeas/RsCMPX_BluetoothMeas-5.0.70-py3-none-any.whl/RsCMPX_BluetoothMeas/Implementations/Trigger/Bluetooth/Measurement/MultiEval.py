from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	def get_threshold(self) -> float or bool:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:MEValuation:THReshold \n
		Snippet: value: float or bool = driver.trigger.bluetooth.measurement.multiEval.get_threshold() \n
		Defines the trigger threshold for the power trigger. \n
			:return: power: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:BLUetooth:MEASurement<Instance>:MEValuation:THReshold?')
		return Conversions.str_to_float_or_bool(response)

	def set_threshold(self, power: float or bool) -> None:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:MEValuation:THReshold \n
		Snippet: driver.trigger.bluetooth.measurement.multiEval.set_threshold(power = 1.0) \n
		Defines the trigger threshold for the power trigger. \n
			:param power: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(power)
		self._core.io.write(f'TRIGger:BLUetooth:MEASurement<Instance>:MEValuation:THReshold {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float or bool = driver.trigger.bluetooth.measurement.multiEval.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. \n
			:return: trigger_timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:BLUetooth:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, trigger_timeout: float or bool) -> None:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.trigger.bluetooth.measurement.multiEval.set_timeout(trigger_timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. \n
			:param trigger_timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(trigger_timeout)
		self._core.io.write(f'TRIGger:BLUetooth:MEASurement<Instance>:MEValuation:TOUT {param}')
