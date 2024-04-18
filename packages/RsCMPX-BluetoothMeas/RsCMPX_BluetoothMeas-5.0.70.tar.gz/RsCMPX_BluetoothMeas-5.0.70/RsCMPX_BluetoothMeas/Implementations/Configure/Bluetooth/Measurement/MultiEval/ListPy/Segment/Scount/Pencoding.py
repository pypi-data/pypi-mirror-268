from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PencodingCls:
	"""Pencoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pencoding", core, parent)

	def set(self, phase_enc_stat_cnt: int, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SCOunt:PENCoding \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.scount.pencoding.set(phase_enc_stat_cnt = 1, segment = repcap.Segment.Default) \n
		No command help available \n
			:param phase_enc_stat_cnt: No help available
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.decimal_value_to_str(phase_enc_stat_cnt)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SCOunt:PENCoding {param}')

	def get(self, segment=repcap.Segment.Default) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SCOunt:PENCoding \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.listPy.segment.scount.pencoding.get(segment = repcap.Segment.Default) \n
		No command help available \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: phase_enc_stat_cnt: No help available"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SCOunt:PENCoding?')
		return Conversions.str_to_int(response)
