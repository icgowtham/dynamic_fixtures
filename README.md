## Dynamic Pytest Fixtures

### Introduction
This application shows a way to create `pytest` `fixtures` dynamically during runtime based on some conditions passed through the command line.


### Setting Up
* Clone the repository.
```bash
git clone https://github.com/icgowtham/dynamic_fixtures.git
```

* Change to the cloned directory.
```bash
cd dynamic_fixtures
```

* Setup the virtual environment.
```bash
virtualenv -p /usr/bin/python3 env3
```

* Activate the environment.
```bash
source env3/bin/activate
```

* Install the required packages.
```bash
pip3 install -r requirements.txt
```

* Run the sample test case.
```bash
pytest -vs  --myEnv '{"type": "vm", "configure": True}' sample_testcase/test_tc.py
```
```bash
pytest -vs  --myEnv '{"type": "cloud", "configure": True}' sample_testcase/test_tc.py
```
```bash
pytest -vs  --myEnv '{"type": "hw", "configure": True}' sample_testcase/test_tc.py
```

As you can see from the output, the class responsible for the `type` parameter gets injected as a fixture onto the test which is getting executed.


### TODO
* This is just a demonstration. This can be extended to add more features.