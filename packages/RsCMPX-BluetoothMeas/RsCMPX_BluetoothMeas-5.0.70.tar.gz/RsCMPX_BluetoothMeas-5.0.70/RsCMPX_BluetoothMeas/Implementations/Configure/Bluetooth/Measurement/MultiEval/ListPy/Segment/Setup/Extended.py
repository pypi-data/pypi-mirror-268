from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtendedCls:
	"""Extended commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extended", core, parent)

	# noinspection PyTypeChecker
	class ExtendedStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Burst_Type: enums.BurstType: BR: Basic Rate EDR: Enhanced Data Rate LE: Low Energy
			- Phy: enums.LePhyType: LE1M: LE 1 Msymbol/s uncoded PHY LE2M: LE 2 Msymbol/s uncoded PHY LELR: LE 1 Msymbol/s long range (LE coded PHY)
			- Coding: enums.CodingScheme: Coding S = 8 or S = 2 is relevant only for LE coded PHY.
			- Packet_Type: enums.SegmentPacketType: Packet type expected in the segment DH1, DH3, DH5: BR packet E21P, E23P, E25P, E31P, E33P, E35P: 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5 EDR packet RFPHytest: LE test packet ADVertiser: LE advertiser RFCTe: LE with CTE test packet
			- Pattern_Type: enums.MevPatternType: Payload pattern type expected in the segment. ALL1: 11111111 P11: 10101010 OTHer: any pattern except P11, P44 and ALL1 ALTernating: the periodical change of the pattern P11, P44 P44: 11110000
			- Payload_Length: int: Payload length expected in the segment
			- No_Of_Off_Slots: int: Number of unused slots between any two occupied slots or slot sequences expected in the segment.
			- Segment_Length: int: Number of measured bursts in the segment. The sum of the length of all active segments must not exceed 6700 timeslots (1 timeslot = 625 μs duration) .
			- Meas_On_Exception: bool: Specifies whether the segment results that the CMP180 identifies as faulty or inaccurate are rejected. ON: include the erroneous bursts OFF: exclude the erroneous bursts
			- Level: float: Expected nominal power in the segment. The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
			- Frequency: float: Center frequency for the segment
			- Meas_Filter: enums.FilterWidth: Filter bandwidth for the segment NARRow: Narrowband filter WIDE: Wideband filter
			- Retrigger: bool: Specifies whether a trigger event is required for the segment or not. The setting is ignored for the first segment of a measurement. OFF: measure the segment without retrigger ON: trigger event required
			- Cte_Units: int: Optional setting parameter. No. of CTE units for LE with CTE, one unit corresponds to 8 μs.
			- Cte_Type: enums.CteType: Optional setting parameter. CTE slot type for LE with CTE AOA: CTE type angle of arrival, 2 μs slot AOD1: CTE type angle of departure, 1 μs slot AOD2: CTE type angle of departure, 2 μs slot"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Burst_Type', enums.BurstType),
			ArgStruct.scalar_enum('Phy', enums.LePhyType),
			ArgStruct.scalar_enum('Coding', enums.CodingScheme),
			ArgStruct.scalar_enum('Packet_Type', enums.SegmentPacketType),
			ArgStruct.scalar_enum('Pattern_Type', enums.MevPatternType),
			ArgStruct.scalar_int('Payload_Length'),
			ArgStruct.scalar_int('No_Of_Off_Slots'),
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_bool('Meas_On_Exception'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Meas_Filter', enums.FilterWidth),
			ArgStruct.scalar_bool('Retrigger'),
			ArgStruct.scalar_int_optional('Cte_Units'),
			ArgStruct.scalar_enum_optional('Cte_Type', enums.CteType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Burst_Type: enums.BurstType = None
			self.Phy: enums.LePhyType = None
			self.Coding: enums.CodingScheme = None
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
			self.Cte_Units: int = None
			self.Cte_Type: enums.CteType = None

	def set(self, structure: ExtendedStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:EXTended \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.extended.ExtendedStruct() \n
		structure.Burst_Type: enums.BurstType = enums.BurstType.BR \n
		structure.Phy: enums.LePhyType = enums.LePhyType.LE1M \n
		structure.Coding: enums.CodingScheme = enums.CodingScheme.S2 \n
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
		structure.Cte_Units: int = 1 \n
		structure.Cte_Type: enums.CteType = enums.CteType.AOA \n
		driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.extended.set(structure, segment = repcap.Segment.Default) \n
		Defines the segment length, the signal properties including Bluetooth version 5.0 and higher, and the analyzer settings
		for a selected segment. In general, this command must be sent for all segments to be measured. \n
			:param structure: for set value, see the help for ExtendedStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:EXTended', structure)

	def get(self, segment=repcap.Segment.Default) -> ExtendedStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:EXTended \n
		Snippet: value: ExtendedStruct = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.extended.get(segment = repcap.Segment.Default) \n
		Defines the segment length, the signal properties including Bluetooth version 5.0 and higher, and the analyzer settings
		for a selected segment. In general, this command must be sent for all segments to be measured. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ExtendedStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:EXTended?', self.__class__.ExtendedStruct())
