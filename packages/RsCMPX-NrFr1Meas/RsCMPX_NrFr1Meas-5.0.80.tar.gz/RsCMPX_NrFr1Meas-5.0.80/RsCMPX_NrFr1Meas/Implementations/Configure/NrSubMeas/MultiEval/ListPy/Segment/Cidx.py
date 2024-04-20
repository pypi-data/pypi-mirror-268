from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CidxCls:
	"""Cidx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cidx", core, parent)

	def set(self, connection_index: int, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIST:SEGMent<no>:CIDX \n
		Snippet: driver.configure.nrSubMeas.multiEval.listPy.segment.cidx.set(connection_index = 1, sEGMent = repcap.SEGMent.Default) \n
		Selects the RF connection index for segment <no>. For a definition of the connection indices,
		see ROUTe:NRSub:MEAS<i>:SPATh. \n
			:param connection_index: No help available
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.decimal_value_to_str(connection_index)
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CIDX {param}')

	def get(self, sEGMent=repcap.SEGMent.Default) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIST:SEGMent<no>:CIDX \n
		Snippet: value: int = driver.configure.nrSubMeas.multiEval.listPy.segment.cidx.get(sEGMent = repcap.SEGMent.Default) \n
		Selects the RF connection index for segment <no>. For a definition of the connection indices,
		see ROUTe:NRSub:MEAS<i>:SPATh. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: connection_index: No help available"""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CIDX?')
		return Conversions.str_to_int(response)
