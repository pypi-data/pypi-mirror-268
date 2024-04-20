from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Main_State: enums.ResourceState: Current state or target state of ongoing state transition OFF: measurement off RUN: measurement running RDY: measurement completed
			- Sync_State: enums.ResourceState: PEND: transition to MainState ongoing ADJ: MainState reached
			- Res_State: enums.ResourceState: QUE: waiting for resource allocation ACT: resources allocated INV: no resources allocated"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Main_State', enums.ResourceState),
			ArgStruct.scalar_enum('Sync_State', enums.ResourceState),
			ArgStruct.scalar_enum('Res_State', enums.ResourceState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Main_State: enums.ResourceState = None
			self.Sync_State: enums.ResourceState = None
			self.Res_State: enums.ResourceState = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:STATe:ALL \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.state.all.fetch() \n
		Queries the main measurement state and the measurement substates. Without query parameters, the states are returned
		immediately. With query parameters, the states are returned when the <TargetMainState> and the <TargetSyncState> are
		reached or when the <Timeout> expires. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:STATe:ALL?', self.__class__.FetchStruct())
