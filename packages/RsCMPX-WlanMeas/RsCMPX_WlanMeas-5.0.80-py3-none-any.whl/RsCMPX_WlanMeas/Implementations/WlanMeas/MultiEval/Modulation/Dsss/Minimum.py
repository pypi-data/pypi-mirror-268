from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Mod_Type: enums.ModulationTypeC: DBPSk1: 1 Mbit/s DBPSK DQPSk2: 2 Mbit/s DQPSK CCK5: 5.5 Mbit/s CCK CCK11: 11 Mbit/s CCK
			- Plcp_Type: enums.PlcpType: Short or long PLCP
			- Payload_Length: int: No parameter help available
			- Burst_Power: float: No parameter help available
			- Evm_Peak: float: Error vector magnitude peak value
			- Evm: float: No parameter help available
			- Freq_Error: float: Center frequency error
			- Clock_Error: float: Chip clock error
			- Iq_Offset: float: No parameter help available
			- Gain_Imbalance: float: Gain imbalance
			- Quad_Error: float: Quadrature error
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Burst_Rate: float: If a modulation filter is used, the burst rate indicates the share of bursts of the selected modulation format in the bursts received. Otherwise, it returns 1."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Mod_Type', enums.ModulationTypeC),
			ArgStruct.scalar_enum('Plcp_Type', enums.PlcpType),
			ArgStruct.scalar_int('Payload_Length'),
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Evm'),
			ArgStruct.scalar_float('Freq_Error'),
			ArgStruct.scalar_float('Clock_Error'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Gain_Imbalance'),
			ArgStruct.scalar_float('Quad_Error'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Burst_Rate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Mod_Type: enums.ModulationTypeC = None
			self.Plcp_Type: enums.PlcpType = None
			self.Payload_Length: int = None
			self.Burst_Power: float = None
			self.Evm_Peak: float = None
			self.Evm: float = None
			self.Freq_Error: float = None
			self.Clock_Error: float = None
			self.Iq_Offset: float = None
			self.Gain_Imbalance: float = None
			self.Quad_Error: float = None
			self.Out_Of_Tol: float = None
			self.Burst_Rate: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:MINimum \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.modulation.dsss.minimum.read() \n
		Return the current, average, minimum, maximum and standard deviation single value results for DSSS signals. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:MINimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:MINimum \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.modulation.dsss.minimum.fetch() \n
		Return the current, average, minimum, maximum and standard deviation single value results for DSSS signals. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:MINimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Mod_Type: enums.ResultStatus2: DBPSk1: 1 Mbit/s DBPSK DQPSk2: 2 Mbit/s DQPSK CCK5: 5.5 Mbit/s CCK CCK11: 11 Mbit/s CCK
			- Plcp_Type: enums.ResultStatus2: Short or long PLCP
			- Payload_Length: enums.ResultStatus2: No parameter help available
			- Burst_Power: enums.ResultStatus2: No parameter help available
			- Evm_Peak: enums.ResultStatus2: Error vector magnitude peak value
			- Evm: enums.ResultStatus2: No parameter help available
			- Freq_Error: enums.ResultStatus2: Center frequency error
			- Clock_Error: enums.ResultStatus2: Chip clock error
			- Iq_Offset: enums.ResultStatus2: No parameter help available
			- Gain_Imbalance: enums.ResultStatus2: Gain imbalance
			- Quad_Error: enums.ResultStatus2: Quadrature error
			- Out_Of_Tol: enums.ResultStatus2: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Burst_Rate: enums.ResultStatus2: If a modulation filter is used, the burst rate indicates the share of bursts of the selected modulation format in the bursts received. Otherwise, it returns 1."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Mod_Type', enums.ResultStatus2),
			ArgStruct.scalar_enum('Plcp_Type', enums.ResultStatus2),
			ArgStruct.scalar_enum('Payload_Length', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Peak', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm', enums.ResultStatus2),
			ArgStruct.scalar_enum('Freq_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Clock_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset', enums.ResultStatus2),
			ArgStruct.scalar_enum('Gain_Imbalance', enums.ResultStatus2),
			ArgStruct.scalar_enum('Quad_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Rate', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Mod_Type: enums.ResultStatus2 = None
			self.Plcp_Type: enums.ResultStatus2 = None
			self.Payload_Length: enums.ResultStatus2 = None
			self.Burst_Power: enums.ResultStatus2 = None
			self.Evm_Peak: enums.ResultStatus2 = None
			self.Evm: enums.ResultStatus2 = None
			self.Freq_Error: enums.ResultStatus2 = None
			self.Clock_Error: enums.ResultStatus2 = None
			self.Iq_Offset: enums.ResultStatus2 = None
			self.Gain_Imbalance: enums.ResultStatus2 = None
			self.Quad_Error: enums.ResultStatus2 = None
			self.Out_Of_Tol: enums.ResultStatus2 = None
			self.Burst_Rate: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:MINimum \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.modulation.dsss.minimum.calculate() \n
		Return the current, average, minimum, maximum and standard deviation single value results for DSSS signals. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:DSSS:MINimum?', self.__class__.CalculateStruct())
