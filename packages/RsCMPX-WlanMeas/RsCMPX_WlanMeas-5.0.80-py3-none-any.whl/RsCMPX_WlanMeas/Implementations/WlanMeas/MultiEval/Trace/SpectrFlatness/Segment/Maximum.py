from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def read(self, start: float = None, count: float = None, decimation: float = None, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:SEGMent<seg>:MAXimum \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.spectrFlatness.segment.maximum.read(start = 1.0, count = 1.0, decimation = 1.0, segment = repcap.Segment.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param start: No help available
			:param count: No help available
			:param decimation: No help available
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: spec_flat_trace_segment_max: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:SEGMent{segment_cmd_val}:MAXimum? {param}'.rstrip(), suppressed)
		return response

	def fetch(self, start: float = None, count: float = None, decimation: float = None, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:SEGMent<seg>:MAXimum \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.spectrFlatness.segment.maximum.fetch(start = 1.0, count = 1.0, decimation = 1.0, segment = repcap.Segment.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param start: No help available
			:param count: No help available
			:param decimation: No help available
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: spec_flat_trace_segment_max: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:SEGMent{segment_cmd_val}:MAXimum? {param}'.rstrip(), suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self, start: float = None, count: float = None, decimation: float = None, segment=repcap.Segment.Default) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:SEGMent<seg>:MAXimum \n
		Snippet: value: List[enums.ResultStatus2] = driver.wlanMeas.multiEval.trace.spectrFlatness.segment.maximum.calculate(start = 1.0, count = 1.0, decimation = 1.0, segment = repcap.Segment.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param start: No help available
			:param count: No help available
			:param decimation: No help available
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: spec_flat_trace_segment_max: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:SEGMent{segment_cmd_val}:MAXimum? {param}'.rstrip(), suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
