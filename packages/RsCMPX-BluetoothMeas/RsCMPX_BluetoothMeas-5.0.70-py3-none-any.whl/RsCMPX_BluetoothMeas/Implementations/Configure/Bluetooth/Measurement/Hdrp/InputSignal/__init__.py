from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputSignalCls:
	"""InputSignal commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputSignal", core, parent)

	@property
	def plength(self):
		"""plength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import PlengthCls
			self._plength = PlengthCls(self._core, self._cmd_group)
		return self._plength

	# noinspection PyTypeChecker
	def get_phy(self) -> enums.PhysicalLayer:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PHY \n
		Snippet: value: enums.PhysicalLayer = driver.configure.bluetooth.measurement.hdrp.inputSignal.get_phy() \n
		No command help available \n
			:return: phy: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PHY?')
		return Conversions.str_to_scalar_enum(response, enums.PhysicalLayer)

	def set_phy(self, phy: enums.PhysicalLayer) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PHY \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.inputSignal.set_phy(phy = enums.PhysicalLayer.P4HP) \n
		No command help available \n
			:param phy: No help available
		"""
		param = Conversions.enum_scalar_to_str(phy, enums.PhysicalLayer)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PHY {param}')

	# noinspection PyTypeChecker
	def get_pcoding(self) -> enums.PayloadCoding:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PCODing \n
		Snippet: value: enums.PayloadCoding = driver.configure.bluetooth.measurement.hdrp.inputSignal.get_pcoding() \n
		No command help available \n
			:return: coding: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PCODing?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadCoding)

	def set_pcoding(self, coding: enums.PayloadCoding) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PCODing \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.inputSignal.set_pcoding(coding = enums.PayloadCoding.L12D) \n
		No command help available \n
			:param coding: No help available
		"""
		param = Conversions.enum_scalar_to_str(coding, enums.PayloadCoding)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:PCODing {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.AutoManualMode:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:DMODe \n
		Snippet: value: enums.AutoManualMode = driver.configure.bluetooth.measurement.hdrp.inputSignal.get_dmode() \n
		No command help available \n
			:return: detection_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_dmode(self, detection_mode: enums.AutoManualMode) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:DMODe \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.inputSignal.set_dmode(detection_mode = enums.AutoManualMode.AUTO) \n
		No command help available \n
			:param detection_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(detection_mode, enums.AutoManualMode)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:ISIGnal:DMODe {param}')

	def clone(self) -> 'InputSignalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputSignalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
