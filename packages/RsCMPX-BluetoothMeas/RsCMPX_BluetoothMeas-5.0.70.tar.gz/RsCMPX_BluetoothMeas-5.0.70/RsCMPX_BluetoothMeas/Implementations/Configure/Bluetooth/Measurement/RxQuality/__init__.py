from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxQualityCls:
	"""RxQuality commands group definition. 16 total commands, 5 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rxQuality", core, parent)

	@property
	def sensitivity(self):
		"""sensitivity commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_sensitivity'):
			from .Sensitivity import SensitivityCls
			self._sensitivity = SensitivityCls(self._core, self._cmd_group)
		return self._sensitivity

	@property
	def spotCheck(self):
		"""spotCheck commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spotCheck'):
			from .SpotCheck import SpotCheckCls
			self._spotCheck = SpotCheckCls(self._core, self._cmd_group)
		return self._spotCheck

	@property
	def per(self):
		"""per commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_per'):
			from .Per import PerCls
			self._per = PerCls(self._core, self._cmd_group)
		return self._per

	@property
	def route(self):
		"""route commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_route'):
			from .Route import RouteCls
			self._route = RouteCls(self._core, self._cmd_group)
		return self._route

	@property
	def eattenuation(self):
		"""eattenuation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Eattenuation import EattenuationCls
			self._eattenuation = EattenuationCls(self._core, self._cmd_group)
		return self._eattenuation

	def get_doffset(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:DOFFset \n
		Snippet: value: int = driver.configure.bluetooth.measurement.rxQuality.get_doffset() \n
		No command help available \n
			:return: delay_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:DOFFset?')
		return Conversions.str_to_int(response)

	def set_doffset(self, delay_offset: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:DOFFset \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.set_doffset(delay_offset = 1) \n
		No command help available \n
			:param delay_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(delay_offset)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:DOFFset {param}')

	def get_saddress(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SADDress \n
		Snippet: value: str = driver.configure.bluetooth.measurement.rxQuality.get_saddress() \n
		No command help available \n
			:return: scanner_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SADDress?')
		return trim_str_response(response)

	def set_saddress(self, scanner_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SADDress \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.set_saddress(scanner_address = rawAbc) \n
		No command help available \n
			:param scanner_address: No help available
		"""
		param = Conversions.value_to_str(scanner_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SADDress {param}')

	# noinspection PyTypeChecker
	def get_sa_type(self) -> enums.AddressType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SATYpe \n
		Snippet: value: enums.AddressType = driver.configure.bluetooth.measurement.rxQuality.get_sa_type() \n
		No command help available \n
			:return: scanner_address_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SATYpe?')
		return Conversions.str_to_scalar_enum(response, enums.AddressType)

	def set_sa_type(self, scanner_address_type: enums.AddressType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SATYpe \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.set_sa_type(scanner_address_type = enums.AddressType.PUBLic) \n
		No command help available \n
			:param scanner_address_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(scanner_address_type, enums.AddressType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SATYpe {param}')

	def get_adetect(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:ADETect \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.rxQuality.get_adetect() \n
		No command help available \n
			:return: addr_auto_user: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:ADETect?')
		return Conversions.str_to_bool(response)

	def set_adetect(self, addr_auto_user: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:ADETect \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.set_adetect(addr_auto_user = False) \n
		No command help available \n
			:param addr_auto_user: No help available
		"""
		param = Conversions.bool_to_str(addr_auto_user)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:ADETect {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.RxQualityMeasMode:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:MMODe \n
		Snippet: value: enums.RxQualityMeasMode = driver.configure.bluetooth.measurement.rxQuality.get_mmode() \n
		No command help available \n
			:return: meas_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.RxQualityMeasMode)

	def set_mmode(self, meas_mode: enums.RxQualityMeasMode) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:MMODe \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.set_mmode(meas_mode = enums.RxQualityMeasMode.PER) \n
		No command help available \n
			:param meas_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(meas_mode, enums.RxQualityMeasMode)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:MMODe {param}')

	def get_garb(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:GARB \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.rxQuality.get_garb() \n
		No command help available \n
			:return: arb_during_tx: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:GARB?')
		return Conversions.str_to_bool(response)

	def set_garb(self, arb_during_tx: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:GARB \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.set_garb(arb_during_tx = False) \n
		No command help available \n
			:param arb_during_tx: No help available
		"""
		param = Conversions.bool_to_str(arb_during_tx)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:GARB {param}')

	def get_aindex(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:AINDex \n
		Snippet: value: int = driver.configure.bluetooth.measurement.rxQuality.get_aindex() \n
		Specifies the advertiser channel index to be measured. See also Figure 'RF channel index'. \n
			:return: adv_chan_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:AINDex?')
		return Conversions.str_to_int(response)

	def set_aindex(self, adv_chan_index: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:AINDex \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.set_aindex(adv_chan_index = 1) \n
		Specifies the advertiser channel index to be measured. See also Figure 'RF channel index'. \n
			:param adv_chan_index: No help available
		"""
		param = Conversions.decimal_value_to_str(adv_chan_index)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:AINDex {param}')

	def clone(self) -> 'RxQualityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxQualityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
