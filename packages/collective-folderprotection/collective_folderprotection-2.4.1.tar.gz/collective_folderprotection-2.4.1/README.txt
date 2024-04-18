.. contents::

Introduction
============

This package provides 3 behaviors to secure your Dexterity content types in 3 ways:

  * "Password Protected": Will allow you to set a password to specific object so any user, except manager or its owner, needs to provide it to access it or its children (if the protected content type is a folderish)

  * "Delete Protection": Intended for folderish content types, this behavior will protect the content's children for being removed.

  * "Rename Protection": Intended for folderish content types, this behavior will protect the content's children for being renamed. Note: For this particular behavior, this only protects renaming through the UI, and does not protect the object if it is renamed using manage_renameObjects programatically from its parent.


Installation
============

Just add 'collective_folderprotection' to your eggs list in your buildout and re-run buildout. The dexterity is included by the use of the 'dexterity' extra, so make sure to include that, or to pull dexterity separatedly.


Usage
=====

After installing this product, you should be provided with 3 new behaviors to activate from the "Dexterity content types" tool.
If you want to enable them from your type XML, just add any of the following:

  * collective_folderprotection.behaviors.interfaces.IPasswordProtected

  * collective_folderprotection.behaviors.interfaces.IDeleteProtected

  * collective_folderprotection.behaviors.interfaces.IRenameProtected


Password protection
===================

There are 3 different ways in which you can assign a password to your "Password protected" enabled content.

Through the add/edit views
++++++++++++++++++++++++++

When adding or editing a content type which has the behavior enabled, you should see a new field along the schema, with the "Password" label.
Enter your password here to assign it. Leave it blank, to remove password protection for this specific object.
NOTE: This is not available for Archetypes.

Through the "Assign password" view
++++++++++++++++++++++++++++++++++

You should see a new tab for an object which has the behavior enabled. Going to this view and entering any password will assign it. Leave it blank, to remove password protection for this specific object. This view is independent from the add/edit ones, you can use either one.

Programatically on content creation
+++++++++++++++++++++++++++++++++++

If you are creating content programatically, you can assign a password when calling the function, just by adding the optional "password" argumnent.


.. code-block:: python

    from plone.dexterity.utils import createContentInContainer
    ...
    ...
    createContentInContainer(self.portal, "your.app.dexterity.fti.information", title=title, password=pw)


Delete protection
=================

When the behavior is enabled for a given content type, a new checkbox will be shown in both the add and the edit screens, when creating or editing that specific content type. Marking the checkbox will protect this element and its direct children (if this is a folderish type) from being deleted.

Rename protection
=================

When the behavior is enabled for a given content type, a new checkbox will be shown in both the add and the edit screens, when creating or editing that specific content type. Marking the checkbox will protect this element and its direct children (if this is a folderish type) from being renamed.