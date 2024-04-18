from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtxCls:
	"""Ptx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptx", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: Percentage of measured bursts with failed limit check
			- Nominal_Power: float: Average power during the carrier-on state
			- No_Of_Exceptions: int: The number of exceptions, whose power is above Exception PTX.
			- Ptx_Ref: float: Reference power obtained within the center channel (EDR)
			- Ptx_N_26_Ch_N_1_Abs: float: No parameter help available
			- Ptx_N_26_Ch_P_1_Abs: float: No parameter help available
			- Ptx_N_26_Ch_N_1_Rel: float: No parameter help available
			- Ptx_N_26_Ch_P_1_Rel: float: No parameter help available
			- Acp: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_int('No_Of_Exceptions'),
			ArgStruct.scalar_float('Ptx_Ref'),
			ArgStruct.scalar_float('Ptx_N_26_Ch_N_1_Abs'),
			ArgStruct.scalar_float('Ptx_N_26_Ch_P_1_Abs'),
			ArgStruct.scalar_float('Ptx_N_26_Ch_N_1_Rel'),
			ArgStruct.scalar_float('Ptx_N_26_Ch_P_1_Rel'),
			ArgStruct('Acp', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.No_Of_Exceptions: int = None
			self.Ptx_Ref: float = None
			self.Ptx_N_26_Ch_N_1_Abs: float = None
			self.Ptx_N_26_Ch_P_1_Abs: float = None
			self.Ptx_N_26_Ch_N_1_Rel: float = None
			self.Ptx_N_26_Ch_P_1_Rel: float = None
			self.Acp: List[float] = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SACP[:PTX] \n
		Snippet: value: FetchStruct = driver.bluetooth.measurement.multiEval.listPy.segment.sacp.ptx.fetch(segment = repcap.Segment.Default) \n
		Returns spectrum ACP single value results for segment<no> in list mode. The command returns all parameters listed below,
		independent of the selected list mode setup. However, only for some of the parameters measured values are available. For
		the other parameters, only an indicator is returned (e.g. NAV) . \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SACP:PTX?', self.__class__.FetchStruct())
