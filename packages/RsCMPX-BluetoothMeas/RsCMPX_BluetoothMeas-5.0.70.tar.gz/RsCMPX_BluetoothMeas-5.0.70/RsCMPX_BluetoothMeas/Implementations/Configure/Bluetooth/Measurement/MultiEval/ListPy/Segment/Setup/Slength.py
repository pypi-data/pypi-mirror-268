from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlengthCls:
	"""Slength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slength", core, parent)

	def set(self, segment_length: int, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:SLENgth \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.slength.set(segment_length = 1, segment = repcap.Segment.Default) \n
		Defines the number of measured bursts in the segment \n
			:param segment_length: The sum of the length of all active segments must not exceed 6700 timeslots (1 timeslot = 625 μs duration) .
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.decimal_value_to_str(segment_length)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:SLENgth {param}')

	def get(self, segment=repcap.Segment.Default) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:SLENgth \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.slength.get(segment = repcap.Segment.Default) \n
		Defines the number of measured bursts in the segment \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: segment_length: The sum of the length of all active segments must not exceed 6700 timeslots (1 timeslot = 625 μs duration) ."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:SLENgth?')
		return Conversions.str_to_int(response)
