from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def read(self, mimo=repcap.Mimo.Default) -> float:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:MIMO<n>:MAXimum \n
		Snippet: value: float = driver.wlanMeas.multiEval.powerVsTime.terror.mimo.maximum.read(mimo = repcap.Mimo.Default) \n
		Return the current, average, minimum, maximum and standard deviation timing error single value results of the power vs
		time MIMO measurement. The commands are only supported for OFDM standards. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: timing_error_max: No help available"""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:MIMO{mimo_cmd_val}:MAXimum?', suppressed)
		return Conversions.str_to_float(response)

	def fetch(self, mimo=repcap.Mimo.Default) -> float:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:MIMO<n>:MAXimum \n
		Snippet: value: float = driver.wlanMeas.multiEval.powerVsTime.terror.mimo.maximum.fetch(mimo = repcap.Mimo.Default) \n
		Return the current, average, minimum, maximum and standard deviation timing error single value results of the power vs
		time MIMO measurement. The commands are only supported for OFDM standards. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: timing_error_max: No help available"""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:MIMO{mimo_cmd_val}:MAXimum?', suppressed)
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def calculate(self, mimo=repcap.Mimo.Default) -> enums.ResultStatus2:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:MIMO<n>:MAXimum \n
		Snippet: value: enums.ResultStatus2 = driver.wlanMeas.multiEval.powerVsTime.terror.mimo.maximum.calculate(mimo = repcap.Mimo.Default) \n
		Return the current, average, minimum, maximum and standard deviation timing error single value results of the power vs
		time MIMO measurement. The commands are only supported for OFDM standards. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: timing_error_max: No help available"""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:MIMO{mimo_cmd_val}:MAXimum?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus2)
