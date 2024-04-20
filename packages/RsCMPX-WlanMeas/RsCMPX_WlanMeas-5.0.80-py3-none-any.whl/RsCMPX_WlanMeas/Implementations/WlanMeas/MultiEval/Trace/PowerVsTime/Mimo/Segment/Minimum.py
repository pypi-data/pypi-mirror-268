from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def read(self, start: float = None, count: float = None, decimation: float = None, mimo=repcap.Mimo.Default, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:PVTime:MIMO<n>:SEGMent<seg>:MINimum \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.powerVsTime.mimo.segment.minimum.read(start = 1.0, count = 1.0, decimation = 1.0, mimo = repcap.Mimo.Default, segment = repcap.Segment.Default) \n
		Return the values of the power vs time traces for MIMO measurements and bandwidths > 160 MHz. The results are available
		for the left 160 MHz segment <1> and for the right 160 MHz segment <2>. \n
		Suppressed linked return values: reliability \n
			:param start: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param count: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param decimation: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: power_min: Comma-separated list of max 1024 time values (1024 values without subarrays)"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:PVTime:MIMO{mimo_cmd_val}:SEGMent{segment_cmd_val}:MINimum? {param}'.rstrip(), suppressed)
		return response

	def fetch(self, start: float = None, count: float = None, decimation: float = None, mimo=repcap.Mimo.Default, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:PVTime:MIMO<n>:SEGMent<seg>:MINimum \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.powerVsTime.mimo.segment.minimum.fetch(start = 1.0, count = 1.0, decimation = 1.0, mimo = repcap.Mimo.Default, segment = repcap.Segment.Default) \n
		Return the values of the power vs time traces for MIMO measurements and bandwidths > 160 MHz. The results are available
		for the left 160 MHz segment <1> and for the right 160 MHz segment <2>. \n
		Suppressed linked return values: reliability \n
			:param start: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param count: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param decimation: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: power_min: Comma-separated list of max 1024 time values (1024 values without subarrays)"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:PVTime:MIMO{mimo_cmd_val}:SEGMent{segment_cmd_val}:MINimum? {param}'.rstrip(), suppressed)
		return response
