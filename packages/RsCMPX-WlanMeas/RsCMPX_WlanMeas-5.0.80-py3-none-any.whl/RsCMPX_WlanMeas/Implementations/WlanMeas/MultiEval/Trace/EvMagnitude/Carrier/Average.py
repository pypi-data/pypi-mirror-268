from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def read(self, start: float = None, count: float = None, decimation: float = None) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:CARRier:AVERage \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.evMagnitude.carrier.average.read(start = 1.0, count = 1.0, decimation = 1.0) \n
		Return the values of the EVM vs subcarrier traces for SISO connections. The results of the current, average, minimum and
		maximum traces can be retrieved. \n
		Suppressed linked return values: reliability \n
			:param start: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param count: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param decimation: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:return: evm_trace_aver: Comma-separated list of 2n+1 values, for subcarrier -n to subcarrier +n (including data, pilot and unused subcarriers / for 802.11ax, excluding subcarrier -3 to subcarrier 3) n depends on the WLAN standard, channel bandwidth and mode, see Table 'OFDM subcarriers'."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:CARRier:AVERage? {param}'.rstrip(), suppressed)
		return response

	def fetch(self, start: float = None, count: float = None, decimation: float = None) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:CARRier:AVERage \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.trace.evMagnitude.carrier.average.fetch(start = 1.0, count = 1.0, decimation = 1.0) \n
		Return the values of the EVM vs subcarrier traces for SISO connections. The results of the current, average, minimum and
		maximum traces can be retrieved. \n
		Suppressed linked return values: reliability \n
			:param start: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param count: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param decimation: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:return: evm_trace_aver: Comma-separated list of 2n+1 values, for subcarrier -n to subcarrier +n (including data, pilot and unused subcarriers / for 802.11ax, excluding subcarrier -3 to subcarrier 3) n depends on the WLAN standard, channel bandwidth and mode, see Table 'OFDM subcarriers'."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:CARRier:AVERage? {param}'.rstrip(), suppressed)
		return response
