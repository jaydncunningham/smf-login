# smf-login

simple machines forum does some kind of weird hashing with your username, password and a key

not good for bruteforcing with existing tools

use this to generate the `hash_passwrd` field for posting

# quick rundown

on a simple machines forum's login page, this exists

```html
<input type="hidden" name="hash_passwrd" value="" />
```

it is populated on form submission as shown

```html
<form action="https://redacted/forum/index.php?action=login2" method="post" accept-charset="ISO-8859-1" name="frmLogin" id="frmLogin" style="margin-top: 4ex;" onsubmit="hashLoginPassword(this, '82a546006ce2c598f4cbc923e73662bf');">
```

which makes a call to `hashLoginPassword`, the active part of which shown below

```javascript
doForm.hash_passwrd.value = hex_sha1(hex_sha1(doForm.user.value.php_to8bit().php_strtolower() + doForm.passwrd.value.php_to8bit()) + cur_session_id);
```
