from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	@property
	def aoffset(self):
		"""aoffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aoffset'):
			from .Aoffset import AoffsetCls
			self._aoffset = AoffsetCls(self._core, self._cmd_group)
		return self._aoffset

	def get_nantenna(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:NANTenna \n
		Snippet: value: int = driver.configure.bluetooth.measurement.rfSettings.cte.lowEnergy.get_nantenna() \n
		No command help available \n
			:return: nof_antennas: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:NANTenna?')
		return Conversions.str_to_int(response)

	def set_nantenna(self, nof_antennas: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:NANTenna \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.cte.lowEnergy.set_nantenna(nof_antennas = 1) \n
		No command help available \n
			:param nof_antennas: No help available
		"""
		param = Conversions.decimal_value_to_str(nof_antennas)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:NANTenna {param}')

	def get_roffset(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:ROFFset \n
		Snippet: value: float = driver.configure.bluetooth.measurement.rfSettings.cte.lowEnergy.get_roffset() \n
		No command help available \n
			:return: ant_ref: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:ROFFset?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'LowEnergyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LowEnergyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
