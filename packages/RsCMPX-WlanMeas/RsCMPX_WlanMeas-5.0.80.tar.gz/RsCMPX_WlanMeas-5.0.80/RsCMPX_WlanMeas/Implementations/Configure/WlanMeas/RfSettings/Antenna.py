from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AntennaCls:
	"""Antenna commands group definition. 1 total commands, 0 Subgroups, 1 group commands
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

	def set(self, connector_all: str, ext_att: float = None, enp: float = None, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:ANTenna<n> \n
		Snippet: driver.configure.wlanMeas.rfSettings.antenna.set(connector_all = rawAbc, ext_att = 1.0, enp = 1.0, antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param connector_all: No help available
			:param ext_att: No help available
			:param enp: No help available
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector_all', connector_all, DataType.RawString), ArgSingle('ext_att', ext_att, DataType.Float, None, is_optional=True), ArgSingle('enp', enp, DataType.Float, None, is_optional=True))
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:ANTenna{antenna_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Connector_Smimo: enums.ConnectorSwitch: No parameter help available
			- Connector_Tmimo: enums.RxConnectorExt: No parameter help available
			- Ext_Att: float: No parameter help available
			- Enp: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Connector_Smimo', enums.ConnectorSwitch),
			ArgStruct.scalar_enum('Connector_Tmimo', enums.RxConnectorExt),
			ArgStruct.scalar_float('Ext_Att'),
			ArgStruct.scalar_float('Enp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Connector_Smimo: enums.ConnectorSwitch = None
			self.Connector_Tmimo: enums.RxConnectorExt = None
			self.Ext_Att: float = None
			self.Enp: float = None

	def get(self, antenna=repcap.Antenna.Default) -> GetStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:ANTenna<n> \n
		Snippet: value: GetStruct = driver.configure.wlanMeas.rfSettings.antenna.get(antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:ANTenna{antenna_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'AntennaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AntennaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
