from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Evm_Vs_Stream_Vs_User_All: float: No parameter help available
			- Evm_Vs_Stream_Vs_User_Data: float: No parameter help available
			- Evm_Vs_Stream_Vs_User_Pilot: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Evm_Vs_Stream_Vs_User_All'),
			ArgStruct.scalar_float('Evm_Vs_Stream_Vs_User_Data'),
			ArgStruct.scalar_float('Evm_Vs_Stream_Vs_User_Pilot')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Evm_Vs_Stream_Vs_User_All: float = None
			self.Evm_Vs_Stream_Vs_User_Data: float = None
			self.Evm_Vs_Stream_Vs_User_Pilot: float = None

	def fetch(self, user=repcap.User.Default, stream=repcap.Stream.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:MODulation:EVMagnitude:USER<user>:STReam<str>:SDEViation \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.modulation.evMagnitude.user.stream.standardDev.fetch(user = repcap.User.Default, stream = repcap.Stream.Default) \n
		Return the single value results for OFDMA MIMO measurements for the specified user and stream. There are current, average,
		minimum, maximum and standard deviation results. \n
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:EVMagnitude:USER{user_cmd_val}:STReam{stream_cmd_val}:SDEViation?', self.__class__.FetchStruct())
