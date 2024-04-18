from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScenarioCls:
	"""Scenario commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenario", core, parent)

	@property
	def maProtocol(self):
		"""maProtocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maProtocol'):
			from .MaProtocol import MaProtocolCls
			self._maProtocol = MaProtocolCls(self._core, self._cmd_group)
		return self._maProtocol

	@property
	def salone(self):
		"""salone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_salone'):
			from .Salone import SaloneCls
			self._salone = SaloneCls(self._core, self._cmd_group)
		return self._salone

	def get_cspath(self) -> str:
		"""SCPI: ROUTe:BLUetooth:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: value: str = driver.route.bluetooth.measurement.scenario.get_cspath() \n
		No command help available \n
			:return: master: No help available
		"""
		response = self._core.io.query_str('ROUTe:BLUetooth:MEASurement<Instance>:SCENario:CSPath?')
		return trim_str_response(response)

	def set_cspath(self, master: str) -> None:
		"""SCPI: ROUTe:BLUetooth:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: driver.route.bluetooth.measurement.scenario.set_cspath(master = 'abc') \n
		No command help available \n
			:param master: No help available
		"""
		param = Conversions.value_to_quoted_str(master)
		self._core.io.write(f'ROUTe:BLUetooth:MEASurement<Instance>:SCENario:CSPath {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.TestScenario:
		"""SCPI: ROUTe:BLUetooth:MEASurement<Instance>:SCENario \n
		Snippet: value: enums.TestScenario = driver.route.bluetooth.measurement.scenario.get_value() \n
		No command help available \n
			:return: scenario: No help available
		"""
		response = self._core.io.query_str('ROUTe:BLUetooth:MEASurement<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.TestScenario)

	def clone(self) -> 'ScenarioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScenarioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
