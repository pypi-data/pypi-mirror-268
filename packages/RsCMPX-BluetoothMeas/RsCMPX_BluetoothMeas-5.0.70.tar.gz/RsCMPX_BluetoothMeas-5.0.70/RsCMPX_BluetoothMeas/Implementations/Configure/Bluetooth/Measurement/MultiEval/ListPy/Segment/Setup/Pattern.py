from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PatternCls:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern_type: enums.MevPatternType, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:PATTern \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.pattern.set(pattern_type = enums.MevPatternType.ALL1, segment = repcap.Segment.Default) \n
		Specifies the payload pattern type expected in the segment. \n
			:param pattern_type: ALL1: 11111111 P11: 10101010 OTHer: any pattern except P11, P44, ALL1 ALTernating: the periodical change between the pattern P11 and P44 P44: 11110000
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(pattern_type, enums.MevPatternType)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:PATTern {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.MevPatternType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:PATTern \n
		Snippet: value: enums.MevPatternType = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.pattern.get(segment = repcap.Segment.Default) \n
		Specifies the payload pattern type expected in the segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: pattern_type: ALL1: 11111111 P11: 10101010 OTHer: any pattern except P11, P44, ALL1 ALTernating: the periodical change between the pattern P11 and P44 P44: 11110000"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.MevPatternType)
