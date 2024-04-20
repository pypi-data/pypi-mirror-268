from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InfoCls:
	"""Info commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- No_Of_Users: int: No. of users
			- No_Of_Rus: int: No. of resource units
			- Guard_Interval: enums.GuardInterval: SHORt, LONG: short or long guard interval (up to 802.11ac) GI08, GI16, GI32: 0.8 μs, 1.6 μs, and 3.2 μs guard interval durations (for 802.11ax)
			- Ltf_Size: enums.LtfSize: 1x LTF (3.2 μs) , 2x LTF (6.4 μs) , 4x LTF (12.8 μs)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('No_Of_Users'),
			ArgStruct.scalar_int('No_Of_Rus'),
			ArgStruct.scalar_enum('Guard_Interval', enums.GuardInterval),
			ArgStruct.scalar_enum('Ltf_Size', enums.LtfSize)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.No_Of_Users: int = None
			self.No_Of_Rus: int = None
			self.Guard_Interval: enums.GuardInterval = None
			self.Ltf_Size: enums.LtfSize = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:OFDMa:INFO \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.ofdma.info.fetch() \n
		Queries OFDMA common information. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:OFDMa:INFO?', self.__class__.FetchStruct())
