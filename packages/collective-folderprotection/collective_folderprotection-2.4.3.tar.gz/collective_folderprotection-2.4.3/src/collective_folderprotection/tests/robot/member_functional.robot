*** Settings ***

Library  Selenium2Library  timeout=10 seconds  implicit_wait=1 seconds
Resource  keywords.robot
Variables  plone/app/testing/interfaces.py

Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Variables ***

*** Test Cases ***

Member can access a folder that was not given a password
    Go to homepage
    Log In As Site Owner
    Create Protected Folder Disabled  Protected
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Not Contain  This resource is password protected

Member can access protected folder after providing password
    Go to homepage
    Log In As Site Owner
    Create Password Protected Folder  Protected  thepassword
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Contain  This resource is password protected
    Input Text  css=input#password  thepassword
    Click Button  submit
    Page Should Not Contain  This resource is password protected
    
Member should be redirected to the inner content where he requested access in the first place
    Go to homepage
    Log In As Site Owner
    Create Password Protected Folder  Protected  thepassword
    Go to   ${protected_folder_url}
    Create Page  A Page  This is an internal page
    Custom Log out
    Log In As Test User
    Go to   ${internal_protected}
    Page Should Contain  This resource is password protected
    Input Text  css=input#password  thepassword
    Click Button  submit
    Page Should Not Contain  This resource is password protected
    Page Should Contain  This is an internal page
    
Member can still access a folder that is not protected
    Go to homepage
    Log In As Site Owner
    Create Protected Folder Disabled  Not-Protected
    Create Page  A Page  This is an internal page
    Custom Log out
    Log In As Test User
    Go to   ${internal_not_protected}
    Page Should Not Contain  This resource is password protected
    Page Should Contain  This is an internal page

After a first attempt, Member should still be redirected to the inner content where he requested access in the first place
    Go to homepage
    Log In As Site Owner
    Create Password Protected Folder  Protected  thepassword
    Go to   ${protected_folder_url}
    Create Page  A Page  This is an internal page
    Custom Log out
    Log In As Test User
    Go to   ${internal_protected}
    Page Should Contain  This resource is password protected
    Input Text  css=input#password  thewrongpassword
    Click Button  submit
    Page Should Contain  This resource is password protected
    Input Text  css=input#password  thepassword
    Click Button  submit
    Page Should Not Contain  This resource is password protected
    Page Should Contain  This is an internal page

Password can be set from the add view
    Go to homepage
    Log In As Site Owner
    Click Add Folderish Protected
    Input Text  css=input#form-widgets-IDublinCore-title  Protected
    Input Text  css=input#form-widgets-IPasswordProtected-passw_hash  thepassword
    Click Button  Save
    Page Should Contain  Item created
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Contain  This resource is password protected

Password can be set from the edit view
    Go to homepage
    Log In As Site Owner
    Click Add Folderish Protected
    Input Text  css=input#form-widgets-IDublinCore-title  Protected
    Click Button  Save
    Page Should Contain  Item created
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Not Contain  This resource is password protected
    Custom Log out
    Log In As Site Owner
    Go to   ${protected_folder_url}
    Click Link  link=Edit    
    Input Text  css=input#form-widgets-IPasswordProtected-passw_hash  thepassword
    Click Button  Save
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Contain  This resource is password protected

Password can be removed from the edit view
    Go to homepage
    Log In As Site Owner
    Click Add Folderish Protected
    Input Text  css=input#form-widgets-IDublinCore-title  Protected
    Click Button  Save
    Page Should Contain  Item created
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Not Contain  This resource is password protected
    Custom Log out
    Log In As Site Owner
    Go to   ${protected_folder_url}
    Click Link  link=Edit    
    Select Checkbox  css=input#form-widgets-IPasswordProtected-reset_password-0
    Click Button  Save
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Not Contain  This resource is password protected

Password can be removed from the Assign password view
    Go to homepage
    Log In As Site Owner
    Click Add Folderish Protected
    Input Text  css=input#form-widgets-IDublinCore-title  Protected
    Click Button  Save
    Page Should Contain  Item created
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Not Contain  This resource is password protected
    Custom Log out
    Log In As Site Owner
    Go to   ${protected_folder_url}
    Click Link  link=Assign password
    Select Checkbox  css=input#form-widgets-reset_password-0
    Click Button  Save
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Not Contain  This resource is password protected

If password field is left empty, the password should not change
    Go to homepage
    Log In As Contributor User
    Create Password Protected Folder  Protected  thepassword
    Go to   ${protected_folder_url}
    Click Link  link=Assign password
    Click Button  Save
    Page Should Not Contain  This content is not going to be password protected.
    Custom Log out
    Log In As Test User
    Go to   ${protected_folder_url}
    Page Should Contain  This resource is password protected
    Input Text  css=input#password  thepassword
    Click Button  submit
    Page Should Not Contain  This resource is password protected
