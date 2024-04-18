from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	@property
	def extended(self):
		"""extended commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_extended'):
			from .Extended import ExtendedCls
			self._extended = ExtendedCls(self._core, self._cmd_group)
		return self._extended

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: Percentage of measured bursts with failed limit check
			- Nominal_Power: float: Standard deviation of average power during the carrier-on state
			- Freq_Acc_Or_Init_Freq_Error: float: Standard deviation of frequency accuracy (BR, LE) or initial center frequency error ωi (EDR)
			- Freq_Drift: float: Standard deviation of frequency drift (BR, LE)
			- Max_Drift_Rate: float: Standard deviation of maximal drift rate (BR, LE)
			- Delta_F_299_P: float: Standard deviation of frequency deviation value Δf2 above which 99.9% of all measured Δf2 values occur (BR, LE) .
			- Omegai_Omega_0: float: Standard deviation of overall uncompensated frequency error (EDR)
			- Omega_0_Max: float: Standard deviation of maximum compensated frequency error (EDR)
			- Rms_Devm: float: Standard deviation of RMS DEVM (EDR)
			- Peak_Devm: float: Standard deviation of peak DEVM (EDR)
			- P_99_Devm: float: Standard deviation of DEVM value below which 99% of all measured DEVM values occur (EDR) .
			- Freq_Offset: float: Standard deviation of frequency offset (LE)
			- Initial_Freq_Drift: float: Standard deviation of initial frequency drift (LE)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Freq_Acc_Or_Init_Freq_Error'),
			ArgStruct.scalar_float('Freq_Drift'),
			ArgStruct.scalar_float('Max_Drift_Rate'),
			ArgStruct.scalar_float('Delta_F_299_P'),
			ArgStruct.scalar_float('Omegai_Omega_0'),
			ArgStruct.scalar_float('Omega_0_Max'),
			ArgStruct.scalar_float('Rms_Devm'),
			ArgStruct.scalar_float('Peak_Devm'),
			ArgStruct.scalar_float('P_99_Devm'),
			ArgStruct.scalar_float('Freq_Offset'),
			ArgStruct.scalar_float('Initial_Freq_Drift')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Freq_Acc_Or_Init_Freq_Error: float = None
			self.Freq_Drift: float = None
			self.Max_Drift_Rate: float = None
			self.Delta_F_299_P: float = None
			self.Omegai_Omega_0: float = None
			self.Omega_0_Max: float = None
			self.Rms_Devm: float = None
			self.Peak_Devm: float = None
			self.P_99_Devm: float = None
			self.Freq_Offset: float = None
			self.Initial_Freq_Drift: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation:SDEViation \n
		Snippet: value: FetchStruct = driver.bluetooth.measurement.multiEval.listPy.segment.modulation.standardDev.fetch(segment = repcap.Segment.Default) \n
		Returns modulation single value results for segment<no> in list mode. The command returns all parameters listed below,
		independent of the selected list mode setup. However, only for some of the parameters measured values are available. For
		the other parameters, only an indicator is returned (e.g. NAV) . \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation:SDEViation?', self.__class__.FetchStruct())

	def clone(self) -> 'StandardDevCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StandardDevCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
