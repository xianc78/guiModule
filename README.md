# Alert Box Module
This is a simple Python GUI module for alert boxes and prompts using ctypes.  
Currently it only works for Windows but I may add GNU/Linux, OSX, and/or BSD support in the future.

## Functions

Name | Description | Return Values
--- | --- | ---
MessageBox(message, title)| Shows an alert box | None |
YesNo(message, title) | Shows a Yes/No box | True or False depending on what the user clicked on
OkCancel(message, title) | Same as above but shows Ok/Cancel instead of Yes/No | Same as above
YesNoCancel(message, title)| Shows a prompt with Yes, No, or Cancel | "Yes" if the user clicked Yes, "No" if the user clicked No, and "Cancel" if the user clicked "Cancel".

## License
This software is licensed under the ISC license.

## TODO
* Add an InputBox function which probably means that I may have to use something like GTK or QT. (Windows API does not have a bult-in input box believe it or not)