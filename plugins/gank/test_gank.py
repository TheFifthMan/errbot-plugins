pytest_plugins = ["errbot.backends.test"]
extra_plugin_dir = '.'

def test_command(testbot):
    testbot.push_message('!gank --type="fuli" --count=10')
    assert "refer" in testbot.pop_message()
