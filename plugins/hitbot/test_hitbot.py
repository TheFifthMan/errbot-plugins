pytest_plugins = ["errbot.backends.test"]
extra_plugin_dir = '.'

def test_command(testbot):
    testbot.push_message('!hitbot')
    assert "errbot" in testbot.pop_message()
