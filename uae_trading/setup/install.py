from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

EMIRATES = "\nAbu Dhabi\nDubai\nSharjah\nAjman\nUmm Al Quwain\nRas Al Khaimah\nFujairah"


def party_fields():
    return [
        dict(fieldname="uae_section", label="UAE Details", fieldtype="Section Break",
             insert_after="tax_id", collapsible=1),
        dict(fieldname="trn", label="TRN", fieldtype="Data", length=15,
             insert_after="uae_section"),
        dict(fieldname="trade_licence_no", label="Trade Licence No.", fieldtype="Data",
             insert_after="trn"),
        dict(fieldname="licence_expiry", label="Licence Expiry", fieldtype="Date",
             insert_after="trade_licence_no"),
        dict(fieldname="emirate", label="Emirate", fieldtype="Select",
             options=EMIRATES, insert_after="licence_expiry"),
    ]


def setup_custom_fields():
    fields = {
        "Customer": party_fields(),
        "Supplier": party_fields(),
        "Item": [
            dict(fieldname="hs_code", label="HS Code", fieldtype="Data",
                 insert_after="item_group"),
        ],
    }
    create_custom_fields(fields, update=True)


def after_install():
    setup_custom_fields()


def after_migrate():
    setup_custom_fields()
