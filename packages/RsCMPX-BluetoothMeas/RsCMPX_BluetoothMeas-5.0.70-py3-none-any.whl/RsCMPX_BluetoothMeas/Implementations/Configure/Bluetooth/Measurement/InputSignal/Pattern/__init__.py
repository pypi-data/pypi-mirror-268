from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PatternCls:
	"""Pattern commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DetectedPatternType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern \n
		Snippet: value: enums.DetectedPatternType = driver.configure.bluetooth.measurement.inputSignal.pattern.get_value() \n
		The command specifies the data pattern type that the DUT transmits as user payload data on its BR packets. \n
			:return: pattern_type: P11: 10101010 P44: 11110000 OTHer: any pattern except P11, P44 ALTernating: the periodical change between the pattern P11 and P44
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.DetectedPatternType)

	def set_value(self, pattern_type: enums.DetectedPatternType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.pattern.set_value(pattern_type = enums.DetectedPatternType.ALTernating) \n
		The command specifies the data pattern type that the DUT transmits as user payload data on its BR packets. \n
			:param pattern_type: P11: 10101010 P44: 11110000 OTHer: any pattern except P11, P44 ALTernating: the periodical change between the pattern P11 and P44
		"""
		param = Conversions.enum_scalar_to_str(pattern_type, enums.DetectedPatternType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PATTern {param}')

	def clone(self) -> 'PatternCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PatternCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
