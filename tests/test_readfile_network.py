import sys
sys.path.append('.')
import pytest

from click.testing import CliRunner

from led_tester import led_tester
from led_tester import cli
from led_tester import utils


def test_read_file2():
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    instructions = led_tester.parseFile(ifile)
    instructions = instructions.split('\n')[:5]
    assert instructions == ['1000', 'turn off 660,55 through 986,197', 'turn off 341,304 through 638,850', 'turn off 199,133 through 461,193', 'switch 322,558 through 977,958']