from selfpkg.greeting import greeting


def test_correct_greetings(capfd):
    msg: str = "Hello, world!"
    greeting(msg)
    
    out, err = capfd.readouterr()
    
    assert out == msg + "\n"

