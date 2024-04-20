from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 4 total commands, 1 Subgroups, 2 group commands
	Repeated Capability: Mimo, default value after init: Mimo.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_mimo_get', 'repcap_mimo_set', repcap.Mimo.Nr1)

	def repcap_mimo_set(self, mimo: repcap.Mimo) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Mimo.Default
		Default value after init: Mimo.Nr1"""
		self._cmd_group.set_repcap_enum_value(mimo)

	def repcap_mimo_get(self) -> repcap.Mimo:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def segments(self):
		"""segments commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_segments'):
			from .Segments import SegmentsCls
			self._segments = SegmentsCls(self._core, self._cmd_group)
		return self._segments

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Obw_Values_Tx: List[float]: No parameter help available
			- Obw_Leri_Tx: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Obw_Values_Tx', DataType.FloatList, None, False, False, 4),
			ArgStruct('Obw_Leri_Tx', DataType.FloatList, None, False, False, 2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Obw_Values_Tx: List[float] = None
			self.Obw_Leri_Tx: List[float] = None

	def read(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:MIMO<n> \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.obw.mimo.read(mimo = repcap.Mimo.Default) \n
		Return the OBW results for MIMO measurements, antenna <n>, bandwidths with one segment. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:MIMO{mimo_cmd_val}?', self.__class__.ResultData())

	def fetch(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:MIMO<n> \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.obw.mimo.fetch(mimo = repcap.Mimo.Default) \n
		Return the OBW results for MIMO measurements, antenna <n>, bandwidths with one segment. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:MIMO{mimo_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'MimoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MimoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
