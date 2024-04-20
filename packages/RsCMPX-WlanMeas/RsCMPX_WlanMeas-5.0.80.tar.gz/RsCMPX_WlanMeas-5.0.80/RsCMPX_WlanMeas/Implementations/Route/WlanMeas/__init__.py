from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WlanMeasCls:
	"""WlanMeas commands group definition. 9 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wlanMeas", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_scenario'):
			from .Scenario import ScenarioCls
			self._scenario = ScenarioCls(self._core, self._cmd_group)
		return self._scenario

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	# noinspection PyTypeChecker
	class SmimoStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Gui_Scenario: enums.GuiScenario: No parameter help available
			- Controller: str: No parameter help available
			- Rx_Connector_1: enums.RxConnectorExt: No parameter help available
			- Rx_Converter_1: enums.RxConverter: No parameter help available
			- Rx_Connector_2: enums.RxConnectorExt: No parameter help available
			- Rx_Converter_2: enums.RxConverter: No parameter help available
			- Rx_Connector_3: enums.RxConnectorExt: No parameter help available
			- Rx_Converter_3: enums.RxConverter: No parameter help available
			- Rx_Connector_4: enums.RxConnectorExt: No parameter help available
			- Rx_Converter_4: enums.RxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Gui_Scenario', enums.GuiScenario),
			ArgStruct.scalar_str('Controller'),
			ArgStruct.scalar_enum('Rx_Connector_1', enums.RxConnectorExt),
			ArgStruct.scalar_enum('Rx_Converter_1', enums.RxConverter),
			ArgStruct.scalar_enum('Rx_Connector_2', enums.RxConnectorExt),
			ArgStruct.scalar_enum('Rx_Converter_2', enums.RxConverter),
			ArgStruct.scalar_enum('Rx_Connector_3', enums.RxConnectorExt),
			ArgStruct.scalar_enum('Rx_Converter_3', enums.RxConverter),
			ArgStruct.scalar_enum('Rx_Connector_4', enums.RxConnectorExt),
			ArgStruct.scalar_enum('Rx_Converter_4', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Gui_Scenario: enums.GuiScenario = None
			self.Controller: str = None
			self.Rx_Connector_1: enums.RxConnectorExt = None
			self.Rx_Converter_1: enums.RxConverter = None
			self.Rx_Connector_2: enums.RxConnectorExt = None
			self.Rx_Converter_2: enums.RxConverter = None
			self.Rx_Connector_3: enums.RxConnectorExt = None
			self.Rx_Converter_3: enums.RxConverter = None
			self.Rx_Connector_4: enums.RxConnectorExt = None
			self.Rx_Converter_4: enums.RxConverter = None

	def get_smimo(self) -> SmimoStruct:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:SMIMo \n
		Snippet: value: SmimoStruct = driver.route.wlanMeas.get_smimo() \n
		No command help available \n
			:return: structure: for return value, see the help for SmimoStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WLAN:MEASurement<Instance>:SMIMo?', self.__class__.SmimoStruct())

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.MimoScenario: No parameter help available
			- Controller: str: No parameter help available
			- Rx_Connector_1: enums.RxConnectorExt: No parameter help available
			- Rx_Converter_1: enums.RxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.MimoScenario),
			ArgStruct.scalar_str('Controller'),
			ArgStruct.scalar_enum('Rx_Connector_1', enums.RxConnectorExt),
			ArgStruct.scalar_enum('Rx_Converter_1', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.MimoScenario = None
			self.Controller: str = None
			self.Rx_Connector_1: enums.RxConnectorExt = None
			self.Rx_Converter_1: enums.RxConverter = None

	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance> \n
		Snippet: value: ValueStruct = driver.route.wlanMeas.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WLAN:MEASurement<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'WlanMeasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = WlanMeasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
