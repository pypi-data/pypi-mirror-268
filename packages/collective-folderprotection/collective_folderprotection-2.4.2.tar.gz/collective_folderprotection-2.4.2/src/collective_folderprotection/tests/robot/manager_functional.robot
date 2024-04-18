*** Settings ***

Library  Selenium2Library  timeout=10 seconds  implicit_wait=1 seconds
Resource  keywords.robot
Variables  plone/app/testing/interfaces.py

Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Variables ***

*** Test Cases ***

Manager should be able to access the 'Assign password' view
    Go to homepage
    Log In As Site Owner
    Create Password Protected Folder  Protected  pw123
    Custom Log out
    Log In As Manager User
    Go to   ${protected_folder_url}
    Page Should Contain  Assign password
    Click Link  link=Assign password
    Page Should Contain  Choose a password to protect this object and, if it is a folder, its children.

Manager should be allowed to access protected folder
    Go to homepage
    Log In As Site Owner
    Create Password Protected Folder  Protected  pw123
    Custom Log out
    Log In As Manager User
    Go to   ${protected_folder_url}
    Page Should Not Contain  This resource is password protected

Manager should not see the 'Assign password' view for a non protected folder
    Go to homepage
    Log In As Site Owner
    Create Not Protected Folder  Not-Protected
    Go to   ${not_protected_folder_url}
    Page Should Not Contain  Assign password
    Custom Log out
    Log In As Manager User
    Go to   ${not_protected_folder_url}
    Page Should Not Contain  Assign password

Manager should not be able to remove contents from protected folder
    Go to homepage
    Log In As Site Owner
    Create Delete Protected Folder  Protected
    Go to   ${protected_folder_url}
    Create Page  A Page  This is an internal page
    Go to   ${internal_protected}
    Failed Remove Content
    Go to   ${internal_protected}
    Page Should Not Contain  This page does not seem to exist
    Custom Log out
    Log In As Manager User
    Go to   ${internal_protected}
    Failed Remove Content
    Go to   ${internal_protected}
    Page Should Not Contain  This page does not seem to exist

Manager should be able to remove from protected folder disabled
    Go to homepage
    Log In As Site Owner
    Create Protected Folder Disabled  Not-Protected
    Go to   ${not_protected_folder_url}
    Create Page  A Page  This is an internal page
    Go to   ${internal_not_protected}
    Custom Remove Content
    Go to   ${internal_not_protected}
    Page Should Contain  This page does not seem to exist
    Go to   ${not_protected_folder_url}
    Create Page  A Page  This is an internal page
    Custom Log out
    Log In As Manager User
    Go to   ${internal_not_protected}
    Custom Remove Content
    Go to   ${internal_not_protected}
    Page Should Contain  This page does not seem to exist

Manager should not be able to rename content inside protected folder
    Go to homepage
    Log In As Site Owner
    Create Rename Protected Folder  Protected
    Go to   ${protected_folder_url}
    Create Page  A Page  This is an internal page
    Go to   ${internal_protected}
    Failed Rename Content  a-page  new-page  New Page
    Custom Log out
    Log In As Manager User
    Go to   ${internal_protected}
    Failed Rename Content  a-page  new-page  New Page

Manager should be able to rename content inside protected folder disabled
    Go to homepage
    Log In As Site Owner
    Create Protected Folder Disabled  Not-Protected
    Go to   ${not_protected_folder_url}
    Create Page  A Page  This is an internal page
    Go to   ${internal_not_protected}
    Rename Content  a-page  new-page  New Page
    Wait Until Page Contains  New Page
    ${BASE}=  Get Element Attribute  tag=body   data-base-url
    Should Be Equal  ${BASE}  ${not_protected_folder_url}/new-page
    Page Should Contain  New Page
    Custom Log out
    Log In As Manager User
    Go to   ${not_protected_folder_url}/new-page
    Rename Content  new-page  a-page  A Page
    Wait Until Page Contains  A Page
    ${BASE}=  Get Element Attribute  tag=body   data-base-url
    Should Be Equal  ${BASE}  ${internal_not_protected}
    Page Should Contain  A Page
