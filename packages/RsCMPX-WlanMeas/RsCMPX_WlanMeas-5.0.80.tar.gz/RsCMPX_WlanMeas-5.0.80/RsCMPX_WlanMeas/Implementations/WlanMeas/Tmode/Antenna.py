from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AntennaCls:
	"""Antenna commands group definition. 3 total commands, 0 Subgroups, 3 group commands
	Repeated Capability: Antenna, default value after init: Antenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antenna_get', 'repcap_antenna_set', repcap.Antenna.Nr1)

	def repcap_antenna_set(self, antenna: repcap.Antenna) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Antenna.Default
		Default value after init: Antenna.Nr1"""
		self._cmd_group.set_repcap_enum_value(antenna)

	def repcap_antenna_get(self) -> repcap.Antenna:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Decode_Status: enums.DecodeStatus: No parameter help available
			- Mcs: int: No parameter help available
			- Power: float: No parameter help available
			- Pilot_Evm: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Decode_Status', enums.DecodeStatus),
			ArgStruct.scalar_int('Mcs'),
			ArgStruct.scalar_float('Power'),
			ArgStruct.scalar_float('Pilot_Evm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Decode_Status: enums.DecodeStatus = None
			self.Mcs: int = None
			self.Power: float = None
			self.Pilot_Evm: float = None

	def read(self, antenna=repcap.Antenna.Default) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:TMODe:ANTenna<Antennas> \n
		Snippet: value: ResultData = driver.wlanMeas.tmode.antenna.read(antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:TMODe:ANTenna{antenna_cmd_val}?', self.__class__.ResultData())

	def fetch(self, antenna=repcap.Antenna.Default) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:TMODe:ANTenna<Antennas> \n
		Snippet: value: ResultData = driver.wlanMeas.tmode.antenna.fetch(antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:TMODe:ANTenna{antenna_cmd_val}?', self.__class__.ResultData())

	def initiate(self, antenna=repcap.Antenna.Default, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:WLAN:MEASurement<Instance>:TMODe:ANTenna<Antennas> \n
		Snippet: driver.wlanMeas.tmode.antenna.initiate(antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write_with_opc(f'INITiate:WLAN:MEASurement<Instance>:TMODe:ANTenna{antenna_cmd_val}', opc_timeout_ms)

	def clone(self) -> 'AntennaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AntennaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
