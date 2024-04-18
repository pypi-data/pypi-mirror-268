from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BtypeCls:
	"""Btype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btype", core, parent)

	def set(self, burst_type: enums.BurstType, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:BTYPe \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.btype.set(burst_type = enums.BurstType.BR, segment = repcap.Segment.Default) \n
		Specifies the burst type of the signal expected in the segment. \n
			:param burst_type: BR: Basic Rate EDR: Enhanced Data Rate LE: Low Energy
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(burst_type, enums.BurstType)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:BTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.BurstType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:BTYPe \n
		Snippet: value: enums.BurstType = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.btype.get(segment = repcap.Segment.Default) \n
		Specifies the burst type of the signal expected in the segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: burst_type: BR: Basic Rate EDR: Enhanced Data Rate LE: Low Energy"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:BTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.BurstType)
