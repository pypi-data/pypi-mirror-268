from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	def calculate(self, start: float = None, count: float = None, decimation: float = None) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:CURRent \n
		Snippet: value: List[enums.ResultStatus2] = driver.wlanMeas.multiEval.trace.spectrFlatness.current.calculate(start = 1.0, count = 1.0, decimation = 1.0) \n
		Return the values of the spectrum flatness traces for OFDM and OFDMA SISO signals. The results of the current, average,
		minimum and maximum traces can be retrieved. \n
		Suppressed linked return values: reliability \n
			:param start: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param count: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:param decimation: For the optional query parameters start, count and decimation, see 'Trace subarrays'.
			:return: sflat_curr: Comma-separated list power level, one value per subcarrier (including data and pilot subcarriers) The number of subcarriers depends on the WLAN standard, channel bandwidth and mode, see Table 'OFDM subcarriers'."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float, None, is_optional=True), ArgSingle('count', count, DataType.Float, None, is_optional=True), ArgSingle('decimation', decimation, DataType.Float, None, is_optional=True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TRACe:SFLatness:CURRent? {param}'.rstrip(), suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
