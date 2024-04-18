from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtypeCls:
	"""Ptype commands group definition. 10 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptype", core, parent)

	@property
	def qhsl(self):
		"""qhsl commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_qhsl'):
			from .Qhsl import QhslCls
			self._qhsl = QhslCls(self._core, self._cmd_group)
		return self._qhsl

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	# noinspection PyTypeChecker
	def get_edrate(self) -> enums.EdrPacketType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:EDRate \n
		Snippet: value: enums.EdrPacketType = driver.configure.bluetooth.measurement.inputSignal.ptype.get_edrate() \n
		Specifies the EDR packet type of the measured signal. \n
			:return: packet_type: 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, or 3-DH5 packets
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:EDRate?')
		return Conversions.str_to_scalar_enum(response, enums.EdrPacketType)

	def set_edrate(self, packet_type: enums.EdrPacketType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:EDRate \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.ptype.set_edrate(packet_type = enums.EdrPacketType.E21P) \n
		Specifies the EDR packet type of the measured signal. \n
			:param packet_type: 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, or 3-DH5 packets
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.EdrPacketType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:EDRate {param}')

	# noinspection PyTypeChecker
	def get_brate(self) -> enums.BrPacketType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:BRATe \n
		Snippet: value: enums.BrPacketType = driver.configure.bluetooth.measurement.inputSignal.ptype.get_brate() \n
		Specifies the BR packet type of the measured signal. \n
			:return: packet_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:BRATe?')
		return Conversions.str_to_scalar_enum(response, enums.BrPacketType)

	def set_brate(self, packet_type: enums.BrPacketType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:BRATe \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.ptype.set_brate(packet_type = enums.BrPacketType.DH1) \n
		Specifies the BR packet type of the measured signal. \n
			:param packet_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.BrPacketType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:BRATe {param}')

	def clone(self) -> 'PtypeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PtypeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
