from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self, start: float = None, count: float = None, decimation: float = None, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:CARRier:SEGMent<seg>:CURRent \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.evMagnitude.carrier.segment.current.read(start = 1.0, count = 1.0, decimation = 1.0, segment = repcap.Segment.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param start: No help available
			:param count: No help available
			:param decimation: No help available
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: evm_vs_carr_cur: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:CARRier:SEGMent{segment_cmd_val}:CURRent? {param}'.rstrip(), suppressed)
		return response

	def fetch(self, start: float = None, count: float = None, decimation: float = None, segment=repcap.Segment.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:CARRier:SEGMent<seg>:CURRent \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.evMagnitude.carrier.segment.current.fetch(start = 1.0, count = 1.0, decimation = 1.0, segment = repcap.Segment.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param start: No help available
			:param count: No help available
			:param decimation: No help available
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: evm_vs_carr_cur: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:CARRier:SEGMent{segment_cmd_val}:CURRent? {param}'.rstrip(), suppressed)
		return response
