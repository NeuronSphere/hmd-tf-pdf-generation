*** Settings ***
Library           Collections
Library           OperatingSystem
Library           hmd_lib_robot_shared.containers_lib.ContainerLib
Library           resources.PdfChecks.PdfChecks
Variables         tx_vars.py
Test Setup        Test Cleanup

*** Test Cases ***
Test PDF Generation
    [Documentation]    Runs built Transform Image
    &{context}=    Create Dictionary    title=Robot Test    filename=report
    Run Transform Container    ghcr.io/neuronsphere/hmd-tf-pdf-generation:0.1    ${context}
    File Should Exist    ./report.pdf
    Should Contain Correct Title    ./report.pdf    Robot Test

*** Keywords ***
Test Cleanup
    Remove File    ./report.pdf
