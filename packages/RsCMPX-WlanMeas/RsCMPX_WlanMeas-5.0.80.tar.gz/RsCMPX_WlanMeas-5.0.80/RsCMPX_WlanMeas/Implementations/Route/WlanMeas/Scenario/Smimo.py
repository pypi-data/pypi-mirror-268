from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmimoCls:
	"""Smimo commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: SMimoPath, default value after init: SMimoPath.Count2"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smimo", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_sMimoPath_get', 'repcap_sMimoPath_set', repcap.SMimoPath.Count2)

	def repcap_sMimoPath_set(self, sMimoPath: repcap.SMimoPath) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SMimoPath.Default
		Default value after init: SMimoPath.Count2"""
		self._cmd_group.set_repcap_enum_value(sMimoPath)

	def repcap_sMimoPath_get(self) -> repcap.SMimoPath:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, con_tuple: enums.ConnectorTuple = None, sMimoPath=repcap.SMimoPath.Default) -> None:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:SCENario:SMIMo<PathCount> \n
		Snippet: driver.route.wlanMeas.scenario.smimo.set(con_tuple = enums.ConnectorTuple.CT12, sMimoPath = repcap.SMimoPath.Default) \n
		No command help available \n
			:param con_tuple: No help available
			:param sMimoPath: optional repeated capability selector. Default value: Count2 (settable in the interface 'Smimo')
		"""
		param = ''
		if con_tuple:
			param = Conversions.enum_scalar_to_str(con_tuple, enums.ConnectorTuple)
		sMimoPath_cmd_val = self._cmd_group.get_repcap_cmd_value(sMimoPath, repcap.SMimoPath)
		self._core.io.write(f'ROUTe:WLAN:MEASurement<Instance>:SCENario:SMIMo{sMimoPath_cmd_val} {param}'.strip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Gui_Scenario: enums.GuiScenario: No parameter help available
			- Con_Tuple: enums.ConnectorTuple: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Gui_Scenario', enums.GuiScenario),
			ArgStruct.scalar_enum('Con_Tuple', enums.ConnectorTuple)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Gui_Scenario: enums.GuiScenario = None
			self.Con_Tuple: enums.ConnectorTuple = None

	def get(self, sMimoPath=repcap.SMimoPath.Default) -> GetStruct:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:SCENario:SMIMo<PathCount> \n
		Snippet: value: GetStruct = driver.route.wlanMeas.scenario.smimo.get(sMimoPath = repcap.SMimoPath.Default) \n
		No command help available \n
			:param sMimoPath: optional repeated capability selector. Default value: Count2 (settable in the interface 'Smimo')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		sMimoPath_cmd_val = self._cmd_group.get_repcap_cmd_value(sMimoPath, repcap.SMimoPath)
		return self._core.io.query_struct(f'ROUTe:WLAN:MEASurement<Instance>:SCENario:SMIMo{sMimoPath_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'SmimoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SmimoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
