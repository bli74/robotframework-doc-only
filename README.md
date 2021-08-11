# Welcome to Robot Framework Doc Only

## Motivation
Robotframework offers module robot.testdoc to generate 
an HTML documentation of the testcases.
This documentation includes technical details, that may
not be relevant for readers, who are just interested in
the business cases covered by the tests.

Additionally robot does not install a shell script to
call testdoc directly. That is different to the similar
tool libdoc for keyword documentation. 

## Getting started

```
    $ pip install robotframework-doc-only
    $ testdoc_small ${ROBOT_TEST_ROOT} ${DOCU_HTML_FILE}
    # OR
    $ testdoc_full ${ROBOT_TEST_ROOT} ${DOCU_HTML_FILE}
```

## Websites

Source code, screenshots, and additional documentation can be
found here:

* Source code: https://github.com/bli74/robotframework-doc-only
