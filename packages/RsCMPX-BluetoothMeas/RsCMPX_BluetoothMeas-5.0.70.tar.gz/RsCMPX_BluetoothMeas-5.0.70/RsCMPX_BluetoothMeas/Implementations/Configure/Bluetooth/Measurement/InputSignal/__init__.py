from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputSignalCls:
	"""InputSignal commands group definition. 72 total commands, 18 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputSignal", core, parent)

	@property
	def qhsl(self):
		"""qhsl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qhsl'):
			from .Qhsl import QhslCls
			self._qhsl = QhslCls(self._core, self._cmd_group)
		return self._qhsl

	@property
	def bdAddress(self):
		"""bdAddress commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bdAddress'):
			from .BdAddress import BdAddressCls
			self._bdAddress = BdAddressCls(self._core, self._cmd_group)
		return self._bdAddress

	@property
	def lap(self):
		"""lap commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_lap'):
			from .Lap import LapCls
			self._lap = LapCls(self._core, self._cmd_group)
		return self._lap

	@property
	def uap(self):
		"""uap commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_uap'):
			from .Uap import UapCls
			self._uap = UapCls(self._core, self._cmd_group)
		return self._uap

	@property
	def nap(self):
		"""nap commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_nap'):
			from .Nap import NapCls
			self._nap = NapCls(self._core, self._cmd_group)
		return self._nap

	@property
	def aacc(self):
		"""aacc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aacc'):
			from .Aacc import AaccCls
			self._aacc = AaccCls(self._core, self._cmd_group)
		return self._aacc

	@property
	def dacc(self):
		"""dacc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dacc'):
			from .Dacc import DaccCls
			self._dacc = DaccCls(self._core, self._cmd_group)
		return self._dacc

	@property
	def ptype(self):
		"""ptype commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_ptype'):
			from .Ptype import PtypeCls
			self._ptype = PtypeCls(self._core, self._cmd_group)
		return self._ptype

	@property
	def plength(self):
		"""plength commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import PlengthCls
			self._plength = PlengthCls(self._core, self._cmd_group)
		return self._plength

	@property
	def cte(self):
		"""cte commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cte'):
			from .Cte import CteCls
			self._cte = CteCls(self._core, self._cmd_group)
		return self._cte

	@property
	def dtMode(self):
		"""dtMode commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dtMode'):
			from .DtMode import DtModeCls
			self._dtMode = DtModeCls(self._core, self._cmd_group)
		return self._dtMode

	@property
	def oslots(self):
		"""oslots commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_oslots'):
			from .Oslots import OslotsCls
			self._oslots = OslotsCls(self._core, self._cmd_group)
		return self._oslots

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	@property
	def accAddress(self):
		"""accAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_accAddress'):
			from .AccAddress import AccAddressCls
			self._accAddress = AccAddressCls(self._core, self._cmd_group)
		return self._accAddress

	@property
	def synWord(self):
		"""synWord commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synWord'):
			from .SynWord import SynWordCls
			self._synWord = SynWordCls(self._core, self._cmd_group)
		return self._synWord

	@property
	def pattern(self):
		"""pattern commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import PatternCls
			self._pattern = PatternCls(self._core, self._cmd_group)
		return self._pattern

	@property
	def cscheme(self):
		"""cscheme commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cscheme'):
			from .Cscheme import CschemeCls
			self._cscheme = CschemeCls(self._core, self._cmd_group)
		return self._cscheme

	@property
	def fec(self):
		"""fec commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fec'):
			from .Fec import FecCls
			self._fec = FecCls(self._core, self._cmd_group)
		return self._fec

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.AutoManualMode:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DMODe \n
		Snippet: value: enums.AutoManualMode = driver.configure.bluetooth.measurement.inputSignal.get_dmode() \n
		Selects an algorithm which the CMP180 uses to detect the measured burst. \n
			:return: detection_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_dmode(self, detection_mode: enums.AutoManualMode) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DMODe \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.set_dmode(detection_mode = enums.AutoManualMode.AUTO) \n
		Selects an algorithm which the CMP180 uses to detect the measured burst. \n
			:param detection_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(detection_mode, enums.AutoManualMode)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:DMODe {param}')

	# noinspection PyTypeChecker
	def get_btype(self) -> enums.BurstType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BTYPe \n
		Snippet: value: enums.BurstType = driver.configure.bluetooth.measurement.inputSignal.get_btype() \n
		Specifies the measured burst / packet type. \n
			:return: burst_type: BR: Basic Rate EDR: Enhanced Data Rate LE: Low Energy
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.BurstType)

	def set_btype(self, burst_type: enums.BurstType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BTYPe \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.set_btype(burst_type = enums.BurstType.BR) \n
		Specifies the measured burst / packet type. \n
			:param burst_type: BR: Basic Rate EDR: Enhanced Data Rate LE: Low Energy
		"""
		param = Conversions.enum_scalar_to_str(burst_type, enums.BurstType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:BTYPe {param}')

	def get_asynchronize(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:ASYNchronize \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.inputSignal.get_asynchronize() \n
		Disables / enables automatic synchronization to the captured signal for an unspecified Bluetooth device address. \n
			:return: auto_synch: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:ASYNchronize?')
		return Conversions.str_to_bool(response)

	def set_asynchronize(self, auto_synch: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:ASYNchronize \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.set_asynchronize(auto_synch = False) \n
		Disables / enables automatic synchronization to the captured signal for an unspecified Bluetooth device address. \n
			:param auto_synch: No help available
		"""
		param = Conversions.bool_to_str(auto_synch)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:ASYNchronize {param}')

	def clone(self) -> 'InputSignalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputSignalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
