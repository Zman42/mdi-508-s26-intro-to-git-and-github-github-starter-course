def pytest_addoption(parser):
    parser.addoption("--data-file", action="store", default=None)
    parser.addoption("--expected", action="store", default=None)
    parser.addoption("--atol", action="store", default="1e-6")
