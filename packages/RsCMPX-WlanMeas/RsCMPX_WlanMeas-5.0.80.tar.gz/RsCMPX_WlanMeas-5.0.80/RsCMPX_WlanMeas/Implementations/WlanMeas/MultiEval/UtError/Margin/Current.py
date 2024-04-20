from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self, utError=repcap.UtError.Default) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:UTERror<n>:MARGin:CURRent \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.utError.margin.current.read(utError = repcap.UtError.Default) \n
		Returns the margin values of the unused tone error measurement for the current, average, minimum and maximum traces.
		A positive margin indicates a violation of the unused tone error limit line. The respective trace value is located above
		the upper limit line. The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param utError: optional repeated capability selector. Default value: Nr1 (settable in the interface 'UtError')
			:return: ute_margin: Comma-separated list of margins to the unused tone error limits, one value per each 26-tone RU. The total number of RUs depends on the bandwidth, see table below."""
		utError_cmd_val = self._cmd_group.get_repcap_cmd_value(utError, repcap.UtError)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:UTERror{utError_cmd_val}:MARGin:CURRent?', suppressed)
		return response

	def fetch(self, utError=repcap.UtError.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:UTERror<n>:MARGin:CURRent \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.utError.margin.current.fetch(utError = repcap.UtError.Default) \n
		Returns the margin values of the unused tone error measurement for the current, average, minimum and maximum traces.
		A positive margin indicates a violation of the unused tone error limit line. The respective trace value is located above
		the upper limit line. The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param utError: optional repeated capability selector. Default value: Nr1 (settable in the interface 'UtError')
			:return: ute_margin: Comma-separated list of margins to the unused tone error limits, one value per each 26-tone RU. The total number of RUs depends on the bandwidth, see table below."""
		utError_cmd_val = self._cmd_group.get_repcap_cmd_value(utError, repcap.UtError)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:UTERror{utError_cmd_val}:MARGin:CURRent?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self, utError=repcap.UtError.Default) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:UTERror<n>:MARGin:CURRent \n
		Snippet: value: List[enums.ResultStatus2] = driver.wlanMeas.multiEval.utError.margin.current.calculate(utError = repcap.UtError.Default) \n
		Returns the margin values of the unused tone error measurement for the current, average, minimum and maximum traces.
		A positive margin indicates a violation of the unused tone error limit line. The respective trace value is located above
		the upper limit line. The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param utError: optional repeated capability selector. Default value: Nr1 (settable in the interface 'UtError')
			:return: ute_margin: Comma-separated list of margins to the unused tone error limits, one value per each 26-tone RU. The total number of RUs depends on the bandwidth, see table below."""
		utError_cmd_val = self._cmd_group.get_repcap_cmd_value(utError, repcap.UtError)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:UTERror{utError_cmd_val}:MARGin:CURRent?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
