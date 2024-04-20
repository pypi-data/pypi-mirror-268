from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReservedCls:
	"""Reserved commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Reserved, default value after init: Reserved.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reserved", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_reserved_get', 'repcap_reserved_set', repcap.Reserved.Nr1)

	def repcap_reserved_set(self, reserved: repcap.Reserved) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Reserved.Default
		Default value after init: Reserved.Nr1"""
		self._cmd_group.set_repcap_enum_value(reserved)

	def repcap_reserved_get(self) -> repcap.Reserved:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

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

	def fetch(self, reserved=repcap.Reserved.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:SINFo:HETB:REServed<index> \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.sinfo.hetb.reserved.fetch(reserved = repcap.Reserved.Default) \n
		Queries the value of Reserved field signaled in HE signal field for trigger based uplink single user MIMO (HE-SIG-A) . \n
			:param reserved: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Reserved')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		reserved_cmd_val = self._cmd_group.get_repcap_cmd_value(reserved, repcap.Reserved)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:SINFo:HETB:REServed{reserved_cmd_val}?', self.__class__.FetchStruct())

	def clone(self) -> 'ReservedCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ReservedCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
