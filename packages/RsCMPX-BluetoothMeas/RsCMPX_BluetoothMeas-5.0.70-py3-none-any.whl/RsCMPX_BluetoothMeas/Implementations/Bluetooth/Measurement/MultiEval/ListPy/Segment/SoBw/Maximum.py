from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: Percentage of measured bursts with failed limit check.
			- Nominal_Power: float: Average power during the carrier-on state.
			- Peak_Emission: float: Peak power within the maximum spectral trace.
			- Fl: float: The smallest frequency at which the transmit power drops 20 dB below the peak power.
			- Fh: float: The highest frequency at which the transmit power drops 20 dB below the peak power.
			- Fh_Min_Fl: float: Difference between the 7_fH and 6_fL"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Peak_Emission'),
			ArgStruct.scalar_float('Fl'),
			ArgStruct.scalar_float('Fh'),
			ArgStruct.scalar_float('Fh_Min_Fl')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Peak_Emission: float = None
			self.Fl: float = None
			self.Fh: float = None
			self.Fh_Min_Fl: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SOBW:MAXimum \n
		Snippet: value: FetchStruct = driver.bluetooth.measurement.multiEval.listPy.segment.soBw.maximum.fetch(segment = repcap.Segment.Default) \n
		Returns spectrum occupied bandwidth (20 dB bandwidth) single value results for segment<no> in list mode.
		The 20 dB bandwidth measurement is available for BR bursts only. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SOBW:MAXimum?', self.__class__.FetchStruct())
