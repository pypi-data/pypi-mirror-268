from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Le1MCls:
	"""Le1M commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("le1M", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Current_Pdu_Type: enums.PduType: No parameter help available
			- Previous_Pdu_Type: enums.PduType: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Current_Pdu_Type', enums.PduType),
			ArgStruct.scalar_enum('Previous_Pdu_Type', enums.PduType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Current_Pdu_Type: enums.PduType = None
			self.Previous_Pdu_Type: enums.PduType = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PDUType:LENergy[:LE1M] \n
		Snippet: value: FetchStruct = driver.bluetooth.measurement.inputSignal.adetected.pduType.lowEnergy.le1M.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PDUType:LENergy:LE1M?', self.__class__.FetchStruct())
