from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.LeChannelsRange:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:QHSL:MEASurement:MODE \n
		Snippet: value: enums.LeChannelsRange = driver.configure.bluetooth.measurement.multiEval.sacp.qhsl.measurement.get_mode() \n
		No command help available \n
			:return: meas_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:QHSL:MEASurement:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.LeChannelsRange)

	def set_mode(self, meas_mode: enums.LeChannelsRange) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:QHSL:MEASurement:MODE \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.sacp.qhsl.measurement.set_mode(meas_mode = enums.LeChannelsRange.CH10) \n
		No command help available \n
			:param meas_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(meas_mode, enums.LeChannelsRange)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SACP:QHSL:MEASurement:MODE {param}')
