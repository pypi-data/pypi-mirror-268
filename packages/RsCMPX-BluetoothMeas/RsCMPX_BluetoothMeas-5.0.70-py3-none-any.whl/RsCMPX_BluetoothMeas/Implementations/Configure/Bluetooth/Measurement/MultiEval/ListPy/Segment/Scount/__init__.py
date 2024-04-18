from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScountCls:
	"""Scount commands group definition. 7 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	@property
	def mscalar(self):
		"""mscalar commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mscalar'):
			from .Mscalar import MscalarCls
			self._mscalar = MscalarCls(self._core, self._cmd_group)
		return self._mscalar

	@property
	def pencoding(self):
		"""pencoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pencoding'):
			from .Pencoding import PencodingCls
			self._pencoding = PencodingCls(self._core, self._cmd_group)
		return self._pencoding

	@property
	def pscalar(self):
		"""pscalar commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pscalar'):
			from .Pscalar import PscalarCls
			self._pscalar = PscalarCls(self._core, self._cmd_group)
		return self._pscalar

	@property
	def soBw(self):
		"""soBw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soBw'):
			from .SoBw import SoBwCls
			self._soBw = SoBwCls(self._core, self._cmd_group)
		return self._soBw

	@property
	def sacp(self):
		"""sacp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sacp'):
			from .Sacp import SacpCls
			self._sacp = SacpCls(self._core, self._cmd_group)
		return self._sacp

	@property
	def sgacp(self):
		"""sgacp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgacp'):
			from .Sgacp import SgacpCls
			self._sgacp = SgacpCls(self._core, self._cmd_group)
		return self._sgacp

	def set(self, mod_stat_count: int, power_stat_count: int, spec_obw_stat_cnt: int, spec_acp_stat_cnt: int, spec_gat_acp_stat_cnt: int, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SCOunt \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.scount.set(mod_stat_count = 1, power_stat_count = 1, spec_obw_stat_cnt = 1, spec_acp_stat_cnt = 1, spec_gat_acp_stat_cnt = 1, segment = repcap.Segment.Default) \n
		Defines the statistic count for the particular measurement type in the segment. \n
			:param mod_stat_count: Statistic count for statistical modulation measurement
			:param power_stat_count: Statistic count for statistical power measurement
			:param spec_obw_stat_cnt: Statistic count for spectrum 20 dB bandwidth measurement (BR)
			:param spec_acp_stat_cnt: Statistic count for spectrum ACP (BR, LE)
			:param spec_gat_acp_stat_cnt: Statistic count for spectrum gated ACP measurement (EDR)
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('mod_stat_count', mod_stat_count, DataType.Integer), ArgSingle('power_stat_count', power_stat_count, DataType.Integer), ArgSingle('spec_obw_stat_cnt', spec_obw_stat_cnt, DataType.Integer), ArgSingle('spec_acp_stat_cnt', spec_acp_stat_cnt, DataType.Integer), ArgSingle('spec_gat_acp_stat_cnt', spec_gat_acp_stat_cnt, DataType.Integer))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SCOunt {param}'.rstrip())

	# noinspection PyTypeChecker
	class ScountStruct(StructBase):
		"""Response structure. Fields: \n
			- Mod_Stat_Count: int: Statistic count for statistical modulation measurement
			- Power_Stat_Count: int: Statistic count for statistical power measurement
			- Spec_Obw_Stat_Cnt: int: Statistic count for spectrum 20 dB bandwidth measurement (BR)
			- Spec_Acp_Stat_Cnt: int: Statistic count for spectrum ACP (BR, LE)
			- Spec_Gat_Acp_Stat_Cnt: int: Statistic count for spectrum gated ACP measurement (EDR)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Mod_Stat_Count'),
			ArgStruct.scalar_int('Power_Stat_Count'),
			ArgStruct.scalar_int('Spec_Obw_Stat_Cnt'),
			ArgStruct.scalar_int('Spec_Acp_Stat_Cnt'),
			ArgStruct.scalar_int('Spec_Gat_Acp_Stat_Cnt')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Stat_Count: int = None
			self.Power_Stat_Count: int = None
			self.Spec_Obw_Stat_Cnt: int = None
			self.Spec_Acp_Stat_Cnt: int = None
			self.Spec_Gat_Acp_Stat_Cnt: int = None

	def get(self, segment=repcap.Segment.Default) -> ScountStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SCOunt \n
		Snippet: value: ScountStruct = driver.configure.bluetooth.measurement.multiEval.listPy.segment.scount.get(segment = repcap.Segment.Default) \n
		Defines the statistic count for the particular measurement type in the segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ScountStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SCOunt?', self.__class__.ScountStruct())

	def clone(self) -> 'ScountCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScountCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
