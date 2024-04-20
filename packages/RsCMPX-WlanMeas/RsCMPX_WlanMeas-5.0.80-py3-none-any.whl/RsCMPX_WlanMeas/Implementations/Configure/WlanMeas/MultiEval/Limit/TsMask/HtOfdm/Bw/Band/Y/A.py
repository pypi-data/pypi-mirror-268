from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ACls:
	"""A commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)

	def set(self, tsm_lim_yrel_lev_a: float, bandwidthC=repcap.BandwidthC.Default, band=repcap.Band.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW<bandwidth>:BAND<band>:Y:A \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.htOfdm.bw.band.y.a.set(tsm_lim_yrel_lev_a = 1.0, bandwidthC = repcap.BandwidthC.Default, band = repcap.Band.Default) \n
		Defines the relative spectral density limit for point A (frequency offset: 2*bandwidth) on the transmit spectrum mask for
		802.11n signals with the specified <bandwidth> and the selected <band>. See 'Transmit spectrum mask OFDM, default masks'
		for background information. \n
			:param tsm_lim_yrel_lev_a: No help available
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:param band: optional repeated capability selector. Default value: Nr2 (settable in the interface 'Band')
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_a)
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		band_cmd_val = self._cmd_group.get_repcap_cmd_value(band, repcap.Band)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW{bandwidthC_cmd_val}:BAND{band_cmd_val}:Y:A {param}')

	def get(self, bandwidthC=repcap.BandwidthC.Default, band=repcap.Band.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW<bandwidth>:BAND<band>:Y:A \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.tsMask.htOfdm.bw.band.y.a.get(bandwidthC = repcap.BandwidthC.Default, band = repcap.Band.Default) \n
		Defines the relative spectral density limit for point A (frequency offset: 2*bandwidth) on the transmit spectrum mask for
		802.11n signals with the specified <bandwidth> and the selected <band>. See 'Transmit spectrum mask OFDM, default masks'
		for background information. \n
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:param band: optional repeated capability selector. Default value: Nr2 (settable in the interface 'Band')
			:return: tsm_lim_yrel_lev_a: No help available"""
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		band_cmd_val = self._cmd_group.get_repcap_cmd_value(band, repcap.Band)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HTOFdm:BW{bandwidthC_cmd_val}:BAND{band_cmd_val}:Y:A?')
		return Conversions.str_to_float(response)
