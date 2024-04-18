from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DtxCls:
	"""Dtx commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtx", core, parent)

	# noinspection PyTypeChecker
	def get_st_error(self) -> enums.LeSymolTimeError:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:STERror \n
		Snippet: value: enums.LeSymolTimeError = driver.configure.bluetooth.measurement.rfSettings.dtx.get_st_error() \n
		No command help available \n
			:return: sym_tim_err: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:STERror?')
		return Conversions.str_to_scalar_enum(response, enums.LeSymolTimeError)

	def set_st_error(self, sym_tim_err: enums.LeSymolTimeError) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:STERror \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.dtx.set_st_error(sym_tim_err = enums.LeSymolTimeError.NEG50) \n
		No command help available \n
			:param sym_tim_err: No help available
		"""
		param = Conversions.enum_scalar_to_str(sym_tim_err, enums.LeSymolTimeError)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:STERror {param}')

	def get_foffset(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:FOFFset \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rfSettings.dtx.get_foffset() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, level: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:FOFFset \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.dtx.set_foffset(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:FOFFset {param}')

	def get_mindex(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:MINDex \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rfSettings.dtx.get_mindex() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:MINDex?')
		return Conversions.str_to_float(response)

	def set_mindex(self, level: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:MINDex \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.dtx.set_mindex(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX:MINDex {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.rfSettings.dtx.get_value() \n
		No command help available \n
			:return: dtx_state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX?')
		return Conversions.str_to_bool(response)

	def set_value(self, dtx_state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.dtx.set_value(dtx_state = False) \n
		No command help available \n
			:param dtx_state: No help available
		"""
		param = Conversions.bool_to_str(dtx_state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:DTX {param}')
