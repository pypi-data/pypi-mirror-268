from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 18 total commands, 5 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def dtx(self):
		"""dtx commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_dtx'):
			from .Dtx import DtxCls
			self._dtx = DtxCls(self._core, self._cmd_group)
		return self._dtx

	@property
	def cte(self):
		"""cte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cte'):
			from .Cte import CteCls
			self._cte = CteCls(self._core, self._cmd_group)
		return self._cte

	@property
	def mmode(self):
		"""mmode commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmode'):
			from .Mmode import MmodeCls
			self._mmode = MmodeCls(self._core, self._cmd_group)
		return self._mmode

	@property
	def mchannel(self):
		"""mchannel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mchannel'):
			from .Mchannel import MchannelCls
			self._mchannel = MchannelCls(self._core, self._cmd_group)
		return self._mchannel

	@property
	def lrStart(self):
		"""lrStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lrStart'):
			from .LrStart import LrStartCls
			self._lrStart = LrStartCls(self._core, self._cmd_group)
		return self._lrStart

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:return: external_att: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, external_att: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.set_eattenuation(external_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:param external_att: No help available
		"""
		param = Conversions.decimal_value_to_str(external_att)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rfSettings.get_umargin() \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. \n
			:return: user_margin: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. \n
			:param user_margin: No help available
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal. \n
			:return: exp_nominal_power: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nominal_power: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.set_envelope_power(exp_nominal_power = 1.0) \n
		Sets the expected nominal power of the measured RF signal. \n
			:param exp_nominal_power: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		param = Conversions.decimal_value_to_str(exp_nominal_power)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:ENPower {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rfSettings.get_frequency() \n
		Selects the center frequency of the RF analyzer. \n
			:return: analyzer_freq: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, analyzer_freq: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.set_frequency(analyzer_freq = 1.0) \n
		Selects the center frequency of the RF analyzer. \n
			:param analyzer_freq: No help available
		"""
		param = Conversions.decimal_value_to_str(analyzer_freq)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:FREQuency {param}')

	def get_rlevel(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:RLEVel \n
		Snippet: value: int = driver.configure.bluetooth.measurement.rfSettings.get_rlevel() \n
		Queries the reference level of the measured RF signal. The value is calculated as the expected peak power at the output
		of the DUT: Reference level = Expected Nominal Power + User Margin \n
			:return: reference_level: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:RLEVel?')
		return Conversions.str_to_int(response)

	def get_lr_interval(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:LRINterval \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rfSettings.get_lr_interval() \n
		Defines the measurement interval for level adjustment. \n
			:return: lvl_rang_interval: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:LRINterval?')
		return Conversions.str_to_float(response)

	def set_lr_interval(self, lvl_rang_interval: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:LRINterval \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.set_lr_interval(lvl_rang_interval = 1.0) \n
		Defines the measurement interval for level adjustment. \n
			:param lvl_rang_interval: No help available
		"""
		param = Conversions.decimal_value_to_str(lvl_rang_interval)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:LRINterval {param}')

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
