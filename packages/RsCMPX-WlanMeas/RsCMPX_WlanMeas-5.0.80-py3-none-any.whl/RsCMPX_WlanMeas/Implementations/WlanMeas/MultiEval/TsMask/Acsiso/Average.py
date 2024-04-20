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
			- Reliability: int: No parameter help available
			- Ab_Aver: float: No parameter help available
			- Bc_Aver: float: No parameter help available
			- Cd_Aver: float: No parameter help available
			- De_Aver: float: No parameter help available
			- Ed_Aver: float: No parameter help available
			- Dc_Aver: float: No parameter help available
			- Cb_Aver: float: No parameter help available
			- Ba_Aver: float: No parameter help available
			- Out_Of_Tol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ab_Aver'),
			ArgStruct.scalar_float('Bc_Aver'),
			ArgStruct.scalar_float('Cd_Aver'),
			ArgStruct.scalar_float('De_Aver'),
			ArgStruct.scalar_float('Ed_Aver'),
			ArgStruct.scalar_float('Dc_Aver'),
			ArgStruct.scalar_float('Cb_Aver'),
			ArgStruct.scalar_float('Ba_Aver'),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ab_Aver: float = None
			self.Bc_Aver: float = None
			self.Cd_Aver: float = None
			self.De_Aver: float = None
			self.Ed_Aver: float = None
			self.Dc_Aver: float = None
			self.Cb_Aver: float = None
			self.Ba_Aver: float = None
			self.Out_Of_Tol: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:AVERage \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.acsiso.average.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:AVERage?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:AVERage \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.acsiso.average.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Ab_Aver: enums.ResultStatus2: No parameter help available
			- Bc_Aver: enums.ResultStatus2: No parameter help available
			- Cd_Aver: enums.ResultStatus2: No parameter help available
			- De_Aver: enums.ResultStatus2: No parameter help available
			- Ed_Aver: enums.ResultStatus2: No parameter help available
			- Dc_Aver: enums.ResultStatus2: No parameter help available
			- Cb_Aver: enums.ResultStatus2: No parameter help available
			- Ba_Aver: enums.ResultStatus2: No parameter help available
			- Out_Of_Tol: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Ab_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Bc_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Cd_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('De_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ed_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dc_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Cb_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ba_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ab_Aver: enums.ResultStatus2 = None
			self.Bc_Aver: enums.ResultStatus2 = None
			self.Cd_Aver: enums.ResultStatus2 = None
			self.De_Aver: enums.ResultStatus2 = None
			self.Ed_Aver: enums.ResultStatus2 = None
			self.Dc_Aver: enums.ResultStatus2 = None
			self.Cb_Aver: enums.ResultStatus2 = None
			self.Ba_Aver: enums.ResultStatus2 = None
			self.Out_Of_Tol: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:AVERage \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.tsMask.acsiso.average.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:ACSiso:AVERage?', self.__class__.CalculateStruct())
