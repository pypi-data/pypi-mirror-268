from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def read(self, start: float = None, count: float = None, decimation: float = None, rxAntenna=repcap.RxAntenna.Default, stream=repcap.Stream.Default, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:MIMO:RXANtenna<n>:STReam<s>:SEGMent<seg>:AVERage \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.spectrFlatness.mimo.rxAntenna.stream.segment.average.read(start = 1.0, count = 1.0, decimation = 1.0, rxAntenna = repcap.RxAntenna.Default, stream = repcap.Stream.Default, segment = repcap.Segment.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param start: No help available
			:param count: No help available
			:param decimation: No help available
			:param rxAntenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RxAntenna')
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: spec_flat_trace_segment_tx: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		rxAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(rxAntenna, repcap.RxAntenna)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:MIMO:RXANtenna{rxAntenna_cmd_val}:STReam{stream_cmd_val}:SEGMent{segment_cmd_val}:AVERage? {param}'.rstrip(), suppressed)
		return response

	def fetch(self, start: float = None, count: float = None, decimation: float = None, rxAntenna=repcap.RxAntenna.Default, stream=repcap.Stream.Default, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:MIMO:RXANtenna<n>:STReam<s>:SEGMent<seg>:AVERage \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.spectrFlatness.mimo.rxAntenna.stream.segment.average.fetch(start = 1.0, count = 1.0, decimation = 1.0, rxAntenna = repcap.RxAntenna.Default, stream = repcap.Stream.Default, segment = repcap.Segment.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param start: No help available
			:param count: No help available
			:param decimation: No help available
			:param rxAntenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RxAntenna')
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: spec_flat_trace_segment_tx: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		rxAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(rxAntenna, repcap.RxAntenna)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:MIMO:RXANtenna{rxAntenna_cmd_val}:STReam{stream_cmd_val}:SEGMent{segment_cmd_val}:AVERage? {param}'.rstrip(), suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self, start: float = None, count: float = None, decimation: float = None, rxAntenna=repcap.RxAntenna.Default, stream=repcap.Stream.Default, segment=repcap.Segment.Default) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:MIMO:RXANtenna<n>:STReam<s>:SEGMent<seg>:AVERage \n
		Snippet: value: List[enums.ResultStatus2] = driver.wlanMeas.multiEval.trace.spectrFlatness.mimo.rxAntenna.stream.segment.average.calculate(start = 1.0, count = 1.0, decimation = 1.0, rxAntenna = repcap.RxAntenna.Default, stream = repcap.Stream.Default, segment = repcap.Segment.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param start: No help available
			:param count: No help available
			:param decimation: No help available
			:param rxAntenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RxAntenna')
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: spec_flat_trace_segment_tx: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		rxAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(rxAntenna, repcap.RxAntenna)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:MIMO:RXANtenna{rxAntenna_cmd_val}:STReam{stream_cmd_val}:SEGMent{segment_cmd_val}:AVERage? {param}'.rstrip(), suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
