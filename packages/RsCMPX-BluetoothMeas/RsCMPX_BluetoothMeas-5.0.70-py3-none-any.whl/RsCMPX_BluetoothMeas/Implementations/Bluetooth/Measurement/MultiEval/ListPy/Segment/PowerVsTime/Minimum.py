from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: Percentage of measured bursts with failed limit check
			- Nominal_Power: float: Average power during the carrier-on state
			- Peak_Power: float: Peak power
			- Leakage_Power: float: Leakage power (BR, LE)
			- Gfsk_Power: float: Average power within the GFSK modulated part of the burst (EDR)
			- Dpsk_Power: float: Average power within the DPSK modulated part of the burst (EDR)
			- Dpsk_Minus_Gfsk: float: Difference between the 8_DPSKPower and 7_GFSKPower (EDR)
			- Guard_Period: float: Length of the guard band between the packet header and the EDR synchronization sequence (EDR)
			- Peak_Minus_Avg: float: Difference between the peak power and the average power in the burst (LE)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Peak_Power'),
			ArgStruct.scalar_float('Leakage_Power'),
			ArgStruct.scalar_float('Gfsk_Power'),
			ArgStruct.scalar_float('Dpsk_Power'),
			ArgStruct.scalar_float('Dpsk_Minus_Gfsk'),
			ArgStruct.scalar_float('Guard_Period'),
			ArgStruct.scalar_float('Peak_Minus_Avg')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Peak_Power: float = None
			self.Leakage_Power: float = None
			self.Gfsk_Power: float = None
			self.Dpsk_Power: float = None
			self.Dpsk_Minus_Gfsk: float = None
			self.Guard_Period: float = None
			self.Peak_Minus_Avg: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:PVTime:MINimum \n
		Snippet: value: FetchStruct = driver.bluetooth.measurement.multiEval.listPy.segment.powerVsTime.minimum.fetch(segment = repcap.Segment.Default) \n
		Returns statistical power vs time single value results for segment<no> in list mode. The command returns all parameters
		listed below, independent of the selected list mode setup. However, only for some of the parameters measured values are
		available. For the other parameters, only an indicator is returned (e.g. NAV) . \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:PVTime:MINimum?', self.__class__.FetchStruct())
