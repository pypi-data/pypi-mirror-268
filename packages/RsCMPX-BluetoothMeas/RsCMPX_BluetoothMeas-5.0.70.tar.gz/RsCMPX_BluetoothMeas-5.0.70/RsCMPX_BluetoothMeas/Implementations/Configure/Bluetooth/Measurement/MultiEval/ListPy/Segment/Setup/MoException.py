from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MoExceptionCls:
	"""MoException commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("moException", core, parent)

	def set(self, meas_on_exception: bool, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:MOEXception \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.moException.set(meas_on_exception = False, segment = repcap.Segment.Default) \n
		Specifies whether the segment results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: ON: include the erroneous bursts OFF: exclude the erroneous bursts
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:MOEXception {param}')

	def get(self, segment=repcap.Segment.Default) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:MOEXception \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.moException.get(segment = repcap.Segment.Default) \n
		Specifies whether the segment results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: meas_on_exception: ON: include the erroneous bursts OFF: exclude the erroneous bursts"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:MOEXception?')
		return Conversions.str_to_bool(response)
