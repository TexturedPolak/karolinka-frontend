from karolinka import Karolinka
from pyscript import web, when
import warnings

warnings.filterwarnings("always")



def delete_errors():
    errors = web.page.find(".py-error")
    for error in errors:
        error.style["display"] = "none"


@when("click", "#zaszyfruj")
def zaszyfruj(event):
    delete_errors()
    input_wiadomosc = web.page["wiadomosc"]
    wiadomosc = input_wiadomosc.value

    slowoklucz = web.page["slowo-klucz"].value

    alfabet = web.page["alfabet"].value

    output_textarea = web.page["wynik"]

    _karolinka = Karolinka(słowo_klucz=slowoklucz, alfabet=alfabet, debug=True)
    
    output_textarea.innerHTML = _karolinka.zaszyfruj(wiadomosc)

@when("click", "#odszyfruj")
def odszyfruj(event):
    delete_errors()
    input_wiadomosc = web.page["wiadomosc"]
    wiadomosc = input_wiadomosc.value

    slowoklucz = web.page["slowo-klucz"].value

    alfabet = web.page["alfabet"].value

    output_textarea = web.page["wynik"]

    _karolinka = Karolinka(słowo_klucz=slowoklucz, alfabet=alfabet, debug=True)
    
    output_textarea.innerHTML = _karolinka.odszyfruj(wiadomosc)

ui = web.page.find(".ui")
for element in ui:
    element.style["display"] = "inline"
loading = web.page.find(".loading")
for element in loading:
    element.style["display"] = "none"