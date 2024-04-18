from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BrEdrChannelsRange:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SACP:MEASurement:MODE \n
		Snippet: value: enums.BrEdrChannelsRange = driver.configure.bluetooth.measurement.hdrp.sacp.measurement.get_mode() \n
		No command help available \n
			:return: meas_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SACP:MEASurement:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BrEdrChannelsRange)

	def set_mode(self, meas_mode: enums.BrEdrChannelsRange) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SACP:MEASurement:MODE \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.sacp.measurement.set_mode(meas_mode = enums.BrEdrChannelsRange.CH21) \n
		No command help available \n
			:param meas_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(meas_mode, enums.BrEdrChannelsRange)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SACP:MEASurement:MODE {param}')
