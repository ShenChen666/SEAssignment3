import sys
sys.path.append('.')
import pytest

from click.testing import CliRunner

from led_tester import led_tester
from led_tester import cli
from led_tester import utils

def test_relex():
	cmd = 'turn on 247,321 through 1053,1053'
	m = led_tester.relex(cmd)
	assert m == [('turn on', '247', '321', '1053', '1053')]