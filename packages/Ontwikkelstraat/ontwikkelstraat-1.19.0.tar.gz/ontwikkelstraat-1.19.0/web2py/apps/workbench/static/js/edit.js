// elke form input field heeft de class .string
// we willen hier de Enter knop voor uitschakelen om te voorkomen dat het formulier gesubmit wordt.
// maar, een textarea moet nog wel de Enter knop kunnen gebruiken, deze submit namelijk niet als je op Enter drukt.
$('.string').keydown(function (e) {
    if (this.id !== 'item_contact_id') {
        if (e.key === 'Enter') {
            e.preventDefault();  // voorkom de uitvoering van submit.
        }
    }
})

$("#submit_master").click(function () {
    $(".overlay").show(); // laat de overlay zien, zo zorg je dat de gebruiker niets kan veranderen op de pagina.
    // itereer over elke verborgen submit knop
    $(".hide_submit").each(function () {
        // klik deze submit knop aan
        this.click();
        // zorg dat de pagina niet gaat herladen
        // event.preventDefault();
        // return false leek niet te werken, vandaar event.preventDefault() deze werkt nog wel om het javascript proces af
        // te breken.
    })
    // klik als laatste de submit_item knop aan, dit doen we pas op het laatst omdat de pagina anders
    // herladen wordt en de gegevens verloren gaan.
    // .submit_item is de knop om het daadwerkelijke item op te slaan. hierna gebeurd er automatisch een reload zo wordt de overlay weer verborgen.
    setTimeout(function () {$('.submit_item').click()}, 5000);+ console.log('timeout requested');
})
