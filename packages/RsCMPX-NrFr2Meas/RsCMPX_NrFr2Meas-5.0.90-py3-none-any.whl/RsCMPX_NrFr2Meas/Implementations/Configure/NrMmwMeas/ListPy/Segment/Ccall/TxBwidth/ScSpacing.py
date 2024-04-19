from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScSpacingCls:
	"""ScSpacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scSpacing", core, parent)

	def set(self, scs: enums.ScSpacing, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:CCALl:TXBWidth:SCSPacing \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.ccall.txBwidth.scSpacing.set(scs = enums.ScSpacing.S120k, sEGMent = repcap.SEGMent.Default) \n
		Selects the subcarrier spacing used in segment <no>, for all carriers. \n
			:param scs: In the current software version, you must configure the same value for all segments.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(scs, enums.ScSpacing)
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CCALl:TXBWidth:SCSPacing {param}')

	# noinspection PyTypeChecker
	def get(self, sEGMent=repcap.SEGMent.Default) -> enums.ScSpacing:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:CCALl:TXBWidth:SCSPacing \n
		Snippet: value: enums.ScSpacing = driver.configure.nrMmwMeas.listPy.segment.ccall.txBwidth.scSpacing.get(sEGMent = repcap.SEGMent.Default) \n
		Selects the subcarrier spacing used in segment <no>, for all carriers. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: scs: In the current software version, you must configure the same value for all segments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CCALl:TXBWidth:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.ScSpacing)
