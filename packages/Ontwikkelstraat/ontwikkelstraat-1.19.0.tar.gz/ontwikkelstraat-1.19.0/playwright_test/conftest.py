# Add arguments to the pytest command line.
def pytest_addoption(parser):
    parser.addoption("--screenshot", action="store", default="no_screenshot")


# Make the argument usable in any test using fixtures.
def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.screenshot
    if "screenshot" in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("screenshot", [option_value])
