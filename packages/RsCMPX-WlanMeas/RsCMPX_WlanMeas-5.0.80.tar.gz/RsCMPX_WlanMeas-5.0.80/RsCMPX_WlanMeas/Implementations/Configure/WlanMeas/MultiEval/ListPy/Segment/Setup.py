from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetupCls:
	"""Setup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Segment_Time: float: Duration of the segment
			- Meas_Time: float: Duration of measurement for the segment
			- Meas_Offset: float: Measurement offset for the segment
			- Level: float: Expected nominal power of the measured RF signal within the segment The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin
			- Frequency: float: Configures the center frequency of the RF analyzer. Set it to the center frequency of the received WLAN channel.
			- Standard: enums.IeeeStandard: DSSS: 802.11b/g (DSSS) LOFDm: 802.11a/g (OFDM) HTOFdm: 802.11n VHTofdm: 802.11ac EHTofdm: 802.11be
			- Bandwidth: enums.Bandwidth: BW05mhz: 5 MHz BW10mhz: 10 MHz BW20mhz: 20 MHz BW40mhz: 40 MHz BW80mhz: 80 MHz BW16mhz: 160 MHz BW32mhz: 320 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Segment_Time'),
			ArgStruct.scalar_float('Meas_Time'),
			ArgStruct.scalar_float('Meas_Offset'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Standard', enums.IeeeStandard),
			ArgStruct.scalar_enum('Bandwidth', enums.Bandwidth)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Time: float = None
			self.Meas_Time: float = None
			self.Meas_Offset: float = None
			self.Level: float = None
			self.Frequency: float = None
			self.Standard: enums.IeeeStandard = None
			self.Bandwidth: enums.Bandwidth = None

	def set(self, structure: SetupStruct, segmentB=repcap.SegmentB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:SETup \n
		Snippet with structure: \n
		structure = driver.configure.wlanMeas.multiEval.listPy.segment.setup.SetupStruct() \n
		structure.Segment_Time: float = 1.0 \n
		structure.Meas_Time: float = 1.0 \n
		structure.Meas_Offset: float = 1.0 \n
		structure.Level: float = 1.0 \n
		structure.Frequency: float = 1.0 \n
		structure.Standard: enums.IeeeStandard = enums.IeeeStandard.DSSS \n
		structure.Bandwidth: enums.Bandwidth = enums.Bandwidth.BW05mhz \n
		driver.configure.wlanMeas.multiEval.listPy.segment.setup.set(structure, segmentB = repcap.SegmentB.Default) \n
		Specifies burst parameter settings for segment <no> in list mode. Send this command for all segments to be measured. \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		self._core.io.write_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:SETup', structure)

	def get(self, segmentB=repcap.SegmentB.Default) -> SetupStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:SETup \n
		Snippet: value: SetupStruct = driver.configure.wlanMeas.multiEval.listPy.segment.setup.get(segmentB = repcap.SegmentB.Default) \n
		Specifies burst parameter settings for segment <no> in list mode. Send this command for all segments to be measured. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:SETup?', self.__class__.SetupStruct())
