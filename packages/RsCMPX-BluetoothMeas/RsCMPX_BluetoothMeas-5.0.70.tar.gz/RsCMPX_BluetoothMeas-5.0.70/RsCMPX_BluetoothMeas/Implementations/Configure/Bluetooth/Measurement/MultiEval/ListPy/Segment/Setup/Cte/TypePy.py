from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, cte_type: enums.CteType, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:CTE:TYPE \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.cte.typePy.set(cte_type = enums.CteType.AOA, segment = repcap.Segment.Default) \n
		Defines the CTE type for segment. \n
			:param cte_type: CTE slot type for LE with CTE AOA: CTE type angle of arrival, 2 μs slot AOD1: CTE type angle of departure, 1 μs slot AOD2: CTE type angle of departure, 2 μs slot
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(cte_type, enums.CteType)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:CTE:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.CteType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:CTE:TYPE \n
		Snippet: value: enums.CteType = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.cte.typePy.get(segment = repcap.Segment.Default) \n
		Defines the CTE type for segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: cte_type: CTE slot type for LE with CTE AOA: CTE type angle of arrival, 2 μs slot AOD1: CTE type angle of departure, 1 μs slot AOD2: CTE type angle of departure, 2 μs slot"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:CTE:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.CteType)
