from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetupCls:
	"""Setup commands group definition. 20 total commands, 17 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	@property
	def cte(self):
		"""cte commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cte'):
			from .Cte import CteCls
			self._cte = CteCls(self._core, self._cmd_group)
		return self._cte

	@property
	def btype(self):
		"""btype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_btype'):
			from .Btype import BtypeCls
			self._btype = BtypeCls(self._core, self._cmd_group)
		return self._btype

	@property
	def ptype(self):
		"""ptype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptype'):
			from .Ptype import PtypeCls
			self._ptype = PtypeCls(self._core, self._cmd_group)
		return self._ptype

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import PatternCls
			self._pattern = PatternCls(self._core, self._cmd_group)
		return self._pattern

	@property
	def plength(self):
		"""plength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import PlengthCls
			self._plength = PlengthCls(self._core, self._cmd_group)
		return self._plength

	@property
	def oslots(self):
		"""oslots commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oslots'):
			from .Oslots import OslotsCls
			self._oslots = OslotsCls(self._core, self._cmd_group)
		return self._oslots

	@property
	def slength(self):
		"""slength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slength'):
			from .Slength import SlengthCls
			self._slength = SlengthCls(self._core, self._cmd_group)
		return self._slength

	@property
	def moException(self):
		"""moException commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_moException'):
			from .MoException import MoExceptionCls
			self._moException = MoExceptionCls(self._core, self._cmd_group)
		return self._moException

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_envelopePower'):
			from .EnvelopePower import EnvelopePowerCls
			self._envelopePower = EnvelopePowerCls(self._core, self._cmd_group)
		return self._envelopePower

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def rtrigger(self):
		"""rtrigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtrigger'):
			from .Rtrigger import RtriggerCls
			self._rtrigger = RtriggerCls(self._core, self._cmd_group)
		return self._rtrigger

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmwCls
			self._singleCmw = SingleCmwCls(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def phy(self):
		"""phy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phy'):
			from .Phy import PhyCls
			self._phy = PhyCls(self._core, self._cmd_group)
		return self._phy

	@property
	def cscheme(self):
		"""cscheme commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cscheme'):
			from .Cscheme import CschemeCls
			self._cscheme = CschemeCls(self._core, self._cmd_group)
		return self._cscheme

	@property
	def extended(self):
		"""extended commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_extended'):
			from .Extended import ExtendedCls
			self._extended = ExtendedCls(self._core, self._cmd_group)
		return self._extended

	@property
	def qhsl(self):
		"""qhsl commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_qhsl'):
			from .Qhsl import QhslCls
			self._qhsl = QhslCls(self._core, self._cmd_group)
		return self._qhsl

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Burst_Type: enums.BurstType: BR: Basic Rate EDR: Enhanced Data Rate LE: Low Energy
			- Packet_Type: enums.SegmentPacketType: Packet type expected in the segment DH1, DH3, DH5: BR packet E21P, E23P, E25P, E31P, E33P, E35P: 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5 EDR packet RFPHytest: LE test packet ADVertiser: LE advertiser RFCTe: LE with CTE test packet
			- Pattern_Type: enums.MevPatternType: Payload pattern type expected in the segment: ALL1: 11111111 P11: 10101010 OTHer: any pattern except P11, P44 and ALL1 ALTernating: the periodical change of the pattern P11, P44 P44: 11110000
			- Payload_Length: int: Payload length expected in the segment
			- No_Of_Off_Slots: int: Number of unused slots between any two occupied slots or slot sequences expected in the segment.
			- Segment_Length: int: Number of measured bursts in the segment. The sum of the length of all active segments must not exceed 6700 timeslots (1 timeslot = 625 μs duration) .
			- Meas_On_Exception: bool: Specifies whether the segment results that the CMP180 identifies as faulty or inaccurate are rejected. ON: include the erroneous bursts OFF: exclude the erroneous bursts
			- Level: float: Expected nominal power in the segment. The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
			- Frequency: float: Center frequency for the segment
			- Meas_Filter: enums.FilterWidth: Filter bandwidth for the segment NARRow: Narrowband filter WIDE: Wideband filter
			- Retrigger: bool: Optional setting parameter. Specifies whether a trigger event is required for the segment or not. The setting is ignored for the first segment of a measurement. OFF: measure the segment without retrigger ON: trigger event required"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Burst_Type', enums.BurstType),
			ArgStruct.scalar_enum('Packet_Type', enums.SegmentPacketType),
			ArgStruct.scalar_enum('Pattern_Type', enums.MevPatternType),
			ArgStruct.scalar_int('Payload_Length'),
			ArgStruct.scalar_int('No_Of_Off_Slots'),
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_bool('Meas_On_Exception'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Meas_Filter', enums.FilterWidth),
			ArgStruct.scalar_bool_optional('Retrigger')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Burst_Type: enums.BurstType = None
			self.Packet_Type: enums.SegmentPacketType = None
			self.Pattern_Type: enums.MevPatternType = None
			self.Payload_Length: int = None
			self.No_Of_Off_Slots: int = None
			self.Segment_Length: int = None
			self.Meas_On_Exception: bool = None
			self.Level: float = None
			self.Frequency: float = None
			self.Meas_Filter: enums.FilterWidth = None
			self.Retrigger: bool = None

	def set(self, structure: SetupStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup] \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.SetupStruct() \n
		structure.Burst_Type: enums.BurstType = enums.BurstType.BR \n
		structure.Packet_Type: enums.SegmentPacketType = enums.SegmentPacketType.ADVertiser \n
		structure.Pattern_Type: enums.MevPatternType = enums.MevPatternType.ALL1 \n
		structure.Payload_Length: int = 1 \n
		structure.No_Of_Off_Slots: int = 1 \n
		structure.Segment_Length: int = 1 \n
		structure.Meas_On_Exception: bool = False \n
		structure.Level: float = 1.0 \n
		structure.Frequency: float = 1.0 \n
		structure.Meas_Filter: enums.FilterWidth = enums.FilterWidth.NARRow \n
		structure.Retrigger: bool = False \n
		driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.set(structure, segment = repcap.Segment.Default) \n
		Defines the segment length, the signal properties and the analyzer settings for a selected segment. In general, this
		command must be sent for all segments to be measured. \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup', structure)

	def get(self, segment=repcap.Segment.Default) -> SetupStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup] \n
		Snippet: value: SetupStruct = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.get(segment = repcap.Segment.Default) \n
		Defines the segment length, the signal properties and the analyzer settings for a selected segment. In general, this
		command must be sent for all segments to be measured. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup?', self.__class__.SetupStruct())

	def clone(self) -> 'SetupCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SetupCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
