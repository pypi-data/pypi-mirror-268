*** Settings ***

Library  Selenium2Library  timeout=10 seconds  implicit_wait=1 seconds
Resource  keywords.robot
Variables  plone/app/testing/interfaces.py

Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Variables ***

*** Test Cases ***

Owner should be allowed to access protected folder
    Go to homepage
    Log In As Contributor User
    Create Protected Folder Disabled  Protected
    Go to   ${protected_folder_url}
    Page Should Not Contain  This resource is password protected

Owner should be able to access the 'Assign password' view
    Go to homepage
    Log In As Contributor User
    Create Protected Folder Disabled  Protected
    Go to   ${protected_folder_url}
    Page Should Contain  Assign password
    Click Link  link=Assign password
    Page Should Contain  Choose a password to protect this object and, if it is a folder, its children.

Owner should not see the 'Assign password' view for a not protected folder
    Go to homepage
    Log In As Contributor User
    Create Not Protected Folder  Not-Protected
    Go to   ${not_protected_folder_url}
    Page Should Not Contain  Assign password

# XXX Icons don't work in plone 5.2
#If there are 2 protected folders, one with password and the other without, then show 2 different icons in folder_contents view
#    Go to homepage
#    Log In As Contributor User
#    Create Protected Folder  Protected
#    Go to   ${PLONE_URL}/folder_contents
#    Page Should Not Contain Image  xpath=//img[@src="${PLONE_URL}/++resource++resources/lock_locked_16.png"]
#    Page Should Contain Image  xpath=//img[@src="${PLONE_URL}/++resource++resources/lock_unlocked_16.png"]
#    Go to   ${protected_folder_url}
#    Click Link  link=Assign password
#    Input Text  css=input#form-widgets-passw_hash  thepassword
#    Click Button  Save
#    Go to   ${PLONE_URL}/folder_contents
#    Page Should Contain Image  xpath=//img[@src="${PLONE_URL}/++resource++resources/lock_locked_16.png"]
#    Page Should Not Contain Image  xpath=//img[@src="${PLONE_URL}/++resource++resources/lock_unlocked_16.png"]
#    Go to homepage
#    Create Protected Folder  ProtectedNoPassword
#    Go to   ${PLONE_URL}/folder_contents
#    Page Should Contain Image  xpath=//img[@src="${PLONE_URL}/++resource++resources/lock_locked_16.png"]
#    Page Should Contain Image  xpath=//img[@src="${PLONE_URL}/++resource++resources/lock_unlocked_16.png"]

To remove password, check the "Reset password" checkbox
    Go to homepage
    Log In As Contributor User
    Create Protected Folder Disabled  Protected
    Click Link  link=Assign password
    Input Text  css=input#form-widgets-passw_hash  thepassword
    Click Button  Save
    Go to   ${protected_folder_url}
    Click Link  link=Assign password
    Select Checkbox  css=input#form-widgets-reset_password-0
    Click Button  Save
    Page Should Contain  This content is not going to be password protected.

