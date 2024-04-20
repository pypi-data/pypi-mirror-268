from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Mcs_Index: int: No parameter help available
			- Nof_Ss: int: No parameter help available
			- No_Of_Sts: int: No parameter help available
			- Data_Symbols: int: No parameter help available
			- Power_Total: float: No parameter help available
			- Evm_All_Carr: float: No parameter help available
			- Evm_Data_Carr: float: No parameter help available
			- Evm_Pilot_Carr: float: No parameter help available
			- Clock_Error: float: No parameter help available
			- Freq_Error: float: No parameter help available
			- Evm_All_S_1: float: No parameter help available
			- Evm_Data_S_1: float: No parameter help available
			- Evm_Pilot_S_1: float: No parameter help available
			- Evm_All_S_2: float: No parameter help available
			- Evm_Data_S_2: float: No parameter help available
			- Evm_Pilot_S_2: float: No parameter help available
			- Evm_All_S_3: float: No parameter help available
			- Evm_Data_S_3: float: No parameter help available
			- Evm_Pilot_S_3: float: No parameter help available
			- Evm_All_S_4: float: No parameter help available
			- Evm_Data_S_4: float: No parameter help available
			- Evm_Pilot_S_4: float: No parameter help available
			- Power_Tx_1: float: No parameter help available
			- Power_Tx_2: float: No parameter help available
			- Power_Tx_3: float: No parameter help available
			- Power_Tx_4: float: No parameter help available
			- Iq_Offset_1: float: No parameter help available
			- Iq_Offset_2: float: No parameter help available
			- Iq_Offset_3: float: No parameter help available
			- Iq_Offset_4: float: No parameter help available
			- Out_Of_Tol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Mcs_Index'),
			ArgStruct.scalar_int('Nof_Ss'),
			ArgStruct.scalar_int('No_Of_Sts'),
			ArgStruct.scalar_int('Data_Symbols'),
			ArgStruct.scalar_float('Power_Total'),
			ArgStruct.scalar_float('Evm_All_Carr'),
			ArgStruct.scalar_float('Evm_Data_Carr'),
			ArgStruct.scalar_float('Evm_Pilot_Carr'),
			ArgStruct.scalar_float('Clock_Error'),
			ArgStruct.scalar_float('Freq_Error'),
			ArgStruct.scalar_float('Evm_All_S_1'),
			ArgStruct.scalar_float('Evm_Data_S_1'),
			ArgStruct.scalar_float('Evm_Pilot_S_1'),
			ArgStruct.scalar_float('Evm_All_S_2'),
			ArgStruct.scalar_float('Evm_Data_S_2'),
			ArgStruct.scalar_float('Evm_Pilot_S_2'),
			ArgStruct.scalar_float('Evm_All_S_3'),
			ArgStruct.scalar_float('Evm_Data_S_3'),
			ArgStruct.scalar_float('Evm_Pilot_S_3'),
			ArgStruct.scalar_float('Evm_All_S_4'),
			ArgStruct.scalar_float('Evm_Data_S_4'),
			ArgStruct.scalar_float('Evm_Pilot_S_4'),
			ArgStruct.scalar_float('Power_Tx_1'),
			ArgStruct.scalar_float('Power_Tx_2'),
			ArgStruct.scalar_float('Power_Tx_3'),
			ArgStruct.scalar_float('Power_Tx_4'),
			ArgStruct.scalar_float('Iq_Offset_1'),
			ArgStruct.scalar_float('Iq_Offset_2'),
			ArgStruct.scalar_float('Iq_Offset_3'),
			ArgStruct.scalar_float('Iq_Offset_4'),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mcs_Index: int = None
			self.Nof_Ss: int = None
			self.No_Of_Sts: int = None
			self.Data_Symbols: int = None
			self.Power_Total: float = None
			self.Evm_All_Carr: float = None
			self.Evm_Data_Carr: float = None
			self.Evm_Pilot_Carr: float = None
			self.Clock_Error: float = None
			self.Freq_Error: float = None
			self.Evm_All_S_1: float = None
			self.Evm_Data_S_1: float = None
			self.Evm_Pilot_S_1: float = None
			self.Evm_All_S_2: float = None
			self.Evm_Data_S_2: float = None
			self.Evm_Pilot_S_2: float = None
			self.Evm_All_S_3: float = None
			self.Evm_Data_S_3: float = None
			self.Evm_Pilot_S_3: float = None
			self.Evm_All_S_4: float = None
			self.Evm_Data_S_4: float = None
			self.Evm_Pilot_S_4: float = None
			self.Power_Tx_1: float = None
			self.Power_Tx_2: float = None
			self.Power_Tx_3: float = None
			self.Power_Tx_4: float = None
			self.Iq_Offset_1: float = None
			self.Iq_Offset_2: float = None
			self.Iq_Offset_3: float = None
			self.Iq_Offset_4: float = None
			self.Out_Of_Tol: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:MODulation:SMIMo:AVERage \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.modulation.smimo.average.read() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:SMIMo:AVERage?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:MODulation:SMIMo:AVERage \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.modulation.smimo.average.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:SMIMo:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Mcs_Index: enums.ResultStatus2: No parameter help available
			- Nof_Ss: enums.ResultStatus2: No parameter help available
			- No_Of_Sts: enums.ResultStatus2: No parameter help available
			- Data_Symbols: enums.ResultStatus2: No parameter help available
			- Power_Total: enums.ResultStatus2: No parameter help available
			- Evm_All_Carr: enums.ResultStatus2: No parameter help available
			- Evm_Data_Carr: enums.ResultStatus2: No parameter help available
			- Evm_Pilot_Carr: enums.ResultStatus2: No parameter help available
			- Clock_Error: enums.ResultStatus2: No parameter help available
			- Freq_Error: enums.ResultStatus2: No parameter help available
			- Evm_All_S_1: enums.ResultStatus2: No parameter help available
			- Evm_Data_S_1: enums.ResultStatus2: No parameter help available
			- Evm_Pilot_S_1: enums.ResultStatus2: No parameter help available
			- Evm_All_S_2: enums.ResultStatus2: No parameter help available
			- Evm_Data_S_2: enums.ResultStatus2: No parameter help available
			- Evm_Pilot_S_2: enums.ResultStatus2: No parameter help available
			- Evm_All_S_3: enums.ResultStatus2: No parameter help available
			- Evm_Data_S_3: enums.ResultStatus2: No parameter help available
			- Evm_Pilot_S_3: enums.ResultStatus2: No parameter help available
			- Evm_All_S_4: enums.ResultStatus2: No parameter help available
			- Evm_Data_S_4: enums.ResultStatus2: No parameter help available
			- Evm_Pilot_S_4: enums.ResultStatus2: No parameter help available
			- Power_Tx_1: enums.ResultStatus2: No parameter help available
			- Power_Tx_2: enums.ResultStatus2: No parameter help available
			- Power_Tx_3: enums.ResultStatus2: No parameter help available
			- Power_Tx_4: enums.ResultStatus2: No parameter help available
			- Iq_Offset_1: enums.ResultStatus2: No parameter help available
			- Iq_Offset_2: enums.ResultStatus2: No parameter help available
			- Iq_Offset_3: enums.ResultStatus2: No parameter help available
			- Iq_Offset_4: enums.ResultStatus2: No parameter help available
			- Out_Of_Tol: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mcs_Index', enums.ResultStatus2),
			ArgStruct.scalar_enum('Nof_Ss', enums.ResultStatus2),
			ArgStruct.scalar_enum('No_Of_Sts', enums.ResultStatus2),
			ArgStruct.scalar_enum('Data_Symbols', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Total', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_Carr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Clock_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Freq_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_S_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_S_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_S_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_S_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_S_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_S_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_S_3', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_S_3', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_S_3', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_S_4', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_S_4', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_S_4', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Tx_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Tx_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Tx_3', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Tx_4', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset_2', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset_3', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset_4', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mcs_Index: enums.ResultStatus2 = None
			self.Nof_Ss: enums.ResultStatus2 = None
			self.No_Of_Sts: enums.ResultStatus2 = None
			self.Data_Symbols: enums.ResultStatus2 = None
			self.Power_Total: enums.ResultStatus2 = None
			self.Evm_All_Carr: enums.ResultStatus2 = None
			self.Evm_Data_Carr: enums.ResultStatus2 = None
			self.Evm_Pilot_Carr: enums.ResultStatus2 = None
			self.Clock_Error: enums.ResultStatus2 = None
			self.Freq_Error: enums.ResultStatus2 = None
			self.Evm_All_S_1: enums.ResultStatus2 = None
			self.Evm_Data_S_1: enums.ResultStatus2 = None
			self.Evm_Pilot_S_1: enums.ResultStatus2 = None
			self.Evm_All_S_2: enums.ResultStatus2 = None
			self.Evm_Data_S_2: enums.ResultStatus2 = None
			self.Evm_Pilot_S_2: enums.ResultStatus2 = None
			self.Evm_All_S_3: enums.ResultStatus2 = None
			self.Evm_Data_S_3: enums.ResultStatus2 = None
			self.Evm_Pilot_S_3: enums.ResultStatus2 = None
			self.Evm_All_S_4: enums.ResultStatus2 = None
			self.Evm_Data_S_4: enums.ResultStatus2 = None
			self.Evm_Pilot_S_4: enums.ResultStatus2 = None
			self.Power_Tx_1: enums.ResultStatus2 = None
			self.Power_Tx_2: enums.ResultStatus2 = None
			self.Power_Tx_3: enums.ResultStatus2 = None
			self.Power_Tx_4: enums.ResultStatus2 = None
			self.Iq_Offset_1: enums.ResultStatus2 = None
			self.Iq_Offset_2: enums.ResultStatus2 = None
			self.Iq_Offset_3: enums.ResultStatus2 = None
			self.Iq_Offset_4: enums.ResultStatus2 = None
			self.Out_Of_Tol: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<instance>:MEValuation:MODulation:SMIMo:AVERage \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.modulation.smimo.average.calculate() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:SMIMo:AVERage?', self.__class__.CalculateStruct())
