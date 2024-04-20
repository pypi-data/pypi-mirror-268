from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmiCls:
	"""Smi commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Smi, default value after init: Smi.Nr4"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smi", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_smi_get', 'repcap_smi_set', repcap.Smi.Nr4)

	def repcap_smi_set(self, smi: repcap.Smi) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Smi.Default
		Default value after init: Smi.Nr4"""
		self._cmd_group.set_repcap_enum_value(smi)

	def repcap_smi_get(self) -> repcap.Smi:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class SmiStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Rx_Connector_1: enums.RxConnectorExt: No parameter help available
			- Rx_Converter_1: enums.RxConverter: No parameter help available
			- Rx_Connector_2: enums.RxConnectorExt: No parameter help available
			- Rx_Converter_2: enums.RxConverter: No parameter help available
			- Rx_Connector_3: enums.RxConnector: No parameter help available
			- Rx_Converter_3: enums.RxTxConverter: No parameter help available
			- Rx_Connector_4: enums.RxConnectorExt: No parameter help available
			- Rx_Converter_4: enums.RxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector_1', enums.RxConnectorExt),
			ArgStruct.scalar_enum('Rx_Converter_1', enums.RxConverter),
			ArgStruct.scalar_enum('Rx_Connector_2', enums.RxConnectorExt),
			ArgStruct.scalar_enum('Rx_Converter_2', enums.RxConverter),
			ArgStruct.scalar_enum('Rx_Connector_3', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter_3', enums.RxTxConverter),
			ArgStruct.scalar_enum('Rx_Connector_4', enums.RxConnectorExt),
			ArgStruct.scalar_enum('Rx_Converter_4', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector_1: enums.RxConnectorExt = None
			self.Rx_Converter_1: enums.RxConverter = None
			self.Rx_Connector_2: enums.RxConnectorExt = None
			self.Rx_Converter_2: enums.RxConverter = None
			self.Rx_Connector_3: enums.RxConnector = None
			self.Rx_Converter_3: enums.RxTxConverter = None
			self.Rx_Connector_4: enums.RxConnectorExt = None
			self.Rx_Converter_4: enums.RxConverter = None

	def set(self, structure: SmiStruct, smi=repcap.Smi.Default) -> None:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:SCENario:SMI<nr> \n
		Snippet with structure: \n
		structure = driver.route.wlanMeas.scenario.smi.SmiStruct() \n
		structure.Rx_Connector_1: enums.RxConnectorExt = enums.RxConnectorExt.I11I \n
		structure.Rx_Converter_1: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Rx_Connector_2: enums.RxConnectorExt = enums.RxConnectorExt.I11I \n
		structure.Rx_Converter_2: enums.RxConverter = enums.RxConverter.IRX1 \n
		structure.Rx_Connector_3: enums.RxConnector = enums.RxConnector.I11I \n
		structure.Rx_Converter_3: enums.RxTxConverter = enums.RxTxConverter.IRX1 \n
		structure.Rx_Connector_4: enums.RxConnectorExt = enums.RxConnectorExt.I11I \n
		structure.Rx_Converter_4: enums.RxConverter = enums.RxConverter.IRX1 \n
		driver.route.wlanMeas.scenario.smi.set(structure, smi = repcap.Smi.Default) \n
		No command help available \n
			:param structure: for set value, see the help for SmiStruct structure arguments.
			:param smi: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Smi')
		"""
		smi_cmd_val = self._cmd_group.get_repcap_cmd_value(smi, repcap.Smi)
		self._core.io.write_struct(f'ROUTe:WLAN:MEASurement<Instance>:SCENario:SMI{smi_cmd_val}', structure)

	def get(self, smi=repcap.Smi.Default) -> SmiStruct:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:SCENario:SMI<nr> \n
		Snippet: value: SmiStruct = driver.route.wlanMeas.scenario.smi.get(smi = repcap.Smi.Default) \n
		No command help available \n
			:param smi: optional repeated capability selector. Default value: Nr4 (settable in the interface 'Smi')
			:return: structure: for return value, see the help for SmiStruct structure arguments."""
		smi_cmd_val = self._cmd_group.get_repcap_cmd_value(smi, repcap.Smi)
		return self._core.io.query_struct(f'ROUTe:WLAN:MEASurement<Instance>:SCENario:SMI{smi_cmd_val}?', self.__class__.SmiStruct())

	def clone(self) -> 'SmiCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SmiCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
