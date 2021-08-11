*** Variables ***
| ${docu_dir} | tests/_docu

*** Settings ***
| Library | OperatingSystem

*** Test Cases ***
| Run testdoc_small without arguments
| | [Documentation]
| | ... | test fails and prints usage without parameters
| | ${rc} | ${output} | Run And Return Rc And Output | testdoc_small
| | Should Not Be Equal As Integers | 0 | ${rc}
| | Should Start With | ${output} | Expected at least

| Run testdoc_full without arguments
| | [Documentation]
| | ... | test fails and prints usage without parameters
| | ${rc} | ${output} | Run And Return Rc And Output | testdoc_full
| | Should Not Be Equal As Integers | 0 | ${rc}
| | Should Start With | ${output} | Expected at least

| Run testdoc_small with mandatory parameters
| | [Documentation]
| | ... | testdoc_full creates testcase documentation
| | ${rc} | ${output} | Run And Return Rc And Output | testdoc_small tests/ ${docu_dir}${/}docu_1.html
| | Should Be Equal As Integers | 0 | ${rc}
| | File Should Exist | ${docu_dir}${/}docu_1.html

| Run testdoc_full with mandatory parameters
| | [Documentation]
| | ... | testdoc_full creates testcase documentation
| | ${rc} | ${output} | Run And Return Rc And Output | testdoc_full tests/ ${docu_dir}${/}docu_2.html
| | Should Be Equal As Integers | 0 | ${rc}
| | File Should Exist | ${docu_dir}${/}docu_2.html

| Run testdoc_small with title
| | [Documentation]
| | ... | testdoc_full creates testcase documentation
| | ${rc} | ${output} | Run And Return Rc And Output | testdoc_small --title "Custom Title" tests/ ${docu_dir}${/}docu_3.html
| | Should Be Equal As Integers | 0 | ${rc}
| | File Should Exist | ${docu_dir}${/}docu_1.html
