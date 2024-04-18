from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QhslCls:
	"""Qhsl commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qhsl", core, parent)

	@property
	def phy(self):
		"""phy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phy'):
			from .Phy import PhyCls
			self._phy = PhyCls(self._core, self._cmd_group)
		return self._phy

	# noinspection PyTypeChecker
	class QhslStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Burst_Type: enums.BurstType: No parameter help available
			- Phy: enums.LePhyType: No parameter help available
			- Coding: enums.CodingScheme: No parameter help available
			- Packet_Type: enums.SegmentPacketType: No parameter help available
			- Pattern_Type: enums.MevPatternType: No parameter help available
			- Payload_Length: int: No parameter help available
			- No_Of_Off_Slots: int: No parameter help available
			- Segment_Length: int: No parameter help available
			- Meas_On_Exception: bool: No parameter help available
			- Level: float: No parameter help available
			- Frequency: float: No parameter help available
			- Meas_Filter: enums.FilterWidth: No parameter help available
			- Retrigger: bool: No parameter help available
			- Cte_Units: int: No parameter help available
			- Cte_Type: enums.CteType: No parameter help available"""
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

	def set(self, structure: QhslStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:QHSL \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.qhsl.QhslStruct() \n
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
		driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.qhsl.set(structure, segment = repcap.Segment.Default) \n
		No command help available \n
			:param structure: for set value, see the help for QhslStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:QHSL', structure)

	def get(self, segment=repcap.Segment.Default) -> QhslStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:QHSL \n
		Snippet: value: QhslStruct = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.qhsl.get(segment = repcap.Segment.Default) \n
		No command help available \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for QhslStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:QHSL?', self.__class__.QhslStruct())

	def clone(self) -> 'QhslCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = QhslCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
