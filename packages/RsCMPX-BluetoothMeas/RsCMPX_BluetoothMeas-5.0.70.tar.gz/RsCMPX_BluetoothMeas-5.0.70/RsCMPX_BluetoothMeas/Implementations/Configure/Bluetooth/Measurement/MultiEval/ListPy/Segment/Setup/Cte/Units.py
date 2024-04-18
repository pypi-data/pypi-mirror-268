from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UnitsCls:
	"""Units commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("units", core, parent)

	def set(self, cte_units: int, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:CTE:UNITs \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.cte.units.set(cte_units = 1, segment = repcap.Segment.Default) \n
		Defines the No. of CTE units for segment. \n
			:param cte_units: No. of CTE units for LE with CTE, one unit corresponds to 8 μs.
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.decimal_value_to_str(cte_units)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:CTE:UNITs {param}')

	def get(self, segment=repcap.Segment.Default) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:CTE:UNITs \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.cte.units.get(segment = repcap.Segment.Default) \n
		Defines the No. of CTE units for segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: cte_units: No. of CTE units for LE with CTE, one unit corresponds to 8 μs."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:CTE:UNITs?')
		return Conversions.str_to_int(response)
