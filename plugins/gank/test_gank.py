pytest_plugins = ["errbot.backends.test"]
extra_plugin_dir = '.'

def test_command(testbot):
    testbot.push_message('!gank help')
    assert "Hello" in testbot.pop_message()
