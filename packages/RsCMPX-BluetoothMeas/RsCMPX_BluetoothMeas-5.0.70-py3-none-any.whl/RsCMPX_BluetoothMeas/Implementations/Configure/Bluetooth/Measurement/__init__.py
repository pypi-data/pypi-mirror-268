from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 389 total commands, 11 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def bhRate(self):
		"""bhRate commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_bhRate'):
			from .BhRate import BhRateCls
			self._bhRate = BhRateCls(self._core, self._cmd_group)
		return self._bhRate

	@property
	def hdrp(self):
		"""hdrp commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_hdrp'):
			from .Hdrp import HdrpCls
			self._hdrp = HdrpCls(self._core, self._cmd_group)
		return self._hdrp

	@property
	def hdr(self):
		"""hdr commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_hdr'):
			from .Hdr import HdrCls
			self._hdr = HdrCls(self._core, self._cmd_group)
		return self._hdr

	@property
	def multiEval(self):
		"""multiEval commands group. 14 Sub-classes, 4 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def inputSignal(self):
		"""inputSignal commands group. 18 Sub-classes, 3 commands."""
		if not hasattr(self, '_inputSignal'):
			from .InputSignal import InputSignalCls
			self._inputSignal = InputSignalCls(self._core, self._cmd_group)
		return self._inputSignal

	@property
	def dtMode(self):
		"""dtMode commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dtMode'):
			from .DtMode import DtModeCls
			self._dtMode = DtModeCls(self._core, self._cmd_group)
		return self._dtMode

	@property
	def comSettings(self):
		"""comSettings commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_comSettings'):
			from .ComSettings import ComSettingsCls
			self._comSettings = ComSettingsCls(self._core, self._cmd_group)
		return self._comSettings

	@property
	def rxQuality(self):
		"""rxQuality commands group. 5 Sub-classes, 7 commands."""
		if not hasattr(self, '_rxQuality'):
			from .RxQuality import RxQualityCls
			self._rxQuality = RxQualityCls(self._core, self._cmd_group)
		return self._rxQuality

	@property
	def trx(self):
		"""trx commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trx'):
			from .Trx import TrxCls
			self._trx = TrxCls(self._core, self._cmd_group)
		return self._trx

	@property
	def rfSettings(self):
		"""rfSettings commands group. 5 Sub-classes, 6 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def display(self):
		"""display commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Display import DisplayCls
			self._display = DisplayCls(self._core, self._cmd_group)
		return self._display

	# noinspection PyTypeChecker
	def get_hw_interface(self) -> enums.HwInterface:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HWINterface \n
		Snippet: value: enums.HwInterface = driver.configure.bluetooth.measurement.get_hw_interface() \n
		No command help available \n
			:return: hw_interface: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HWINterface?')
		return Conversions.str_to_scalar_enum(response, enums.HwInterface)

	def set_hw_interface(self, hw_interface: enums.HwInterface) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HWINterface \n
		Snippet: driver.configure.bluetooth.measurement.set_hw_interface(hw_interface = enums.HwInterface.NONE) \n
		No command help available \n
			:param hw_interface: No help available
		"""
		param = Conversions.enum_scalar_to_str(hw_interface, enums.HwInterface)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HWINterface {param}')

	# noinspection PyTypeChecker
	def get_cprotocol(self) -> enums.CommProtocol:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:CPRotocol \n
		Snippet: value: enums.CommProtocol = driver.configure.bluetooth.measurement.get_cprotocol() \n
		No command help available \n
			:return: comm_protocol: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:CPRotocol?')
		return Conversions.str_to_scalar_enum(response, enums.CommProtocol)

	def set_cprotocol(self, comm_protocol: enums.CommProtocol) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:CPRotocol \n
		Snippet: driver.configure.bluetooth.measurement.set_cprotocol(comm_protocol = enums.CommProtocol.HCI) \n
		No command help available \n
			:param comm_protocol: No help available
		"""
		param = Conversions.enum_scalar_to_str(comm_protocol, enums.CommProtocol)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:CPRotocol {param}')

	def get_gdelay(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:GDELay \n
		Snippet: value: float = driver.configure.bluetooth.measurement.get_gdelay() \n
		No command help available \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:GDELay?')
		return Conversions.str_to_float(response)

	def set_gdelay(self, delay: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:GDELay \n
		Snippet: driver.configure.bluetooth.measurement.set_gdelay(delay = 1.0) \n
		No command help available \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:GDELay {param}')

	# noinspection PyTypeChecker
	def get_cfilter(self) -> enums.FilterWidth:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:CFILter \n
		Snippet: value: enums.FilterWidth = driver.configure.bluetooth.measurement.get_cfilter() \n
		No command help available \n
			:return: capture_filter: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:CFILter?')
		return Conversions.str_to_scalar_enum(response, enums.FilterWidth)

	def set_cfilter(self, capture_filter: enums.FilterWidth) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:CFILter \n
		Snippet: driver.configure.bluetooth.measurement.set_cfilter(capture_filter = enums.FilterWidth.NARRow) \n
		No command help available \n
			:param capture_filter: No help available
		"""
		param = Conversions.enum_scalar_to_str(capture_filter, enums.FilterWidth)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:CFILter {param}')

	def get_othreshold(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:OTHReshold \n
		Snippet: value: float = driver.configure.bluetooth.measurement.get_othreshold() \n
		No command help available \n
			:return: overdriven_threshold: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:OTHReshold?')
		return Conversions.str_to_float(response)

	def set_othreshold(self, overdriven_threshold: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:OTHReshold \n
		Snippet: driver.configure.bluetooth.measurement.set_othreshold(overdriven_threshold = 1.0) \n
		No command help available \n
			:param overdriven_threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(overdriven_threshold)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:OTHReshold {param}')

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
