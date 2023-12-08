#!/home/python/venv/main/bin/python

from main import main


def test_main():
  response = main()
  expected = "Hey there"
  assert(expected == response)
