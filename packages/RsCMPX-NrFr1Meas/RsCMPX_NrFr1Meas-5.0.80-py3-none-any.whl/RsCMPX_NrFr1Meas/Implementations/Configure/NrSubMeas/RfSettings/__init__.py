from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 8 total commands, 2 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def eattenuation(self):
		"""eattenuation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Eattenuation import EattenuationCls
			self._eattenuation = EattenuationCls(self._core, self._cmd_group)
		return self._eattenuation

	@property
	def lrStart(self):
		"""lrStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lrStart'):
			from .LrStart import LrStartCls
			self._lrStart = LrStartCls(self._core, self._cmd_group)
		return self._lrStart

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.nrSubMeas.rfSettings.get_umargin() \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. \n
			:return: user_margin: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.nrSubMeas.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. \n
			:param user_margin: No help available
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.nrSubMeas.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal. \n
			:return: exp_nom_pow: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nom_pow: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: driver.configure.nrSubMeas.rfSettings.set_envelope_power(exp_nom_pow = 1.0) \n
		Sets the expected nominal power of the measured RF signal. \n
			:param exp_nom_pow: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		param = Conversions.decimal_value_to_str(exp_nom_pow)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:RFSettings:ENPower {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.nrSubMeas.rfSettings.get_frequency() \n
		No command help available \n
			:return: analyzer_freq: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, analyzer_freq: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.nrSubMeas.rfSettings.set_frequency(analyzer_freq = 1.0) \n
		No command help available \n
			:param analyzer_freq: No help available
		"""
		param = Conversions.decimal_value_to_str(analyzer_freq)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:RFSettings:FREQuency {param}')

	def get_foffset(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: value: int = driver.configure.nrSubMeas.rfSettings.get_foffset() \n
		No command help available \n
			:return: offset: No help available
		"""
		response = self._core.io.query_str_with_opc('CONFigure:NRSub:MEASurement<Instance>:RFSettings:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, offset: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: driver.configure.nrSubMeas.rfSettings.set_foffset(offset = 1) \n
		No command help available \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write_with_opc(f'CONFigure:NRSub:MEASurement<Instance>:RFSettings:FOFFset {param}')

	def get_ml_offset(self) -> float:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: value: float = driver.configure.nrSubMeas.rfSettings.get_ml_offset() \n
		No command help available \n
			:return: mix_lev_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:RFSettings:MLOFfset?')
		return Conversions.str_to_float(response)

	def set_ml_offset(self, mix_lev_offset: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: driver.configure.nrSubMeas.rfSettings.set_ml_offset(mix_lev_offset = 1.0) \n
		No command help available \n
			:param mix_lev_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(mix_lev_offset)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:RFSettings:MLOFfset {param}')

	def get_lr_interval(self) -> float:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:LRINterval \n
		Snippet: value: float = driver.configure.nrSubMeas.rfSettings.get_lr_interval() \n
		Defines the measurement interval for level adjustment. \n
			:return: lvl_rang_interval: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:RFSettings:LRINterval?')
		return Conversions.str_to_float(response)

	def set_lr_interval(self, lvl_rang_interval: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:RFSettings:LRINterval \n
		Snippet: driver.configure.nrSubMeas.rfSettings.set_lr_interval(lvl_rang_interval = 1.0) \n
		Defines the measurement interval for level adjustment. \n
			:param lvl_rang_interval: No help available
		"""
		param = Conversions.decimal_value_to_str(lvl_rang_interval)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:RFSettings:LRINterval {param}')

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
