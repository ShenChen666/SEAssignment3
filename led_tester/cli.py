# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click
click.disable_unicode_literals_warning = True
from led_tester import led_tester

@click.command()

# def  main(args=None):
#  """Comsole script for led_tester."""
#  click.echo("Replace this message by putting your code into "
#     "led_tester.cli.main")
#  click.echo("See click documentation at http://click.pocoo.org/")
#  return 0

@click.option("--input", default=None, help="input URI (file or URL)")

def main(input=None):
	""" Console script for led_tester."""
	print("input", input)
	insturctions = led_tester.parseFile(input)
	firstLine = insturctions.split('\n')[0]
	lights = led_tester.LightTester(firstLine)
	insturctions = led_tester.relex(insturctions)
	for i in insturctions:
		lights.apply(i)
	print("#occupied: ", lights.count())
	return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
