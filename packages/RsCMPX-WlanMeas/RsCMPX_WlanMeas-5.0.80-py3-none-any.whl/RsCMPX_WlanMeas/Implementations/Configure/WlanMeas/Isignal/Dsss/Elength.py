from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ElengthCls:
	"""Elength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("elength", core, parent)

	def set(self, evaluation_length_chips: int, skip_ph: bool = None) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:DSSS:ELENgth \n
		Snippet: driver.configure.wlanMeas.isignal.dsss.elength.set(evaluation_length_chips = 1, skip_ph = False) \n
		Specifies the evaluation length of the burst for DSSS signals. \n
			:param evaluation_length_chips: Number of payload chips
			:param skip_ph: OFF: measure also preamble and header ON: skip preamble and header
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('evaluation_length_chips', evaluation_length_chips, DataType.Integer), ArgSingle('skip_ph', skip_ph, DataType.Boolean, None, is_optional=True))
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:DSSS:ELENgth {param}'.rstrip())

	# noinspection PyTypeChecker
	class ElengthStruct(StructBase):
		"""Response structure. Fields: \n
			- Evaluation_Length_Chips: int: No parameter help available
			- Skip_Ph: bool: OFF: measure also preamble and header ON: skip preamble and header"""
		__meta_args_list = [
			ArgStruct.scalar_int('Evaluation_Length_Chips'),
			ArgStruct.scalar_bool('Skip_Ph')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evaluation_Length_Chips: int = None
			self.Skip_Ph: bool = None

	def get(self) -> ElengthStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:DSSS:ELENgth \n
		Snippet: value: ElengthStruct = driver.configure.wlanMeas.isignal.dsss.elength.get() \n
		Specifies the evaluation length of the burst for DSSS signals. \n
			:return: structure: for return value, see the help for ElengthStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:DSSS:ELENgth?', self.__class__.ElengthStruct())
