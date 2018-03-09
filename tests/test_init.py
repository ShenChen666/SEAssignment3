import sys
sys.path.append('.')
import pytest

from click.testing import CliRunner

from led_tester import led_tester
from led_tester import cli
from led_tester import utils

def test_init():
	lights = led_tester.LightTester(5)
	lightsT = lights.__init__(5)
	assert lightsT == None