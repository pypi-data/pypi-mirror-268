from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	def read(self) -> float:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:SDEViation \n
		Snippet: value: float = driver.wlanMeas.multiEval.powerVsTime.terror.standardDev.read() \n
		Return the current, average, minimum, maximum and standard deviation timing error single value results of the power vs
		time measurement. The commands are only supported for OFDM standards. The values described below are returned by FETCh
		and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: timing_error_sdev: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:SDEViation?', suppressed)
		return Conversions.str_to_float(response)

	def fetch(self) -> float:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:SDEViation \n
		Snippet: value: float = driver.wlanMeas.multiEval.powerVsTime.terror.standardDev.fetch() \n
		Return the current, average, minimum, maximum and standard deviation timing error single value results of the power vs
		time measurement. The commands are only supported for OFDM standards. The values described below are returned by FETCh
		and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: timing_error_sdev: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:SDEViation?', suppressed)
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def calculate(self) -> enums.ResultStatus2:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:SDEViation \n
		Snippet: value: enums.ResultStatus2 = driver.wlanMeas.multiEval.powerVsTime.terror.standardDev.calculate() \n
		Return the current, average, minimum, maximum and standard deviation timing error single value results of the power vs
		time measurement. The commands are only supported for OFDM standards. The values described below are returned by FETCh
		and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: timing_error_sdev: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:PVTime:TERRor:SDEViation?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus2)
