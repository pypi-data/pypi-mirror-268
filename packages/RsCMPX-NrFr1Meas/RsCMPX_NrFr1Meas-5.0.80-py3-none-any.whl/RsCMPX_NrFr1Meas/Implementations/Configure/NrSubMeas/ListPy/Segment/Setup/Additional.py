from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdditionalCls:
	"""Additional commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("additional", core, parent)

	def set(self, narrow_band_trigger: enums.NbTrigger, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent<no>:SETup:ADDitional \n
		Snippet: driver.configure.nrSubMeas.listPy.segment.setup.additional.set(narrow_band_trigger = enums.NbTrigger.M010, sEGMent = repcap.SEGMent.Default) \n
		No command help available \n
			:param narrow_band_trigger: No help available
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(narrow_band_trigger, enums.NbTrigger)
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SETup:ADDitional {param}')

	# noinspection PyTypeChecker
	def get(self, sEGMent=repcap.SEGMent.Default) -> enums.NbTrigger:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent<no>:SETup:ADDitional \n
		Snippet: value: enums.NbTrigger = driver.configure.nrSubMeas.listPy.segment.setup.additional.get(sEGMent = repcap.SEGMent.Default) \n
		No command help available \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: narrow_band_trigger: No help available"""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SETup:ADDitional?')
		return Conversions.str_to_scalar_enum(response, enums.NbTrigger)
