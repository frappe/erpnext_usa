## ERPNext USA

App to hold regional code for the United States, built on top of ERPNext.

### Introduction

ERPNext USA holds regional customizations for the United States. It is built on Frappe, a full-stack, meta-data driven, web framework, and integrates seamlessly with ERPNext, the most agile ERP software.


### Installation

Using bench, [install ERPNext](https://github.com/frappe/bench#installation) as mentioned here.

Once ERPNext is installed, add ERPNext USA app to your bench by running

```sh
$ bench get-app https://github.com/frappe/erpnext_usa.git
```

After that, you can install the app on required site (let's say demo.com )by running

```sh
$ bench --site demo.com install-app erpnext_usa
```

### License

GNU GPL V3. See [license.txt](https://github.com/frappe/erpnext_usa/blob/develop/license.txt) for more information.