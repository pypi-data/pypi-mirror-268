from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RtriggerCls:
	"""Rtrigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtrigger", core, parent)

	def set(self, retrigger: bool, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:RTRigger \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.rtrigger.set(retrigger = False, segment = repcap.Segment.Default) \n
		Specifies whether a trigger event is required for the segment or not. The setting is ignored for the first segment of a
		measurement. \n
			:param retrigger: OFF: measure the segment without retrigger ON: trigger event required
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.bool_to_str(retrigger)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:RTRigger {param}')

	def get(self, segment=repcap.Segment.Default) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:RTRigger \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.rtrigger.get(segment = repcap.Segment.Default) \n
		Specifies whether a trigger event is required for the segment or not. The setting is ignored for the first segment of a
		measurement. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: retrigger: OFF: measure the segment without retrigger ON: trigger event required"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:RTRigger?')
		return Conversions.str_to_bool(response)
