from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for spectrum emission measurements exceeding the specified transmit spectrum mask limits.
			- Frequencies: List[float]: Comma-separated list of frequencies, one value per margin The number of margins equals the number of spectrum mask areas and depends on the selected standard, see Table 'Spectrum mask areas'."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct('Frequencies', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Frequencies: List[float] = None

	def fetch(self, segmentB=repcap.SegmentB.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:TSMask:FREQuency:AVERage \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.listPy.segment.tsMask.frequency.average.fetch(segmentB = repcap.SegmentB.Default) \n
		Return the X-positions of the limit line margins of the transmit spectrum mask for list mode, segment <no>. Positions for
		the current, average, minimum, maximum and standard deviation results are returned. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:TSMask:FREQuency:AVERage?', self.__class__.FetchStruct())
