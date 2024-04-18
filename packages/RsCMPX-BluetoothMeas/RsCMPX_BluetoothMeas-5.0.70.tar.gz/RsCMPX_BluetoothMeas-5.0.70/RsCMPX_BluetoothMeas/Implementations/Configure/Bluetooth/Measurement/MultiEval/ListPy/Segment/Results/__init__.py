from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultsCls:
	"""Results commands group definition. 7 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("results", core, parent)

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

	def set(self, enable_mod_scalar: bool, enable_pow_scalar: bool, enable_spec_obw: bool, enable_spec_acp: bool, enable_spec_gat_acp: bool, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:RESults \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.results.set(enable_mod_scalar = False, enable_pow_scalar = False, enable_spec_obw = False, enable_spec_acp = False, enable_spec_gat_acp = False, segment = repcap.Segment.Default) \n
		Enables or disables the evaluation of the particular measurement type in the segment. \n
			:param enable_mod_scalar: Enable/disable statistical modulation results
			:param enable_pow_scalar: Enable/disable statistical power results
			:param enable_spec_obw: Enable/disable the spectrum 20 dB bandwidth results (BR)
			:param enable_spec_acp: Enable/disable the spectrum ACP results (BR, LE)
			:param enable_spec_gat_acp: Enable/disable the spectrum gated ACP results (EDR)
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable_mod_scalar', enable_mod_scalar, DataType.Boolean), ArgSingle('enable_pow_scalar', enable_pow_scalar, DataType.Boolean), ArgSingle('enable_spec_obw', enable_spec_obw, DataType.Boolean), ArgSingle('enable_spec_acp', enable_spec_acp, DataType.Boolean), ArgSingle('enable_spec_gat_acp', enable_spec_gat_acp, DataType.Boolean))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:RESults {param}'.rstrip())

	# noinspection PyTypeChecker
	class ResultsStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable_Mod_Scalar: bool: Enable/disable statistical modulation results
			- Enable_Pow_Scalar: bool: Enable/disable statistical power results
			- Enable_Spec_Obw: bool: Enable/disable the spectrum 20 dB bandwidth results (BR)
			- Enable_Spec_Acp: bool: Enable/disable the spectrum ACP results (BR, LE)
			- Enable_Spec_Gat_Acp: bool: Enable/disable the spectrum gated ACP results (EDR)"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Mod_Scalar'),
			ArgStruct.scalar_bool('Enable_Pow_Scalar'),
			ArgStruct.scalar_bool('Enable_Spec_Obw'),
			ArgStruct.scalar_bool('Enable_Spec_Acp'),
			ArgStruct.scalar_bool('Enable_Spec_Gat_Acp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Mod_Scalar: bool = None
			self.Enable_Pow_Scalar: bool = None
			self.Enable_Spec_Obw: bool = None
			self.Enable_Spec_Acp: bool = None
			self.Enable_Spec_Gat_Acp: bool = None

	def get(self, segment=repcap.Segment.Default) -> ResultsStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:RESults \n
		Snippet: value: ResultsStruct = driver.configure.bluetooth.measurement.multiEval.listPy.segment.results.get(segment = repcap.Segment.Default) \n
		Enables or disables the evaluation of the particular measurement type in the segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ResultsStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:RESults?', self.__class__.ResultsStruct())

	def clone(self) -> 'ResultsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
