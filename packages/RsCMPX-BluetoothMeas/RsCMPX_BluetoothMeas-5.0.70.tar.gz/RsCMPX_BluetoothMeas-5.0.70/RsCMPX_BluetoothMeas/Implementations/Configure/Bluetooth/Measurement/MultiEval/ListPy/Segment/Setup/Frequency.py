from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:FREQuency \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.frequency.set(frequency = 1.0, segment = repcap.Segment.Default) \n
		Specifies the center frequency of the signal expected in the segment. \n
			:param frequency: No help available
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:FREQuency {param}')

	def get(self, segment=repcap.Segment.Default) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:FREQuency \n
		Snippet: value: float = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.frequency.get(segment = repcap.Segment.Default) \n
		Specifies the center frequency of the signal expected in the segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: frequency: No help available"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:FREQuency?')
		return Conversions.str_to_float(response)
