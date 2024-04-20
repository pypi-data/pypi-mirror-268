from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CruCls:
	"""Cru commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cru", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Value_Bin: str: No parameter help available
			- Value_Dec: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Value_Bin'),
			ArgStruct.scalar_int('Value_Dec')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Value_Bin: str = None
			self.Value_Dec: int = None

	def fetch(self, channel=repcap.Channel.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:SINFo:HEB:CHANnel<ch_index>:CFIeld:CRU \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.sinfo.heb.channel.cfield.cru.fetch(channel = repcap.Channel.Default) \n
		Queries the value of the Center 26-tone RU field signaled for the channel in HE-SIG-B common field for multi-user MIMO. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:SINFo:HEB:CHANnel{channel_cmd_val}:CFIeld:CRU?', self.__class__.FetchStruct())
