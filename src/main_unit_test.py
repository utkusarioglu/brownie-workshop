#!/home/python/venv/main/bin/python

from get_sepolia_transactions import main


def test_main():
    response = main()
    expected = "Hey there"
    assert expected == response
