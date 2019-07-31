

class Locators():


#Login Page

    login_button = "//span[text()='Log in']"
    username_textbox = "//input[@type= 'email']"
    password_textbox = "//input[@type= 'password']"
    login_btn = "//button[@class= 'btn btn-primary btn-lg btn-block btn-login']"
    user = "//span[@title='vinodh682@gmail.com']"
    logout_btn = "//span[text()='Log out']"


#Home Page

    audio_clk="//a[contains(text(),'Audio & Video')]"
    home_theatre_clk="//*[@title='Home Theatre' and @href='/home-theatre']"
    product_clk="//article[@class='art'][6]"
    add_to_cart="//a[@class='btn btn-primary btn-lg btn-block btn-add-to-cart ajax-cart-link']"
    checkout="btn btn-clear btn-block btn-action"
    checkout_guest="a[class='btn btn-secondary btn-lg btn-block checkout-as-guest-button']"


#ExcelRead

    company="input#NewAddress_Company"
    first_name="input#NewAddress_FirstName"
    last_name="input#NewAddress_LastName"
    address_1="input#NewAddress_Address1"
    address_2="input#NewAddress_Address2"
    city="input#NewAddress_City"
    zip_code="input#NewAddress_ZipPostalCode"
    select_country="span#select2-NewAddress_CountryId-container"
    country="//li[@role='treeitem'][2]"
    select_state="span#select2-NewAddress_StateProvinceId-container"
    state="//li[@role='treeitem'][1]"
    email="input#NewAddress_Email"
    phone_number="input#NewAddress_PhoneNumber"
    next_button="//button[@class='btn btn-warning btn-lg new-address-next-step-button']"
    ship_button="//button[@class='btn btn-warning btn-block select-shipping-address-button']"
    next_button1="//button[@class='btn btn-warning btn-lg shipping-method-next-step-button']"
    next_button2="//button[@class='btn btn-warning btn-lg payment-method-next-step-button']"




    #ExcelWrite


    home_appliances="//a[@class='nav-link dropdown-toggle' and @href='/home-appliances']"
    kitchen_appliances="//span[@class='has-count' and text()='Kitchen Appliances']"
    Page_count="//button[@class='btn btn-secondary btn-artlist-action active focus']"





    

