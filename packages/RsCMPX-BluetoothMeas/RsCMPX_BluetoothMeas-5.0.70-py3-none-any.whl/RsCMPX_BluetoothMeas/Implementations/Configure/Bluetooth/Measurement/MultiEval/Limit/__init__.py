from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 69 total commands, 9 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def qhsl(self):
		"""qhsl commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_qhsl'):
			from .Qhsl import QhslCls
			self._qhsl = QhslCls(self._core, self._cmd_group)
		return self._qhsl

	@property
	def frange(self):
		"""frange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frange'):
			from .Frange import FrangeCls
			self._frange = FrangeCls(self._core, self._cmd_group)
		return self._frange

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	@property
	def sacp(self):
		"""sacp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sacp'):
			from .Sacp import SacpCls
			self._sacp = SacpCls(self._core, self._cmd_group)
		return self._sacp

	@property
	def soBw(self):
		"""soBw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soBw'):
			from .SoBw import SoBwCls
			self._soBw = SoBwCls(self._core, self._cmd_group)
		return self._soBw

	@property
	def cte(self):
		"""cte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cte'):
			from .Cte import CteCls
			self._cte = CteCls(self._core, self._cmd_group)
		return self._cte

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	@property
	def edrate(self):
		"""edrate commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_edrate'):
			from .Edrate import EdrateCls
			self._edrate = EdrateCls(self._core, self._cmd_group)
		return self._edrate

	@property
	def brate(self):
		"""brate commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_brate'):
			from .Brate import BrateCls
			self._brate = BrateCls(self._core, self._cmd_group)
		return self._brate

	# noinspection PyTypeChecker
	class SgacpStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Ptx_Limit: float: No parameter help available
			- Exc_Ptx_Limit: float: No parameter help available
			- No_Of_Ex_Limit: int: No parameter help available
			- Ptxm_26_N_1_Rel_Lim: float: No parameter help available
			- Ptxm_26_P_1_Rel_Lim: float: No parameter help available
			- Ptx_Enable: bool: No parameter help available
			- No_Of_Exc_Enable: bool: No parameter help available
			- Ptxm_26_N_1_Rel_Enable: bool: No parameter help available
			- Ptxm_26_P_1_Rel_Enable: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ptx_Limit'),
			ArgStruct.scalar_float('Exc_Ptx_Limit'),
			ArgStruct.scalar_int('No_Of_Ex_Limit'),
			ArgStruct.scalar_float('Ptxm_26_N_1_Rel_Lim'),
			ArgStruct.scalar_float('Ptxm_26_P_1_Rel_Lim'),
			ArgStruct.scalar_bool('Ptx_Enable'),
			ArgStruct.scalar_bool('No_Of_Exc_Enable'),
			ArgStruct.scalar_bool('Ptxm_26_N_1_Rel_Enable'),
			ArgStruct.scalar_bool('Ptxm_26_P_1_Rel_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ptx_Limit: float = None
			self.Exc_Ptx_Limit: float = None
			self.No_Of_Ex_Limit: int = None
			self.Ptxm_26_N_1_Rel_Lim: float = None
			self.Ptxm_26_P_1_Rel_Lim: float = None
			self.Ptx_Enable: bool = None
			self.No_Of_Exc_Enable: bool = None
			self.Ptxm_26_N_1_Rel_Enable: bool = None
			self.Ptxm_26_P_1_Rel_Enable: bool = None

	def get_sgacp(self) -> SgacpStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SGACp \n
		Snippet: value: SgacpStruct = driver.configure.bluetooth.measurement.multiEval.limit.get_sgacp() \n
		Defines and enables the upper limits for the Spectrum Gated ACP measurement for EDR packets: PTx, Exceptions PTx, No. of
		Exceptions, PTx–26 dB–1 (rel) , PTx–26 dB +1 (rel) , and limit check enabling. \n
			:return: structure: for return value, see the help for SgacpStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SGACp?', self.__class__.SgacpStruct())

	def set_sgacp(self, value: SgacpStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SGACp \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.limit.SgacpStruct() \n
		structure.Ptx_Limit: float = 1.0 \n
		structure.Exc_Ptx_Limit: float = 1.0 \n
		structure.No_Of_Ex_Limit: int = 1 \n
		structure.Ptxm_26_N_1_Rel_Lim: float = 1.0 \n
		structure.Ptxm_26_P_1_Rel_Lim: float = 1.0 \n
		structure.Ptx_Enable: bool = False \n
		structure.No_Of_Exc_Enable: bool = False \n
		structure.Ptxm_26_N_1_Rel_Enable: bool = False \n
		structure.Ptxm_26_P_1_Rel_Enable: bool = False \n
		driver.configure.bluetooth.measurement.multiEval.limit.set_sgacp(value = structure) \n
		Defines and enables the upper limits for the Spectrum Gated ACP measurement for EDR packets: PTx, Exceptions PTx, No. of
		Exceptions, PTx–26 dB–1 (rel) , PTx–26 dB +1 (rel) , and limit check enabling. \n
			:param value: see the help for SgacpStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SGACp', value)

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
