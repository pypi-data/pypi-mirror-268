from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def set(self, enable_mod: bool, enable_sem: bool, segmentB=repcap.SegmentB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:RESult \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.segment.result.set(enable_mod = False, enable_sem = False, segmentB = repcap.SegmentB.Default) \n
		Enables or disables the evaluation of results for modulation and transmit spectrum mask measurements for segment <no> in
		list mode. \n
			:param enable_mod: No help available
			:param enable_sem: No help available
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable_mod', enable_mod, DataType.Boolean), ArgSingle('enable_sem', enable_sem, DataType.Boolean))
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:RESult {param}'.rstrip())

	# noinspection PyTypeChecker
	class ResultStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable_Mod: bool: No parameter help available
			- Enable_Sem: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Mod'),
			ArgStruct.scalar_bool('Enable_Sem')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Mod: bool = None
			self.Enable_Sem: bool = None

	def get(self, segmentB=repcap.SegmentB.Default) -> ResultStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:RESult \n
		Snippet: value: ResultStruct = driver.configure.wlanMeas.multiEval.listPy.segment.result.get(segmentB = repcap.SegmentB.Default) \n
		Enables or disables the evaluation of results for modulation and transmit spectrum mask measurements for segment <no> in
		list mode. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ResultStruct structure arguments."""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:RESult?', self.__class__.ResultStruct())
